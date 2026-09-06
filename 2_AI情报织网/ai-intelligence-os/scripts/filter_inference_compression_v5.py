"""
推理压缩论文筛选器 v5
智能分类：精确匹配 + 方法推断对象
"""
import json
import os
from collections import defaultdict
from datetime import datetime

# LLM上下文
LLM_CONTEXT = [
    'llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
    'diffusion model', 'vision language', 'vlm', 'multimodal',
    'inference', 'serving', 'deployment', 'generation', 'autoregressive',
]

# 压缩对象（精确匹配）
OBJECTS = {
    '参数(Weights)': ['weight quantization', 'model quantization', 'parameter compress',
                      'layer compress', 'neural network quantization', 'int4', 'int8', 'fp8',
                      'quantized weight', 'model compression', 'network compress'],
    '状态(State/KV)': ['kv cache', 'kvcache', 'key-value cache', 'cache compress',
                       'attention state', 'activation cache', 'state compress',
                       'context compress', 'memory efficient', 'memory compress'],
    '通信(Comm)': ['distributed inference', 'tensor parallel', 'pipeline parallel',
                   'model parallel', 'mixture of expert', 'moe', 'expert routing',
                   'expert parallel', 'all-to-all', 'communication compress',
                   'collective communication', 'allreduce', 'moe inference',
                   'mixture-of-expert', 'distributed serving'],
}

# 压缩方法
METHODS = {
    '量化(Quant)': ['quantization', 'quantize', 'quant', 'low bit', 'int4', 'int8',
                    'fp8', 'fp4', '4bit', '8bit', '4-bit', '8-bit', 'quantized'],
    '剪枝(Prune)': ['pruning', 'prune', 'structured prune', 'unstructured prune',
                    'channel prune', 'head prune', 'layer prune', 'model prune'],
    '稀疏(Sparse)': ['sparse', 'sparsity', 'dynamic sparse', 'sparsification',
                     'sparse attention', 'token prune', 'attention prune'],
    '蒸馏(Distill)': ['distillation', 'distill', 'knowledge distill', 'student model',
                      'distillated', 'distillating'],
    '低秩(LowRank)': ['low rank', 'matrix factorization', 'svd', 'rank reduction',
                      'kron', 'decomposition', 'low-rank'],
}

# 方法 → 默认对象推断
METHOD_TO_OBJECT = {
    '量化(Quant)': '参数(Weights)',  # 量化主要针对权重
    '剪枝(Prune)': '参数(Weights)',  # 剪枝主要针对权重
    '稀疏(Sparse)': '状态(State/KV)',  # 稀疏主要针对注意力/激活状态
    '低秩(LowRank)': '参数(Weights)',  # 低秩主要针对权重矩阵分解
    '蒸馏(Distill)': '参数(Weights)',  # 蒸馏主要压缩模型参数
}

# 排除词（非LLM压缩）
EXCLUDE = [
    'image compression', 'video compression', 'audio compression', 'speech compression',
    'jpeg', 'mpeg', 'h264', 'hevc', 'av1', 'vp9',
    'point cloud', 'mesh compression', '3d gaussian', 'neural radiance',
    'dataset distillation', 'data distillation',
    'quantum', 'quantum machine',
    'recommendation', 'recommender system',
]

def has_llm_context(title_lower):
    for ctx in LLM_CONTEXT:
        if ctx in title_lower:
            return True
    return False

def should_exclude(title_lower):
    for ex in EXCLUDE:
        if ex in title_lower:
            return True
    return False

def infer_object_from_methods(title_lower, matched_methods):
    """根据方法推断对象"""
    inferred = []

    # 特殊上下文检测
    if 'kv' in title_lower or 'cache' in title_lower or 'memory' in title_lower:
        inferred.append('状态(State/KV)')

    if 'moe' in title_lower or 'expert' in title_lower:
        inferred.append('通信(Comm)')

    if 'distributed' in title_lower or 'tensor parallel' in title_lower:
        inferred.append('通信(Comm)')

    # 如果没有特殊上下文，用方法默认推断
    for method in matched_methods:
        if method in METHOD_TO_OBJECT:
            obj = METHOD_TO_OBJECT[method]
            if obj not in inferred:
                inferred.append(obj)

    return inferred

