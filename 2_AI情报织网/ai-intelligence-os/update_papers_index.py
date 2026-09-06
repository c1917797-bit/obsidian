# -*- coding: utf-8 -*-
"""
update_papers_index.py
- 根据 papers_meta_v2.json 更新 papers_index.csv
- 替换旧 CSV
"""
import os
import json
import csv
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

META_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\papers_meta_v2.json'
CSV_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\papers_index.csv'

def main():
    with open(META_PATH, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    print(f"已加载: {len(papers)} 篇")

    with open(CSV_PATH, 'w', encoding='utf-8', newline='', errors='replace') as f:
        writer = csv.writer(f)
        writer.writerow([
            'citekey', 'title', 'year', 'venue', 'url',
            'matched_problems', 'matched_techs', 'grid', 'scenario',
            'relevance_score', 'citation_count'
        ])
        for p in papers:
            problems = '|'.join(p['matched_problems']) if isinstance(p['matched_problems'], list) else (p['matched_problems'] or '')
            techs = '|'.join(p['matched_techs']) if isinstance(p['matched_techs'], list) else (p['matched_techs'] or '')
            writer.writerow([
                p['citekey'],
                (p['title'] or '')[:200],
                p['year'],
                p['venue'],
                p['url'],
                problems,
                techs,
                p['grid'] or '',
                p['scenario'] or '',
                p['relevance_score'],
                p['citation_count'],
            ])
    print(f"已更新: {CSV_PATH}")

    print("\n=== Grid 分布 ===")
    grid_count = defaultdict(int)
    for p in papers:
        grid_count[p.get('grid') or 'Unclassified'] += 1
    for g, c in sorted(grid_count.items(), key=lambda x: -x[1]):
        print(f"  {g}: {c}")

    print("\n=== Scenario 分布 ===")
    scenario_count = defaultdict(int)
    for p in papers:
        scenario_count[p.get('scenario') or 'Unclassified'] += 1
    for s, c in sorted(scenario_count.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")

    csv_unclassified_grid = 0
    csv_unclassified_scenario = 0
    for p in papers:
        if not p.get('grid') or p['grid'] == 'Unclassified':
            csv_unclassified_grid += 1
        if not p.get('scenario') or p['scenario'] == 'Unclassified':
            csv_unclassified_scenario += 1
    print(f"\n未分类 grid: {csv_unclassified_grid} ({csv_unclassified_grid*100/len(papers):.1f}%)")
    print(f"未分类 scenario: {csv_unclassified_scenario} ({csv_unclassified_scenario*100/len(papers):.1f}%)")

if __name__ == '__main__':
    main()
