"""
推理压缩论文全面分析 v2
策略：KV cache本身就可以作为LLM上下文的证据
"""
import json
from collections import defaultdict

data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# LLM上下文（扩展：包含KV cache）
LLM_CTX = [
    'llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
    'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
    'deployment', 'generation', 'autoregressive', 'neural network',
    'llama', 'mixtral', 'moe', 'decoder', 'attention',
    # KV cache 本身就是LLM相关的证据
    'kv cache', 'kvcache', 'key-value cache'
]

# 核心压缩关键词
COMPRESS_KW = [
    'quantization', 'quantize', 'quant', 'pruning', 'prune', 'sparse',
    'distillation', 'distill', 'compression', 'compress', 'efficient',
    'low rank', 'low-rank', 'lora', 'acceleration', 'speedup', 'memory',
    'eviction', 'merge', 'reduction'
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
KV_KW = ['kv cache', 'kvcache', 'key-value', 'attention state', 'cache compress', 'memory cache']
COMM_KW = ['distributed', 'tensor parallel', 'pipeline parallel', 'model parallel',
           'moe', 'expert', 'all-to-all', 'communication compress', 'allreduce', 'expert routing']

# 方法推断
METHODS = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', 'fp4', 'low-bit', '2-bit', '4-bit'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured', 'channel', 'head', 'layer prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'sparsification', 'token prune', 'eviction'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student', 'teacher'],
    '低秩(LowRank)': ['low rank', 'low-rank', 'lora', 'svd', 'matrix factorization', 'decomposition'],
    '高效推理(Efficient)': ['acceleration', 'speedup', 'efficient', 'fast', 'memory reduction', 'reduction']
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

# 筛选
results = []
matrix = defaultdict(list)

for pid, paper in papers.items():
    title = paper.get('title', '')

    # 必须同时满足：LLM上下文 + 压缩关键词
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

# 保存
output = {
    'total': len(papers),
    'filtered': len(results),
    'matrix': {k: len(v) for k, v in matrix.items()},
    'top_100': [{'title': p['title'], 'objects': p['objects'], 'methods': p['methods']} for p in results[:100]]
}

with open('full_analysis_v2.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Done. Filtered: {len(results)}, Matrix entries: {len(matrix)}')
