"""
Research Framework - 研究主题工作流的基础数据结构
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Evidence:
    """研究证据"""
    source: str           # 来源名称
    source_type: str      # paper / github / news / arxiv / signal
    title: str            # 标题
    content: str          # 摘要/关键段落
    url: str              # 链接
    relevance: float       # 0-1 和课题的相关度
    quality: str           # high / medium / low
    claim: str             # 核心主张
    evidence_type: str     # supporting / contradicting / neutral
    citation_count: int    # 论文引用数 / star数
    venue: str            # 会议/来源
    authors: List[str] = field(default_factory=list)
    published_date: str = ""

    def to_dict(self) -> Dict:
        return {
            'source': self.source,
            'source_type': self.source_type,
            'title': self.title,
            'content': self.content,
            'url': self.url,
            'relevance': self.relevance,
            'quality': self.quality,
            'claim': self.claim,
            'evidence_type': self.evidence_type,
            'citation_count': self.citation_count,
            'venue': self.venue,
            'authors': self.authors,
            'published_date': self.published_date
        }


@dataclass
class ResearchQuestion:
    """研究问题"""
    id: str
    question: str
    keywords: List[str]
    priority: str  # P0 / P1 / P2
    source_type: str  # academic / engineering / industry


@dataclass
class ResearchTopic:
    """研究课题（分解后）"""
    original_topic: str
    decomposed_questions: List[ResearchQuestion]
    search_queries: List[str]
    source_priority: List[str]  # 搜索优先级来源列表
    estimated_depth: str  # shallow / medium / deep

    @property
    def topic_id(self) -> str:
        """生成唯一ID"""
        import hashlib
        return hashlib.md5(self.original_topic.encode()).hexdigest()[:8]


@dataclass
class ResearchGap:
    """研究空白"""
    gap_type: str  # unsolved / underexplored / contradiction / transfer
    description: str
    evidence_refs: List[str]  # 引用到相关Evidence的ID
    urgency: str  # high / medium / low
    potential_impact: str  # high / medium / low

    def __str__(self) -> str:
        return f"[{self.gap_type.upper()}] {self.description}"


@dataclass
class MethodComparison:
    """方法对比"""
    method_name: str
    strengths: List[str]
    limitations: List[str]
    applicable_scenarios: List[str]
    key_papers: List[str]  # citation references
    performance_notes: str  # 性能对比备注

    def to_table_row(self) -> str:
        return f"| {self.method_name} | {', '.join(self.strengths)} | {', '.join(self.limitations)} | {', '.join(self.applicable_scenarios)} |"


@dataclass
class ResearchReport:
    """研究报告"""
    title: str
    topic: str
    abstract: str
    research_questions: List[str]
    methodology_comparisons: List[MethodComparison]
    key_findings: List[str]
    research_gaps: List[ResearchGap]
    future_directions: List[str]
    references: List[Evidence]
    confidence: str  # high / medium / low
    generated_at: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M'))

    @property
    def markdown(self) -> str:
        """生成Markdown格式的报告"""
        nl = "\n"

        # 方法对比表
        method_table = "| 方法 | 优势 | 局限 | 适用场景 |" + nl
        method_table += "|------|------|------|------|" + nl
        for m in self.methodology_comparisons:
            method_table += m.to_table_row() + nl

        # 参考文献
        refs = ""
        for i, ev in enumerate(self.references[:20], 1):  # 最多20条
            refs += f"{i}. [{ev.title}]({ev.url}) - {ev.source} ({ev.citation_count} citations){nl}"

        # 研究空白
        gaps_text = ""
        for gap in self.research_gaps:
            gaps_text += f"- **{gap.gap_type.upper()}**: {gap.description}{nl}"

        content = f"""# {self.title}

> 自动生成的研究报告 | 置信度: {self.confidence} | 生成时间: {self.generated_at}

## 摘要

{self.abstract}

---

## 研究背景

本报告围绕课题「{self.topic}」展开系统研究，综合了来自论文、GitHub、新闻等多源信息。

---

## 研究问题分解

"""
        for q in self.research_questions:
            content += f"- **{q}**{nl}"

        content += f"""
---

## 方法论对比

{method_table}

---

## 关键发现

"""
        for i, finding in enumerate(self.key_findings, 1):
            content += f"{i}. {finding}{nl}"

        content += f"""
---

## 研究空白与未来方向

{gaps_text if gaps_text else "暂无明显研究空白。"}

**未来研究方向：**
"""
        for direction in self.future_directions:
            content += f"- {direction}{nl}"

        content += f"""
---

## 参考文献

{refs}

---

## 报告元数据

- **课题**: {self.topic}
- **置信度**: {self.confidence}
- **生成时间**: {self.generated_at}
- **证据数量**: {len(self.references)}
"""
        return content

    def save_to_file(self, filepath: str):
        """保存到文件"""
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.markdown)