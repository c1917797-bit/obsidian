import json

# 加载两个数据源
print("=== 数据源对比 ===\n")

# 数据源1: inference_compression_strict.json (专门整理的)
with open(r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_strict.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)

# 数据源2: paper_index.json (原始论文库)
with open(r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os\layers\data\paper_index\paper_index.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

papers1 = data1['papers']
papers2 = data2['papers']

print("数据源1: inference_compression_strict.json")
print(f"  - 总论文数: {len(papers1)}")
print(f"  - KV相关: {data1['by_object'].get('kv', 0)}")

print("\n数据源2: paper_index.json")
print(f"  - 总论文数: {len(papers2)}")

# 统计我们之前筛选的结果
LLM_CTX = ['llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
            'diffusion model', 'vlm', 'multimodal', 'inference', 'serving',
            'deployment', 'generation', 'autoregressive', 'neural network',
            'llama', 'mixtral', 'moe', 'decoder', 'attention',
            'kv cache', 'kvcache', 'key-value cache']

COMPRESS_KW = ['quantization', 'quantize', 'quant', 'pruning', 'prune', 'sparse',
                'distillation', 'distill', 'compression', 'compress',
                'low rank', 'low-rank', 'lora', 'memory reduction']

KV_KW = ['kv cache', 'kvcache', 'key-value']

our_kv_titles = []
for pid, p in papers2.items():
    title = p.get('title', '').lower()
    if any(ctx in title for ctx in LLM_CTX) and any(kw in title for kw in COMPRESS_KW):
        if any(kv in title for kv in KV_KW):
            our_kv_titles.append(p.get('title', ''))

print(f"\n我们之前筛选的KV相关: {len(our_kv_titles)}")

# 检查inference_compression_strict中的KV论文标题
print("\n=== inference_compression_strict.json 中的 KV论文标题 (前30) ===")
kv_count = 0
kv_titles = []
for p in papers1:
    if 'kv' in p.get('objects', []):
        kv_count += 1
        kv_titles.append(p.get('title', ''))

print(f"总KV论文: {kv_count}")
print("\n前30个标题:")
for i, t in enumerate(kv_titles[:30], 1):
    print(f"{i}. {t[:70]}")

# 对比我们筛选的标题
print("\n=== 我们之前筛选的 KV论文标题 (前30) ===")
print(f"总KV论文: {len(our_kv_titles)}")
print("\n前30个标题:")
for i, t in enumerate(our_kv_titles[:30], 1):
    print(f"{i}. {t[:70]}")
