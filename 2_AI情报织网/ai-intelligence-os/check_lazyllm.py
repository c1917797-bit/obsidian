import json
data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# Check LazyLLM paper
for pid, p in papers.items():
    title = p.get('title', '').lower()
    if 'lazyllm' in title:
        print(f'Found: {p.get("title")}')
        print(f'URL: {p.get("url")}')

        # Check if it would pass our filter
        LLM_CTX = ['llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
                    'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
                    'deployment', 'generation', 'autoregressive', 'neural network',
                    'llama', 'mixtral', 'moe', 'decoder', 'attention',
                    'kv cache', 'kvcache', 'key-value cache']

        COMPRESS_KW = ['quantization', 'quantize', 'quant', 'pruning', 'prune', 'sparse',
                        'distillation', 'distill', 'compression', 'compress',
                        'low rank', 'low-rank', 'lora', 'memory reduction']

        t = title
        has_llm = any(ctx in t for ctx in LLM_CTX)
        has_comp = any(kw in t for kw in COMPRESS_KW)

        print(f'Has LLM context: {has_llm}')
        print(f'Has compress kw: {has_comp}')
        print(f'Would pass filter: {has_llm and has_comp}')

        # Check exact keywords
        print(f'\nKeywords found:')
        for ctx in LLM_CTX:
            if ctx in t:
                print(f'  LLM: {ctx}')
        for kw in COMPRESS_KW:
            if kw in t:
                print(f'  Comp: {kw}')
        break
