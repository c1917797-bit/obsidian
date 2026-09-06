import json

# Load the analysis
data = json.load(open('full_analysis_v3.json','r',encoding='utf-8'))

# Check if these papers are in the filtered set
target_papers = ['LazyLLM', 'SwiftKV', 'R-KV', 'KIVI', 'SnapKV', 'H2O', 'ClusterKV', 'MUSTAFAR', 'LogQuant']

found = []
for p in data['top_100']:
    title = p['title']
    for target in target_papers:
        if target in title:
            found.append(title)

print(f'Found {len(found)} target papers in top 100:')
for t in found:
    print(f'  - {t[:60]}')

# Count KV papers
kv_count = sum(1 for p in data['top_100'] if 'State/KV' in str(p['objects']))
print(f'\nTotal KV papers in top 100: {kv_count}')

# Check total filtered
print(f'\nTotal filtered papers: {data["filtered"]}')
