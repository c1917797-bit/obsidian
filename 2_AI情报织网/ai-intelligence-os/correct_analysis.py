"""
推理压缩论文精确分析
基于方法推断对象，而非关键词匹配
"""
import json
from collections import defaultdict

data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# LLM上下文关键词
LLM_KW = [
    'llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
    'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
    'deployment', 'generation', 'autoregressive', 'neural network',
    'llama', 'mixtral', 'moe', 'mixture of expert', 'decoder', 'attention'
]

# 压缩方法关键词
METHOD_KW = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', 'fp4', '4bit', '8bit', 'low-bit', 'low bit'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured', 'channel prune', 'head prune', 'layer prune', 'model prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'sparsification', 'dynamic sparse', 'token prune'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student model', 'teacher'],
    '低秩(LowRank)': ['low rank', 'low-rank', 'lora', 'svd', 'matrix factorization', 'decomposition', 'rank reduction'],
}

# KV/Cache相关关键词
KV_KW = ['kv cache', 'kvcache', 'key-value', 'attention state', 'cache compression', 'kvcompress', 'memory cache']

# 通信相关关键词
COMM_KW = ['distributed', 'tensor parallel', 'pipeline parallel', 'model parallel', 'moe', 'expert', 'all-to-all', 'communication compress', 'allreduce', 'expert routing']

# 排除词
EXCLUDE = [
    'image compression', 'video compression', 'audio compression', 'jpeg', 'mpeg', 'h264',
    'point cloud', '3d gaussian', 'dataset distillation', 'quantum', 'recommender'
]

def has_llm_ctx(title):
    t = title.lower()
    return any(kw in t for kw in LLM_KW)

def should_exclude(title):
    t = title.lower()
    return any(ex in t for ex in EXCLUDE)

def match_methods(title):
    t = title.lower()
    matched = []
    for method, kws in METHOD_KW.items():
        if any(kw in t for kw in kws):
            matched.append(method)
    return matched

def infer_objects(title):
    """根据上下文推断压缩对象"""
    t = title.lower()
    objects = []

    # KV/Cache相关 → 状态
    if any(kw in t for kw in KV_KW):
        objects.append('状态(State/KV)')

    # 通信相关 → 通信
    if any(kw in t for kw in COMM_KW):
        objects.append('通信(Comm)')

    # 其他默认 → 参数（权重量化/剪枝/蒸馏/低秩）
    return objects

def classify_paper(title):
    if not has_llm_ctx(title):
        return None, None
    if should_exclude(title):
        return None, None

    methods = match_methods(title)
    if not methods:
        return None, None

    # 推断对象
    objects = infer_objects(title)

    # 如果没有特殊上下文，所有方法都默认关联参数
    if not objects:
        objects = ['参数(Weights)']

    return objects, methods

# 统计分析
results = []
matrix = defaultdict(list)

for pid, paper in papers.items():
    title = paper.get('title', '')
    objs, methods = classify_paper(title)

    if objs and methods:
        results.append({
            'paper_id': pid,
            'title': title,
            'url': paper.get('url', ''),
            'venue': paper.get('venue', ''),
            'objects': objs,
            'methods': methods
        })

        for o in objs:
            for m in methods:
                matrix[f'{o} x {m}'].append(title)

# 排序
results.sort(key=lambda x: len(x['objects']) + len(x['methods']), reverse=True)

# Save to JSON
output = {
    'total': len(papers),
    'filtered': len(results),
    'matrix': {k: len(v) for k, v in matrix.items()},
    'top_50': [{'title': p['title'], 'objects': p['objects'], 'methods': p['methods']} for p in results[:50]]
}

with open('corrected_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Total: {len(papers)}, Filtered: {len(results)}')
print(f'Matrix entries: {len(matrix)}')
print('Saved to corrected_analysis.json')

# 保存
output = {
    'total': len(papers),
    'filtered': len(results),
    'matrix': {k: len(v) for k, v in matrix.items()},
    'top_50': results[:50]
}

with open('corrected_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print()
print('Saved to corrected_analysis.json')
