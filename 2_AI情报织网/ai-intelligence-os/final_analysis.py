import json
from collections import defaultdict

data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

LLM_CTX = ['llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
            'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
            'deployment', 'generation', 'autoregressive', 'neural network',
            'llama', 'mixtral', 'moe', 'decoder', 'attention',
            'kv cache', 'kvcache', 'key-value cache']

COMPRESS_KW = ['quantization', 'quantize', 'quant', 'pruning', 'prune', 'sparse',
                'distillation', 'distill', 'compression', 'compress',
                'low rank', 'low-rank', 'lora', 'memory reduction']

EXCLUDE = ['image compression', 'video compression', 'audio compression', 'jpeg', 'mpeg',
           'point cloud', '3d gaussian', 'dataset distillation', 'quantum',
           'recommender', 'protein', 'molecule', 'drug discovery']

KV_KW = ['kv cache', 'kvcache', 'key-value', 'attention state', 'cache compress', 'memory cache']
COMM_KW = ['distributed', 'tensor parallel', 'pipeline parallel', 'model parallel',
           'moe', 'expert', 'all-to-all', 'communication compress', 'allreduce', 'expert routing']

METHODS = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', 'fp4', 'low-bit', '2-bit', '4-bit'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured', 'channel', 'head', 'layer prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'sparsification', 'token prune'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student', 'teacher'],
    '低秩(LowRank)': ['low rank', 'low-rank', 'lora', 'svd', 'matrix factorization', 'decomposition'],
}

def is_llm_related(title):
    t = title.lower()
    return any(ctx in t for ctx in LLM_CTX)

def has_compress_kw(title):
    t = title.lower()
    return any(kw in t for kw in COMPRESS_KW)

def should_exclude(title):
    t = title.lower()
    return any(ex in t for ex in EXCLUDE)

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

    results.append({'paper_id': pid, 'title': title, 'objects': objs, 'methods': methods})

    for o in objs:
        for m in methods:
            matrix[f'{o} x {m}'].append(title)

# Save to JSON
output = {
    'total_papers': len(papers),
    'filtered_papers': len(results),
    'matrix': {k: len(v) for k, v in matrix.items()},
    'all_kv_papers': [p['title'] for p in results if '状态(State/KV)' in p['objects']]
}

with open('final_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print('Done')
print(f'Total: {len(papers)}')
print(f'Filtered: {len(results)}')
print(f'KV papers: {len([p for p in results if "状态(State/KV)" in p["objects"]])}')
