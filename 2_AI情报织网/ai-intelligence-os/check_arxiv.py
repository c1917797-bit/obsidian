import requests, re, json

# 测试几个关键词的总结果数和时间范围
queries = [
    'kv cache quantization',
    'kv cache compression',
    'llm inference quantization',
    'paged attention',
    'mixture of experts inference',
]

one_year_ago = '2025-06-01'
cutoff = '2026-06-26'

for q in queries:
    qp = q.replace(' ', '+')
    url = f'http://export.arxiv.org/api/query?search_query=cat:cs.LG+AND+all:{qp}&max_results=200&sortBy=submittedDate&sortOrder=descending'
    r = requests.get(url, timeout=30)
    
    m = re.search(r'<opensearch:totalResults>(\d+)</opensearch:totalResults>', r.text)
    total = int(m.group(1)) if m else 0
    
    entries = re.split(r'<entry>', r.text)
    dates = []
    for e in entries[1:]:
        d = re.findall(r'<updated>([\d-]+)T', e)
        if d:
            dates.append(d[0])
    
    oldest = min(dates) if dates else 'N/A'
    newest = max(dates) if dates else 'N/A'
    in_year = [d for d in dates if one_year_ago <= d <= cutoff]
    
    print(f'{q}: total={total}, newest={newest}, oldest={oldest}, in_year={len(in_year)}')
