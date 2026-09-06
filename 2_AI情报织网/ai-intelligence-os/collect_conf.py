"""从 paper Copilot 顶会 JSON 中过滤推理压缩相关论文"""
import requests, json, re, sys

# 修复 Windows cp1252 输出问题
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CONFS = {
    'iclr2025': 'https://raw.githubusercontent.com/Papercopilot/paperlists/main/iclr/iclr2025.json',
    'neurips2025': 'https://raw.githubusercontent.com/Papercopilot/paperlists/main/nips/nips2025.json',
    'icml2025': 'https://raw.githubusercontent.com/Papercopilot/paperlists/main/icml/icml2025.json',
    'cvpr2025': 'https://raw.githubusercontent.com/Papercopilot/paperlists/main/cvpr/cvpr2025.json',
    'acl2025': 'https://raw.githubusercontent.com/Papercopilot/paperlists/main/acl/acl2025.json',
    'corl2025': 'https://raw.githubusercontent.com/Papercopilot/paperlists/main/corl/corl2025.json',
}

KEYWORDS = [
    'kv cache', 'kv-cache', 'key-value cache', 'key value cache',
    'cache eviction', 'cache compression', 'paged attention',
    'prefix caching', 'prefix cache', 'streaming llm',
    'attention cache', 'cache management', 'cache reuse',
    'quantization', 'quantize', 'int8', 'int4', 'int2', 'fp8',
    'weight compression', 'activation compression', 'low-rank',
    'pruning', 'prune', 'sparsity', 'sparse attention',
    'distillation', 'knowledge distillation',
    'inference efficiency', 'inference optimization', 'memory efficient',
    'decoding speed', 'inference latency', 'throughput',
    'speculative decoding', 'draft model', 'tree verification',
    'mixture of experts', 'moe', 'expert routing',
    'communication compression', 'tensor parallelism',
    'long context', 'long-range', 'context compression',
    'eviction policy', 'retention', 'cache hit',
    'llm inference', 'generative inference',
    'continuous batching', 'chunked prefill', 'prefill decode',
]

def load_conf(url, name):
    print(f'Loading {name}...')
    try:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        papers = r.json()
        print(f'  -> {len(papers)} papers loaded')
        return papers
    except Exception as e:
        print(f'  -> ERROR: {e}')
        return []

def is_relevant(paper):
    title = str(paper.get('title', '')).lower()
    abstract = str(paper.get('abstract', '')).lower()
    text = title + ' ' + abstract
    for kw in KEYWORDS:
        if kw.lower() in text:
            return True, kw
    return False, None

# 采集
all_relevant = []
seen_ids = set()
by_conf = {}

for conf, url in CONFS.items():
    papers = load_conf(url, conf)
    rel = []
    for p in papers:
        is_rel, kw = is_relevant(p)
        if is_rel:
            pid = p.get('id') or p.get('paper_id') or ''
            m = re.findall(r'(\d+\.\d+)', str(pid))
            pid = m[0] if m else pid
            rel.append({**p, 'matched_keyword': kw, 'pid': pid})
            if pid not in seen_ids:
                seen_ids.add(pid)
                all_relevant.append({**p, 'matched_keyword': kw, 'conference': conf})
    by_conf[conf] = rel
    print(f'  -> {len(rel)}/{len(papers)} relevant')

print(f'\nTotal unique relevant papers: {len(all_relevant)}')

# 保存
output = {
    'source': 'paper Copilot conferences 2025',
    'total': len(all_relevant),
    'by_conference': by_conf,
    'all': all_relevant,
}
save_path = 'C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/conf_inference_compression_2025.json'
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print(f'Saved: {save_path}')
