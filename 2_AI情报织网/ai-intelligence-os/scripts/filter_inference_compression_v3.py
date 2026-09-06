"""
推理压缩论文筛选器 v3
研究框架：压缩对象(参数/状态/通信) × 压缩方法(量化/剪枝/稀疏/蒸馏)
"""
import json
import os
from collections import defaultdict
from datetime import datetime

# ============== 你的研究框架关键词 ==============

# 压缩对象
OBJECTS = {
    '参数(Weights)': ['weight quantization', 'model quantization', 'parameter compress',
                      'layer compression', 'network compression', 'int4', 'int8', 'fp8',
                      'quantized weights', 'weight only', 'model compression',
                      'llm quantization', 'neural network quantization'],
    '状态(State/KV)': ['kv cache', 'kvcache', 'key-value cache', 'cache compress',
                       'attention state', 'activation cache', 'state compress',
                       'context compress', 'kv', 'memory efficient', 'memory compress',
                       'activation compress'],
    '通信(Comm)': ['distributed inference', 'tensor parallel', 'pipeline parallel',
                   'model parallel', 'mixture of expert', 'moe', 'expert routing',
                   'expert parallel', 'all-to-all', 'communication compress',
                   'collective communication', 'allreduce', 'moe inference',
                   'expert', 'mixture-of-expert'],
}

# 压缩方法
METHODS = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'low bit', 'int4', 'int8',
                    'fp8', 'fp4', '4bit', '8bit', '4-bit', '8-bit', 'quantized'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured prune', 'unstructured prune',
                    'channel prune', 'head prune', 'layer prune', 'model prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'dynamic sparse', 'sparsification',
                     'sparse attention', 'sparse inference', 'token prune'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student model',
                      'compress model', 'small language model', 'distillated'],
    '低秩(LowRank)': ['low rank', 'matrix factorization', 'svd', 'rank reduction',
                      'kron', 'decomposition', 'low-rank'],
}

# ============== 排除词 ==============
EXCLUDE = [
    'image compression', 'video compression', 'audio compression',
    'jpeg', 'mpeg', 'h264', 'hevc', 'av1',
    'point cloud', 'mesh compression',
    'neural render', ' radiance field', '3d gaussian',
]

def should_exclude(title_lower):
    for ex in EXCLUDE:
        if ex in title_lower:
            return True
    return False

def score_paper(paper):
    """宽松筛选 + 框架分类"""
    title_lower = paper.get('title', '').lower()

    if should_exclude(title_lower):
        return 0, {}, {}

    # 检查对象
    matched_objects = {}
    for obj, keywords in OBJECTS.items():
        for kw in keywords:
            if kw in title_lower:
                matched_objects[obj] = True
                break

    # 检查方法
    matched_methods = {}
    for method, keywords in METHODS.items():
        for kw in keywords:
            if kw in title_lower:
                matched_methods[method] = True
                break

    # 宽松：只要匹配对象或方法之一
    if matched_objects or matched_methods:
        score = len(matched_objects) + len(matched_methods)
        return score, matched_objects, matched_methods

    return 0, {}, {}

def filter_and_categorize(papers):
    """筛选并分类"""
    results = []
    obj_method_matrix = defaultdict(list)

    for paper_id, paper in papers.items():
        score, objects, methods = score_paper(paper)

        if score > 0:
            paper_data = {
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
            }
            results.append(paper_data)

            # 按对象×方法矩阵分组
            objs = paper_data['matched_objects']
            meths = paper_data['matched_methods']

            if objs and meths:
                for o in objs:
                    for m in meths:
                        obj_method_matrix[f"{o} × {m}"].append(paper_data)
            elif objs:
                for o in objs:
                    obj_method_matrix[f"{o} × 其他"].append(paper_data)
            elif meths:
                for m in meths:
                    obj_method_matrix[f"其他 × {m}"].append(paper_data)

    results.sort(key=lambda x: -x['score'])
    return results, obj_method_matrix

