"""回溯采集过去一年的推理压缩论文"""
import requests
import re
import json
import time
from datetime import datetime, timedelta

QUERIES = [
    'kv cache quantization',
    'kv cache compression',
    'llm quantization inference',
    'llm pruning inference inference',
    'paged attention',
    'prefix caching llm',
    'mixture of experts communication inference',
    'llm inference memory',
    'speculative decoding',
    'streaming llm',
    'layer skipping inference',
    'continuous batching',
]

ONE_YEAR_AGO = '2025-06-01'
CUTOFF_DATE = '2026-06-26'
MAX_RESULTS_PER_QUERY = 300  # 多取一些再过滤

seen_ids = set()
results_by_query = {}

for q in QUERIES:
    query_param = q.replace(' ', '+')
    url = f'http://export.arxiv.org/api/query?search_query=cat:cs.LG+AND+all:{query_param}&max_results={MAX_RESULTS_PER_QUERY}&sortBy=submittedDate&sortOrder=descending'
    
    print(f'Querying: {q}...', end=' ', flush=True)
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        
        # 提取所有条目
        entries = re.split(r'<entry>', r.text)
        entries = [e for e in entries if '<id>http://arxiv.org/abs/' in e]
        
        count_in_year = 0
        papers = []
        for entry in entries:
            ids = re.findall(r'<id>http://arxiv.org/abs/([0-9.]+)</id>', entry)
            dates = re.findall(r'<updated>([\d-]+)T', entry)
            titles = re.findall(r'<title[^>]*>([^<]+)</title>', entry)
            summaries = re.findall(r'<summary[^>]*>([^<]+)</summary>', entry)
            authors_list = re.findall(r'<author>.*?<name>([^<]+)</name>', entry)
            
            if ids and dates:
                aid = ids[0]
                date = dates[0]
                title = titles[0].strip().replace('\n', ' ') if titles else ''
                summary = summaries[0].strip().replace('\n', ' ')[:300] if summaries else ''
                authors = authors_list[:3] if authors_list else []
                
                if ONE_YEAR_AGO <= date <= CUTOFF_DATE and aid not in seen_ids:
                    seen_ids.add(aid)
                    count_in_year += 1
                    papers.append({
                        'id': aid,
                        'date': date,
                        'title': title,
                        'summary': summary,
                        'authors': authors,
                        'query': q,
                    })
        
        results_by_query[q] = papers
        print(f'{count_in_year} papers (total entries: {len(entries)})')
        
    except Exception as e:
        print(f'ERROR: {e}')
        results_by_query[q] = []
    
    time.sleep(0.5)  # 避免限流

# 汇总
all_papers = []
for q, papers in results_by_query.items():
    all_papers.extend(papers)

# 按日期排序（新的在前）
all_papers.sort(key=lambda x: x['date'], reverse=True)

print(f'\n=== 汇总 ===')
print(f'查询词数: {len(QUERIES)}')
print(f'总唯一论文: {len(all_papers)}')
for q, papers in sorted(results_by_query.items(), key=lambda x: -len(x[1])):
    print(f'  {q}: {len(papers)}')

# 保存
output = {
    'collected_at': datetime.now().isoformat(),
    'date_range': f'{ONE_YEAR_AGO} to {CUTOFF_DATE}',
    'total_unique': len(all_papers),
    'papers': all_papers,
}

with open('C:/Users/Huawei/Documents/code/Obsidian/4_AI情报洞察/inference_compression_arxiv_1year.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'\n已保存到 inference_compression_arxiv_1year.json')
