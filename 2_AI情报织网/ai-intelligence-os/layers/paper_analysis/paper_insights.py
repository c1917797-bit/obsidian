"""
Paper Insights Generator - 论文洞察生成器
实现:
1. PaperCardGenerator - 30秒速读卡片
2. TrendReportGenerator - 技术趋势报告
3. ObsidianPaperSink - Obsidian论文洞察输出
"""
import os
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict

from core.logger import get_logger
from core.minimax_client import get_client
from layers.paper_analysis.paper_search_engine import PaperSearchEngine, PaperMatch, ReadingPyramid

logger = get_logger("PaperInsights")


@dataclass
class PaperCard:
    """论文速读卡片"""
    title: str
    venue: str
    year: int
    one_sentence_summary: str
    key_contributions: List[str]
    why_important: str
    matched_problems: List[str]
    matched_techs: List[str]
    read_time_minutes: int
    url: str
    pdf_url: str
    citation_count: int
    relevance_score: float


@dataclass
class TrendReport:
    """技术趋势报告"""
    title: str
    period: str
    total_papers_analyzed: int
    problem_distribution: Dict[str, int]
    tech_distribution: Dict[str, int]
    top_papers: List[PaperCard]
    emerging_themes: List[str]
    recommendations: List[str]
    generated_at: str


class PaperCardGenerator:
    """
    论文速读卡片生成器
    输入: PaperMatch
    输出: 30秒可阅读的卡片
    """

    def __init__(self, client=None):
        self.client = client or get_client()

    def generate_card(self, paper: PaperMatch) -> PaperCard:
        """生成单篇论文卡片"""
        abstract_text = paper.abstract[:800] if paper.abstract and len(paper.abstract) > 50 else "无摘要信息"

        prompt = f"""请根据以下论文信息，生成30秒速读卡片。

论文标题: {paper.title}
会议/年份: {paper.venue or 'Unknown'} {paper.year or 2024}
摘要: {abstract_text}
领域: {paper.primary_area or 'Unknown'}
引用数: {paper.citation_count or 0}
匹配问题: {', '.join(paper.matched_problems) if paper.matched_problems else 'Unknown'}
匹配技术: {', '.join(paper.matched_techs) if paper.matched_techs else 'Unknown'}

请用JSON格式输出:
{{
    "one_sentence_summary": "一句话总结论文核心贡献（不超过50字）",
    "key_contributions": ["贡献1", "贡献2", "贡献3"],
    "why_important": "为什么这项研究重要？（不超过100字）"
}}

只输出JSON，不要其他内容。
"""

        try:
            response = self.client.chat([{"role": "user", "content": prompt}], temperature=0.3, max_tokens=800)
            # Remove markdown code block wrapper if present
            response = response.strip()
            if response.startswith('```json'):
                response = response[7:]
            elif response.startswith('```'):
                response = response[3:]
            if response.endswith('```'):
                response = response[:-3]
            response = response.strip()
            data = json.loads(response)

            return PaperCard(
                title=paper.title,
                venue=paper.venue or "Unknown",
                year=paper.year or 2024,
                one_sentence_summary=data.get("one_sentence_summary", ""),
                key_contributions=data.get("key_contributions", []),
                why_important=data.get("why_important", ""),
                matched_problems=paper.matched_problems,
                matched_techs=paper.matched_techs,
                read_time_minutes=paper.read_time_minutes or 30,
                url=paper.url,
                pdf_url=paper.pdf_url,
                citation_count=paper.citation_count or 0,
                relevance_score=paper.relevance_score
            )
        except json.JSONDecodeError as e:
            logger.warning(f"JSON decode error for {paper.title[:50]}: {e}")
            return PaperCard(
                title=paper.title,
                venue=paper.venue or "Unknown",
                year=paper.year or 2024,
                one_sentence_summary=f"论文涉及{'/'.join(paper.matched_problems[:2]) if paper.matched_problems else '相关技术问题'}",
                key_contributions=[f"涉及{tech}" for tech in (paper.matched_techs[:3] if paper.matched_techs else ["需阅读原文"])],
                why_important="生成失败，请阅读原文",
                matched_problems=paper.matched_problems,
                matched_techs=paper.matched_techs,
                read_time_minutes=paper.read_time_minutes or 30,
                url=paper.url,
                pdf_url=paper.pdf_url,
                citation_count=paper.citation_count or 0,
                relevance_score=paper.relevance_score
            )
        except Exception as e:
            logger.warning(f"Failed to generate card for {paper.title[:50]}: {e}")
            return PaperCard(
                title=paper.title,
                venue=paper.venue or "Unknown",
                year=paper.year or 2024,
                one_sentence_summary=abstract_text[:80] + "..." if len(abstract_text) > 80 else abstract_text,
                key_contributions=["见原文摘要"],
                why_important="生成失败，请阅读原文",
                matched_problems=paper.matched_problems,
                matched_techs=paper.matched_techs,
                read_time_minutes=paper.read_time_minutes or 30,
                url=paper.url,
                pdf_url=paper.pdf_url,
                citation_count=paper.citation_count or 0,
                relevance_score=paper.relevance_score
            )

    def generate_cards_batch(self, papers: List[PaperMatch], limit: int = 10) -> List[PaperCard]:
        """批量生成论文卡片"""
        cards = []
        for paper in papers[:limit]:
            card = self.generate_card(paper)
            cards.append(card)
            logger.info(f"Generated card: {paper.title[:50]}...")
        return cards

    def format_card_markdown(self, card: PaperCard) -> str:
        """格式化为Markdown"""
        contributions = "\n".join([f"{i+1}. {c}" for i, c in enumerate(card.key_contributions)])

        md = f"""### 📄 {card.title}

**{card.venue} {card.year}** | Citations: {card.citation_count} | ⏱️ {card.read_time_minutes}min

#### 一句话总结
{card.one_sentence_summary}

#### 核心贡献
{contributions}

#### 为什么重要
{card.why_important}

#### 🏷️ 标签
{" / ".join([f"`{p}`" for p in card.matched_problems])}
{" / ".join([f"`{t}`" for t in card.matched_techs])}

#### 🔗 链接
[Paper]({card.url}) | [PDF]({card.pdf_url})

---
"""
        return md


