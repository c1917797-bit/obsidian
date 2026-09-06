import json

data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# 更宽松的LLM上下文
LLM_CTX = ['llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
            'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
            'deployment', 'generation', 'autoregressive', 'efficient', 'neural network']

# 压缩相关关键词
COMP_KW = ['quantization', 'quantize', 'quant', 'pruning', 'prune', 'sparse',
           'distillation', 'distill', 'compression', 'compress', 'memory',
           'kv cache', 'cache', 'acceleration', 'speedup', 'efficient',
           'low rank', 'sparsification']

# 排除词
EXCLUDE = ['image compression', 'video compression', 'audio compression',
           'jpeg', 'mpeg', 'h264', 'hevc', 'av1', 'vp9', 'point cloud',
           'mesh compression', '3d gaussian', 'neural radiance',
           'dataset distillation', 'data distillation', 'quantum',
           'recommendation', 'recommender']

def is_llm(title):
    t = title.lower()
    return any(ctx in t for ctx in LLM_CTX)

def is_comp(title):
    t = title.lower()
    return any(kw in t for kw in COMP_KW)

def should_exclude(title):
    t = title.lower()
    return any(ex in t for ex in EXCLUDE)

# 统计
total = 0
titles = []
for pid, p in papers.items():
    title = p.get('title', '')
    if is_llm(title) and is_comp(title) and not should_exclude(title):
        total += 1
        titles.append(title)

print(f'=== Loose filter inference compression papers: {total} ===')

# 分析kv/cache相关但不含llm的
kv_not_llm_titles = []
for pid, p in papers.items():
    title = p.get('title', '')
    t = title.lower()
    if ('kv cache' in t or 'cache' in t or 'memory' in t) and 'llm' not in t:
        if not any(ex in t for ex in EXCLUDE):
            kv_not_llm_titles.append(title)

print(f'\n=== Papers with kv/cache/memory but no llm: {len(kv_not_llm_titles)} ===')
for t in kv_not_llm_titles[:20]:
    print(f'  - {t[:70]}')

# 统计各关键词组合
print('\n=== Keyword Stats ===')
kw_stats = {}
for kw in ['quantization', 'pruning', 'sparse', 'distillation', 'kv cache', 'memory', 'efficient', 'inference']:
    kw_stats[kw] = sum(1 for t in titles if kw in t.lower())
print(f'  quantization: {kw_stats.get("quantization", 0)}')
print(f'  pruning: {kw_stats.get("pruning", 0)}')
print(f'  sparse: {kw_stats.get("sparse", 0)}')
print(f'  distillation: {kw_stats.get("distillation", 0)}')
print(f'  kv cache: {kw_stats.get("kv cache", 0)}')
print(f'  memory: {kw_stats.get("memory", 0)}')
print(f'  efficient: {kw_stats.get("efficient", 0)}')
print(f'  inference: {kw_stats.get("inference", 0)}')
