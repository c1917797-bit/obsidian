import json

# Load the analysis
data = json.load(open('full_analysis_v3.json','r',encoding='utf-8'))

# Check if these papers are in the filtered set
target_papers = ['LazyLLM', 'SwiftKV', 'R-KV', 'KIVI', 'SnapKV', 'H2O', 'ClusterKV', 'MUSTAFAR', 'LogQuant']

for p in data['top_100']:
    title = p['title']
    for target in target_papers:
        if target in title:
            print(f'Found: {title[:70]}')
            print(f'  Objects: {p["objects"]}')
            print(f'  Methods: {p["methods"]}')
            print()

# Also check how many total KV papers we have
kv_count = sum(1 for p in data['top_100'] if 'State/KV' in str(p['objects']))
print(f'Total KV papers in top 100: {kv_count}')
