"""
EvidenceCollector - 研究证据收集器
从多源收集证据：顶会论文、vault论文笔记、GitHub releases、产业动态
"""
import os
import re
from typing import List, Dict

from core.logger import get_logger
from layers.research import Evidence, ResearchTopic

logger = get_logger("EvidenceCollector")


class EvidenceCollector:
    """证据收集器：从多个来源收集研究证据并去重排序"""

    def __init__(self, store=None, conference_store=None, paper_search_engine=None):
        self.store = store
        self.conference_store = conference_store
        self.paper_search_engine = paper_search_engine

    def collect(self, research_topic: ResearchTopic) -> List[Evidence]:
        """主入口：从所有相关来源收集证据"""
        all_evidence = []

        source_priority = research_topic.source_priority
        queries = research_topic.search_queries

        for source_type in source_priority:
            try:
                if source_type in ['arxiv', 'conference', 'paper']:
                    evidence = self._collect_from_papers(queries)
                elif source_type == 'github':
                    evidence = self._collect_from_github(queries)
                elif source_type == 'signals':
                    evidence = self._collect_from_signals(queries)
                else:
                    continue

                all_evidence.extend(evidence)
                logger.info("从 %s 收集到 %d 条证据", source_type, len(evidence))
            except Exception as e:
                logger.error("从 %s 收集失败: %s", source_type, e)

        unique_evidence = self._deduplicate(all_evidence)
        unique_evidence.sort(key=lambda x: x.relevance, reverse=True)
        logger.info("共收集 %d 条唯一证据", len(unique_evidence))
        return unique_evidence

    def _collect_from_papers(self, queries: List[str]) -> List[Evidence]:
        """从顶会论文和vault已有论文笔记收集"""
        if not self.conference_store:
            from layers.paper_analysis.conference_papers import ConferencePaperStore
            self.conference_store = ConferencePaperStore()

        evidence_list = []

        # 1. 搜顶会论文
        for query in queries[:5]:
            try:
                papers = self.conference_store.search_papers(keyword=query, limit=10)
                for paper in papers:
                    ev = self._paper_to_evidence(paper, query)
                    evidence_list.append(ev)
            except Exception:
                pass

        # 2. 如果顶会论文无结果，搜 vault 论文笔记
        if not evidence_list:
            evidence_list = self._search_vault_papers(queries)

        return evidence_list

    def _search_vault_papers(self, queries: List[str]) -> List[Evidence]:
        """搜索 vault 里已有的论文笔记（每日pipeline已抓取并存入）"""
        evidence_list = []

        # vault 论文笔记目录
        base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        vault_dir = os.path.join(base, '4_AI情报洞察', '论文洞察', 'Daily')

        if not os.path.exists(vault_dir):
            logger.warning("Vault papers dir not found: %s", vault_dir)
            return evidence_list

        for filename in os.listdir(vault_dir):
            if not filename.endswith('.md'):
                continue
            filepath = os.path.join(vault_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
            except Exception:
                continue

            # 关键词匹配
            matched_query = None
            for query in queries[:3]:
                if query.lower() in content.lower():
                    matched_query = query
                    break
            if not matched_query:
                continue

            # 提取标题 (# 开头行)
            title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_m.group(1)[:100] if title_m else filename

            # 提取 venue（**NIPS 2025** 格式）
            venue_m = re.search(r'\*\*([A-Z]+\s*\d{4})\*\*', content)
            venue = venue_m.group(1) if venue_m else ''

            # 提取日期
            date_m = re.search(r'\*\*([\d-]{10})\*\*', content)
            date_str = date_m.group(1) if date_m else ''

            # 提取一句话总结
            summary_m = re.search(r'##\s*一句话总结\s+(.+?)(?:\n##|\n---)', content, re.DOTALL)
            summary = summary_m.group(1).strip()[:300] if summary_m else ''

            ev = Evidence(
                source='vault_papers',
                source_type='paper',
                title=title,
                content=summary,
                url='',
                relevance=0.8,
                quality='medium',
                claim=title,
                evidence_type='supporting',
                citation_count=0,
                venue=venue,
                authors=[],
                published_date=date_str
            )
            evidence_list.append(ev)

        logger.info("从 vault 论文目录找到 %d 条相关论文", len(evidence_list))
        return evidence_list

    def _collect_from_github(self, queries: List[str]) -> List[Evidence]:
        """从 GitHub releases 收集"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        evidence_list = []
        for query in queries[:3]:
            try:
                events = self.store.get_events_by_tech(query, days=90, limit=10)
                for event in events:
                    if event.source_type == 'github' or 'github' in (event.source or '').lower():
                        ev = Evidence(
                            source=event.source or 'GitHub',
                            source_type='github',
                            title=event.title or '',
                            content=event.summary or '',
                            url=event.url or '',
                            relevance=0.7,
                            quality='medium',
                            claim=self._extract_claim(event),
                            evidence_type='supporting',
                            citation_count=0,
                            venue='',
                            authors=[]
                        )
                        evidence_list.append(ev)
            except Exception:
                pass
        return evidence_list

    def _collect_from_signals(self, queries: List[str]) -> List[Evidence]:
        """从已采集的信号收集"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        evidence_list = []
        for query in queries[:5]:
            try:
                events = self.store.get_events_by_tech(query, days=90, limit=15)
                for event in events:
                    ev = Evidence(
                        source=event.source or 'unknown',
                        source_type='signal',
                        title=event.title or '',
                        content=event.summary or '',
                        url=event.url or '',
                        relevance=0.5,
                        quality='medium',
                        claim=self._extract_claim(event),
                        evidence_type='neutral',
                        citation_count=0,
                        venue='',
                        authors=[]
                    )
                    evidence_list.append(ev)
            except Exception:
                pass
        return evidence_list

    def _paper_to_evidence(self, paper: Dict, query: str) -> Evidence:
        """将论文 dict 转换为 Evidence"""
        title_lower = (paper.get('title') or '').lower()
        query_lower = query.lower()
        relevance = sum(1 for kw in query_lower.split() if kw in title_lower)
        relevance = min(relevance * 0.5 + 0.3, 1.0)

        return Evidence(
            source=paper.get('venue', paper.get('source', 'paper')),
            source_type='paper',
            title=paper.get('title', ''),
            content=paper.get('abstract', paper.get('summary', ''))[:500],
            url=paper.get('url', paper.get('pdf_url', '')),
            relevance=relevance,
            quality='high' if paper.get('citation_count', 0) > 10 else 'medium',
            claim=paper.get('title', ''),
            evidence_type='supporting',
            citation_count=paper.get('citation_count', 0),
            venue=paper.get('venue', ''),
            authors=paper.get('authors', [])
        )

    def _extract_claim(self, event) -> str:
        """从事件中提取核心主张"""
        if hasattr(event, 'innovation') and event.innovation:
            return event.innovation
        if hasattr(event, 'summary') and event.summary:
            return event.summary[:200]
        return event.title or ''

    def _deduplicate(self, evidence_list: List[Evidence]) -> List[Evidence]:
        """去重：相同 title 或 URL 的证据只保留一个"""
        seen_titles = set()
        seen_urls = set()
        unique = []
        for ev in evidence_list:
            title_key = ev.title[:50].lower().strip()
            url_key = ev.url[:100].lower().strip() if ev.url else ''
            if title_key in seen_titles or (url_key and url_key in seen_urls):
                continue
            seen_titles.add(title_key)
            if url_key:
                seen_urls.add(url_key)
            unique.append(ev)
        return unique
