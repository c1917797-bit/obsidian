import json
data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

LLM_CTX = ['llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
            'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
            'deployment', 'generation', 'autoregressive', 'neural network',
            'llama', 'mixtral', 'moe', 'decoder', 'attention']

COMPRESS_KW = ['quantization', 'pruning', 'spars', 'distill', 'compress',
                'efficient', 'low rank', 'lora', 'acceleration', 'speedup']

kv_papers = []
for pid, p in papers.items():
    title = p.get('title', '').lower()
    if 'kv cache' in title or 'kvcache' in title or 'key-value cache' in title:
        has_llm = any(ctx in title for ctx in LLM_CTX)
        has_comp = any(kw in title for kw in COMPRESS_KW)
        kv_papers.append({
            'title': p.get('title', ''),
            'has_llm': has_llm,
            'has_comp': has_comp,
            'both': has_llm and has_comp
        })

print(f'Total KV cache papers: {len(kv_papers)}')
has_llm_count = sum(1 for p in kv_papers if p['has_llm'])
has_comp_count = sum(1 for p in kv_papers if p['has_comp'])
both_count = sum(1 for p in kv_papers if p['both'])
print(f'Has LLM context: {has_llm_count}')
print(f'Has compress kw: {has_comp_count}')
print(f'Has both: {both_count}')

print()
print('=== Papers missing LLM context (first 20) ===')
for p in kv_papers[:20]:
    if not p['has_llm']:
        print(f'  - {p["title"][:70]}')
