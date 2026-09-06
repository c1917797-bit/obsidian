"""
增量采集脚本 - 基于上次采集时间，只采集最新论文

用法:
    python collect_incremental.py              # 增量采集（从上次时间到今天）
    python collect_incremental.py --since 2026-06-01  # 指定起始日期
    python collect_incremental.py --dry-run    # 只看不入库
    python collect_incremental.py --reset      # 重置状态（下次从头采）

工作流程:
    1. 读取 config/incremental_state.json 获取上次采集时间
    2. 用 scholar_alerts.json 的压缩关键词 + deep_collect 基础查询
    3. 从上次时间到今天，arXiv 分页采集
    4. 与 inference_compression_v8.json 去重
    5. 新论文入库（v8 + full_tagged）
    6. 更新状态文件
"""
import os
os.environ['PYTHONUTF8'] = '1'

import sys, io, re, time, json, argparse, urllib.request, urllib.parse
from datetime import datetime, timedelta

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============ 路径配置 ============
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(PROJECT_DIR, 'config')
STATE_PATH = os.path.join(CONFIG_DIR, 'incremental_state.json')

INSIGHT_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察'
V8_PATH = os.path.join(INSIGHT_DIR, 'inference_compression_v8.json')
FULL_PATH = os.path.join(INSIGHT_DIR, 'inference_optimization_full_tagged.json')
OUTPUT_PATH = os.path.join(INSIGHT_DIR, 'inference_compression_incremental.json')

BATCH_SIZE = 200
MAX_PER_QUERY = 500  # 增量采集单关键词上限

# ============ 多分类(与deep_collect.py一致) ============
CAT_FILTER = '(cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.DC+OR+cat:cs.AR+OR+cat:cs.PF)'

# ============ 52组短语查询(与deep_collect.py一致) ============
# 格式: (URL编码的短语, 标签)
PHRASE_QUERIES = [
    ('%22KV+cache%22', 'KV_cache'),
    ('%22speculative+decoding%22', 'spec_decode'),
    ('%22LLM+quantization%22', 'llm_quant'),
    ('%22model+pruning%22', 'pruning'),
    ('%22knowledge+distillation%22', 'distillation'),
    ('%22token+compression%22', 'token_comp'),
    ('%22token+merging%22', 'token_merge'),
    ('%22prompt+compression%22', 'prompt_comp'),
    ('%22sparse+attention%22', 'sparse_attn'),
    ('%22linear+attention%22', 'linear_attn'),
    ('%22mixture+of+experts%22', 'moe'),
    ('%22weight+quantization%22', 'weight_quant'),
    ('%22activation+quantization%22', 'act_quant'),
    ('%22early+exit%22', 'early_exit'),
    ('%22tensor+parallel%22', 'tensor_par'),
    ('%22expert+parallel%22', 'expert_par'),
    ('%22prefix+caching%22', 'prefix_cache'),
    ('%22LLM+serving%22', 'llm_serving'),
    ('%22cross-layer%22', 'cross_layer'),
    ('%22grouped+query%22', 'gqa'),
    ('%22continuous+batching%22', 'cont_batch'),
    ('%22cache+eviction%22', 'cache_evict'),
    ('%22cache+offloading%22', 'cache_offload'),
    ('%22paged+attention%22', 'paged_attn'),
    ('%22inference+acceleration%22', 'infer_accel'),
    ('%22memory+efficient%22', 'mem_eff'),
    ('%22model+distillation%22', 'model_distill'),
    ('%22context+compression%22', 'ctx_comp'),
    ('%22visual+token%22', 'visual_token'),
    ('%22long+context%22', 'long_ctx'),
    # 补充高频广词
    ('%22quantization%22', 'quantization'),
    ('%22pruning%22', 'pruning_broad'),
    ('%22distillation%22', 'distillation_broad'),
    ('%22low-rank%22', 'low_rank'),
    ('%22LoRA%22', 'lora'),
    ('%22model+compression%22', 'model_comp'),
    ('%22efficient+inference%22', 'eff_infer'),
    ('%22state+space+model%22', 'ssm'),
    ('%22Mamba%22', 'mamba'),
    ('%22sparsification%22', 'sparsification'),
    ('%22draft+model%22', 'draft_model'),
    ('%22FP8%22', 'fp8'),
    ('%22rotary+position%22', 'rope'),
    ('%22edge+deployment%22', 'edge_deploy'),
    ('%22INT4%22', 'int4'),
    ('%22GQA%22', 'gqa_short'),
    ('%22inference+optimization%22', 'infer_opt'),
    ('%22on-device+LLM%22', 'on_device'),
]

