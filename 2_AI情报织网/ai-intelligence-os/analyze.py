import json, re
from collections import Counter

with open('C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/conf_inference_compression_2025.json', encoding='utf-8') as f:
    d = json.load(f)

papers = d['all']
print(f'Total: {len(papers)} papers')

conf_count = Counter(p['conference'] for p in papers)
print('\nBy conference:')
for c, n in conf_count.most_common():
    print(f'  {c}: {n}')

kw_count = Counter(p['matched_keyword'] for p in papers)
print('\nTop matched keywords:')
for kw, n in kw_count.most_common(30):
    print(f'  [{n:4d}] {kw}')

# 多关键词论文（高度相关）
kw_by_pid = {}
for p in papers:
    pid = p.get('pid', '')
    if pid not in kw_by_pid:
        kw_by_pid[pid] = {'kws': set(), 'paper': p}
    kw_by_pid[pid]['kws'].add(p['matched_keyword'])

multi_kw = [(v['paper'], len(v['kws'])) for v in kw_by_pid.values()]
multi_kw.sort(key=lambda x: -x[1])
print(f'\nMost relevant papers (multiple keyword matches):')
for p, cnt in multi_kw[:15]:
    title = p.get('title', '')[:70]
    print(f'  [{cnt}] {title}')

# 显示各主题数量
theme_papers = {
    'KV Cache Quantization/Compression': [],
    'KV Cache Management/Eviction': [],
    'Weight Quantization': [],
    'Speculative Decoding': [],
    'MoE / Expert Routing': [],
    'Inference System Optimization': [],
    'Long Context': [],
    'Distillation': [],
}

for pid, v in kw_by_pid.items():
    kws = v['kws']
    if any(k in kws for k in ['kv cache', 'kv-cache', 'key-value cache', 'key value cache']):
        if any(k in kws for k in ['quantization', 'int8', 'int4', 'int2', 'fp8', 'low-rank', 'weight compression']):
            theme_papers['KV Cache Quantization/Compression'].append(v['paper'])
        elif any(k in kws for k in ['eviction', 'streaming llm', 'paged attention', 'cache management', 'cache eviction']):
            theme_papers['KV Cache Management/Eviction'].append(v['paper'])
    if any(k in kws for k in ['quantization', 'int8', 'int4', 'int2', 'fp8']) and 'llm' in str(kws):
        theme_papers['Weight Quantization'].append(v['paper'])
    if any(k in kws for k in ['speculative decoding', 'draft model']):
        theme_papers['Speculative Decoding'].append(v['paper'])
    if any(k in kws for k in ['mixture of experts', 'moe', 'expert routing']):
        theme_papers['MoE / Expert Routing'].append(v['paper'])
    if any(k in kws for k in ['inference efficiency', 'inference optimization', 'inference latency', 'throughput', 'decoding speed']):
        theme_papers['Inference System Optimization'].append(v['paper'])
    if any(k in kws for k in ['long context', 'context compression']):
        theme_papers['Long Context'].append(v['paper'])
    if any(k in kws for k in ['distillation', 'knowledge distillation']):
        theme_papers['Distillation'].append(v['paper'])

print('\n=== Theme distribution (unique papers) ===')
for theme, ps in sorted(theme_papers.items(), key=lambda x: -len(x[1])):
    if ps:
        print(f'  {theme}: {len(ps)}')
