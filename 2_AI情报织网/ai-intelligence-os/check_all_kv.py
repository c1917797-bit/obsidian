import json

# Load the full analysis results
with open('full_analysis_v3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Search for LazyLLM in all filtered papers
found_lazyllm = False
for p in data['top_100']:
    if 'LazyLLM' in p['title']:
        print(f'Found LazyLLM in top 100:')
        print(f'  Title: {p["title"]}')
        print(f'  Objects: {p["objects"]}')
        print(f'  Methods: {p["methods"]}')
        found_lazyllm = True

if not found_lazyllm:
    print('LazyLLM not in top 100')

# Also check the matrix for 状态 papers
print(f'\n=== Matrix ===')
for k, v in data['matrix'].items():
    print(f'{k}: {v}')

# Count total KV papers
kv_papers = [p for p in data['top_100'] if 'State/KV' in str(p['objects'])]
print(f'\n=== KV Papers in top 100: {len(kv_papers)} ===')
for p in kv_papers[:20]:
    print(f'  - {p["title"][:60]}')
