"""
继续完成 OpenReview 采集 - 专注于 NeurIPS/ICML/ACL/EMNLP
用搜索API而非venue过滤，因为venue过滤被403禁用
对每个venue只跑少量特定查询
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, json, time, urllib.request, urllib.parse, re
from collections import Counter
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

VENUES = [
    ('NeurIPS.cc/2025/Conference', 'NeurIPS 2025'),
    ('ICML.cc/2025/Conference', 'ICML 2025'),
    ('ACL.org/2025/Conference', 'ACL 2025'),
    ('EMNLP/2024/Conference', 'EMNLP 2024'),
]

# 用针对性短语而非宽词，确保返回的论文确实相关
SPECIFIC_TERMS = [
    'quantization',
    'pruning compression',
    'distillation efficient',
    'KV cache',
    'speculative decoding',
    'model compression',
    'inference acceleration',
    'sparse attention',
    'low-rank',
    'token compression',
    'memory efficient',
    'mixture of experts efficient',
]

CHECKPOINT = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\_or_venue_supp_ckpt.json'

def load_ckpt():
    if os.path.exists(CHECKPOINT):
        with open(CHECKPOINT, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed': [], 'arxiv_to_venue': {}, 'paper_data': {}}

def save_ckpt(c):
    with open(CHECKPOINT, 'w', encoding='utf-8') as f:
        json.dump(c, f)

ckpt = load_ckpt()
arxiv_to_venue = ckpt['arxiv_to_venue']
paper_data = ckpt['paper_data']
completed = set(ckpt['completed'])

def extract_arxiv_id_from_note(note):
    """从OpenReview note提取arxiv_id"""
    content = note.get('content', {})
    
    # 方法1: 显式字段
    for key in ['arxiv_id', 'code', '_bibtex', 'supplementary_material']:
        val = content.get(key, {})
        if isinstance(val, dict):
            val = val.get('value', '')
        if isinstance(val, str):
            m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)', val)
            if m:
                return m.group(1).replace('v1', '').replace('v2', '')
    
    # 方法2: HTML字段
    for key in ['HTML', 'abstract', 'venue']:
        val = content.get(key, {})
        if isinstance(val, dict):
            val = val.get('value', '')
        if isinstance(val, str):
            m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)', val)
            if m:
                return m.group(1).replace('v1', '').replace('v2', '')
    
    # 方法3: 通过PDF url
    for key in ['pdf', 'code']:
        val = content.get(key, {})
        if isinstance(val, dict):
            val = val.get('value', '')
        if isinstance(val, str) and 'arxiv.org' in val:
            m = re.search(r'(\d{4}\.\d{4,5}(?:v\d+)?)', val)
            if m:
                return m.group(1).replace('v1', '').replace('v2', '')
    
    return None

def search_or(term, group, limit=100, offset=0):
    url = (
        'https://api2.openreview.net/notes/search?'
        'term={}&content=all&group={}&limit={}&offset={}&source=forum&details=replyCount,presentation'
    ).format(urllib.parse.quote(term), group, limit, offset)
    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research/1.0'})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode('utf-8'))

for venue_id, venue_name in VENUES:
    for term in SPECIFIC_TERMS:
        task_id = '{}|{}'.format(venue_name, term)
        if task_id in completed:
            continue
        
        print('\n[{}] {}'.format(venue_name, term))
        offset = 0
        term_new = 0
        
        while True:
            try:
                data = search_or(term, venue_id, limit=1000, offset=offset)
                notes = data.get('notes', [])
                count = data.get('count', 0)
                
                if not notes:
                    break
                
                for note in notes:
                    forum = note.get('forum', '')
                    arxiv_id = extract_arxiv_id_from_note(note)
                    if arxiv_id:
                        arxiv_to_venue[arxiv_id] = {
                            'venue': venue_name,
                            'forum': forum,
                        }
                        term_new += 1
                    
                    # 也保存完整paper数据以防后续用
                    if forum and forum not in paper_data:
                        paper_data[forum] = {
                            'forum': forum,
                            'title': note.get('content', {}).get('title', {}).get('value', '') if isinstance(note.get('content', {}).get('title'), dict) else note.get('content', {}).get('title', ''),
                            'venue_name': venue_name,
                            'search_term': term,
                            'arxiv_id': arxiv_id,
                        }
                
                print('  offset={}: page={}, arxiv_found={}'.format(
                    offset, len(notes), term_new))
                
                if len(notes) < 1000 or offset + 1000 >= count:
                    break
                
                offset += 1000
                time.sleep(1)
                
            except Exception as e:
                if '429' in str(e):
                    print('  RATE LIMITED, wait 60s...')
                    time.sleep(60)
                    continue
                print('  ERROR: {}'.format(str(e)[:60]))
                break
        
        completed.add(task_id)
        ckpt['completed'] = list(completed)
        ckpt['arxiv_to_venue'] = arxiv_to_venue
        ckpt['paper_data'] = paper_data
        save_ckpt(ckpt)
        time.sleep(1)
        print('  -> total arxiv mappings: {}'.format(len(arxiv_to_venue)))

# 保存
out = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\or_arxiv_venue_map.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump({
        'collected_at': datetime.now().isoformat(),
        'source': 'OpenReview search',
        'total_arxiv_mappings': len(arxiv_to_venue),
        'by_venue': dict(Counter(v['venue'] for v in arxiv_to_venue.values())),
        'map': arxiv_to_venue,
    }, f, ensure_ascii=False, indent=2)

print('\n=== Summary ===')
print('Total arxiv_id mappings: {}'.format(len(arxiv_to_venue)))
counter = Counter(v['venue'] for v in arxiv_to_venue.values())
for v, c in counter.most_common():
    print('  {}: {}'.format(v, c))
print('Saved: {}'.format(out))

if os.path.exists(CHECKPOINT):
    os.remove(CHECKPOINT)
