# -*- coding: utf-8 -*-
"""
consistency_test.py
- Krippendorff's alpha 评分者一致性测试
- 3-5 个评分者独立评分 25 个课题
- 计算 alpha 系数
"""
import os
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OUTPUT_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\方法论'

SAMPLE_TOPICS = [
    {"id": 1, "title": "K×Q 量化 KV Cache 到 4-bit", "expected": "topic_A"},
    {"id": 2, "title": "W×P 动态剪枝 MoE 模型", "expected": "topic_B"},
    {"id": 3, "title": "C×Q AllReduce 量化压缩", "expected": "topic_C"},
    {"id": 4, "title": "S×G 投机解码在 Agent 场景应用", "expected": "topic_D"},
    {"id": 5, "title": "M×Q ViT 视觉编码器 INT8 量化", "expected": "topic_E"},
    {"id": 6, "title": "V×D 声码器蒸馏", "expected": "topic_F"},
    {"id": 7, "title": "A×G FlashAttention 算子优化", "expected": "topic_G"},
    {"id": 8, "title": "K×D KV Cache 跨层蒸馏", "expected": "topic_H"},
    {"id": 9, "title": "W×L LoRA 风格低秩压缩", "expected": "topic_I"},
    {"id": 10, "title": "C×G NCCL 自适应拓扑调度", "expected": "topic_J"},
    {"id": 11, "title": "K×S KV Cache 稀疏化（滑动窗口）", "expected": "topic_K"},
    {"id": 12, "title": "S×G Beam Search 状态压缩", "expected": "topic_L"},
    {"id": 13, "title": "M×L 视觉编码器低秩分解", "expected": "topic_M"},
    {"id": 14, "title": "A×Q 激活值 INT4 量化", "expected": "topic_N"},
    {"id": 15, "title": "W×S 2:4 稀疏化训练", "expected": "topic_O"},
    {"id": 16, "title": "C×S 通信梯度稀疏化", "expected": "topic_P"},
    {"id": 17, "title": "K×G MQA/GQA 多查询注意力", "expected": "topic_Q"},
    {"id": 18, "title": "S×Q Speculative Decoding 量化", "expected": "topic_R"},
    {"id": 19, "title": "V×G 流式 TTS 实时合成", "expected": "topic_S"},
    {"id": 20, "title": "W×D 大模型蒸馏到小模型", "expected": "topic_T"},
    {"id": 21, "title": "K×Q Page Attention 内存管理", "expected": "topic_U"},
    {"id": 22, "title": "A×G PagedAttention 内核优化", "expected": "topic_V"},
    {"id": 23, "title": "C×G ZeRO 通信优化", "expected": "topic_W"},
    {"id": 24, "title": "M×D 视觉-语言模型蒸馏", "expected": "topic_X"},
    {"id": 25, "title": "S×G Agent 状态压缩", "expected": "topic_Y"},
]

SCORING_DIMENSIONS = [
    {"name": "技术深度", "min": 1, "max": 3, "examples": {
        1: "应用已知方法",
        2: "在现有方法上改进",
        3: "提出全新算法"
    }},
    {"name": "工程影响", "min": 1, "max": 3, "examples": {
        1: "边际改进",
        2: "有改进但非核心",
        3: "解决核心瓶颈"
    }},
    {"name": "趋势强度", "min": 1, "max": 2, "examples": {
        1: "平稳发展（年发表<10篇）",
        2: "快速增长（年发表>20篇）"
    }},
    {"name": "行业影响", "min": 1, "max": 2, "examples": {
        1: "特定场景",
        2: "跨场景通用"
    }},
    {"name": "反方证据-历史失败", "min": 1, "max": 3, "examples": {
        1: "无失败案例",
        2: "1-2个失败",
        3: "多次失败"
    }},
    {"name": "反方证据-专利壁垒", "min": 1, "max": 3, "examples": {
        1: "无专利",
        2: "部分专利",
        3: "完全被专利保护"
    }},
    {"name": "反方证据-资源门槛", "min": 1, "max": 3, "examples": {
        1: "<10 GPU×月",
        2: "10-50 GPU×月",
        3: ">50 GPU×月"
    }},
    {"name": "反方证据-团队不匹配", "min": 1, "max": 3, "examples": {
        1: "完全匹配",
        2: "部分匹配",
        3: "完全不匹配"
    }},
    {"name": "反方证据-反向场景", "min": 1, "max": 3, "examples": {
        1: "无反向场景",
        2: "1-2个反向",
        3: "多场景反向"
    }},
]

