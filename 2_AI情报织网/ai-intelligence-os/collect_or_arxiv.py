"""
专用OpenReview采集器: 获取NeurIPS/ICML/ACL/CVPR的所有投稿，提取arxiv_id
不依赖term搜索，直接通过venue_id filter获取
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, json, time, urllib.request, urllib.parse, re
from collections import Counter
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 直接通过venue ID获取所有投稿，效率高且准确
VENUES = [
    ('NeurIPS.cc/2025/Conference/-/Submission', 'NeurIPS 2025'),
    ('ICML.cc/2025/Conference/-/Submission', 'ICML 2025'),
    ('ACL.org/2025/Conference/-/Submission', 'ACL 2025'),
    ('CVPR/2025/Conference/-/Submission', 'CVPR 2025'),
    ('EMNLP/2024/Conference/-/Submission', 'EMNLP 2024'),
]

# OAI-style API endpoint for venue submissions
def get_submissions(venue_id, limit=1000, offset=0):
    """通过venue_id获取所有投稿"""
    url = (
        'https://api2.openreview.net/notes?'
        'content.venueid={}&'
        'limit={}&offset={}&'
        'details=replyCount,presentation,writable'
    ).format(venue_id, limit, offset)
    req = urllib.request.Request(url, headers={'User-Agent': 'AI-Research/1.0'})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode('utf-8'))

def extract_arxiv_id(content):
    """从OpenReview content中提取arxiv_id"""
    # 方法1: content._bibtex或content.arxiv_id字段
    for key in ['arxiv_id', 'code', '_bibtex']:
        val = content.get(key, '')
        if isinstance(val, str):
            m = re.search(r'arxiv[:\s]*(\d{4}\.\d{4,5}(?:v\d+)?)', val.lower())
            if m:
                return m.group(1)
    
    # 方法2: 从HTML字段提取
    for key in ['code', 'HTML', 'abstract']:
        val = content.get(key, '')
        if isinstance(val, dict):
            val = val.get('value', '')
        if isinstance(val, str):
            m = re.search(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', val)
            if m:
                return m.group(1)
    
    return None

CHECKPOINT = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\_or_venue_checkpoint.json'
def load_ckpt():
    if os.path.exists(CHECKPOINT):
        with open(CHECKPOINT, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed': [], 'arxiv_to_venue': {}}
def save_ckpt(c):
    with open(CHECKPOINT, 'w', encoding='utf-8') as f:
        json.dump(c, f)

ckpt = load_ckpt()
arxiv_to_venue = ckpt['arxiv_to_venue']
completed = set(ckpt['completed'])

for venue_id, venue_name in VENUES:
    if venue_name in completed:
        print('SKIP: {}'.format(venue_name))
        continue
    
    print('\n=== {} ==='.format(venue_name))
    offset = 0
    total_for_venue = 0
    
    while True:
        try:
            data = get_submissions(venue_id, limit=1000, offset=offset)
            notes = data.get('notes', [])
            count = data.get('count', 0)
            
            if not notes:
                print('  No more notes')
                break
            
            venue_new = 0
            for note in notes:
                content = note.get('content', {})
                
                # 提取arxiv_id
                arxiv_id = extract_arxiv_id(content)
                if arxiv_id:
                    arxiv_to_venue[arxiv_id] = {
                        'venue': venue_name,
                        'forum': note.get('forum', ''),
                    }
                    venue_new += 1
                
                total_for_venue += 1
            
            print('  offset={}: page={}, total={}, arxiv_id_found={}'.format(
                offset, len(notes), total_for_venue, venue_new))
            
            if len(notes) < 1000:
                break
            
            offset += 1000
            time.sleep(2)
            
        except Exception as e:
            if '429' in str(e):
                print('  RATE LIMITED, wait 60s...')
                time.sleep(60)
                continue
            print('  ERROR: {}'.format(str(e)[:80]))
            break
    
    completed.add(venue_name)
    ckpt['arxiv_to_venue'] = arxiv_to_venue
    ckpt['completed'] = list(completed)
    save_ckpt(ckpt)
    print('  -> {} total, {} with arxiv_id, checkpoint saved'.format(
        total_for_venue, sum(1 for k,v in arxiv_to_venue.items() if v['venue']==venue_name)))
    time.sleep(3)

# ============ 保存arxiv->venue映射 ============
out = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\or_arxiv_venue_map.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump({
        'collected_at': datetime.now().isoformat(),
        'source': 'OpenReview (NeurIPS 2025/ICML 2025/ACL 2025/CVPR 2025/EMNLP 2024)',
        'total_with_arxiv_id': len(arxiv_to_venue),
        'map': arxiv_to_venue,
    }, f, ensure_ascii=False, indent=2)

print('\n=== Summary ===')
print('Total arxiv_id mappings: {}'.format(len(arxiv_to_venue)))
counter = Counter(v['venue'] for v in arxiv_to_venue.values())
for v, c in counter.most_common():
    print('  {}: {}'.format(v, c))
print('Saved: {}'.format(out))

# 清理
if os.path.exists(CHECKPOINT):
    os.remove(CHECKPOINT)