TODAY = datetime.now().strftime('%Y-%m-%d')
START_DATE_NUM = ''
END_DATE_NUM = ''

# ============ 状态管理 ============
def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'last_collected_date': None,
        'last_run': None,
        'history': [],
        'total_collected': 0,
    }

def save_state(state, start_date=None, end_date=None):
    state['last_run'] = datetime.now().isoformat()
    actual_end = end_date or TODAY
    actual_start = start_date or state.get('last_collected_date', actual_end)
    state['last_collected_date'] = actual_end
    state['history'].append({
        'run_at': state['last_run'],
        'date_range': '{} to {}'.format(actual_start, actual_end),
        'new_papers': state.get('last_new_count', 0),
    })
    state['history'] = state['history'][-20:]  # 保留最近20次记录
    with open(STATE_PATH, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

# ============ 加载查询(直接用PHRASE_QUERIES) ============
def load_queries():
    return [(qe, label, label) for qe, label in PHRASE_QUERIES]

# ============ arXiv 采集(短语搜索+多分类+日期范围) ============
def fetch_page(query_encoded, start):
    url = (
        'http://export.arxiv.org/api/query?'
        'search_query={}+AND+all:{}+AND+submittedDate:[{}+TO+{}]&'
        'max_results={}&sortBy=submittedDate&sortOrder=descending&start={}'
    ).format(CAT_FILTER, query_encoded,
             START_DATE_NUM, END_DATE_NUM, BATCH_SIZE, start)
    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research/1.0'})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode('utf-8')

def parse_entries(xml_text):
    entries = re.split(r'<entry>', xml_text)
    papers = []
    for e in entries[1:]:
        ids = re.findall(r'<id>http://arxiv.org/abs/([0-9.]+)', e)
        pub_dates = re.findall(r'<published>([\d-]+)T', e)
        upd_dates = re.findall(r'<updated>([\d-]+)T', e)
        titles = re.findall(r'<title[^>]*>([^<]+)</title>', e)
        summaries = re.findall(r'<summary[^>]*>(.*?)</summary>', e, re.DOTALL)
        authors = re.findall(r'<name>([^<]+)</name>', e)
        
        if not ids:
            continue
        
        date = pub_dates[0] if pub_dates else (upd_dates[0] if upd_dates else 'unknown')
        title = titles[0].strip().replace('\n', ' ') if titles else ''
        summary = summaries[0].strip().replace('\n', ' ')[:600] if summaries else ''
        authors_short = authors[:5] if authors else []
        
        papers.append({
            'id': ids[0],
            'date': date,
            'title': title,
            'summary': summary,
            'authors': authors_short,
        })
    return papers

# ============ 20格分类 ============
def classify(title, summary):
    text = (title + ' ' + summary).lower()
    
    objects = []
    methods = []
    
    if any(kw in text for kw in ['kv cache', 'kv-cache', 'key-value cache', 'attention cache', 'prefill', 'paged attention']):
        objects.append('KV')
    if any(kw in text for kw in ['weight', 'parameter', 'model size', 'model compress']):
        objects.append('参数')
    if any(kw in text for kw in ['activation', 'feature map', 'token compression', 'token pruning', 'token merging', 'visual token', 'prompt compression']):
        objects.append('激活')
    if any(kw in text for kw in ['communication', 'tensor parallel', 'pipeline parallel', 'distributed inference', 'expert parallel']):
        objects.append('通信')
    
    if any(kw in text for kw in ['quantiz', 'int4', 'int8', 'int2', 'fp8', 'fp4', 'low-bit']):
        methods.append('量化')
    if any(kw in text for kw in ['pruning', 'prune', 'sparse', 'sparsity']):
        methods.append('剪枝/稀疏')
    if any(kw in text for kw in ['distill', 'knowledge transfer']):
        methods.append('蒸馏')
    if any(kw in text for kw in ['low-rank', 'low rank', 'svd', 'decomposition', 'lora']):
        methods.append('低秩')
    if any(kw in text for kw in ['speculative decoding', 'draft model']):
        methods.append('投机解码')
    if any(kw in text for kw in ['linear attention', 'flash attention', 'grouped query', 'sliding window', 'sparse attention', 'cross-layer', 'mla']):
        methods.append('注意力优化')
    if any(kw in text for kw in ['early exit', 'layer skip', 'skip layer']):
        methods.append('早退/跳层')
    
    return objects, methods

# ============ 数据库去重 & 合并 ============
def load_db_dedup_pool():
    existing_ids = set()
    existing_titles = set()
    for fpath in [V8_PATH, FULL_PATH]:
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            for p in data.get('papers', []):
                if p.get('arxiv_id'):
                    existing_ids.add(p['arxiv_id'])
                t = p.get('title', '').lower().strip()[:80]
                if t:
                    existing_titles.add(t)
    return existing_ids, existing_titles

def merge_to_db(new_papers, dry_run=False):
    merged_v8 = 0
    merged_full = 0
    
    for fpath, key in [(V8_PATH, 'v8'), (FULL_PATH, 'full')]:
        if not os.path.exists(fpath):
            continue
        
        with open(fpath, 'r', encoding='utf-8-sig') as f:
            db = json.load(f)
        
        db_ids = set(p.get('arxiv_id','') for p in db['papers'])
        db_titles = set(p.get('title','').lower().strip()[:80] for p in db['papers'])
        
        for p in new_papers:
            tkey = p['title'].lower().strip()[:80]
            if p['id'] in db_ids or tkey in db_titles:
                continue
            
            new_entry = {
                'title': p['title'],
                'year': int(p['date'][:4]) if p['date'][:4].isdigit() else 2026,
                'venue': 'arXiv',
                'arxiv_id': p['id'],
                'abstract': p['summary'],
                'url': 'https://arxiv.org/abs/{}'.format(p['id']),
                'published': p['date'],
                'authors': p.get('authors', []),
                'source': 'incremental_{}'.format(TODAY),
            }
            
            if key == 'full':
                new_entry['objects'] = p.get('objects', [])
                new_entry['methods'] = p.get('methods', [])
                new_entry['cells'] = ['{}x{}'.format(o,m) for o in p.get('objects',[]) for m in p.get('methods',[])]
            
            db['papers'].append(new_entry)
            db_ids.add(p['id'])
            db_titles.add(tkey)
            
            if key == 'v8':
                merged_v8 += 1
            else:
                merged_full += 1
        
        db['last_updated'] = TODAY
        db['total_papers'] = len(db['papers'])
        
        if not dry_run:
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(db, f, ensure_ascii=False, indent=2)
    
    return merged_v8, merged_full

# ============ 主流程 ============
def main():
    parser = argparse.ArgumentParser(description='增量采集推理压缩论文')
    parser.add_argument('--since', help='指定起始日期 (YYYY-MM-DD)，覆盖状态文件')
    parser.add_argument('--dry-run', action='store_true', help='只采集不入库')
    parser.add_argument('--reset', action='store_true', help='重置状态文件')
    parser.add_argument('--output', default=OUTPUT_PATH, help='输出JSON路径')
    args = parser.parse_args()
    
    # 状态管理
    state = load_state()
    if args.reset:
        state = {'last_collected_date': None, 'last_run': None, 'history': [], 'total_collected': 0}
        with open(STATE_PATH, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        print("状态已重置")
        return
    
    # 确定起始日期
    if args.since:
        start_date = args.since
    elif state.get('last_collected_date'):
        start_date = state['last_collected_date']
    else:
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    end_date = TODAY
    
    # 转换为arXiv API的submittedDate格式 (YYYYMMDD000000)
    global START_DATE_NUM, END_DATE_NUM
    START_DATE_NUM = start_date.replace('-', '') + '000000'
    END_DATE_NUM = end_date.replace('-', '') + '235959'
    
    print("=" * 70)
    print("增量采集 - 推理压缩论文")
    print("=" * 70)
    print("采集区间: {} ~ {}".format(start_date, end_date))
    print("上次采集: {}".format(state.get('last_collected_date', '无（首次运行）')))
    print("入库模式: {}".format('DRY RUN (不入库)' if args.dry_run else '合并入库'))
    print("查询: {} 组短语 (多分类: cs.LG+cs.CL+cs.DC+cs.AR+cs.PF)".format(len(PHRASE_QUERIES)))
    print("状态文件: {}".format(STATE_PATH))
    print("=" * 70)
    
    # 加载查询
    queries = load_queries()
    print("有效查询: {} 组".format(len(queries)))
    
    # 加载去重池
    existing_ids, existing_titles = load_db_dedup_pool()
    print("去重池: {} IDs + {} titles".format(len(existing_ids), len(existing_titles)))
    
    # 采集
    all_papers = {}
    query_stats = {}
    
    for i, (query_text, query_name, query_id) in enumerate(queries):
        print("\n[{}/{}] {}".format(i+1, len(queries), query_name))
        
        query_new = []
        offset = 0
        rate_limit_hits = 0
        
        while offset < MAX_PER_QUERY:
            try:
                xml = fetch_page(query_text, offset)
                papers = parse_entries(xml)
                
                if not papers:
                    break
                
                dates = [p['date'] for p in papers]
                oldest = min(dates)
                
                in_range = [p for p in papers if start_date <= p['date'] <= end_date]
                too_old = [p for p in papers if p['date'] < start_date]
                
                print("  offset={}: in_range={}, too_old={}, oldest={}".format(
                    offset, len(in_range), len(too_old), oldest))
                
                query_new.extend(in_range)
                
                if too_old:
                    break
                
                offset += BATCH_SIZE
                time.sleep(3)
                
            except Exception as e:
                if '429' in str(e):
                    rate_limit_hits += 1
                    if rate_limit_hits > 3:
                        print("  RATE LIMIT x3, 跳过此关键词")
                        break
                    print("  RATE LIMITED, waiting 30s...")
                    time.sleep(30)
                    continue
                else:
                    print("  ERROR: {}".format(str(e)[:60]))
                    break
        
        # query内去重
        seen = set()
        unique = []
        for p in query_new:
            if p['id'] not in seen:
                seen.add(p['id'])
                p['query_source'] = query_name
                unique.append(p)
        
        query_stats[query_name] = len(unique)
        print("  -> {} unique".format(len(unique)))
        
        for p in unique:
            if p['id'] not in all_papers:
                all_papers[p['id']] = p
        
        time.sleep(1.5)
    
    # 汇总
    papers_list = list(all_papers.values())
    papers_list.sort(key=lambda x: x['date'], reverse=True)
    
    # 与数据库去重
    new_papers = []
    already = 0
    for p in papers_list:
        if p['id'] in existing_ids or p['title'].lower().strip()[:80] in existing_titles:
            already += 1
        else:
            objs, meths = classify(p['title'], p['summary'])
            p['objects'] = objs
            p['methods'] = meths
            new_papers.append(p)
    
    print("\n" + "=" * 70)
    print("采集结果")
    print("=" * 70)
    print("区间内总数: {} 篇".format(len(papers_list)))
    print("已在数据库: {} 篇".format(already))
    print("新增: {} 篇".format(len(new_papers)))
    
    # 显示新增
    if new_papers:
        print("\n新增论文:")
        for i, p in enumerate(new_papers):
            objs = '/'.join(p['objects']) if p['objects'] else '-'
            meths = '/'.join(p['methods']) if p['methods'] else '-'
            print("  {}. [{}] [{}/{}] {}".format(
                i+1, p['date'], objs, meths, p['title'][:65]))
    
    # 保存采集结果
    output = {
        'collected_at': datetime.now().isoformat(),
        'date_range': '{} to {}'.format(start_date, end_date),
        'mode': 'dry_run' if args.dry_run else 'incremental',
        'total_in_range': len(papers_list),
        'already_in_db': already,
        'total_new': len(new_papers),
        'query_stats': query_stats,
        'papers_new': new_papers,
        'papers_all_in_range': papers_list,
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print("\n采集结果已保存: {}".format(args.output))
    
    # 入库
    if new_papers and not args.dry_run:
        print("\n合并入库...")
        merged_v8, merged_full = merge_to_db(new_papers, dry_run=False)
        print("  v8: +{}".format(merged_v8))
        print("  full_tagged: +{}".format(merged_full))
    
    # 更新状态（不管有没有新论文，只要不是dry-run就更新，避免重复采集）
    if not args.dry_run:
        state['last_new_count'] = len(new_papers)
        state['total_collected'] += len(new_papers)
        save_state(state, start_date, end_date)
        print("\n状态已更新: last_collected_date = {}".format(end_date))
        print("完成。下次运行将从 {} 开始采集。".format(end_date))
    else:
        print("\n[DRY RUN] 未入库，未更新状态")

if __name__ == '__main__':
    main()