def krippendorff_alpha_nominal(data, num_items, num_raters, num_categories):
    """
    简化的 Krippendorff's alpha 计算（名义数据）
    data: list of list, data[rater][item] = category
    """
    if num_items == 0 or num_raters < 2:
        return 0.0

    n_total = num_items * num_raters
    n_pairs_total = 0
    observed_disagreement = 0

    for item_idx in range(num_items):
        for i in range(num_raters):
            for j in range(i+1, num_raters):
                n_pairs_total += 1
                if data[i][item_idx] != data[j][item_idx]:
                    observed_disagreement += 1

    if n_pairs_total == 0:
        return 0.0

    Do = observed_disagreement / n_pairs_total

    category_counts = defaultdict(int)
    for rater in data:
        for value in rater:
            category_counts[value] += 1

    n = sum(category_counts.values())
    De = 0.0
    for c, count in category_counts.items():
        for d, count2 in category_counts.items():
            if c != d:
                De += count * count2
    if n <= 1:
        return 0.0
    De = De / (n * (n - 1))

    if De == 0:
        return 1.0

    alpha = 1 - (Do / De)
    return alpha

def generate_test_template():
    """生成评分者测试模板"""
    template = []
    template.append("# Krippendorff's alpha 一致性测试 - 评分表\n")
    template.append(f"> 测试时间: {datetime.now().strftime('%Y-%m-%d')}\n")
    template.append("> 测试目的: 验证方法论评分卡的可执行性\n")
    template.append("> 评分者: ____（你的名字）\n")
    template.append('> 说明: 你不知道课题的「已知标签」，请独立评分\n\n')

    template.append("## 评分维度\n\n")
    for dim in SCORING_DIMENSIONS:
        template.append(f"### {dim['name']} ({dim['min']}-{dim['max']}分)\n")
        for score, example in dim['examples'].items():
            template.append(f"- {score}分: {example}\n")
        template.append("\n")

    template.append("---\n\n## 评分表\n\n")
    template.append("| 课题ID | 标题 | 技术深度 | 工程影响 | 趋势强度 | 行业影响 | 反方-历史 | 反方-专利 | 反方-资源 | 反方-团队 | 反方-反向 |\n")
    template.append("|--------|------|---------|---------|---------|---------|----------|----------|----------|----------|----------|\n")
    for topic in SAMPLE_TOPICS:
        template.append(f"| {topic['id']} | {topic['title']} | | | | | | | | | |\n")

    template.append("\n---\n\n## 评分说明\n\n")
    template.append("- 9个维度独立评分\n")
    template.append("- 每个维度按上述说明打分\n")
    template.append("- 完成后提交给统计人员\n")

    return "\n".join(template)

def generate_test_data():
    """生成示例测试数据（3个评分者，部分不一致）"""
    rater1 = []
    rater2 = []
    rater3 = []

    base_scores = {
        1: [2, 2, 2, 2, 2, 1, 1, 1, 2],
        2: [3, 3, 2, 2, 1, 1, 2, 1, 1],
        3: [2, 2, 1, 1, 2, 1, 1, 1, 1],
        4: [2, 3, 2, 2, 1, 1, 1, 1, 1],
        5: [1, 2, 1, 2, 1, 1, 1, 1, 1],
        6: [1, 1, 1, 1, 1, 1, 1, 1, 1],
        7: [3, 3, 2, 2, 1, 2, 1, 1, 1],
        8: [2, 2, 1, 1, 2, 1, 2, 2, 2],
        9: [2, 2, 1, 2, 1, 1, 1, 1, 1],
        10: [3, 2, 2, 2, 1, 1, 2, 1, 1],
        11: [2, 2, 1, 1, 1, 1, 1, 1, 1],
        12: [1, 1, 1, 1, 1, 1, 1, 1, 1],
        13: [2, 2, 1, 1, 1, 1, 1, 1, 1],
        14: [2, 2, 1, 1, 2, 2, 2, 1, 1],
        15: [2, 2, 1, 1, 2, 2, 2, 2, 1],
        16: [2, 1, 1, 1, 2, 2, 1, 1, 1],
        17: [3, 3, 2, 2, 1, 1, 1, 1, 1],
        18: [2, 2, 1, 1, 2, 2, 2, 1, 1],
        19: [2, 1, 1, 1, 1, 1, 2, 2, 1],
        20: [2, 2, 2, 2, 1, 1, 2, 1, 1],
        21: [3, 3, 2, 2, 1, 1, 1, 1, 1],
        22: [3, 2, 1, 1, 1, 2, 2, 1, 1],
        23: [3, 3, 2, 2, 1, 1, 2, 1, 1],
        24: [2, 2, 1, 1, 1, 1, 2, 2, 1],
        25: [2, 2, 2, 1, 1, 1, 1, 1, 1],
    }

    for item_id in range(1, 26):
        base = base_scores[item_id]
        r1 = list(base)

        r2 = list(base)
        if item_id % 3 == 0:
            r2[0] = max(1, r2[0] - 1)
        if item_id % 5 == 0:
            r2[1] = min(3, r2[1] + 1)

        r3 = list(base)
        if item_id % 4 == 0:
            r3[4] = min(3, r3[4] + 1)
        if item_id % 7 == 0:
            r3[5] = max(1, r3[5] - 1)

        rater1.append(r1)
        rater2.append(r2)
        rater3.append(r3)

    return rater1, rater2, rater3

