"""
继续为剩余核心论文LLM增强
- 支持断点续传(读取已增强卡片)
- API重试
- 批量处理Next 300+
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, re, json, time
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os')

from core.minimax_client import get_client
llm = get_client()

META_ROOT = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文元数据'
CORE_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\core_papers_list.json'
V8_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_v8.json'
FULL_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_optimization_full_tagged.json'

# 加载核心论文
with open(CORE_PATH, 'r', encoding='utf-8') as f:
    core_data = json.load(f)
core_papers = core_data['papers']

# 加载v8补充abstracts
with open(V8_PATH, 'r', encoding='utf-8-sig') as f:
    v8 = json.load(f)
v8_index = {p.get('arxiv_id'): p for p in v8['papers'] if p.get('arxiv_id')}

with open(FULL_PATH, 'r', encoding='utf-8-sig') as f:
    full = json.load(f)
full_index = {p.get('arxiv_id'): p for p in full['papers'] if p.get('arxiv_id')}

# ============ 已增强的列表（断点续传） ============
ALREADY_ENRICHED_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\enriched_papers_progress.json'
if os.path.exists(ALREADY_ENRICHED_PATH):
    with open(ALREADY_ENRICHED_PATH, 'r', encoding='utf-8') as f:
        progress = json.load(f)
    already_done = set(progress.get('done', []))
    failures = progress.get('failures', [])
    print('Resuming from checkpoint: {} done, {} failed'.format(len(already_done), len(failures)))
else:
    already_done = set()
    failures = []
    print('Fresh start')

# ============ 找需要处理的（跳过已增强） ============
def card_already_enriched(aid):
    """检查md文件是否已经有真实的key_innovation"""
    safe_title_pattern = None
    # 我们需要找到文件但不知道标题
    # 用citekey或者文件名模式
    # 简单做法: 直接扫描已有enriched的列表
    return aid in already_done

# 用 v8_id 找 primary cell + 文件
def find_md_path(aid, title, primary_cell):
    safe_title = re.sub(r'[<>:"/\\|?*\n\r\t]', '', title or '')
    safe_title = re.sub(r'\s+', '_', safe_title.strip())[:50]
    fname = '{}_{}.md'.format(aid, safe_title)
    return os.path.join(META_ROOT, primary_cell, fname)

# 给每篇论文找primary cell + 文件
papers_to_process = []
for i, p in enumerate(core_papers):
    aid = p.get('arxiv_id','')
    if not aid:
        continue
    if aid in already_done:
        continue
    
    title = p.get('title','')
    if not title:
        continue
    
    # 补充abstract
    if not p.get('abstract'):
        v8p = v8_index.get(aid)
        if v8p and v8p.get('abstract'):
            p['abstract'] = v8p['abstract']
    
    # 找primary cell
    f_p = full_index.get(aid, {})
    objects = f_p.get('objects', [])
    methods = f_p.get('methods', [])
    primary_obj = objects[0] if objects else '参数'
    primary_meth = methods[0] if methods else '量化'
    primary_cell = '{}×{}'.format(primary_obj, primary_meth)
    
    fpath = find_md_path(aid, title, primary_cell)
    if os.path.exists(fpath):
        papers_to_process.append({
            'p': p,
            'fpath': fpath,
            'primary_cell': primary_cell,
            'aid': aid,
        })

print('Papers to process: {}'.format(len(papers_to_process)))
print('Already done: {}'.format(len(already_done)))
print('Estimated time: ~{:.0f}s ({:.1f} min)'.format(len(papers_to_process) * 3, len(papers_to_process) * 3 / 60))

# ============ 处理 ============
def llm_extract(title, abstract, max_retries=3):
    """提取关键信息 + 重试"""
    prompt = """分析以下AI论文，给出关键创新点。要求简洁。

标题: {title}

摘要: {abstract}

