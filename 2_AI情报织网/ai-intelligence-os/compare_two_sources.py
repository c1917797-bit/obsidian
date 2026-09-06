import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Data source 1: inference_compression_strict.json
with open(r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_strict.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)

# Data source 2: paper_index.json
with open(r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os\layers\data\paper_index\paper_index.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

papers1 = data1['papers']  # inference_compression_strict
papers2 = data2['papers']  # paper_index

print("=" * 60)
print("两个数据源对比分析")
print("=" * 60)

print("\n[1] inference_compression_strict.json")
print(f"    论文总数: {len(papers1)}")
print(f"    KV相关: {data1['by_object'].get('kv', 0)}")
print(f"    来源: ICLR/NeurIPS/ICML/CVPR/ACL/CoRL 2025顶会")

print("\n[2] paper_index.json + 我们的筛选")
print(f"    原始论文总数: {len(papers2)}")
print(f"    筛选出: 685篇 (含LLM上下文+压缩关键词)")
print(f"    KV相关: 约42篇 (含eviction/memory-efficient等)")

# 分析交集
set1_kv = set()
set2_kv = set()

for p in papers1:
    if 'kv' in p.get('objects', []):
        set1_kv.add(p.get('title', '').lower())

for pid, p in papers2.items():
    title = p.get('title', '').lower()
    if 'kv' in title or 'kvcache' in title or 'key-value' in title:
        set2_kv.add(title)

overlap = set1_kv & set2_kv
only_in_set1 = set1_kv - set2_kv
only_in_set2 = set2_kv - set1_kv

print("\n" + "=" * 60)
print("KV论文交集分析")
print("=" * 60)
print(f"\n两个数据集共有: {len(overlap)}篇")
print(f"只在inference_compression_strict: {len(only_in_set1)}篇")
print(f"只在paper_index筛选结果: {len(only_in_set2)}篇")

print("\n--- 只在inference_compression_strict的KV论文 (前20) ---")
for i, t in enumerate(sorted(only_in_set1)[:20], 1):
    print(f"{i}. {t[:70]}")

print("\n--- 只在paper_index筛选的KV论文 (前20) ---")
for i, t in enumerate(sorted(only_in_set2)[:20], 1):
    print(f"{i}. {t[:70]}")

# 两个数据集的矩阵对比
print("\n" + "=" * 60)
print("矩阵对比")
print("=" * 60)

print("\n--- inference_compression_strict矩阵 ---")
for k, v in sorted(data1['by_object'].items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

print("\n--- 各自优势 ---")
print("inference_compression_strict优势:")
print("  - 有顶会论文分类，人工标注objects/methods")
print("  - 包含310篇KV论文，覆盖更全面")
print("  - 有论文评分/引用等元数据")

print("\npaper_index+筛选优势:")
print("  - 覆盖更广（arXiv等非正式渠道）")
print("  - 包含更新发表的论文")
print("  - eviction/memory-efficient等隐式优化覆盖更全")

print("\n" + "=" * 60)
print("互补使用建议")
print("=" * 60)
print("""
【判断研究机会时】
  → 以inference_compression_strict为主（310篇KV，矩阵精确）

【寻找具体论文时】
  → 两个数据集都要搜索，确保不遗漏

【判断论文新旧时】
  → paper_index可能有最新arXiv论文

【最终结论】
  → 两个数据集互补使用，不废弃任何一个
""")