class TrendReportGenerator:
    """
    技术趋势报告生成器
    分析多篇论文，生成趋势洞察
    """

    def __init__(self, search_engine: PaperSearchEngine = None, card_generator: PaperCardGenerator = None):
        self.search_engine = search_engine or PaperSearchEngine()
        self.card_generator = card_generator or PaperCardGenerator()

    def generate_weekly_trend_report(
        self,
        problems: List[str] = None,
        techs: List[str] = None,
        venues: List[str] = None
    ) -> TrendReport:
        """生成周度趋势报告"""

        problems = problems or ['Latency', 'Memory', 'Scalability', 'Agent-Capability']
        techs = techs or ['KV Cache', 'Speculative Decoding', 'Distributed Inference']
        venues = venues or ['iclr', 'nips', 'icml', 'cvpr', 'emnlp', 'acl', 'corl']

        logger.info(f"Searching papers for trend report...")
        papers = self.search_engine.search(
            query=" ".join(problems + techs),
            problems=problems,
            techs=techs,
            venues=venues,
            min_relevance=15.0,
            limit=50
        )

        problem_count = {}
        tech_count = {}
        for p in papers:
            for prob in p.matched_problems:
                problem_count[prob] = problem_count.get(prob, 0) + 1
            for tech in p.matched_techs:
                tech_count[tech] = tech_count.get(tech, 0) + 1

        top_papers = self.card_generator.generate_cards_batch(papers, limit=10)

        emerging = self._extract_emerging_themes(papers)
        recommendations = self._generate_recommendations(problem_count, tech_count, papers)

        report = TrendReport(
            title=f"AI推理技术趋势周报 - {datetime.now().strftime('%Y-%m-%d')}",
            period=self._get_week_period(),
            total_papers_analyzed=len(papers),
            problem_distribution=problem_count,
            tech_distribution=tech_count,
            top_papers=top_papers,
            emerging_themes=emerging,
            recommendations=recommendations,
            generated_at=datetime.now().isoformat()
        )

        return report

    def _get_week_period(self) -> str:
        """获取周次"""
        week = datetime.now().isocalendar()[1]
        year = datetime.now().year
        return f"{year}-W{week:02d}"

    def _extract_emerging_themes(self, papers: List[PaperMatch]) -> List[str]:
        """提取新兴主题"""
        themes = []
        for p in papers[:20]:
            title_lower = p.title.lower()
            if 'agent' in title_lower and 'memory' in title_lower:
                themes.append("Agent + Memory 融合")
            if 'speculative' in title_lower and 'agent' in title_lower:
                themes.append("Speculative Decoding 服务 Agent")
            if 'distributed' in title_lower and 'memory' in title_lower:
                themes.append("分布式内存管理")
            if 'kv cache' in title_lower and 'scale' in title_lower:
                themes.append("KV Cache 大规模扩展")
        return list(set(themes))[:5]

    def _generate_recommendations(
        self,
        problem_count: Dict[str, int],
        tech_count: Dict[str, int],
        papers: List[PaperMatch]
    ) -> List[str]:
        """生成推荐"""
        recs = []

        top_problem = max(problem_count.items(), key=lambda x: x[1]) if problem_count else None
        if top_problem:
            recs.append(f"重点关注问题: {top_problem[0]} (涉及{top_problem[1]}篇论文)")

        top_tech = max(tech_count.items(), key=lambda x: x[1]) if tech_count else None
        if top_tech:
            recs.append(f"热点技术: {top_tech[0]} (涉及{top_tech[1]}篇论文)")

        if papers:
            top_paper = papers[0]
            recs.append(f"最高相关论文: {top_paper.title[:60]}...")

        return recs

    def format_report_markdown(self, report: TrendReport) -> str:
        """格式化为Markdown报告"""
        problem_dist = "\n".join([f"- {k}: {v} 篇" for k, v in sorted(report.problem_distribution.items(), key=lambda x: -x[1])])
        tech_dist = "\n".join([f"- {k}: {v} 篇" for k, v in sorted(report.tech_distribution.items(), key=lambda x: -x[1])])
        recommendations = "\n".join([f"{i+1}. {r}" for i, r in enumerate(report.recommendations)])

        md = f"""---
title: 技术趋势周报
date: {report.generated_at[:10]}
period: {report.period}
tags: [AI-Intelligence, Trend-Report, Weekly]
---

# AI推理技术趋势周报

**周期: {report.period}** | 生成时间: {report.generated_at[:19]}

## 概览

- 分析论文数: {report.total_papers_analyzed} 篇
- 覆盖会议: ICLR 2025, NeurIPS 2025, ICML 2024, CVPR 2024, EMNLP 2024, ACL 2024, CoRL 2024

## 问题分布

{problem_dist}

## 技术分布

{tech_dist}

## 新兴主题

{" / ".join([f"`{t}`" for t in report.emerging_themes])}

## Top 10 论文卡片

"""
        for card in report.top_papers:
            md += self.card_generator.format_card_markdown(card)

        md += f"""
## 行动建议

{recommendations}

---

*本报告由AI Intelligence OS自动生成*
"""

        return md


