# -*- coding: utf-8 -*-
"""
build_corpus_index.py
- 扫描 _corpus/ 所有 .md 文件
- 解析 YAML front matter
- 输出 papers_meta.json + papers_index.csv
"""
import os
import json
import re
import csv
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CORPUS_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\_corpus'
OUTPUT_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察'

def parse_front_matter(content):
    """解析 YAML front matter"""
    if not content.startswith('---'):
        return None, content

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return None, content

    yaml_text = content[3:end_idx].strip()
    body = content[end_idx+3:].strip()

    meta = {}
    current_key = None
    current_list = None

    for line in yaml_text.split('\n'):
        if not line.strip():
            continue

        if line.startswith('  -') and current_list is not None:
            current_list.append(line.strip()[2:].strip())
            continue

        if ':' in line and not line.startswith(' '):
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()

            if value == '|' or value == '>':
                current_key = key
                meta[key] = ''
                continue

            if value == '' or value is None:
                current_list = []
                meta[key] = current_list
                current_key = None
                continue

            if value.startswith('[') and value.endswith(']'):
                items = [x.strip().strip('"').strip("'") for x in value[1:-1].split(',') if x.strip()]
                meta[key] = items
                current_key = None
                current_list = None
            else:
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                meta[key] = value
                current_key = None
                current_list = None

    return meta, body

def extract_title_from_body(body):
    """从 markdown body 提取标题"""
    match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def infer_grid(method_techs):
    """根据 matched_techs 推断 42格"""
    tech_to_grid = {
        'Quantization': 'W×Q',
        'Pruning': 'W×P',
        'Distillation': 'W×D',
        'Sparsity': 'W×S',
        'Low-rank': 'W×L',
        'KV Cache': 'K×Q',
        'Communication': 'C×Q',
        'Speculative Decoding': 'S×G',
        'MoE': 'C×G',
        'Quantization-Aware': 'W×Q',
    }

    if not method_techs:
        return None

    for tech in method_techs:
        if tech in tech_to_grid:
            return tech_to_grid[tech]

    return None

def infer_scenario(problems):
    """根据 matched_problems 推断场景"""
    problem_to_scenario = {
        'Throughput': 'LLM',
        'Quantization': 'LLM',
        'Agent': 'Agent',
        'LongContext': 'LLM',
        'Multimodal': '多模态',
        'Speech': 'ASR',
        'TTS': 'TTS',
    }

    if not problems:
        return None

    for p in problems:
        if p in problem_to_scenario:
            return problem_to_scenario[p]

    return None

def main():
    print(f"扫描目录: {CORPUS_DIR}")

    corpus_path = Path(CORPUS_DIR)
    if not corpus_path.exists():
        print(f"错误: 目录不存在 {CORPUS_DIR}")
        return

    md_files = list(corpus_path.glob('*.md'))
    print(f"找到 {len(md_files)} 个 .md 文件")

    papers = []
    failed = []

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            meta, body = parse_front_matter(content)

            if not meta:
                failed.append(md_file.name)
                continue

            title = meta.get('title', '').strip().strip('"')
            body_title = extract_title_from_body(body)
            if body_title and (not title or len(title) < 5):
                title = body_title

            paper = {
                'citekey': meta.get('citekey', md_file.stem),
                'title': title,
                'authors': meta.get('authors', ''),
                'year': meta.get('year', ''),
                'venue': meta.get('venue', ''),
                'url': meta.get('url', ''),
                'abstract': meta.get('abstract', ''),
                'citation_count': meta.get('citation_count', '0'),
                'relevance_score': meta.get('relevance_score', '0'),
                'matched_problems': meta.get('matched_problems', []),
                'matched_techs': meta.get('matched_techs', []),
                'pre_screened_status': meta.get('pre_screened_status', ''),
                'source': meta.get('source', ''),
                'created': meta.get('created', ''),
                'grid': infer_grid(meta.get('matched_techs', [])),
                'scenario': infer_scenario(meta.get('matched_problems', [])),
            }

            papers.append(paper)

        except Exception as e:
            print(f"解析失败 {md_file.name}: {e}")
            failed.append(md_file.name)

    print(f"\n成功解析: {len(papers)} 篇")
    print(f"失败: {len(failed)} 个文件")

    meta_json_path = os.path.join(OUTPUT_DIR, 'papers_meta.json')
    with open(meta_json_path, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"输出: {meta_json_path}")

    csv_path = os.path.join(OUTPUT_DIR, 'papers_index.csv')
    with open(csv_path, 'w', encoding='utf-8', newline='', errors='replace') as f:
        writer = csv.writer(f)
        writer.writerow([
            'citekey', 'title', 'year', 'venue', 'url',
            'matched_problems', 'matched_techs', 'grid', 'scenario',
            'relevance_score', 'citation_count'
        ])
        for p in papers:
            problems = '|'.join(p['matched_problems']) if isinstance(p['matched_problems'], list) else p['matched_problems']
            techs = '|'.join(p['matched_techs']) if isinstance(p['matched_techs'], list) else p['matched_techs']
            writer.writerow([
                p['citekey'],
                p['title'][:200] if p['title'] else '',
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
    print(f"输出: {csv_path}")

    grid_stats = {}
    scenario_stats = {}
    for p in papers:
        g = p['grid'] or 'Unclassified'
        grid_stats[g] = grid_stats.get(g, 0) + 1
        s = p['scenario'] or 'Unclassified'
        scenario_stats[s] = scenario_stats.get(s, 0) + 1

    print("\n=== 42格分布 ===")
    for g, count in sorted(grid_stats.items(), key=lambda x: -x[1]):
        print(f"  {g}: {count}")

    print("\n=== 场景分布 ===")
    for s, count in sorted(scenario_stats.items(), key=lambda x: -x[1]):
        print(f"  {s}: {count}")

    if failed:
        print(f"\n失败文件: {failed[:10]}{'...' if len(failed) > 10 else ''}")

    return papers

if __name__ == '__main__':
    papers = main()
