"""
重新分析推理压缩论文 - 更准确的筛选逻辑
"""
import json
from collections import defaultdict

data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# 更准确的LLM上下文
LLM_CTX = [
    'llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
    'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
    'deployment', 'generation', 'autoregressive', 'efficient',
    'neural network', 'gpt', 'claude', 'llama', 'mixtral', 'moe',
    'mixture of expert', 'decoder', 'attention'
]

# 压缩对象关键词
OBJECTS = {
    '参数(Weights)': ['weight', 'parameter', 'model weight', 'layer weight',
                      'quantized weight', 'model compression', 'network compress'],
    '状态(State/KV)': ['kv cache', 'kvcache', 'key-value', 'attention state',
                       'activation cache', 'cache', 'memory', 'context'],
    '通信(Comm)': ['distributed', 'tensor parallel', 'pipeline parallel',
                   'model parallel', 'moe', 'expert', 'all-to-all',
                   'communication', 'collective', 'allreduce', 'gpu cluster']
}

# 压缩方法关键词
METHODS = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'low bit', 'int4', 'int8',
                    'fp8', 'fp4', '4bit', '8bit', '4-bit', '8-bit'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured', 'channel', 'head', 'layer prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'dynamic sparse', 'sparsification',
                     'token prune', 'attention prune', 'prune'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student',
                      'distillated', 'teacher'],
    '低秩(LowRank)': ['low rank', 'matrix factorization', 'svd', 'decomposition',
                      'rank', 'low-rank', 'lora', 'adalora'],
}

# 排除词（非LLM/非推理压缩）
EXCLUDE = [
    'image compression', 'video compression', 'audio compression', 'speech compression',
    'jpeg', 'mpeg', 'h264', 'hevc', 'av1', 'vp9', 'point cloud', 'mesh compression',
    '3d gaussian', 'neural radiance', 'dataset distillation', 'data distillation',
    'quantum', 'quantum machine', 'recommendation', 'recommender system',
    'protein', 'molecule', 'drug discovery',  # 生物相关
]

def has_llm_ctx(title):
    t = title.lower()
    return any(ctx in t for ctx in LLM_CTX)

def should_exclude(title):
    t = title.lower()
    return any(ex in t for ex in EXCLUDE)

def match_objects(title):
    t = title.lower()
    matched = []
    for obj, kws in OBJECTS.items():
        if any(kw in t for kw in kws):
            matched.append(obj)
    return matched

def match_methods(title):
    t = title.lower()
    matched = []
    for method, kws in METHODS.items():
        if any(kw in t for kw in kws):
            matched.append(method)
    return matched

def score_paper(title):
    """返回 (总分, 对象列表, 方法列表)"""
    if not has_llm_ctx(title):
        return 0, [], []
    if should_exclude(title):
        return 0, [], []

    objs = match_objects(title)
    methods = match_methods(title)

    if objs or methods:
        score = len(objs) + len(methods)
        return score, objs, methods
    return 0, [], []

# 统计
results = []
matrix = defaultdict(list)

for pid, paper in papers.items():
    title = paper.get('title', '')
    score, objs, methods = score_paper(title)

    if score > 0:
        results.append({
            'paper_id': pid,
            'title': title,
            'url': paper.get('url', ''),
            'venue': paper.get('venue', ''),
            'year': paper.get('year', ''),
            'score': score,
            'objects': objs,
            'methods': methods
        })

        for o in objs:
            for m in methods:
                matrix[f'{o} x {m}'].append(title)

# 排序
results.sort(key=lambda x: -x['score'])

# 写入结果到文件
output = {
    'total_papers': len(papers),
    'filtered_papers': len(results),
    'matrix': {k: len(v) for k, v in matrix.items()},
    'top_papers': results[:100]
}

with open('inference_compression_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Done. Results saved to inference_compression_analysis.json')
print(f'Total papers: {len(papers)}')
print(f'Filtered inference compression papers: {len(results)}')
print(f'Matrix entries: {len(matrix)}')

# Already saved above
