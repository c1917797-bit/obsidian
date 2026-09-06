"""
OpenReview全量采集器
采集ICLR 2026 / NeurIPS 2025 / ICML 2025 的所有投稿(含被拒)
搜索范围: 量化/剪枝/蒸馏/KV cache/压缩/推理加速等
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, json, time, urllib.request, urllib.parse, re
from collections import Counter
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# OpenReview venue IDs
VENUES = [
    ('ICLR.cc/2026/Conference', 'ICLR 2026'),
    ('NeurIPS.cc/2025/Conference', 'NeurIPS 2025'),
    ('ICML.cc/2025/Conference', 'ICML 2025'),
    ('ACL.org/2025/Conference', 'ACL 2025'),
    ('EMNLP/2024/Conference', 'EMNLP 2024'),
]

# 搜索词 - 用OR连接覆盖全面
SEARCH_TERMS = [
    'quantization',
    'pruning compression',
    'distillation efficient',
    'KV cache',
    'speculative decoding',
    'model compression',
    'inference acceleration',
    'sparse attention',
    'low-rank',
    'LoRA inference',
    'token compression',
    'memory efficient',
    'mixture of experts efficient',
    'edge LLM',
]

OUTPUT_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\openreview_papers.json'
CHECKPOINT_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\_openreview_checkpoint.json'

def search_openreview(term, venue_group, limit=100, offset=0):
    """搜索OpenReview"""
    url = (
        'https://api2.openreview.net/notes/search?'
        'term={}&content=all&group={}&limit={}&offset={}&source=forum'
    ).format(urllib.parse.quote(term), venue_group, limit, offset)

    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research/1.0'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode('utf-8'))

def extract_paper(note):
    """从OpenReview note中提取论文信息"""
    content = note.get('content', {})
    
    def get_val(key):
        v = content.get(key, {})
        if isinstance(v, dict):
            return v.get('value', '')
        return v if isinstance(v, str) else str(v)
    
    title = get_val('title')
    abstract = get_val('abstract')
    
    # venue/decision info
    venue = get_val('venue') or get_val('venueid')
    decision = ''
    for key in ['decision', 'withdrawal_rejection', 'desk_reject_decision']:
        val = get_val(key)
        if val:
            decision = val
            break
    
    # authors
    authors = get_val('authors')
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(',')][:5]
    elif isinstance(authors, list):
        authors = [str(a) for a in authors[:5]]
    else:
        authors = []
    
    forum = note.get('forum', '')
    id_ = note.get('id', '')
    
    return {
        'id': id_,
        'forum': forum,
        'title': title.strip() if title else '',
        'abstract': abstract[:600] if abstract else '',
        'authors': authors,
        'venue': venue,
        'decision': decision,
        'url': 'https://openreview.net/forum?id={}'.format(forum) if forum else '',
    }

def load_ckpt():
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed': [], 'papers': {}}

def save_ckpt(c):
    with open(CHECKPOINT_PATH, 'w', encoding='utf-8') as f:
        json.dump(c, f)

# ============ 主流程 ============
print('=' * 70)
print('OpenReview Collector')
print('Venues: {}'.format([v[1] for v in VENUES]))
print('Search terms: {}'.format(len(SEARCH_TERMS)))
print('=' * 70)

ckpt = load_ckpt()
completed = set(ckpt['completed'])
all_papers = ckpt['papers']  # forum_id -> paper

for venue_group, venue_name in VENUES:
    for term in SEARCH_TERMS:
        task_id = '{}|{}'.format(venue_name, term)
        if task_id in completed:
            continue

        print('\n[{}] {}'.format(venue_name, term))
        offset = 0
        term_new = 0

        while True:
            try:
                data = search_openreview(term, venue_group, limit=100, offset=offset)
                notes = data.get('notes', [])
                count = data.get('count', 0)

                if not notes:
                    break

                for note in notes:
                    p = extract_paper(note)
                    fid = p['forum'] or p['id']
                    if fid and fid not in all_papers:
                        p['venue_name'] = venue_name
                        p['search_term'] = term
                        all_papers[fid] = p
                        term_new += 1

                print('  offset={}: page={}, new={}, total_count={}'.format(
                    offset, len(notes), term_new, count))

                if len(notes) < 100 or offset + 100 >= count:
                    break

                offset += 100
                time.sleep(1)

            except Exception as e:
                if '429' in str(e):
                    print('  RATE LIMITED, wait 30s...')
                    time.sleep(30)
                    continue
                print('  ERROR: {}'.format(str(e)[:60]))
                break

        completed.add(task_id)
        ckpt['completed'] = list(completed)
        ckpt['papers'] = all_papers
        save_ckpt(ckpt)
        print('  -> {} new (total: {})'.format(term_new, len(all_papers)))
        time.sleep(1)

# ============ 汇总 ============
papers_list = list(all_papers.values())
print('\n' + '=' * 70)
print('Total unique papers: {}'.format(len(papers_list)))
print('=' * 70)

# 按venue统计
venue_c = Counter(p.get('venue_name', '?') for p in papers_list)
print('\nBy venue:')
for v, c in venue_c.most_common():
    print('  {}: {}'.format(v, c))

# 按decision统计
dec_c = Counter()
for p in papers_list:
    d = p.get('decision', '').lower()
    if 'accept' in d or 'oral' in d or 'spotlight' in d or 'poster' in d:
        dec_c['Accepted'] += 1
    elif 'reject' in d:
        dec_c['Rejected'] += 1
    elif 'withdraw' in d:
        dec_c['Withdrawn'] += 1
    else:
        dec_c['Unknown/Pending'] += 1

print('\nBy decision:')
for d, c in dec_c.most_common():
    print('  {}: {}'.format(d, c))

# 保存
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump({
        'collected_at': datetime.now().isoformat(),
        'source': 'OpenReview API',
        'venues': [v[1] for v in VENUES],
        'total': len(papers_list),
        'stats_venue': dict(venue_c.most_common()),
        'stats_decision': dict(dec_c.most_common()),
        'papers': papers_list,
    }, f, ensure_ascii=False, indent=2)

print('\nSaved: {} ({:.1f}KB)'.format(OUTPUT_PATH, os.path.getsize(OUTPUT_PATH) / 1024))

# 清理checkpoint
if os.path.exists(CHECKPOINT_PATH):
    os.remove(CHECKPOINT_PATH)
