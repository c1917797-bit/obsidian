"""
arXiv盲区检测: 拉取全量cs.LG+cs.CL论文ID列表，与v8比对，找出遗漏
只拉title+id用于快速比对，不拉abstract
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, json, re, time, urllib.request
from collections import Counter

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ONE_YEAR_AGO = '20250705000000'
CUTOFF = '20260705235959'
BATCH_SIZE = 500  # 最大允许值，减少页数

# 加载v8现有标题
v8_path = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_v8.json'
with open(v8_path, 'r', encoding='utf-8-sig') as f:
    v8 = json.load(f)

existing_titles = set()
for p in v8['papers']:
    t = p.get('title', '').lower().strip().replace('  ', ' ')[:80]
    if t:
        existing_titles.add(t)
print('v8 total: {} papers, {} unique titles'.format(len(v8['papers']), len(existing_titles)))

# ============ 拉取全量cs.LG和cs.CL论文(无关键词) ============
# 只获取title，用于快速比对
CATS = ['cs.LG', 'cs.CL', 'cs.DC']
all_arxiv_titles = {}  # title -> id

for cat in CATS:
    print('\n=== {} (no keyword, date range only) ==='.format(cat))
    offset = 0
    
    while True:
        url = (
            'http://export.arxiv.org/api/query?'
            'search_query=cat:{}+AND+submittedDate:[{}+TO+{}]&'
            'max_results={}&sortBy=submittedDate&sortOrder=descending&start={}'
        ).format(cat, ONE_YEAR_AGO, CUTOFF, BATCH_SIZE, offset)
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research/1.0'})
            with urllib.request.urlopen(req, timeout=60) as resp:
                txt = resp.read().decode('utf-8')
            
            # 快速解析: 只提取title和id
            entries = re.split(r'<entry>', txt)
            page_count = 0
            for e in entries[1:]:
                ids = re.findall(r'<id>http://arxiv.org/abs/([0-9.]+)', e)
                titles = re.findall(r'<title[^>]*>([^<]+)</title>', e)
                if ids and titles:
                    title = titles[0].strip().replace('\n', ' ').lower()[:80]
                    all_arxiv_titles[title] = ids[0]
                    page_count += 1
            
            print('  offset={}: got {}'.format(offset, page_count))
            
            if page_count < BATCH_SIZE:
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

print('\nTotal arXiv papers in {} ({} ~ {}): {}'.format(
    '+'.join(CATS), '2025-07-05', '2026-07-05', len(all_arxiv_titles)))

# ============ 比对 ============
# 找出在arXiv但不在v8的论文
gap_titles = set(all_arxiv_titles.keys()) - existing_titles
print('\nGap analysis:')
print('  arXiv total: {}'.format(len(all_arxiv_titles)))
print('  In v8: {}'.format(len(all_arxiv_titles) - len(gap_titles)))
print('  Gap (not in v8): {}'.format(len(gap_titles)))

# 对gap论文做快速相关性判断
COMPRESSION_TERMS = [
    'quantiz', 'int4', 'int8', 'fp8', 'fp4', 'low-bit',
    'pruning', 'prune', 'sparse', 'sparsif',
    'distill', 'knowledge transfer',
    'low-rank', 'low rank', 'svd',
    'kv cache', 'cache compress', 'cache evict', 'paged attention',
    'speculative decod', 'draft model',
    'model compress', 'parameter reduc',
    'token compress', 'token prun', 'token merg', 'token reduc',
    'prompt compress', 'context compress',
    'early exit', 'layer skip',
    'efficient inference', 'inference accelerat', 'inference optim',
    'memory efficient', 'memory footprint',
    'mixture of expert', 'moe',
    'tensor parallel', 'expert parallel',
    'edge llm', 'on-device',
    'flash attention', 'sparse attention', 'linear attention',
    'cross-layer', 'grouped query',
    'lora', 'mamba', 'state space',
    'serving', 'throughput', 'latency',
]

# 只看title判断(快)
relevant_gap = []
for title in gap_titles:
    tl = title.lower()
    matches = [t for t in COMPRESSION_TERMS if t in tl]
    if len(matches) >= 1:
        relevant_gap.append((title, all_arxiv_titles[title]))

print('  Gap with compression terms in TITLE: {}'.format(len(relevant_gap)))

# 显示这些gap论文
if relevant_gap:
    print('\nMissed papers (compression terms in title but not in v8):')
    for i, (title, pid) in enumerate(sorted(relevant_gap)[:30]):
        print('  {}. [{}] {}'.format(i+1, pid, title[:70]))
    if len(relevant_gap) > 30:
        print('  ... and {} more'.format(len(relevant_gap) - 30))

# 保存gap
gap_path = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\arxiv_gap_analysis.json'
with open(gap_path, 'w', encoding='utf-8') as f:
    json.dump({
        'arxiv_total': len(all_arxiv_titles),
        'in_v8': len(all_arxiv_titles) - len(gap_titles),
        'gap_total': len(gap_titles),
        'gap_relevant': len(relevant_gap),
        'gap_relevant_papers': [{'title': t, 'arxiv_id': pid} for t, pid in relevant_gap],
    }, f, ensure_ascii=False, indent=2)
print('\nSaved: {}'.format(gap_path))
