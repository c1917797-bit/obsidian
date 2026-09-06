"""
补充采集 - 用高频广词补充deep_collect_v2的盲区
对已采集的4589篇去重后追加
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
BATCH_SIZE = 200
MAX_PER_QUERY = 3000
CAT_FILTER = '(cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.DC+OR+cat:cs.AR+OR+cat:cs.PF)'

# 补充高频短语
SUPP_QUERIES = [
    '%22quantization%22',        # 1563
    '%22pruning%22',             # 1337
    '%22distillation%22',        # 2723
    '%22low-rank%22',            # 1420
    '%22LoRA%22',                # 1203
    '%22model+compression%22',   # 205
    '%22efficient+inference%22', # 231
    '%22state+space+model%22',   # 379
    '%22Mamba%22',               # 305
    '%22post-training+quantization%22', # 213
    '%22sparsification%22',      # 159
    '%22draft+model%22',         # 140
    '%22PTQ%22',                 # 139
    '%22INT8%22',                # 116
    '%22structured+pruning%22',  # 110
    '%22FP8%22',                 # 99
    '%22rotary+position%22',     # 97
    '%22edge+deployment%22',     # 170
    '%22INT4%22',                # 75
    '%22GQA%22',                 # 71
    '%22inference+optimization%22', # 48
    '%22on-device+LLM%22',       # 41
]

EXCLUDE_PATTERNS = [
    r'quantum\s', r'fermion', r'spectroscop', r'geolocation',
    r'wireless\s+sensor\s+net', r'antenna\s+design', r'radar\s+system',
    r'protein\s+folding', r'drug\s+discovery', r'molecular\s+dynamics',
    r'point\s+cloud\s+segment', r'solar\s+ener', r'weather\s+forec',
    r'climate\s+mod', r'power\s+grid\s+stat', r'smart\s+grid\s+dem',
    r'gene\s+express', r'cancer\s+detect',
]

LLM_INDICATORS = [
    'llm', 'large language', 'language model', 'transformer',
    'gpt', 'llama', 'mistral', 'deepseek', 'qwen', 'gemini',
    'attention mechanism', 'self-attention', 'kv cache',
    'inference', 'serving', 'deployment', 'throughput', 'latency',
    'neural network', 'deep learning', 'foundation model',
    'vlm', 'vision-language', 'multimodal', 'diffusion model',
    'moe', 'mixture of expert', 'speculative decod',
    'quantiz', 'pruning', 'distill', 'low-rank', 'lora',
    'flash attention', 'rotary position', 'rope',
    'token', 'embedding', 'fine-tun', 'pre-train',
    'mamba', 'state space', 'retnet', 'rwkv',
    'int4', 'int8', 'int2', 'fp8', 'fp4', 'ptq', 'qat',
    'edge', 'on-device', 'mobile',
]

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
        papers.append({'id': ids[0], 'date': date, 'title': title, 'summary': summary, 'authors': authors_short})
    return papers

# ============ 加载已有数据 ============
existing_path = 'C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/inference_compression_arxiv_1year.json'
with open(existing_path, 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_papers = {p['id']: p for p in existing['papers']}
print('Existing: {} papers'.format(len(existing_papers)))
print('Supplementary queries: {}'.format(len(SUPP_QUERIES)))

CHECKPOINT = 'C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/_supp_checkpoint.json'
def load_ckpt():
    if os.path.exists(CHECKPOINT):
        with open(CHECKPOINT, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed': [], 'new_papers': {}}
def save_ckpt(c):
    with open(CHECKPOINT, 'w', encoding='utf-8') as f:
        json.dump(c, f)

ckpt = load_ckpt()
completed = set(ckpt['completed'])
new_papers = ckpt['new_papers']

# ============ 补充采集 ============
for i, qe in enumerate(SUPP_QUERIES):
    label = qe.replace('%22', '').replace('+', ' ')
    if label in completed:
        print('[{}/{}] {} -- SKIP'.format(i+1, len(SUPP_QUERIES), label))
        continue

    print('\n[{}/{}] {}'.format(i+1, len(SUPP_QUERIES), label))
    offset = 0
    q_new = 0

    while offset < MAX_PER_QUERY:
        try:
            xml = fetch_page(qe, offset)
            papers = parse_entries(xml)
            if not papers:
                break

            for p in papers:
                pid = p['id']
                if pid not in existing_papers and pid not in new_papers:
                    if is_relevant(p['title'], p.get('summary', '')):
                        p['query_source'] = label
                        new_papers[pid] = p
                        q_new += 1

            print('  offset={}: page={}, new={}'.format(offset, len(papers), q_new))
            if len(papers) < BATCH_SIZE:
                break
            offset += BATCH_SIZE
            time.sleep(3)
        except Exception as e:
            if '429' in str(e):
                print('  RATE LIMITED, wait 60s...')
                time.sleep(60)
                continue
            print('  ERROR: {}'.format(str(e)[:50]))
            break

    completed.add(label)
    ckpt['completed'] = list(completed)
    ckpt['new_papers'] = new_papers
    save_ckpt(ckpt)
    print('  -> {} new, checkpoint saved (total new: {})'.format(q_new, len(new_papers)))
    time.sleep(2)

# ============ 合并 ============
print('\n' + '=' * 60)
print('Supplementary collection done')
print('New relevant papers: {}'.format(len(new_papers)))
print('=' * 60)

all_papers = list(existing_papers.values()) + list(new_papers.values())
all_papers.sort(key=lambda x: x['date'], reverse=True)

# 保存合并结果
with open(existing_path, 'w', encoding='utf-8') as f:
    json.dump({
        'collected_at': datetime.now().isoformat(),
        'version': 'v2_supplemented',
        'date_range': '2025-07-05 to 2026-07-05',
        'categories': 'cs.LG+cs.CL+cs.DC+cs.AR+cs.PF',
        'total_raw': len(all_papers),
        'previous_count': len(existing_papers),
        'supplement_count': len(new_papers),
        'query_count': 52,  # 30 original + 22 supp
        'papers': all_papers,
    }, f, ensure_ascii=False, indent=2)

print('Saved: {} (total {} papers, {:.1f}KB)'.format(
    existing_path, len(all_papers), os.path.getsize(existing_path) / 1024))

# 清理
if os.path.exists(CHECKPOINT):
    os.remove(CHECKPOINT)

month_c = Counter(p['date'][:7] for p in all_papers)
print('\nBy month:')
for m in sorted(month_c.keys(), reverse=True):
    print('  {}: {}'.format(m, month_c[m]))
