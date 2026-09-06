"""
推理压缩论文筛选器 v2
针对核心研究方向：参数/状态/通信压缩 × 量化/剪枝/稀疏/蒸馏
"""
import json
import os
from collections import defaultdict
from datetime import datetime

# ============== 核心研究方向关键词 ==============

# 压缩对象
COMPRESSION_OBJECTS = {
    # 参数压缩
    '参数_权重': ['weight quantization', 'model quantization', 'parameter compress', 'layer compression', 'network compression'],
    '参数_权重INT': ['int4', 'int8', 'fp8', 'fp4', '4-bit', '8-bit', 'quantized weights', 'weight only quantization'],

    # 状态压缩 (KV Cache)
    '状态_KVCache': ['kv cache', 'kvcache', 'key-value cache', 'cache compression', 'cache evict', 'cache reuse', 'cache management'],
    '状态_注意力状态': ['attention state', 'activation cache', 'state compression', 'context compression'],
    '状态_Memory': ['memory efficient', 'memory optimization', 'memory compression', 'activation compression'],

    # 通信压缩
    '通信_分布式': ['distributed inference', 'tensor parallel', 'pipeline parallel', 'model parallel'],
    '通信_MoE': ['mixture of expert', 'moe', 'expert routing', 'expert parallel', 'all-to-all communication'],
    '通信_聚合': ['collective communication', 'allreduce', 'broadcast', 'communication compression'],
}

# 压缩方法
COMPRESSION_METHODS = {
    '方法_量化': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', '4bit', '8bit', 'low bit'],
    '方法_剪枝': ['pruning', 'prune', 'structured prune', 'unstructured prune', 'channel prune', 'head prune'],
    '方法_稀疏': ['sparse', 'sparsity', 'sparse attention', 'dynamic sparse', 'sparsification'],
    '方法_蒸馏': ['distillation', 'distill', 'knowledge distill', 'model compress', 'small language model', 'student model'],
    '方法_低秩': ['low rank', 'matrix factorization', 'svd', 'rank reduction', 'kron'],
}

# 推理优化相关（加分项）
INFERENCE_OPT = {
    '推理_延迟': ['latency', 'ttft', 'time to first', 'response time', 'inference delay'],
    '推理_吞吐': ['throughput', 'inference throughput', 'serving', 'llm serving'],
    '推理_投机': ['speculative', 'specdec', 'draft model', 'medusa', 'eagle', 'lookahead'],
}

# ============== 排除词 ==============
EXCLUDE = [
    'image compression', 'video compression', 'audio compression', 'speech compression',
    'data compression algorithm', 'lossless compression',
    'feature compression', 'signal compression',
    'jpeg', 'mpeg', 'h264', 'hevc', 'av1',
    'neural render', ' radiance field', '3d gaussian',
    'point cloud', 'mesh compression',
]

def should_exclude(title_lower):
    """检查是否应该排除"""
    for ex in EXCLUDE:
        if ex in title_lower:
            return True
    return False

def score_paper(paper):
    """
    给论文打分
    核心逻辑：压缩对象 × 压缩方法都必须匹配
    """
    title = paper.get('title', '')
    title_lower = title.lower()

    # 排除词过滤
    if should_exclude(title_lower):
        return 0, {}, {}

    # 检查压缩对象
    matched_objects = {}
    object_score = 0
    for obj, keywords in COMPRESSION_OBJECTS.items():
        for kw in keywords:
            if kw in title_lower:
                matched_objects[obj] = True
                object_score += 2
                break

    # 检查压缩方法
    matched_methods = {}
    method_score = 0
    for method, keywords in COMPRESSION_METHODS.items():
        for kw in keywords:
            if kw in title_lower:
                matched_methods[method] = True
                method_score += 2
                break

    # 检查推理优化（额外加分）
    inference_bonus = 0
    for inf, keywords in INFERENCE_OPT.items():
        for kw in keywords:
            if kw in title_lower:
                inference_bonus += 0.5
                break

    # 核心逻辑：必须有对象+方法
    has_object = len(matched_objects) > 0
    has_method = len(matched_methods) > 0

    if has_object and has_method:
        # 双重匹配，分数加成
        total_score = object_score + method_score + inference_bonus
        # 对象和方法越多，分数越高
        total_score += (len(matched_objects) - 1) * 1 + (len(matched_methods) - 1) * 1
    else:
        total_score = 0

    return total_score, matched_objects, matched_methods