class ObsidianPaperSink:
    """
    Obsidian论文洞察输出
    将论文卡片和趋势报告写入Obsidian
    """

    def __init__(self, vault_path: str = None):
        if vault_path is None:
            vault_path = os.path.join(os.environ.get(
                'OBSIDIAN_VAULT_PATH',
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            ), '4_AI情报洞察', '论文洞察')
        self.vault_path = vault_path
        self.daily_dir = os.path.join(self.vault_path, 'Daily')
        self.weekly_dir = os.path.join(self.vault_path, 'Weekly')
        os.makedirs(self.daily_dir, exist_ok=True)
        os.makedirs(self.weekly_dir, exist_ok=True)

    def save_paper_card(self, card: PaperCard, filename: str = None) -> str:
        """保存单篇论文卡片"""
        if filename is None:
            safe_title = "".join(c for c in card.title[:50] if c.isalnum() or c in (' ', '-', '_')).strip()
            filename = f"{card.venue}_{card.year}_{safe_title}.md"

        path = os.path.join(self.daily_dir, filename)
        md = self._format_card_markdown(card)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(md)

        logger.info(f"Saved paper card: {path}")
        return path

    def save_paper_cards_batch(self, cards: List[PaperCard], date_str: str = None) -> List[str]:
        """批量保存论文卡片"""
        if date_str is None:
            date_str = datetime.now().strftime('%Y-%m-%d')

        paths = []
        for i, card in enumerate(cards):
            safe_title = "".join(c for c in card.title[:40] if c.isalnum() or c in (' ', '-', '_')).strip()
            filename = f"{date_str}_{i+1:02d}_{card.venue}_{safe_title}.md"
            path = self.save_paper_card(card, filename)
            paths.append(path)

        return paths

    def save_trend_report(self, report: TrendReport, filename: str = None) -> str:
        """保存趋势报告"""
        if filename is None:
            filename = f"TrendReport_{report.period}.md"

        path = os.path.join(self.weekly_dir, filename)
        md = self._format_trend_report_markdown(report)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(md)

        logger.info(f"Saved trend report: {path}")
        return path

    def _format_trend_report_markdown(self, report: TrendReport) -> str:
        """格式化为Markdown报告"""
        problem_dist = "\n".join([f"- **{k}**: {v} 篇" for k, v in sorted(report.problem_distribution.items(), key=lambda x: -x[1])])
        tech_dist = "\n".join([f"- **{k}**: {v} 篇" for k, v in sorted(report.tech_distribution.items(), key=lambda x: -x[1])])
        emerging = "\n".join([f"- `{t}`" for t in report.emerging_themes]) if report.emerging_themes else "_暂无新兴主题_"
        recommendations = "\n".join([f"{i+1}. {r}" for i, r in enumerate(report.recommendations)])

        md = f"""---
title: 技术趋势周报
period: {report.period}
date: {report.generated_at[:10]}
papers_analyzed: {report.total_papers_analyzed}
tags: [AI-Intelligence, Trend-Report, Weekly]
type: trend-report
---

# AI推理技术趋势周报

**周期: {report.period}** | 生成时间: {report.generated_at[:19]}

## 概览

- 分析论文数: **{report.total_papers_analyzed} 篇**
- 覆盖会议: ICLR 2025, NeurIPS 2025, ICML 2024, CVPR 2024, EMNLP 2024, ACL 2024, CoRL 2024

## 问题分布

{problem_dist}

## 技术分布

{tech_dist}

## 新兴主题

{emerging}

## Top 10 论文

"""
        for card in report.top_papers:
            md += f"\n### {card.title}\n"
            md += f"**{card.venue} {card.year}** | Citations: {card.citation_count}\n\n"
            md += f"**一句话**: {card.one_sentence_summary}\n\n"
            md += f"**贡献**: {', '.join(card.key_contributions[:2])}\n\n"

        md += f"""
## 行动建议

{recommendations}

---

*本报告由 AI Intelligence OS 自动生成*
"""

        return md

    def _format_card_markdown(self, card: PaperCard) -> str:
        """格式化论文卡片"""
        contributions = "\n".join([f"{i+1}. {c}" for i, c in enumerate(card.key_contributions)])

        return f"""---
title: "{card.title}"
venue: {card.venue} {card.year}
citations: {card.citation_count}
relevance_score: {card.relevance_score}
tags: [{', '.join(card.matched_problems)}, {', '.join(card.matched_techs)}]
date: {datetime.now().strftime('%Y-%m-%d')}
type: paper-card
---

# {card.title}

**{card.venue} {card.year}** | Citations: {card.citation_count} | ⏱️ {card.read_time_minutes}min

## 一句话总结
{card.one_sentence_summary}

## 核心贡献
{contributions}

## 为什么重要
{card.why_important}

## 标签
- Problems: {', '.join(card.matched_problems)}
- Techs: {', '.join(card.matched_techs)}

## 链接
- [Paper]({card.url})
- [PDF]({card.pdf_url})
"""

