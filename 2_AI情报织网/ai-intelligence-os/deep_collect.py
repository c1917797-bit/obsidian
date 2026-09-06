"""
回溯采集过去一年的推理压缩论文 - v2 (短语搜索+多分类)
关键修正:
  1. all:"phrase" 精确短语搜索 (不是 all:word1+word2)
  2. 多分类: cs.LG OR cs.CL OR cs.DC OR cs.AR OR cs.PF
  3. submittedDate 日期范围在API层过滤
  4. 每个query查完即存盘 (可中断恢复)
  5. 后置相关性过滤去噪
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import re, json, time, urllib.request
from datetime import datetime
from collections import Counter

ONE_YEAR_AGO = '20250705000000'
CUTOFF = '20260705235959'
START_DISPLAY = '2025-07-05'
END_DISPLAY = '2026-07-05'
BATCH_SIZE = 200
MAX_PER_QUERY = 2000

CAT_FILTER = '(cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.DC+OR+cat:cs.AR+OR+cat:cs.PF)'

# 经过验证的短语查询 (totalResults已测试)
QUERIES = [
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
]

# 排除不相关
EXCLUDE_PATTERNS = [
    r'quantum\s', r'fermion', r'spectroscop', r'geolocation',
    r'wireless\s+sensor\s+net', r'antenna\s+design', r'radar\s+system',
    r'protein\s+folding', r'drug\s+discovery', r'molecular\s+dynamics',
    r'point\s+cloud\s+segment', r'federated\s+learning\s+privacy',
    r'solar\s+ener', r'weather\s+forec', r'climate\s+mod',
    r'power\s+grid\s+stat', r'smart\s+grid\s+dem',
    r'gene\s+express', r'cancer\s+detect', r'medical\s+image\s+seg',
]

LLM_INDICATORS = [
    'llm', 'large language', 'language model', 'transformer',
    'gpt', 'llama', 'mistral', 'deepseek', 'qwen', 'gemini', 'claude',
    'attention mechanism', 'self-attention', 'kv cache',
    'inference', 'serving', 'deployment', 'throughput', 'latency',
    'neural network', 'deep learning', 'foundation model',
    'vlm', 'vision-language', 'multimodal', 'diffusion model',
    'moe', 'mixture of expert', 'speculative decod',
    'quantiz', 'pruning', 'distill', 'low-rank', 'lora',
    'flash attention', 'rotary position', 'rope',
    'token', 'embedding', 'fine-tun', 'pre-train',
]

CHECKPOINT_PATH = 'C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/_deep_collect_checkpoint.json'
OUTPUT_PATH = 'C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/inference_compression_arxiv_1year.json'

def is_relevant(title, summary):
    text = (title + ' ' + summary).lower()
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, text):
            return False
    return any(kw in text for kw in LLM_INDICATORS)

def fetch_page(query_encoded, start):
    url = (
        'http://export.arxiv.org/api/query?'
        'search_query={}+AND+all:{}+AND+submittedDate:[{}+TO+{}]&'
        'max_results={}&sortBy=submittedDate&sortOrder=descending&start={}'
    ).format(CAT_FILTER, query_encoded, ONE_YEAR_AGO, CUTOFF, BATCH_SIZE, start)
    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research/1.0'})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode('utf-8')

def parse_entries(xml_text):
    entries = re.split(r'<entry>', xml_text)
    papers = []
    for e in entries[1:]:
        ids = re.findall(r'<id>http://arxiv.org/abs/([0-9.]+)', e)
        pub_dates = re.findall(r'<published>([\d-]+)T', e)
        titles = re.findall(r'<title[^>]*>([^<]+)</title>', e)
        summaries = re.findall(r'<summary[^>]*>(.*?)</summary>', e, re.DOTALL)
        authors = re.findall(r'<name>([^<]+)</name>', e)
        if not ids:
            continue
        date = pub_dates[0] if pub_dates else 'unknown'
        title = titles[0].strip().replace('\n', ' ') if titles else ''
        summary = summaries[0].strip().replace('\n', ' ')[:600] if summaries else ''
        authors_short = [a.strip() for a in authors[:5]] if authors else []
        papers.append({
            'id': ids[0],
            'date': date,
            'title': title,
            'summary': summary,
            'authors': authors_short,
        })
    return papers

def load_checkpoint():
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed_queries': [], 'all_papers': {}}

def save_checkpoint(ckpt):
    with open(CHECKPOINT_PATH, 'w', encoding='utf-8') as f:
        json.dump(ckpt, f, ensure_ascii=False)

# ============ 主流程 ============
print('=' * 70)
print('deep_collect v2 - phrase search + multi-category')
print('Date: {} ~ {}'.format(START_DISPLAY, END_DISPLAY))
print('Cats: cs.LG+cs.CL+cs.DC+cs.AR+cs.PF')
print('Queries: {}'.format(len(QUERIES)))
print('=' * 70)

ckpt = load_checkpoint()
completed = set(ckpt['completed_queries'])
all_papers = ckpt['all_papers']  # id -> paper dict

for i, (query_enc, query_id) in enumerate(QUERIES):
    if query_id in completed:
        print('[{}/{}] {} -- SKIP (already done)'.format(i+1, len(QUERIES), query_id))
        continue

    print('\n[{}/{}] {}'.format(i+1, len(QUERIES), query_id))
    offset = 0
    query_new = 0

    while offset < MAX_PER_QUERY:
        try:
            xml = fetch_page(query_enc, offset)
            papers = parse_entries(xml)

            if not papers:
                break

            for p in papers:
                pid = p['id']
                if pid not in all_papers:
                    p['query_sources'] = [query_id]
                    all_papers[pid] = p
                    query_new += 1
                else:
                    if query_id not in all_papers[pid].get('query_sources', []):
                        all_papers[pid].setdefault('query_sources', []).append(query_id)

            print('  offset={}: page={}, new={}'.format(offset, len(papers), query_new))

            if len(papers) < BATCH_SIZE:
                break

            offset += BATCH_SIZE
            time.sleep(3)

        except Exception as e:
            if '429' in str(e):
                print('  RATE LIMITED, wait 60s...')
                time.sleep(60)
                continue
            print('  ERROR: {}'.format(str(e)[:60]))
            break

    completed.add(query_id)
    ckpt['completed_queries'] = list(completed)
    ckpt['all_papers'] = all_papers
    save_checkpoint(ckpt)
    print('  -> checkpoint saved ({} total unique)'.format(len(all_papers)))
    time.sleep(2)

# ============ 汇总 ============
papers_list = list(all_papers.values())
papers_list.sort(key=lambda x: x['date'], reverse=True)

print('\n' + '=' * 70)
print('Collection done: {} unique papers'.format(len(papers_list)))
print('=' * 70)

# query命中统计
qstat = Counter()
for p in papers_list:
    for qid in p.get('query_sources', []):
        qstat[qid] += 1
print('\nBy query:')
for qid, c in qstat.most_common():
    print('  {}: {}'.format(qid, c))

# ============ 后置过滤 ============
filtered = [p for p in papers_list if is_relevant(p['title'], p.get('summary', ''))]
removed = [p for p in papers_list if not is_relevant(p['title'], p.get('summary', ''))]

print('\nFilter: {} -> {} (removed {} irrelevant)'.format(
    len(papers_list), len(filtered), len(removed)))

# ============ 保存 ============
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump({
        'collected_at': datetime.now().isoformat(),
        'version': 'v2_phrase_search',
        'date_range': '{} to {}'.format(START_DISPLAY, END_DISPLAY),
        'categories': 'cs.LG+cs.CL+cs.DC+cs.AR+cs.PF',
        'total_raw': len(papers_list),
        'total_filtered': len(filtered),
        'total_removed': len(removed),
        'query_stats': dict(qstat.most_common()),
        'papers': filtered,
    }, f, ensure_ascii=False, indent=2)

print('\nSaved: {}'.format(OUTPUT_PATH))
print('Size: {:.1f}KB'.format(os.path.getsize(OUTPUT_PATH) / 1024))

# 清理checkpoint
if os.path.exists(CHECKPOINT_PATH):
    os.remove(CHECKPOINT_PATH)
    print('Checkpoint cleaned.')

# 按月统计
month_c = Counter()
for p in filtered:
    month_c[p['date'][:7]] += 1
print('\nBy month:')
for m in sorted(month_c.keys(), reverse=True):
    print('  {}: {}'.format(m, month_c[m]))