def main():
    print('='*70)
    print('推理压缩论文筛选器 v3')
    print('研究框架: 对象(参数/状态/通信) × 方法(量化/剪枝/稀疏/蒸馏)')
    print('='*70)

    # 加载
    print('\n[1] 加载论文库...')
    with open('layers/data/paper_index/paper_index.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    papers = data['papers']
    print(f'    总论文数: {len(papers)}')

    # 筛选+分类
    print('\n[2] 筛选并分类...')
    results, matrix = filter_and_categorize(papers)
    print(f'    推理压缩论文总数: {len(results)}')

    # 统计
    print('\n[3] 统计分布...')

    # 按对象统计
    obj_counts = defaultdict(int)
    for p in results:
        for o in p['matched_objects']:
            obj_counts[o] += 1

    print('\n    按压缩对象:')
    for o, c in sorted(obj_counts.items(), key=lambda x: -x[1]):
        print(f'      {o}: {c}篇')

    # 按方法统计
    method_counts = defaultdict(int)
    for p in results:
        for m in p['matched_methods']:
            method_counts[m] += 1

    print('\n    按压缩方法:')
    for m, c in sorted(method_counts.items(), key=lambda x: -x[1]):
        print(f'      {m}: {c}篇')

    # 对象×方法矩阵
    print('\n    对象×方法矩阵:')
    for key, papers_list in sorted(matrix.items(), key=lambda x: -len(x[1])):
        print(f'      {key}: {len(papers_list)}篇')

    # Top论文
    print('\n[4] Top 20 高相关论文:')
    print('-'*70)
    for i, p in enumerate(results[:20], 1):
        objs = '/'.join(p['matched_objects'])
        meths = '/'.join(p['matched_methods'])
        print(f'\n{i}. [{p["score"]}] {p["title"][:60]}...')
        print(f'   对象: {objs} | 方法: {meths}')

    # 保存
    print('\n[5] 保存结果...')
    output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\_corpus'
    os.makedirs(output_dir, exist_ok=True)

    # JSON
    output_file = os.path.join(output_dir, 'inference_compression_v3.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_papers': len(papers),
            'filtered_count': len(results),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'papers': results,
            'matrix': {k: len(v) for k, v in matrix.items()}
        }, f, ensure_ascii=False, indent=2)
    print(f'    JSON: {output_file}')

    # Markdown
    md_file = os.path.join(output_dir, 'inference_compression_v3_summary.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('# 推理压缩论文筛选报告 v3\n\n')
        f.write(f'**日期**: {datetime.now().strftime("%Y-%m-%d")}\n')
        f.write(f'**论文库总数**: {len(papers)}\n')
        f.write(f'**推理压缩论文数**: {len(results)}\n\n')

        f.write('## 按压缩对象统计\n\n')
        for o, c in sorted(obj_counts.items(), key=lambda x: -x[1]):
            f.write(f'- **{o}**: {c}篇\n')

        f.write('\n## 按压缩方法统计\n\n')
        for m, c in sorted(method_counts.items(), key=lambda x: -x[1]):
            f.write(f'- **{m}**: {c}篇\n')

        f.write('\n## 对象×方法矩阵\n\n')
        f.write('| 对象 | 方法 | 论文数 |\n')
        f.write('|------|------|--------|\n')
        for key, papers_list in sorted(matrix.items(), key=lambda x: -len(x[1])):
            f.write(f'| {key.replace(" × ", " | ")} | {len(papers_list)} |\n')

        f.write('\n## Top 50 论文\n\n')
        for i, p in enumerate(results[:50], 1):
            objs = ', '.join(p['matched_objects'])
            meths = ', '.join(p['matched_methods'])
            f.write(f'{i}. **{p["title"]}**\n')
            f.write(f'   - 分数: {p["score"]} | 对象: {objs} | 方法: {meths}\n\n')

    print(f'    Markdown: {md_file}')
    print('\n' + '='*70)

if __name__ == '__main__':
    main()
