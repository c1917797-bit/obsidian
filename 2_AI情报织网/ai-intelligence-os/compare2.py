import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Data source 1
with open(r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_strict.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)

# Data source 2
with open(r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os\layers\data\paper_index\paper_index.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

papers1 = data1['papers']
papers2 = data2['papers']

print("Data Source 1: inference_compression_strict.json")
print(f"  Total papers: {len(papers1)}")
print(f"  KV-related: {data1['by_object'].get('kv', 0)}")

print("")
print("Data Source 2: paper_index.json")
print(f"  Total papers: {len(papers2)}")

# Check our filtered KV papers
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

print("")
print(f"Our previous KV filter: {len(our_kv_titles)}")

# Check inference_compression_strict KV titles
print("")
print("=== inference_compression_strict.json KV papers ===")
kv_count = 0
kv_titles = []
for p in papers1:
    if 'kv' in p.get('objects', []):
        kv_count += 1
        kv_titles.append(p.get('title', ''))

print(f"Total KV papers: {kv_count}")
