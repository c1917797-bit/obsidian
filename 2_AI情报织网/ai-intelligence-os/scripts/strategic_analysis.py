"""
Strategic Analysis - 战略分析
使用预建索引快速回答战略问题
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from layers.paper_analysis.paper_search_engine import PaperSearchEngine
from collections import Counter


def analyze_agent_inference_trends():
    """分析Agent时代AI推理的重点方向"""
    engine = PaperSearchEngine(use_index=True)

    print("=" * 60)
    print("Agent时代AI推理战略分析")
    print("=" * 60)

    # 1. Agent核心能力分析
    print("\n【1】Agent核心能力论文分布")
    print("-" * 40)
    results = engine.fast_search(problems=['Agent-Capability'], limit=50)
    print(f"共 {len(results)} 篇相关论文 (Top 50 by citation)")

    # 2. Agent + 推理延迟
    print("\n【2】Agent推理延迟优化")
    print("-" * 40)
    results = engine.fast_search(problems=['Agent-Capability', 'Latency'], limit=20)
    print(f"相关论文: {len(results)} 篇")
    for r in results[:5]:
        print(f"  • {r.title[:55]}...")
        print(f"    Score: {r.relevance_score:.1f}")

    # 3. Agent + 内存优化
    print("\n【3】Agent内存优化技术")
    print("-" * 40)
    results = engine.fast_search(problems=['Agent-Capability', 'Memory'], limit=20)
    print(f"相关论文: {len(results)} 篇")
    for r in results[:5]:
        print(f"  • {r.title[:55]}...")

    # 4. Agent + 扩展性
    print("\n【4】Agent分布式/多智能体扩展")
    print("-" * 40)
    results = engine.fast_search(problems=['Agent-Capability', 'Scalability'], limit=20)
    print(f"相关论文: {len(results)} 篇")
    for r in results[:5]:
        print(f"  • {r.title[:55]}...")

    # 5. 核心技术分布
    print("\n【5】关键技术分布")
    print("-" * 40)
    all_results = engine.fast_search(problems=['Agent-Capability'], limit=100)
    techs = Counter()
    for r in all_results:
        techs.update(r.matched_techs)
    for tech, count in techs.most_common(10):
        print(f"  {tech}: {count} 篇")

    # 6. 综合问题分布
    print("\n【6】Agent相关的问题维度")
    print("-" * 40)
    problems = Counter()
    for r in all_results:
        problems.update(r.matched_problems)
    for prob, count in problems.most_common():
        print(f"  {prob}: {count} 篇")

    print("\n" + "=" * 60)
    print("结论: 重点投入方向建议")
    print("=" * 60)

    # 分析最高分论文
    results = engine.fast_search(problems=['Agent-Capability', 'Latency', 'Memory', 'Scalability'], limit=30)
    results.sort(key=lambda x: x.relevance_score, reverse=True)

    print("\n高优先级论文 (多维度匹配):")
    for i, r in enumerate(results[:10], 1):
        print(f"\n  {i}. {r.title[:60]}...")
        print(f"     问题: {r.matched_problems}")
        print(f"     技术: {r.matched_techs}")


if __name__ == '__main__':
    analyze_agent_inference_trends()
