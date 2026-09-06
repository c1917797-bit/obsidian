"""
全量精读增强 - 处理剩余11,941篇
- 自适应限流处理
- 长跑稳定版
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

# 加载进度（核心300 + 增量）
already_done = set()
enriched_results = {}

for path in [PROGRESS_PATH, r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\enriched_papers_progress.json']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        already_done |= set(d.get('done', []))
        enriched_results.update(d.get('results', {}))

print('Total already done (including core 300):', len(already_done))

# 文件索引 - 用arxiv_id前缀
FILE_INDEX = {}
import os
for cell_dir in os.listdir(META_ROOT):
    if cell_dir.startswith('_'):
        continue
    cell_path = os.path.join(META_ROOT, cell_dir)
    if not os.path.isdir(cell_path):
        continue
    for f in os.listdir(cell_path):
        m = re.match(r'^(\d{4}\.\d{4,5})_', f)
        if m:
            FILE_INDEX[m.group(1)] = os.path.join(cell_path, f)
print('File index size:', len(FILE_INDEX))

# 收集待处理
to_process = []
for p in v8['papers']:
    aid = p.get('arxiv_id','')
    if not aid or aid in already_done:
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

# ============ 自适应LLM调用 ============
sleep_time = 0.5
consecutive_errors = 0

def llm_extract(title, abstract, max_retries=3):
    global sleep_time, consecutive_errors
    
    prompt = '分析论文，给出1句核心创新（25字内）：\n标题:{}\n摘要:{}\n回答:'.format(
        title[:150], (abstract or '无')[:600])
    
    for attempt in range(max_retries):
        try:
            resp = llm.chat([{'role':'user','content':prompt}], max_tokens=80)
            innov = resp.strip().split('\n')[0].strip()
            innov = re.sub(r'^[:：。\.\s]+', '', innov)
            innov = re.sub(r'\.$', '', innov)
            if 5 < len(innov) < 200:
                consecutive_errors = 0
                # 成功：逐步减少sleep
                sleep_time = max(0.3, sleep_time - 0.05)
                return innov
            return None
        except Exception as e:
            err = str(e).lower()
            consecutive_errors += 1
            
            # 限流检测
            if 'rate' in err or '429' in err or 'throttle' in err or 'limit' in err:
                sleep_time = min(20, sleep_time * 2)  # 增加sleep
                time.sleep(sleep_time)
                if attempt < max_retries - 1:
                    continue
            
            # 其他错误
            if attempt < max_retries - 1:
                time.sleep(sleep_time * (attempt + 1))
                continue
            
            return None

def update_md(fpath, innovation):
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
print('\n=== Start processing ===', flush=True)
start_time = time.time()
processed_count = 0
new_enriched = 0
fail_count = 0

BATCH_SAVE = 50  # 更频繁保存

for i, item in enumerate(to_process):
    innov = llm_extract(item['title'], item['abstract'])
    
    if innov:
        if update_md(item['fpath'], innov):
            new_enriched += 1
            enriched_results[item['aid']] = {
                'title': item['title'][:60],
                'innovation': innov[:80],
            }
    else:
        fail_count += 1
    
    processed_count += 1
    already_done.add(item['aid'])
    
    # 打印+保存
    if (i+1) % BATCH_SAVE == 0 or (i+1) == len(to_process):
        elapsed = time.time() - start_time
        rate = (i+1) / elapsed if elapsed > 0 else 0
        eta = (len(to_process) - i - 1) / rate if rate > 0 else 0
        msg = '[{}/{}] new={}, fail={}, sleep={:.1f}s, eta={:.0f}m'.format(
            i+1, len(to_process), new_enriched, fail_count, sleep_time, eta/60)
        print(msg, flush=True)
        
        with open(PROGRESS_PATH, 'w', encoding='utf-8') as f:
            json.dump({
                'last_update': datetime.now().isoformat(),
                'done': list(already_done),
                'results': enriched_results,
                'total_processed': processed_count,
                'failures': fail_count,
            }, f, ensure_ascii=False, indent=2)
    
    time.sleep(sleep_time)
    
    # 限流严重时额外等待
    if consecutive_errors >= 3:
        print('  -- rate limiting detected, sleep 60s --', flush=True)
        time.sleep(60)
        consecutive_errors = 0
        sleep_time = 1.0  # 重置

elapsed = time.time() - start_time
print('\n=== Done ===', flush=True)
print('Processed: {}, enriched: {}, fail: {}'.format(processed_count, new_enriched, fail_count), flush=True)
print('Total all enriched: {}'.format(len(enriched_results)), flush=True)
print('Elapsed: {:.0f}m'.format(elapsed/60), flush=True)