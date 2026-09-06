"""
推理压缩论文全面分析 - 中口径
扩展压缩关键词：包含eviction、management、memory-efficient等
"""
import json
from collections import defaultdict

data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# LLM上下文
LLM_CTX = [
    'llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
    'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
    'deployment', 'generation', 'autoregressive', 'neural network',
    'llama', 'mixtral', 'moe', 'decoder', 'attention',
    'kv cache', 'kvcache', 'key-value cache'
]

# 中口径压缩关键词（扩展）
COMPRESS_KW = [
    # 显式压缩
    'quantization', 'quantize', 'quant', 'pruning', 'prune', 'sparse',
    'distillation', 'distill', 'compression', 'compress',
    'low rank', 'low-rank', 'lora',
    # 隐式优化（中口径扩展）
    'memory-efficient', 'memory efficient', 'memory reduction', 'memory optimization',
    'eviction', 'cache management', 'cache optimization', 'cache eviction',
    'efficient', 'speedup', 'acceleration', 'fast', 'throughput',
    'reduction', 'optimization', 'optimize'
]

# 排除非相关领域
EXCLUDE = [
    'image compression', 'video compression', 'audio compression', 'jpeg', 'mpeg',
    'point cloud', '3d gaussian', 'dataset distillation', 'quantum',
    'recommender', 'protein', 'molecule', 'drug discovery'
]

def is_llm_related(title):
    t = title.lower()
    return any(ctx in t for ctx in LLM_CTX)

def has_compress_kw(title):
    t = title.lower()
    return any(kw in t for kw in COMPRESS_KW)

def should_exclude(title):
    t = title.lower()
    return any(ex in t for ex in EXCLUDE)

# 对象推断关键词
KV_KW = ['kv cache', 'kvcache', 'key-value', 'attention state', 'cache evict', 'memory cache']
COMM_KW = ['distributed', 'tensor parallel', 'pipeline parallel', 'model parallel',
           'moe', 'expert', 'all-to-all', 'communication compress', 'allreduce', 'expert routing']

# 压缩方法
METHODS = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', 'fp4', 'low-bit', '2-bit', '4-bit'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured', 'channel', 'head', 'layer prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'sparsification', 'token prune'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student', 'teacher'],
    '低秩(LowRank)': ['low rank', 'low-rank', 'lora', 'svd', 'matrix factorization', 'decomposition'],
    '高效推理(Efficient)': ['memory-efficient', 'memory efficient', 'eviction', 'cache management',
                            'efficient', 'speedup', 'acceleration', 'fast', 'throughput', 'optimization']
}

def infer_objects(title):
    t = title.lower()
    objs = []
    if any(kw in t for kw in KV_KW):
        objs.append('状态(State/KV)')
    if any(kw in t for kw in COMM_KW):
        objs.append('通信(Comm)')
    if not objs:
        objs.append('参数(Weights)')
    return objs

def match_methods(title):
    t = title.lower()
    matched = []
    for method, kws in METHODS.items():
        if any(kw in t for kw in kws):
            matched.append(method)
    return matched

results = []
matrix = defaultdict(list)

for pid, paper in papers.items():
    title = paper.get('title', '')

    if not (is_llm_related(title) and has_compress_kw(title)):
        continue
    if should_exclude(title):
        continue

    methods = match_methods(title)
    if not methods:
        continue

    objs = infer_objects(title)

    results.append({
        'paper_id': pid,
        'title': title,
        'url': paper.get('url', ''),
        'objects': objs,
        'methods': methods
    })

    for o in objs:
        for m in methods:
            matrix[f'{o} x {m}'].append(title)

# 统计
results.sort(key=lambda x: len(x['objects']) + len(x['methods']), reverse=True)

# 输出
print(f'Total: {len(papers)}')
print(f'Filtered: {len(results)}')
print(f'Matrix entries: {len(matrix)}')

# 保存详细结果
output = {
    'total_papers': len(papers),
    'filtered_papers': len(results),
    'matrix': {k: len(v) for k, v in matrix.items()},
    'top_100': [{'title': p['title'], 'objects': p['objects'], 'methods': p['methods']} for p in results[:100]]
}

with open('medium_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# KV papers
kv_papers = [p for p in results if '状态(State/KV)' in p['objects']]
print(f'KV papers: {len(kv_papers)}')

# Save KV papers list
kv_output = {
    'total_kv': len(kv_papers),
    'kv_papers': [{'title': p['title'], 'methods': p['methods']} for p in kv_papers]
}
with open('kv_papers.json', 'w', encoding='utf-8') as f:
    json.dump(kv_output, f, ensure_ascii=False, indent=2)

print('Done')
