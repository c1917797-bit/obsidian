import json
data = json.load(open('full_analysis_v3.json','r',encoding='utf-8'))

kv_papers = [p for p in data['top_100'] if 'State/KV' in str(p['objects'])]
print(f'KV papers in top 100: {len(kv_papers)}')
for p in kv_papers[:20]:
    title = p['title']
    print(f'  - {title[:60]}')
