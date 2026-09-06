"""
Literary Programming Report - 文学编程报告
集成 litprog-skill 能力

将代码和散文编织成可执行笔记本，适合研报生成
"""
import os
import json
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

from core.logger import get_logger

logger = get_logger("LitProgReport")

@dataclass
class ReportSection:
    """报告章节"""
    title: str
    content: str
    code_blocks: List[str] = field(default_factory=list)
    annotations: List[str] = field(default_factory=list)

class LiteraryProgrammingReport:
    """
    文学编程报告生成器
    类似 litprog-skill 的能力

    特点:
    - 代码与散文交织
    - 可执行代码块
    - 结构化输出
    """

    def __init__(self):
        self.sections = []
        self.title = ""
        self.metadata = {}

    def set_title(self, title: str):
        """设置报告标题"""
        self.title = title
        self.metadata['title'] = title
        self.metadata['created'] = datetime.now().isoformat()

    def add_section(self, section: ReportSection):
        """添加章节"""
        self.sections.append(section)

    def add_narrative(self, title: str, narrative: str):
        """添加叙述章节"""
        section = ReportSection(title=title, content=narrative)
        self.add_section(section)

    def add_code(self, title: str, code: str, explanation: str = ""):
        """添加代码章节"""
        section = ReportSection(
            title=title,
            content=explanation,
            code_blocks=[code]
        )
        self.add_section(section)

    def add_analysis(self, title: str, analysis: str, data_refs: List[str] = None):
        """添加分析章节"""
        section = ReportSection(
            title=title,
            content=analysis,
            annotations=data_refs or []
        )
        self.add_section(section)

    def generate_markdown(self) -> str:
        """生成Markdown格式"""
        md = f"# {self.title}\n\n"
        md += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
        md += "---\n\n"

        for section in self.sections:
            md += f"## {section.title}\n\n"
            md += f"{section.content}\n\n"

            if section.code_blocks:
                md += "```python\n"
                for code in section.code_blocks:
                    md += f"{code}\n"
                md += "```\n\n"

            if section.annotations:
                md += "> **References**: "
                md += ", ".join(section.annotations)
                md += "\n\n"

            md += "---\n\n"

        return md

    def generate_notebook(self, output_path: str = None) -> str:
        """
        生成 Jupyter Notebook 格式
        文学编程的核心输出
        """
        if not output_path:
            output_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'data', 'reports'
            )
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f'litprog_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.ipynb')

        cells = []

        cells.append({
            'cell_type': 'markdown',
            'metadata': {},
            'source': [f"# {self.title}\n", f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"]
        })

        for section in self.sections:
            cells.append({
                'cell_type': 'markdown',
                'metadata': {},
                'source': [f"## {section.title}\n", f"\n{section.content}\n"]
            })

            if section.code_blocks:
                for code in section.code_blocks:
                    cells.append({
                        'cell_type': 'code',
                        'execution_count': None,
                        'metadata': {},
                        'outputs': [],
                        'source': [code]
                    })

            if section.annotations:
                cells.append({
                    'cell_type': 'markdown',
                    'metadata': {},
                    'source': ["> **References**: " + ", ".join(section.annotations) + "\n"]
                })

        notebook = {
            'nbformat': 4,
            'nbformat_minor': 5,
            'metadata': {
                'kernelspec': {
                    'display_name': 'Python 3',
                    'language': 'python',
                    'name': 'python3'
                },
                'language_info': {
                    'name': 'python',
                    'version': '3.9.0'
                }
            },
            'cells': cells
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, ensure_ascii=False, indent=2)

        logger.info(f"Notebook saved: {output_path}")
        return output_path

    def generate_html(self) -> str:
        """生成HTML格式"""
        md_content = self.generate_markdown()

        html_template = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1 {{ color: #1a1a1a; border-bottom: 3px solid #0066cc; padding-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 30px; }}
        .section {{ margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px; }}
        pre {{ background: #2d2d2d; color: #f8f8f2; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
        .metadata {{ color: #666; font-size: 14px; }}
        blockquote {{ border-left: 4px solid #0066cc; margin: 20px 0; padding: 10px 20px; background: #f0f7ff; }}
    </style>
</head>
<body>
    {content}
</body>
</html>'''

        content_html = self._markdown_to_html(md_content)
        return html_template.format(title=self.title, content=content_html)

    def _markdown_to_html(self, md: str) -> str:
        """简单Markdown转HTML"""
        import re

        md = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md, flags=re.MULTILINE)
        md = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md, flags=re.MULTILINE)
        md = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', md)
        md = re.sub(r'`(.+?)`', r'<code>\1</code>', md)
        md = re.sub(r'^---$', '<hr>', md, flags=re.MULTILINE)
        md = re.sub(r'\n\n', '</p><p>', md)

        return f'<p>{md}</p>'


class ReportTemplates:
    """报告模板"""

    @staticmethod
    def techIntelligence_report(events: List[Any]) -> LiteraryProgrammingReport:
        """技术情报报告模板"""
        report = LiteraryProgrammingReport()
        report.set_title("技术情报报告")

        report.add_narrative(
            "概述",
            "本报告汇总近期技术领域的重要进展，涵盖推理优化、Agent系统、评测生态等方向。"
        )

        by_type = {}
        for event in events:
            et = getattr(event, 'event_type', 'unknown')
            if et not in by_type:
                by_type[et] = []
            by_type[et].append(event)

        for event_type, type_events in by_type.items():
            content = f"共 {len(type_events)} 条相关事件\n\n"
            for e in type_events[:5]:
                content += f"- {e.title[:80]}\n"
            report.add_analysis(event_type.replace('_', ' ').title(), content)

        report.add_code(
            "数据统计",
            """import statistics
counts = {k: len(v) for k, v in by_type.items()}
print(f"Total events: {{len(events)}}")
print(f"Events by type: {{counts}}")"""
        )

        return report

    @staticmethod
    def weekly_trends_report(trends: Dict) -> LiteraryProgrammingReport:
        """周度趋势报告模板"""
        report = LiteraryProgrammingReport()
        report.set_title("周度技术趋势报告")

        report.add_narrative(
            "趋势摘要",
            f"本周共监测到 {len(trends.get('trending_techs', []))} 个技术领域有活跃动态。"
        )

        for tech, details in trends.get('trending_techs', {}).items():
            report.add_analysis(
                tech,
                f"活跃度: {details.get('activity', 'normal')}",
                details.get('signals', [])
            )

        return report

    @staticmethod
    def paper_analysis_report(papers: List[Dict]) -> LiteraryProgrammingReport:
        """论文分析报告模板"""
        report = LiteraryProgrammingReport()
        report.set_title("论文分析报告")

        report.add_narrative(
            "分析目标",
            f"本报告分析 {len(papers)} 篇相关论文，覆盖最新研究进展。"
        )

        code = """import pandas as pd
papers_df = pd.DataFrame(papers)
papers_df['citation_count'] = papers_df.get('citation_count', 0)
top_papers = papers_df.nlargest(10, 'citation_count')
print(top_papers[['title', 'citation_count', 'venue']])"""

        report.add_code("论文排名分析", code)

        return report


if __name__ == '__main__':
    print("=" * 60)
    print("Literary Programming Report - Test")
    print("=" * 60)

    report = LiteraryProgrammingReport()
    report.set_title("测试报告")

    report.add_narrative(
        "背景",
        "这是一个测试报告，用于验证文学编程报告生成功能。"
    )

    report.add_code(
        "数据处理",
        """data = [1, 2, 3, 4, 5]
result = sum(data) / len(data)
print(f"Average: {result}")"""
    )

    report.add_analysis(
        "分析结果",
        "数据表明平均值约为 3.0",
        ["data source 1", "data source 2"]
    )

    md_output = report.generate_markdown()
    print("\n--- Markdown Output ---")
    print(md_output[:500])

    nb_path = report.generate_notebook()
    print(f"\n--- Notebook saved to ---")
    print(nb_path)

    print("\n" + "=" * 60)
    print("Test Complete")
    print("=" * 60)