def score_paper(paper):
    """筛选 + 智能分类"""
    title_lower = paper.get('title', '').lower()

    # 必须有LLM上下文
    if not has_llm_context(title_lower):
        return 0, {}, {}

    # 排除
    if should_exclude(title_lower):
        return 0, {}, {}

    # 精确匹配对象
    matched_objects = {}
    for obj, keywords in OBJECTS.items():
        for kw in keywords:
            if kw in title_lower:
                matched_objects[obj] = True
                break

    # 精确匹配方法
    matched_methods = {}
    for method, keywords in METHODS.items():
        for kw in keywords:
            if kw in title_lower:
                matched_methods[method] = True
                break

    # 如果只匹配了方法没匹配对象 → 智能推断
    if matched_methods and not matched_objects:
        inferred = infer_object_from_methods(title_lower, list(matched_methods.keys()))
        for obj in inferred:
            matched_objects[obj] = True

    # 必须有对象或方法
    if matched_objects or matched_methods:
        score = len(matched_objects) + len(matched_methods)
        return score, matched_objects, matched_methods

    return 0, {}, {}

def filter_and_categorize(papers):
    """筛选并分类"""
    results = []
    matrix = defaultdict(list)

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
            }
            results.append(paper_data)

            # 矩阵
            for o in paper_data['matched_objects']:
                for m in paper_data['matched_methods']:
                    matrix[f"{o} × {m}"].append(paper_data)

    results.sort(key=lambda x: -x['score'])
    return results, matrix

def main():
    print('='*70)
    print('推理压缩论文筛选器 v5')
    print('智能分类：精确匹配 + 方法推断对象')
    print('='*70)

    print('\n[1] 加载论文库...')
    with open('layers/data/paper_index/paper_index.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    papers = data['papers']
    print(f'    总论文数: {len(papers)}')

    print('\n[2] 筛选并分类...')
    results, matrix = filter_and_categorize(papers)
    print(f'    推理压缩论文数: {len(results)}')

    # 统计
    obj_counts = defaultdict(int)
    for p in results:
        for o in p['matched_objects']:
            obj_counts[o] += 1

    method_counts = defaultdict(int)
    for p in results:
        for m in p['matched_methods']:
            method_counts[m] += 1

    print('\n[3] 对象×方法矩阵:')
    for key, papers_list in sorted(matrix.items(), key=lambda x: -len(x[1])):
        print(f'    {key}: {len(papers_list)}篇')

    print('\n[4] Top 30:')
    for i, p in enumerate(results[:30], 1):
        objs = '/'.join(p['matched_objects'])
        meths = '/'.join(p['matched_methods'])
        print(f'\n{i}. [{p["score"]}] {p["title"][:60]}...')
        print(f'   对象: {objs} | 方法: {meths}')

    # 保存
    print('\n[5] 保存...')
    output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\_corpus'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'inference_compression_v5.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total': len(papers),
            'filtered': len(results),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'papers': results,
            'matrix': {k: len(v) for k, v in matrix.items()}
        }, f, ensure_ascii=False, indent=2)

    md_file = os.path.join(output_dir, 'inference_compression_v5_summary.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('# 推理压缩论文分类报告 v5\n\n')
        f.write(f'**日期**: {datetime.now().strftime("%Y-%m-%d")}\n')
        f.write(f'**论文库**: {len(papers)} | **筛选**: {len(results)}\n\n')
        f.write('## 对象×方法矩阵\n\n')
        f.write('| 对象 | 方法 | 论文数 |\n|------|------|--------|\n')
        for key, papers_list in sorted(matrix.items(), key=lambda x: -len(x[1])):
            f.write(f'| {key.replace(" × ", " | ")} | {len(papers_list)} |\n')
        f.write('\n## Top 50 论文\n\n')
        for i, p in enumerate(results[:50], 1):
            objs = ', '.join(p['matched_objects'])
            meths = ', '.join(p['matched_methods'])
            f.write(f'{i}. **{p["title"]}**\n')
            f.write(f'   - 对象: {objs} | 方法: {meths}\n')

    print(f'    已保存到 {output_dir}')
    print('\n' + '='*70)

if __name__ == '__main__':
    main()