def analyze_results(rater1, rater2, rater3):
    """分析评分结果"""
    results = {
        "by_dimension": [],
        "overall": {},
    }

    num_dimensions = len(SCORING_DIMENSIONS)
    num_items = len(SAMPLE_TOPICS)

    for dim_idx, dim in enumerate(SCORING_DIMENSIONS):
        col1 = [rater1[item_idx][dim_idx] for item_idx in range(num_items)]
        col2 = [rater2[item_idx][dim_idx] for item_idx in range(num_items)]
        col3 = [rater3[item_idx][dim_idx] for item_idx in range(num_items)]

        max_val = dim['max']

        alpha = krippendorff_alpha_nominal(
            [col1, col2, col3],
            num_items,
            3,
            max_val + 1
        )

        results["by_dimension"].append({
            "dimension": dim['name'],
            "alpha": round(alpha, 3),
            "judgment": "高度一致" if alpha >= 0.8 else "基本一致" if alpha >= 0.6 else "一致性差" if alpha >= 0.4 else "不可用"
        })

    all_col1 = []
    all_col2 = []
    all_col3 = []
    for dim_idx in range(num_dimensions):
        for item_idx in range(num_items):
            all_col1.append(rater1[item_idx][dim_idx] * 10 + dim_idx)
            all_col2.append(rater2[item_idx][dim_idx] * 10 + dim_idx)
            all_col3.append(rater3[item_idx][dim_idx] * 10 + dim_idx)

    overall_alpha = krippendorff_alpha_nominal(
        [all_col1, all_col2, all_col3],
        len(all_col1),
        3,
        100
    )
    results["overall"] = {
        "alpha": round(overall_alpha, 3),
        "judgment": "高度一致" if overall_alpha >= 0.8 else "基本一致" if overall_alpha >= 0.6 else "一致性差" if overall_alpha >= 0.4 else "不可用",
        "num_items": num_items,
        "num_dimensions": num_dimensions,
        "num_raters": 3,
    }

    return results

def main():
    print("=" * 60)
    print("Krippendorff's alpha 一致性测试")
    print("=" * 60)

    template_path = os.path.join(OUTPUT_DIR, '一致性测试_评分表_模板.md')
    template_content = generate_test_template()
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(template_content)
    print(f"\n评分表模板已生成: {template_path}")

    print("\n生成示例测试数据（3个评分者，模拟部分不一致）...")
    rater1, rater2, rater3 = generate_test_data()

    print("\n分析评分结果...")
    results = analyze_results(rater1, rater2, rater3)

    print("\n=== 各维度一致性 ===")
    for dim_result in results['by_dimension']:
        print(f"  {dim_result['dimension']}: α = {dim_result['alpha']:.3f} ({dim_result['judgment']})")

    print(f"\n=== 总体一致性 ===")
    print(f"  α = {results['overall']['alpha']:.3f} ({results['overall']['judgment']})")
    print(f"  课题数: {results['overall']['num_items']}")
    print(f"  维度数: {results['overall']['num_dimensions']}")
    print(f"  评分者数: {results['overall']['num_raters']}")

    report_path = os.path.join(OUTPUT_DIR, '一致性测试_结果分析.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Krippendorff's alpha 一致性测试 - 结果分析\n\n")
        f.write(f"> 测试时间: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"> 测试类型: 示例数据演示（实际测试需真实评分者）\n\n")

        f.write("## 测试设置\n\n")
        f.write(f"- 课题数: {results['overall']['num_items']}\n")
        f.write(f"- 评分维度数: {results['overall']['num_dimensions']}\n")
        f.write(f"- 评分者数: {results['overall']['num_raters']}\n")
        f.write(f"- 数据来源: 示例数据（不是真实评分）\n\n")

        f.write("## 各维度一致性结果\n\n")
        f.write("| 维度 | α 系数 | 判定 |\n")
        f.write("|------|--------|------|\n")
        for dim_result in results['by_dimension']:
            f.write(f"| {dim_result['dimension']} | {dim_result['alpha']:.3f} | {dim_result['judgment']} |\n")

        f.write(f"\n## 总体一致性\n\n")
        f.write(f"**α = {results['overall']['alpha']:.3f}** ({results['overall']['judgment']})\n\n")

        f.write("## 判定标准\n\n")
        f.write("- α ≥ 0.8: 高度一致，方法论可信\n")
        f.write("- 0.6 ≤ α < 0.8: 基本一致，需小幅调整\n")
        f.write("- 0.4 ≤ α < 0.6: 一致性差，需大改\n")
        f.write("- α < 0.4: 方法论不可用\n\n")

        f.write("## 下一步行动\n\n")
        f.write("1. **本次为示例测试** - 真实测试需3-5个团队成员独立评分\n")
        f.write("2. 收集真实评分数据后再次运行本脚本\n")
        f.write("3. 如果 α < 0.6，需要细化评分卡定义\n")
        f.write("4. 如果 α < 0.4，整个方法论需要重构\n")

    print(f"\n分析报告: {report_path}")
    print("\n" + "=" * 60)
    print("下一步: 收集真实评分数据后再次运行")

if __name__ == '__main__':
    main()
