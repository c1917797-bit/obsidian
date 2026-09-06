"""
扩展LLM补全 - 处理剩余14,107篇论文
优化策略:
  - 简化prompt(只取key_innovation)
  - 1.0s间隔
  - 20篇checkpoint
  - 支持续跑
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
V8_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_v8.json'
FULL_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_optimization_full_tagged.json'
PROGRESS_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\enrich_all_progress.json'

# 加载
with open(V8_PATH, 'r', encoding='utf-8-sig') as f:
    v8 = json.load(f)

with open(FULL_PATH, 'r', encoding='utf-8-sig') as f:
    full = json.load(f)
full_index = {p.get('arxiv_id'): p for p in full['papers'] if p.get('arxiv_id')}

# 已有进度
already_done = set()
enriched_results = {}
if os.path.exists(PROGRESS_PATH):
    with open(PROGRESS_PATH, 'r', encoding='utf-8') as f:
        progress = json.load(f)
    already_done = set(progress.get('done', []))
    enriched_results = progress.get('results', {})
print('Resuming: {} done'.format(len(already_done)))

# 通过arxiv_id找文件
FILE_INDEX = {}
for cell_dir in os.listdir(META_ROOT):
    cell_path = os.path.join(META_ROOT, cell_dir)
    if not os.path.isdir(cell_path) or cell_dir.startswith('_'):
        continue
    for f in os.listdir(cell_path):
        m = re.match(r'^(\d{4}\.\d{4,5})_', f)
        if m:
            aid = m.group(1)
            FILE_INDEX[aid] = os.path.join(cell_path, f)
print('File index: {} arxiv_ids'.format(len(FILE_INDEX)))

# 收集待处理 - 跳过已有
to_process = []
for p in v8['papers']:
    aid = p.get('arxiv_id','')
    if not aid:
        # 用title hash做ID
        title = p.get('title','')
        if title:
            import hashlib
            aid = hashlib.md5(title.encode('utf-8')).hexdigest()[:8]
    
    if aid in already_done:
        continue
    if aid not in FILE_INDEX:
        continue
    
    title = p.get('title','')
    if not title or len(title) < 5:
        continue
    
    abstract = p.get('abstract', '')
    
    to_process.append({
        'aid': aid,
        'title': title,
        'abstract': abstract,
        'fpath': FILE_INDEX[aid],
    })

print('To process: {}'.format(len(to_process)))

# ============ 处理 ============
def llm_extract(title, abstract, max_retries=3):
    """单句创新点"""
    prompt = '分析论文，给出1句核心创新（25字内）：\n标题:{}\n摘要:{}\n回答:'.format(
        title[:150], (abstract or '无')[:600])
    
    for attempt in range(max_retries):
        try:
            resp = llm.chat([{'role':'user','content':prompt}], max_tokens=80)
            innov = resp.strip().split('\n')[0].strip()
            innov = re.sub(r'^[:：。\.\s]+', '', innov)
            innov = re.sub(r'\.$', '', innov)
            if 5 < len(innov) < 200:
                return innov
            return None
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            return None

def update_md(fpath, innovation):
    """更新key_innovation字段"""
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(
        r'key_innovation: ".*?"',
        lambda m, t=innovation: 'key_innovation: "{}"'.format(t.replace('"', '\\"').replace('\\', '\\\\')),
        content
    )
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# ============ 主循环 ============
print('\n=== Processing ===')
start_time = time.time()
processed_count = 0
new_enriched = 0
fail_count = 0

BATCH_SAVE = 30
SLEEP_BETWEEN = 0.6  # 减少sleep时间

for i, item in enumerate(to_process):
    aid = item['aid']
    
    innov = llm_extract(item['title'], item['abstract'])
    
    if innov:
        if update_md(item['fpath'], innov):
            new_enriched += 1
            enriched_results[aid] = {
                'title': item['title'][:60],
                'innovation': innov[:80],
            }
    else:
        fail_count += 1
    
    processed_count += 1
    already_done.add(aid)
    
    # 每30篇保存+打印进度
    if (i+1) % BATCH_SAVE == 0 or (i+1) == len(to_process):
        elapsed = time.time() - start_time
        rate = (i+1) / elapsed if elapsed > 0 else 0
        eta = (len(to_process) - i - 1) / rate if rate > 0 else 0
        print('  [{}/{}] new={}, fail={}, rate={:.1f}/s, eta={:.0f}s ({:.0f}m)'.format(
            i+1, len(to_process), new_enriched, fail_count, rate, eta, eta/60))
        
        # 保存
        with open(PROGRESS_PATH, 'w', encoding='utf-8') as f:
            json.dump({
                'last_update': datetime.now().isoformat(),
                'done': list(already_done),
                'results': enriched_results,
                'total_processed': processed_count,
                'failures': fail_count,
            }, f, ensure_ascii=False, indent=2)
    
    time.sleep(SLEEP_BETWEEN)

elapsed = time.time() - start_time
print('\n=== Final ===')
print('Processed: {}'.format(processed_count))
print('New enriched: {}'.format(new_enriched))
print('Failures: {}'.format(fail_count))
print('Total in v2/all: {}'.format(len(enriched_results)))
print('Elapsed: {:.0f}s ({:.1f}m)'.format(elapsed, elapsed/60))