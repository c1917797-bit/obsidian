import json
data = json.load(open('layers/data/paper_index/paper_index.json','r',encoding='utf-8'))
papers = data['papers']

# Check for specific KV cache papers
target_papers = ['SnapKV', 'H2O', 'LazyLLM', 'R-KV', 'KIVI', 'KVQuant', 'SwiftKV', 'ClusterKV']

for pid, p in papers.items():
    title = p.get('title', '').lower()
    for target in target_papers:
        if target.lower() in title:
            print(f'Found: {p.get("title", "")[:70]}')
