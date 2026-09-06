"""
推理压缩论文筛选器 v4
加入 LLM/推理 上下文过滤，确保是本领域论文
"""
import json
import os
from collections import defaultdict
from datetime import datetime

# LLM/推理上下文（必须匹配这些才算）
LLM_CONTEXT = [
    'llm', 'language model', 'transformer', 'bert', 'gpt', 'large language',
    'diffusion model', 'text-to-image', 'vision language', 'vlm', 'multimodal',
    'inference', 'serving', 'deployment', 'generation',
    'autoregressive', 'decoder', 'attention',
]

# 压缩对象
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
                   'expert', 'mixture-of-expert', 'distributed serving'],
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

# 严格排除（非LLM压缩）
EXCLUDE = [
    'image compression', 'video compression', 'audio compression', 'speech compression',
    'jpeg', 'mpeg', 'h264', 'hevc', 'av1', 'vp9',
    'point cloud', 'mesh compression', '3d gaussian', 'neural radiance',
    'dataset distillation', 'data distillation',  # 数据集蒸馏不是模型压缩
    'quantum', 'quantum machine',  # 量子ML
    'recommendation', 'recommender system',  # 推荐系统
    'federated learning', 'federated',  # 联邦学习（虽然涉及分布式但不是本领域）
]

def has_llm_context(title_lower):
    """检查是否有LLM/推理上下文"""
    for ctx in LLM_CONTEXT:
        if ctx in title_lower:
            return True
    return False

def should_exclude(title_lower):
    """检查是否应该排除"""
    for ex in EXCLUDE:
        if ex in title_lower:
            return True
    return False

def score_paper(paper):
    """筛选+分类"""
    title_lower = paper.get('title', '').lower()

    # 必须有LLM上下文
    if not has_llm_context(title_lower):
        return 0, {}, {}

    # 排除非本领域
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
                'problems': paper.get('problems', []),
                'techs': paper.get('techs', []),
            }
            results.append(paper_data)

            # 矩阵分组
            objs = paper_data['matched_objects']
            meths = paper_data['matched_methods']

            if objs and meths:
                for o in objs:
                    for m in meths:
                        matrix[f"{o} × {m}"].append(paper_data)
            elif objs:
                for o in objs:
                    matrix[f"{o} × 其他"].append(paper_data)
            elif meths:
                for m in meths:
                    matrix[f"其他 × {m}"].append(paper_data)

    results.sort(key=lambda x: -x['score'])
    return results, matrix

def main():
    print('='*70)
    print('推理压缩论文筛选器 v4')
    print('过滤: LLM/推理上下文 + 非本领域排除')
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
    print(f'    推理压缩论文数: {len(results)}')

    # 统计
    print('\n[3] 统计分布...')

    obj_counts = defaultdict(int)
    for p in results:
        for o in p['matched_objects']:
            obj_counts[o] += 1

    print('\n    按压缩对象:')
    for o, c in sorted(obj_counts.items(), key=lambda x: -x[1]):
        print(f'      {o}: {c}篇')

    method_counts = defaultdict(int)
    for p in results:
        for m in p['matched_methods']:
            method_counts[m] += 1

    print('\n    按压缩方法:')
    for m, c in sorted(method_counts.items(), key=lambda x: -x[1]):
        print(f'      {m}: {c}篇')

    print('\n    对象×方法矩阵:')
    for key, papers_list in sorted(matrix.items(), key=lambda x: -len(x[1])):
        print(f'      {key}: {len(papers_list)}篇')

    # Top论文
    print('\n[4] Top 20:')
    for i, p in enumerate(results[:20], 1):
        objs = '/'.join(p['matched_objects']) or '其他'
        meths = '/'.join(p['matched_methods']) or '其他'
        print(f'\n{i}. [{p["score"]}] {p["title"][:60]}...')
        print(f'   对象: {objs} | 方法: {meths}')

    # 保存
    print('\n[5] 保存...')
    output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\_corpus'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'inference_compression_v4.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_papers': len(papers),
            'filtered_count': len(results),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'papers': results,
            'matrix': {k: len(v) for k, v in matrix.items()}
        }, f, ensure_ascii=False, indent=2)

    md_file = os.path.join(output_dir, 'inference_compression_v4_summary.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('# 推理压缩论文筛选报告 v4\n\n')
        f.write(f'**日期**: {datetime.now().strftime("%Y-%m-%d")}\n')
        f.write(f'**论文库总数**: {len(papers)}\n')
        f.write(f'**筛选出论文数**: {len(results)}\n\n')

        f.write('## 对象×方法矩阵\n\n')
        f.write('| 对象 | 方法 | 论文数 |\n')
        f.write('|------|------|--------|\n')
        for key, papers_list in sorted(matrix.items(), key=lambda x: -len(x[1])):
            f.write(f'| {key.replace(" × ", " | ")} | {len(papers_list)} |\n')

    print(f'    已保存')
    print('\n' + '='*70)

if __name__ == '__main__':
    main()
