import json
from collections import defaultdict

with open(r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_strict.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

papers = data['papers']
total = data['strict_filtered_count'] + data['marginal_count']

print(f'Total papers: {total}')
print(f'Filtered: {data["strict_filtered_count"]}')
print(f'Marginal: {data["marginal_count"]}')
print()

# By object
print('=== By Object ===')
for k, v in data['by_object'].items():
    print(f'  {k}: {v}')

print()
print('=== By Method ===')
for k, v in data['by_method'].items():
    print(f'  {k}: {v}')

# Build object x method matrix
matrix = defaultdict(list)
kv_papers = []

for p in papers:
    objs = p.get('objects', [])
    methods = p.get('methods', [])

    for o in objs:
        for m in methods:
            if o != 'unclear' and m != 'unclear':
                matrix[f'{o} x {m}'].append(p['title'])

    if 'kv' in objs:
        rating = p.get('rating')
        rating_val = rating[0] if rating and rating[0] else 0
        kv_papers.append({
            'title': p['title'],
            'methods': methods,
            'conference': p.get('conference', ''),
            'rating': rating_val
        })

print()
print(f'=== Object x Method Matrix ===')
for k, v in sorted(matrix.items(), key=lambda x: -len(x[1])):
    print(f'  {k}: {len(v)}')

# Sort KV papers by rating
kv_papers.sort(key=lambda x: -x.get('rating', [0])[0] if x.get('rating') else 0)

print()
print(f'=== KV Papers: {len(kv_papers)} ===')
print('\nTop KV Papers by Rating:')
for p in kv_papers[:30]:
    rating = p.get('rating', [0, 0])
    rating_val = rating[0] if rating else 0
    print(f'  [{p["conference"]}] {rating_val:.2f} - {p["title"][:60]}')
    print(f'      Methods: {p["methods"]}')