回答格式（每行一项）:
创新1: [核心创新点1，一句话]
性能: [具体数字如"加速1.5x",无则填"未提数字"]
代码: [GitHub链接或"未开源"]
""".format(title=title[:200], abstract=(abstract or '无摘要')[:1200])
    
    for attempt in range(max_retries):
        try:
            resp = llm.chat([{'role':'user','content':prompt}], max_tokens=200)
            return parse_response(resp), None
        except Exception as e:
            err = str(e)[:60]
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            return None, err

def parse_response(resp):
    innovations = []
    performance = ''
    code = ''
    for line in resp.split('\n'):
        line = line.strip()
        if line.startswith('创新1') or line.startswith('创新2') or line.startswith('创新3'):
            v = re.sub(r'^\S+:', '', line).strip()
            if v and len(v) > 3:
                innovations.append(v)
        elif line.startswith('性能'):
            performance = re.sub(r'^\S+:', '', line).strip()
        elif line.startswith('代码'):
            code = re.sub(r'^\S+:', '', line).strip()
    
    return {
        'innovations': innovations[:2],
        'performance': performance,
        'code': code,
    }

def update_md(fpath, info):
    """更新md文件 - 用lambda避免反引用冲突"""
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    innovations_text = ' | '.join(info['innovations']) if info['innovations'] else '需精读总结'
    if not innovations_text:
        innovations_text = '需精读总结'
    
    performance = info['performance'] or '未提数字'
    code = info['code'] or ''
    
    new_content = content
    # 用lambda替换避免反引用冲突
    new_content = re.sub(
        r'key_innovation: ".*?"',
        lambda m: 'key_innovation: "{}"'.format(innovations_text.replace('"', '\\"').replace('\\', '\\\\')),
        new_content
    )
    new_content = re.sub(
        r'performance: ".*?"',
        lambda m: 'performance: "{}"'.format(performance.replace('"', '\\"').replace('\\', '\\\\')),
        new_content
    )
    if code and code != '未开源':
        new_content = re.sub(
            r'code_url: ".*?"',
            lambda m: 'code_url: "{}"'.format(code.replace('"', '\\"').replace('\\', '\\\\')),
            new_content
        )
    new_content = re.sub(r'priority: P\d', 'priority: P1', new_content, count=1)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# ============ 批量处理 ============
print('\n=== Processing {} papers ==='.format(len(papers_to_process)))

enriched_results = {}
newly_done = 0
new_failures = []

BATCH_SAVE_INTERVAL = 20
start_time = time.time()

for i, item in enumerate(papers_to_process):
    p = item['p']
    fpath = item['fpath']
    aid = item['aid']
    title = p.get('title','')
    abstract = p.get('abstract','')
    
    info, err = llm_extract(title, abstract)
    
    if err:
        new_failures.append({'aid': aid, 'title': title[:50], 'err': err})
        already_done.add(aid)
        newly_done += 0
        print('  [{}/{}] {} FAILED: {}'.format(i+1, len(papers_to_process), aid, err[:40]))
        time.sleep(3)
        continue
    
    if info:
        update_md(fpath, info)
        enriched_results[aid] = {
            'title': title[:80],
            'primary_cell': item['primary_cell'],
            'innovations': info['innovations'][:2],
            'performance': info['performance'][:50],
            'code': info['code'][:60],
        }
        newly_done += 1
        already_done.add(aid)
        
        if (i+1) % 5 == 0:
            elapsed = time.time() - start_time
            rate = (i+1) / elapsed if elapsed > 0 else 0
            eta = (len(papers_to_process) - i - 1) / rate if rate > 0 else 0
            print('  [{}/{}] done={}, rate={:.1f}/s, eta={:.0f}s'.format(
                i+1, len(papers_to_process), newly_done, rate, eta))
    
    # 每20个保存一次进度
    if (i+1) % BATCH_SAVE_INTERVAL == 0:
        # 合并旧进度
        old_enriched = {}
        if os.path.exists(ALREADY_ENRICHED_PATH):
            with open(ALREADY_ENRICHED_PATH, 'r', encoding='utf-8') as f:
                old = json.load(f)
                old_enriched = old.get('results', {})
        old_enriched.update(enriched_results)
        with open(ALREADY_ENRICHED_PATH, 'w', encoding='utf-8') as f:
            json.dump({
                'last_update': datetime.now().isoformat(),
                'done': list(already_done),
                'results': old_enriched,
                'failures': new_failures + failures,
            }, f, ensure_ascii=False, indent=2)
    
    # 速率控制
    time.sleep(1.5)

# 最终保存
old_enriched = {}
if os.path.exists(ALREADY_ENRICHED_PATH):
    with open(ALREADY_ENRICHED_PATH, 'r', encoding='utf-8') as f:
        old = json.load(f)
        old_enriched = old.get('results', {})
old_enriched.update(enriched_results)
with open(ALREADY_ENRICHED_PATH, 'w', encoding='utf-8') as f:
    json.dump({
        'last_update': datetime.now().isoformat(),
        'done': list(already_done),
        'results': old_enriched,
        'failures': new_failures + failures,
    }, f, ensure_ascii=False, indent=2)

elapsed = time.time() - start_time
print('\n=== Done ===')
print('Newly enriched this run: {}'.format(newly_done))
print('Total enriched: {}'.format(len(already_done) - len(new_failures)))
print('Failures this run: {}'.format(len(new_failures)))
print('Elapsed: {:.0f}s'.format(elapsed))

# 打印几个样例
print('\nSample enriched this run:')
for aid, info in list(enriched_results.items())[:5]:
    print('  [{}]'.format(aid))
    print('    {}'.format(info['title']))
    print('    Innov: {}'.format(' | '.join(info['innovations'])[:100]))
    if info['performance'] != '未提数字':
        print('    Perf: {}'.format(info['performance']))
    if info['code'] and info['code'] != '未开源':
        print('    Code: {}'.format(info['code']))
