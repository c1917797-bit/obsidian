"""
Agent时代AI发展趋势洞察 - 执行脚本
"""
import os
import sys
import io
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except:
        pass

from layers.paper_analysis.conference_papers import ConferencePaperStore, get_available_venues
from layers.paper_analysis.deep_research import DeepResearchPipeline, ResearchQuery, ResearchReportGenerator
from layers.paper_analysis.litrep_report import LiteraryProgrammingReport, ReportTemplates

def main():
    print("=" * 70)
    print("Agent时代AI发展趋势洞察")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    store = ConferencePaperStore()
    pipeline = DeepResearchPipeline()
    report_gen = ResearchReportGenerator(pipeline)

    print("\n" + "-" * 70)
    print("Phase 1: 论文趋势分析")
    print("-" * 70)

    venues_years = [
        ('iclr', 2025),
        ('neurips', 2024),
        ('icml', 2024),
    ]

    agent_keywords = ['agent', 'multi-agent', 'tool use', 'reasoning', 'autonomous']

    all_papers = []
    for venue, year in venues_years:
        print(f"\n搜索 {venue.upper()} {year} 关于Agent的论文...")
        for kw in agent_keywords:
            papers = store.search_papers(venue, year, keyword=kw, limit=10)
            for p in papers:
                p.venue = f"{venue.upper()}_{year}"
                all_papers.append(p)

    unique_papers = {}
    for p in all_papers:
        if p.title not in unique_papers:
            unique_papers[p.title] = p

    sorted_papers = sorted(unique_papers.values(), key=lambda x: x.citation_count, reverse=True)

    print(f"\n共找到 {len(sorted_papers)} 篇相关论文 (去重后)")
    print("\n高影响力论文 (Top 15 by 引用数):")
    print("-" * 70)

    for i, p in enumerate(sorted_papers[:15], 1):
        title_short = p.title[:65] + "..." if len(p.title) > 65 else p.title
        print(f"\n{i}. [{p.citation_count} citations] {title_short}")
        print(f"   关键词: {', '.join(p.keywords[:3]) if p.keywords else 'N/A'}")
        print(f"   来源: {p.venue}")

    print("\n" + "-" * 70)
    print("Phase 2: 深度研究分析")
    print("-" * 70)

    queries = [
        ResearchQuery(topic="Agent Architecture and Frameworks 2025", scope="technical", depth="deep"),
        ResearchQuery(topic="Multi-Agent Collaboration and Communication Protocols", scope="technical", depth="deep"),
        ResearchQuery(topic="Agent Memory and State Management", scope="technical", depth="deep"),
    ]

    all_findings = []
    for query in queries:
        print(f"\n执行深度研究: {query.topic}")
        finding = pipeline.run_research(query)
        all_findings.append(finding)
        print(f"  核心发现: {len(finding.key_points)} 条")
        print(f"  置信度: {finding.confidence:.0%}")

    print("\n" + "-" * 70)
    print("Phase 3: 洞察综合")
    print("-" * 70)

    trends = {
        "Agent架构": [],
        "多Agent协同": [],
        "记忆与状态": [],
        "工具使用": [],
        "安全与对齐": []
    }

    for p in sorted_papers[:50]:
        title_lower = p.title.lower()
        if any(kw in title_lower for kw in ['agent', 'multi-agent', 'collaborat']):
            trends["多Agent协同"].append(p.title[:60])
        if any(kw in title_lower for kw in ['memory', 'state', 'persist']):
            trends["记忆与状态"].append(p.title[:60])
        if any(kw in title_lower for kw in ['tool', 'function', 'calling']):
            trends["工具使用"].append(p.title[:60])
        if any(kw in title_lower for kw in ['security', 'safety', 'align']):
            trends["安全与对齐"].append(p.title[:60])
        if any(kw in title_lower for kw in ['reasoning', 'chain-of-thought', 'planning']):
            trends["Agent架构"].append(p.title[:60])

    for category, papers in trends.items():
        print(f"\n{category}: {len(papers)} 篇相关论文")

    print("\n" + "-" * 70)
    print("Phase 4: 生成洞察报告")
    print("-" * 70)

    report = LiteraryProgrammingReport()
    report.set_title("Agent时代AI发展趋势洞察报告")

    report.add_narrative(
        "背景",
        f"""本报告基于对 {len(sorted_papers)} 篇顶会论文和相关技术资料的系统分析，
        洞察Agent时代下AI技术的发展趋势。报告生成时间: {datetime.now().strftime('%Y-%m-%d')}。"""
    )

    report.add_analysis(
        "论文趋势概览",
        f"""本报告分析了来自 ICLR 2025、NeurIPS 2024、ICML 2024 等顶会的论文。
        共筛选出 {len(sorted_papers)} 篇与Agent相关的论文。

        高影响力研究方向:
        1. Multi-Agent协作系统
        2. Agent记忆与状态管理
        3. Tool Use / Function Calling
        4. Agent安全与对齐
        5. 自主推理与规划"""
    )

    report.add_code(
        "论文影响力分析",
        """import pandas as pd
papers_data = [(p.title[:50], p.citation_count, p.venue) for p in sorted_papers[:20]]
df = pd.DataFrame(papers_data, columns=['Title', 'Citations', 'Venue'])
print(df.to_string(index=False))"""
    )

    top_trends = []
    for category, papers in trends.items():
        if papers:
            top_trends.append((category, len(papers)))

    top_trends.sort(key=lambda x: x[1], reverse=True)

    report.add_analysis(
        "趋势排序",
        f"""基于论文数量的趋势排序:
        1. {top_trends[0][0]}: {top_trends[0][1]} 篇
        2. {top_trends[1][0]}: {top_trends[1][1]} 篇
        3. {top_trends[2][0]}: {top_trends[2][1]} 篇"""
    )

    md_report = report.generate_markdown()

    output_dir = os.path.join(os.path.dirname(__file__), 'data', 'reports')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'Agent趋势洞察_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_report)

    print(f"\n洞察报告已保存: {output_path}")

    notebook_path = report.generate_notebook()
    print(f"Jupyter笔记已保存: {notebook_path}")

    print("\n" + "=" * 70)
    print("洞察执行完成")
    print("=" * 70)

    return {
        'papers_count': len(sorted_papers),
        'report_path': output_path,
        'notebook_path': notebook_path,
        'trends': {k: len(v) for k, v in trends.items()}
    }

if __name__ == '__main__':
    results = main()