def filter_papers(papers, min_score=4):
    """筛选论文（需要对象+方法双重匹配）"""
    results = []

    for paper_id, paper in papers.items():
        score, objects, methods = score_paper(paper)

        if score >= min_score:
            results.append({
                'paper_id': paper_id,
                'title': paper.get('title', ''),
                'url': paper.get('url', ''),
                'venue': paper.get('venue', ''),
                'year': paper.get('year', ''),
                'score': score,
                'matched_objects': list(objects.keys()),
                'matched_methods': list(methods.keys()),
                'problems': paper.get('problems', []),
                'techs': paper.get('techs', []),
            })

    results.sort(key=lambda x: -x['score'])
    return results

def categorize_papers(results):
    """按压缩对象×方法矩阵分组"""
    categories = defaultdict(list)

    for paper in results:
        # 组合主键
        objs = '/'.join(sorted(paper['matched_objects']))
        meths = '/'.join(sorted(paper['matched_methods']))
        key = f"{objs} × {meths}"
        categories[key].append(paper)

    return categories

def main():
    print('='*70)
    print('推理压缩论文筛选器 v2')
    print('核心: 参数/状态/通信压缩 × 量化/剪枝/稀疏/蒸馏')
    print('='*70)

    # 加载
    print('\n[1] 加载论文库...')
    with open('layers/data/paper_index/paper_index.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    papers = data['papers']
    print(f'    总论文数: {len(papers)}')

    # 筛选
    print('\n[2] 筛选论文 (对象+方法双重匹配)...')
    results = filter_papers(papers, min_score=4)
    print(f'    找到 {len(results)} 篇相关论文 (score >= 4)')

    # 分类
    print('\n[3] 按压缩对象×方法分组...')
    categories = categorize_papers(results)

    print('\n    类别分布:')
    for cat, papers_list in sorted(categories.items(), key=lambda x: -len(x[1])):
        print(f'      {cat}: {len(papers_list)}篇')

    # 按压缩对象统计
    obj_stats = defaultdict(int)
    for p in results:
        for o in p['matched_objects']:
            obj_stats[o] += 1

    print('\n    按压缩对象:')
    for o, c in sorted(obj_stats.items(), key=lambda x: -x[1]):
        print(f'      {o}: {c}篇')

    # 按压缩方法统计
    method_stats = defaultdict(int)
    for p in results:
        for m in p['matched_methods']:
            method_stats[m] += 1

    print('\n    按压缩方法:')
    for m, c in sorted(method_stats.items(), key=lambda x: -x[1]):
        print(f'      {m}: {c}篇')

    # Top论文
    print('\n[4] Top 40 高相关论文:')
    print('-'*70)
    for i, paper in enumerate(results[:40], 1):
        objs = ', '.join(paper['matched_objects'])
        meths = ', '.join(paper['matched_methods'])
        print(f'\n{i}. [{paper["score"]:.1f}] {paper["title"][:65]}...')
        print(f'   对象: {objs}')
        print(f'   方法: {meths}')

    # 保存
    print('\n[5] 保存结果...')
    output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\_corpus'
    os.makedirs(output_dir, exist_ok=True)

    # JSON
    output_file = os.path.join(output_dir, 'inference_compression_v2.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_papers': len(papers),
            'filtered_count': len(results),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'papers': results
        }, f, ensure_ascii=False, indent=2)
    print(f'    JSON: {output_file}')

    # Markdown报告
    md_file = os.path.join(output_dir, 'inference_compression_v2_summary.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('# 推理压缩论文筛选报告 v2\n\n')
        f.write(f'**日期**: {datetime.now().strftime("%Y-%m-%d")}\n')
        f.write(f'**论文库总数**: {len(papers)}\n')
        f.write(f'**筛选出论文数**: {len(results)}\n')
        f.write(f'**筛选条件**: 压缩对象+方法双重匹配，score >= 4\n\n')

        f.write('## 按压缩对象统计\n\n')
        for o, c in sorted(obj_stats.items(), key=lambda x: -x[1]):
            f.write(f'- **{o}**: {c}篇\n')

        f.write('\n## 按压缩方法统计\n\n')
        for m, c in sorted(method_stats.items(), key=lambda x: -x[1]):
            f.write(f'- **{m}**: {c}篇\n')

        f.write('\n## 按对象×方法组合统计\n\n')
        for cat, papers_list in sorted(categories.items(), key=lambda x: -len(x[1]))[:20]:
            f.write(f'- **{cat}**: {len(papers_list)}篇\n')

        f.write('\n## Top 50 论文\n\n')
        for i, paper in enumerate(results[:50], 1):
            objs = ', '.join(paper['matched_objects'])
            meths = ', '.join(paper['matched_methods'])
            url = paper['url'] or 'N/A'
            f.write(f'{i}. **{paper["title"]}**\n')
            f.write(f'   - 分数: {paper["score"]} | 对象: {objs} | 方法: {meths}\n')
            f.write(f'   - 链接: {url}\n\n')

    print(f'    Markdown: {md_file}')
    print('\n' + '='*70)

if __name__ == '__main__':
    main()
