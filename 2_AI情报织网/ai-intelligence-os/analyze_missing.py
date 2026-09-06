import json
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

KV_KW = ['kv', 'kvcache', 'key-value', 'key value', 'attention state', 'cache', 'memory']

llm_kv_papers = []
for pid, p in papers.items():
    title = p.get('title', '').lower()
    if any(ctx in title for ctx in LLM_CTX) and any(kw in title for kw in KV_KW):
        llm_kv_papers.append(title)

print(f'LLM + KV papers: {len(llm_kv_papers)}')

# 分析这些论文为什么没被筛选
missing_no_comp = []
missing_excluded = []

for title in llm_kv_papers:
    has_comp = any(kw in title for kw in COMPRESS_KW)
    is_excluded = any(ex in title for ex in EXCLUDE)

    if not has_comp:
        missing_no_comp.append(title)
    elif is_excluded:
        missing_excluded.append(title)

print(f'Missing - no compress keyword: {len(missing_no_comp)}')
print(f'Missing - excluded: {len(missing_excluded)}')
print()
print('=== Sample missing titles (no compress keyword) ===')
for t in missing_no_comp[:25]:
    print(f'  - {t[:70]}')