def _format_report_markdown(self, report: TrendReport) -> str:
        """格式化为Markdown报告"""
        problem_dist = "\n".join([f"- **{k}**: {v} 篇" for k, v in sorted(report.problem_distribution.items(), key=lambda x: -x[1])])
        tech_dist = "\n".join([f"- **{k}**: {v} 篇" for k, v in sorted(report.tech_distribution.items(), key=lambda x: -x[1])])
        emerging = "\n".join([f"- `{t}`" for t in report.emerging_themes]) if report.emerging_themes else "_暂无新兴主题_"
        recommendations = "\n".join([f"{i+1}. {r}" for i, r in enumerate(report.recommendations)])

        md = f"""---
title: 技术趋势周报
period: {report.period}
date: {report.generated_at[:10]}
papers_analyzed: {report.total_papers_analyzed}
tags: [AI-Intelligence, Trend-Report, Weekly]
type: trend-report
---

# AI推理技术趋势周报

**周期: {report.period}** | 生成时间: {report.generated_at[:19]}

## 概览

- 分析论文数: **{report.total_papers_analyzed} 篇**
- 覆盖会议: ICLR 2025, NeurIPS 2025, ICML 2024, CVPR 2024, EMNLP 2024, ACL 2024, CoRL 2024

## 问题分布

{problem_dist}

## 技术分布

{tech_dist}

## 新兴主题

{emerging if emerging else "_暂无新兴主题_"}

## Top 10 论文

"""
        for card in report.top_papers:
            md += f"\n### {card.title}\n"
            md += f"**{card.venue} {card.year}** | Citations: {card.citation_count}\n\n"
            md += f"**一句话**: {card.one_sentence_summary}\n\n"
            md += f"**贡献**: {', '.join(card.key_contributions[:2])}\n\n"

        md += f"""
## 行动建议

{recommendations}

---

*本报告由 AI Intelligence OS 自动生成*
"""

        return md


