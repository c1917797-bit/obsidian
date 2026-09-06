"""
推理压缩论文筛选器
从27784篇论文库中筛选推理压缩相关论文
"""
import json
import os
from collections import defaultdict
from datetime import datetime

# 推理压缩相关关键词
INFERENCE_COMPRESSION_KEYWORDS = {
    # KV Cache相关
    'KV Cache基础': ['kv cache', 'kvcache', 'paged attention', 'cache eviction', 'cache compression', 'key-value cache'],
    'KV管理': ['cache management', 'cache policy', 'cache replacement', 'eviction policy', 'cache reuse', 'prefix cache'],

    # 量化相关
    '量化基础': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', 'fp4', '4bit', '8bit'],
    '量化方法': ['awq', 'gptq', 'gguf', 'smoothquant', 'lleaves', 'quip', 'quik'],
    '量化感知训练': ['quantization aware', 'qat', 'quantization-aware'],

    # 压缩相关
    '压缩基础': ['compression', 'compress', 'pruning', 'prune', 'distillation', 'distill', 'low rank', 'matrix factorization', 'svd'],
    '稀疏化': ['sparse', 'sparsity', 'structured prune'],

    # 推理优化
    '推理延迟': ['latency', 'ttft', 'time to first', 'response time', 'inference speed'],
    '推理吞吐': ['throughput', 'tps', 'qps', 'serving throughput'],
    '推理效率': ['inference efficiency', 'inference optimization', 'serve llm', 'llm serving'],

    # MoE相关
    'MoE基础': ['mixture of expert', 'mixture-of-expert', 'moe', 'mixtral', 'expert'],
    'MoE通信': ['expert routing', 'expert parallel', 'all-to-all', 'alltoall'],

    # 投机解码
    '投机解码': ['speculative', 'specdec', 'draft model', 'medusa', 'eagle', 'lookahead', 'multi-token predict'],

    # 分布式推理
    '分布式推理': ['tensor parallel', 'pipeline parallel', 'data parallel', 'model parallel', 'distributed inference', 'llm inference distributed'],
    'P/D分离': ['prefill decode', 'prefill-decode', 'pd separation', 'disaggregated'],

    # 长上下文
    '长上下文': ['long context', 'long-context', '上下文', 'extended context', 'context window'],
}

# 排除词（减少误判）
EXCLUDE_KEYWORDS = [
    'image compression', 'video compression', 'data compression',
    'speech recognition', 'audio recognition',
]

def check_exclude(title_lower):
    """检查是否应该排除"""
    for ex in EXCLUDE_KEYWORDS:
        if ex in title_lower:
            return True
    return False

def score_paper(paper):
    """给论文打分，判断与推理压缩的相关程度"""
    title = paper.get('title', '').lower()
    title_lower = paper.get('title_lower', '').lower()
    problems = paper.get('problems', [])
    techs = paper.get('techs', [])
    buckets = paper.get('relevance_buckets', [])

    score = 0
    matched_categories = []

    # 检查标题
    for category, keywords in INFERENCE_COMPRESSION_KEYWORDS.items():
        for kw in keywords:
            if kw in title_lower:
                if category not in matched_categories:
                    matched_categories.append(category)
                # 精确匹配权重更高
                if kw in title:
                    score += 3
                else:
                    score += 1
                break

    # 检查标签
    for tag in problems + techs + buckets:
        tag_lower = tag.lower()
        if 'memory' in tag_lower or 'latency' in tag_lower or 'scalability' in tag_lower:
            score += 0.5

    # 排除误判
    if check_exclude(title_lower):
        score = score * 0.1

    return score, matched_categories

def filter_papers(papers, min_score=2):
    """筛选论文"""
    results = []

    for paper_id, paper in papers.items():
        score, categories = score_paper(paper)

        if score >= min_score:
            results.append({
                'paper_id': paper_id,
                'title': paper.get('title', ''),
                'url': paper.get('url', ''),
                'score': score,
                'matched_categories': categories,
                'problems': paper.get('problems', []),
                'techs': paper.get('techs', []),
            })

    # 按分数排序
    results.sort(key=lambda x: -x['score'])
    return results

def categorize_papers(results):
    """按类别分组论文"""
    categories = defaultdict(list)

    for paper in results:
        for cat in paper['matched_categories']:
            categories[cat].append(paper)

    return categories

def main():
    print('='*70)
    print('推理压缩论文筛选器')
    print('='*70)

    # 加载论文
    print('\n[1] 加载论文库...')
    index_path = 'layers/data/paper_index/paper_index.json'
    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data['papers']
    print(f'    总论文数: {len(papers)}')

    # 筛选
    print('\n[2] 筛选推理压缩相关论文...')
    results = filter_papers(papers, min_score=2)
    print(f'    找到 {len(results)} 篇相关论文 (score >= 2)')

    # 分类
    print('\n[3] 按技术类别分组...')
    categories = categorize_papers(results)

    print('\n    类别分布:')
    for cat, papers_list in sorted(categories.items(), key=lambda x: -len(x[1])):
        print(f'      {cat}: {len(papers_list)}篇')

    # 输出Top论文
    print('\n[4] Top 30 高相关论文:')
    print('-'*70)
    for i, paper in enumerate(results[:30], 1):
        cats_str = ', '.join(paper['matched_categories'][:3])
        print(f'\n{i}. [{paper["score"]:.1f}] {paper["title"][:60]}...')
        print(f'   类别: {cats_str}')
        print(f'   链接: {paper["url"] or "N/A"}')

    # 保存结果
    print('\n[5] 保存筛选结果...')
    output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\_corpus'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'inference_compression_filtered.json')

    output_data = {
        'total_papers': len(papers),
        'filtered_count': len(results),
        'filter_date': datetime.now().strftime('%Y-%m-%d'),
        'min_score': 2,
        'categories': {cat: len(papers_list) for cat, papers_list in categories.items()},
        'papers': results
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f'    已保存到: {output_file}')

    # 生成markdown报告
    md_file = os.path.join(output_dir, 'inference_compression_summary.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('# 推理压缩论文筛选报告\n\n')
        f.write(f'**筛选日期**: {datetime.now().strftime("%Y-%m-%d")}\n\n')
        f.write(f'**论文库总数**: {len(papers)}\n')
        f.write(f'**筛选出论文数**: {len(results)}\n')
        f.write(f'**筛选阈值**: score >= 2\n\n')
        f.write('## 类别分布\n\n')
        for cat, papers_list in sorted(categories.items(), key=lambda x: -len(x[1])):
            f.write(f'- **{cat}**: {len(papers_list)}篇\n')
        f.write('\n## 高相关论文 (Top 50)\n\n')
        for i, paper in enumerate(results[:50], 1):
            cats_str = ', '.join(paper['matched_categories'][:3])
            url = paper['url'] or 'N/A'
            f.write(f'{i}. **{paper["title"]}**\n')
            f.write(f'   - 分数: {paper["score"]} | 类别: {cats_str}\n')
            f.write(f'   - 链接: {url}\n\n')

    print(f'    Markdown报告: {md_file}')

    print('\n' + '='*70)
    print('筛选完成')
    print('='*70)

    return results, categories

if __name__ == '__main__':
    main()
