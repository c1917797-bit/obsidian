"""
数据模型 - 统一Signal/Event
消除双schema问题，统一数据表示
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional, Any
from enum import Enum
import hashlib
import json

class EventType(Enum):
    """事件类型枚举"""
    RUNTIME_FEATURE = "runtime_feature"
    INFERENCE_OPT = "inference_opt"
    AGENT_FRAMEWORK = "agent_framework"
    COST_OPT = "cost_opt"
    RESEARCH_PAPER = "research_paper"
    PRODUCT_ANNOUNCEMENT = "product_announcement"
    BENCHMARK_UPDATE = "benchmark_update"
    INDUSTRY_NEWS = "industry_news"
    GOVERNANCE = "governance"

class Importance(Enum):
    """重要性等级"""
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"

class ContentType(Enum):
    """内容类型"""
    RESEARCH = "research"
    ENGINEERING = "engineering"
    PRODUCT = "product"
    INFRASTRUCTURE = "infrastructure"

class TechStage(Enum):
    """技术成熟度阶段"""
    EMERGING = "emerging"
    GROWING = "growing"
    PEAK = "peak"
    CONVERGING = "converging"
    MATURE = "mature"

@dataclass
class TechCategories:
    """技术分类标签"""
    domain: str  # inference_optimization, agent_runtime, cost_optimization
    subcategory: str  # kv_cache, speculative_decoding, moe, etc.
    tags: List[str] = field(default_factory=list)

    def to_list(self) -> List[str]:
        return [self.domain, self.subcategory] + self.tags

    @classmethod
    def from_list(cls, data: List[str]) -> 'TechCategories':
        if len(data) < 2:
            return cls(domain="unknown", subcategory="unknown")
        return cls(domain=data[0], subcategory=data[1], tags=data[2:])

class Entity:
    """实体信息"""
    def __init__(self, name: str, entity_type: str = "project", company: str = ""):
        self.name = name
        self.type = entity_type  # project, company, person, standard
        self.company = company

    def to_dict(self) -> Dict:
        return {"name": self.name, "type": self.type, "company": self.company}

@dataclass
class Signal:
    """
    统一信号数据模型
    来自采集层的原始数据
    """
    id: str
    title: str
    url: str
    source: str  # 来源名称
    source_id: str  # 来源标识
    source_type: str  # rss, atom, hf_api, web, github
    category: str  # tech_papers, inference, agent, etc.
    priority: str = "P1"
    published: str = ""  # ISO格式时间
    published_timestamp: float = 0.0
    summary: str = ""
    content: str = ""
    authors: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    fetched_at: str = field(default_factory=lambda: datetime.now().isoformat())
    language: str = "en"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.published_timestamp and self.published:
            try:
                dt = datetime.fromisoformat(self.published.replace('Z', '+00:00'))
                self.published_timestamp = dt.timestamp()
            except:
                self.published_timestamp = datetime.now().timestamp()

    @property
    def time(self) -> str:
        return self.published or self.fetched_at

    def generate_id(self) -> str:
        """生成唯一ID"""
        content = f"{self.title}_{self.url}_{self.source_id}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()[:16]

    def to_event_dict(self) -> Dict:
        """转换为事件字典"""
        return {
            'id': self.generate_id(),
            'time': self.time,
            'title': self.title,
            'summary': self.summary,
            'source': self.source,
            'url': self.url,
            'category': self.category,
            'published': self.published,
            'tags': self.tags
        }

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'source': self.source,
            'source_id': self.source_id,
            'source_type': self.source_type,
            'category': self.category,
            'priority': self.priority,
            'published': self.published,
            'summary': self.summary,
            'content': self.content,
            'authors': self.authors,
            'tags': self.tags,
            'fetched_at': self.fetched_at,
            'language': self.language,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Signal':
        return cls(
            id=data.get('id', ''),
            title=data.get('title', ''),
            url=data.get('url', ''),
            source=data.get('source', ''),
            source_id=data.get('source_id', ''),
            source_type=data.get('source_type', 'rss'),
            category=data.get('category', ''),
            priority=data.get('priority', 'P1'),
            published=data.get('published', ''),
            summary=data.get('summary', ''),
            content=data.get('content', ''),
            authors=data.get('authors', []),
            tags=data.get('tags', []),
            fetched_at=data.get('fetched_at', datetime.now().isoformat()),
            language=data.get('language', 'en'),
            metadata=data.get('metadata', {})
        )

@dataclass
class TechEvent:
    """
    统一事件数据模型
    经过分类、 enrichment 后的结构化事件
    """
    id: str
    time: str
    event_type: str
    entity: str  # 技术/项目/公司名称
    entity_type: str = "project"
    tech_categories: List[str] = field(default_factory=list)

    title: str = ""
    summary: str = ""

    signals: List[str] = field(default_factory=list)  # 触发信号列表
    innovation: str = ""  # 创新点
    problem_solved: str = ""  # 解决的问题

    importance: str = "P1"
    confidence: float = 0.5

    source: str = ""
    url: str = ""
    authors: List[str] = field(default_factory=list)

    related_events: List[str] = field(default_factory=list)
    related_techs: List[str] = field(default_factory=list)

    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    novelty_score: float = 0.0
    heat_score: float = 0.0

    stage: str = "emerging"  # emerging, growing, peak, converging, mature

    company: str = ""
    direction: str = ""  # 技术方向描述

    metadata: Dict[str, Any] = field(default_factory=dict)

    def __lt__(self, other):
        if not isinstance(other, TechEvent):
            return NotImplemented
        return (self.created_at or '') < (other.created_at or '')

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'time': self.time,
            'event_type': self.event_type,
            'entity': self.entity,
            'entity_type': self.entity_type,
            'tech_categories': self.tech_categories,
            'title': self.title,
            'summary': self.summary,
            'signals': self.signals,
            'innovation': self.innovation,
            'problem_solved': self.problem_solved,
            'importance': self.importance,
            'confidence': self.confidence,
            'source': self.source,
            'url': self.url,
            'authors': self.authors,
            'related_events': self.related_events,
            'related_techs': self.related_techs,
            'created_at': self.created_at,
            'novelty_score': self.novelty_score,
            'heat_score': self.heat_score,
            'stage': self.stage,
            'company': self.company,
            'direction': self.direction,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TechEvent':
        return cls(
            id=data.get('id', ''),
            time=data.get('time', ''),
            event_type=data.get('event_type', 'runtime_feature'),
            entity=data.get('entity', ''),
            entity_type=data.get('entity_type', 'project'),
            tech_categories=data.get('tech_categories', []),
            title=data.get('title', ''),
            summary=data.get('summary', ''),
            signals=data.get('signals', []),
            innovation=data.get('innovation', ''),
            problem_solved=data.get('problem_solved', ''),
            importance=data.get('importance', 'P1'),
            confidence=data.get('confidence', 0.5),
            source=data.get('source', ''),
            url=data.get('url', ''),
            authors=data.get('authors', []),
            related_events=data.get('related_events', []),
            related_techs=data.get('related_techs', []),
            created_at=data.get('created_at', datetime.now().isoformat()),
            novelty_score=data.get('novelty_score', 0.0),
            heat_score=data.get('heat_score', 0.0),
            stage=data.get('stage', 'emerging'),
            company=data.get('company', ''),
            direction=data.get('direction', ''),
            metadata=data.get('metadata', {})
        )

    @classmethod
    def from_signal(cls, signal: Signal, classification: Dict = None) -> 'TechEvent':
        """从Signal转换为TechEvent"""
        classification = classification or {}
        return cls(
            id=signal.generate_id(),
            time=signal.time,
            event_type=classification.get('event_type', 'runtime_feature'),
            entity=classification.get('entity', signal.source),
            entity_type=classification.get('entity_type', 'project'),
            tech_categories=classification.get('tech_categories', []),
            title=signal.title[:500],
            summary=signal.summary[:2000],
            source=signal.source,
            url=signal.url,
            authors=signal.authors,
            importance=classification.get('importance', 'P1'),
            confidence=classification.get('confidence', 0.5),
            signals=[signal.id],
            metadata={'signal_source': signal.source_id, 'language': signal.language, 'source_type': signal.source_type}
        )

class Report:
    """报告数据模型"""
    def __init__(self, title: str, content: str, report_type: str, period: str = ""):
        self.id = hashlib.md5(f"{title}_{datetime.now().isoformat()}".encode()).hexdigest()[:16]
        self.title = title
        self.content = content
        self.report_type = report_type  # daily, weekly, monthly, convergence, company_strategy
        self.period = period  # 2024-W01, 2024-01, etc.
        self.created_at = datetime.now().isoformat()
        self.events = []
        self.trends = {}
        self.insights = []
        self.metadata = {}  # Added for compatibility

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'report_type': self.report_type,
            'period': self.period,
            'created_at': self.created_at,
            'events': self.events,
            'trends': self.trends,
            'insights': self.insights,
            'metadata': self.metadata
        }

    def add_event(self, event_id: str):
        self.events.append(event_id)

    def add_insight(self, insight: str):
        self.insights.append(insight)