class PaperInsightsPipeline:
    """
    论文洞察完整流水线
    整合搜索、卡片生成、趋势报告、Obsidian输出
    """

    def __init__(self):
        self.search_engine = PaperSearchEngine()
        self.card_generator = PaperCardGenerator()
        self.trend_generator = TrendReportGenerator(self.search_engine, self.card_generator)
        self.obsidian_sink = ObsidianPaperSink()

    def run_weekly_pipeline(
        self,
        problems: List[str] = None,
        techs: List[str] = None
    ) -> Dict:
        """
        运行周度论文洞察流水线

        Returns:
            包含报告路径、卡片列表等
        """
        logger.info("=== 论文洞察流水线启动 ===")

        problems = problems or ['Latency', 'Memory', 'Scalability', 'Agent-Capability']
        techs = techs or ['KV Cache', 'Speculative Decoding', 'Distributed Inference']

        logger.info(f"搜索问题: {problems}")
        logger.info(f"搜索技术: {techs}")

        papers = self.search_engine.search(
            query=" ".join(problems + techs),
            problems=problems,
            techs=techs,
            min_relevance=15.0,
            limit=50
        )
        logger.info(f"找到 {len(papers)} 篇相关论文")

        cards = self.card_generator.generate_cards_batch(papers, limit=10)
        logger.info(f"生成 {len(cards)} 篇论文卡片")

        report = self.trend_generator.generate_weekly_trend_report(problems, techs)
        logger.info(f"生成趋势报告: {report.title}")

        card_paths = self.obsidian_sink.save_paper_cards_batch(cards)
        report_path = self.obsidian_sink.save_trend_report(report)

        logger.info("=== 论文洞察流水线完成 ===")

        return {
            'report_path': report_path,
            'card_paths': card_paths,
            'papers_found': len(papers),
            'cards_generated': len(cards),
            'period': report.period
        }
