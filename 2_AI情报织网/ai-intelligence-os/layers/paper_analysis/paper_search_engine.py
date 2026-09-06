"""
Paper Search Engine - 增强版论文搜索引擎
实现问题导向搜索 + 多Venue覆盖 + 阅读金字塔
"""
import os
import json
import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor, as_completed

from core.logger import get_logger
from layers.agents.scoring_engine import ScoringEngine, TechInterestWeights

logger = get_logger("PaperSearchEngine")


PAPER_VENUES = {
    'iclr': {'year': 2025, 'name': 'ICLR'},
    'nips': {'year': 2025, 'name': 'NeurIPS'},
    'icml': {'year': 2024, 'name': 'ICML'},
    'cvpr': {'year': 2024, 'name': 'CVPR'},
    'emnlp': {'year': 2024, 'name': 'EMNLP'},
    'acl': {'year': 2024, 'name': 'ACL'},
    'corl': {'year': 2024, 'name': 'CoRL'},
}


PROBLEM_TO_KEYWORDS = {
    'Latency': [
        'latency', 'delay', 'response time', 'time to first token', 'ttft',
        '首字延迟', '延迟优化', '响应速度', 'inference speed', 'fast inference',
        '低延迟', '实时', 'realtime', 'streaming', 'continuous batching'
    ],
    'Throughput': [
        'throughput', 'tokens per second', 'tps', 'qps', 'output speed',
        '吞吐', '并发', '带宽', 'high throughput', 'efficiency',
        'serving throughput', 'batch processing', 'parallel'
    ],
    'Memory': [
        'memory', '显存', 'vram', 'gpu memory', 'oom', 'out of memory',
        'memory efficiency', '内存', 'kv cache', 'cache', 'paged attention',
        'memory management', 'offload', 'compression'
    ],
    'Scalability': [
        'scalability', 'scale', 'multi-gpu', 'multi-node', 'distributed',
        '扩展', '扩展性', '多卡', 'tensor parallel', 'pipeline parallel',
        'data parallel', 'model parallel', 'sharding'
    ],
    'Cost': [
        'cost', 'price', 'cheap', 'expensive', 'compute', 'flops',
        '费用', '成本', '性价比', 'energy efficiency', 'power',
        'compute efficiency', 'resource efficient'
    ],
    'Reliability': [
        'reliability', 'availability', 'fault tolerance', 'recovery',
        '可用性', '可靠性', '容错', 'robust', 'stable', 'consistent'
    ],
    'Accuracy': [
        'accuracy', 'quality', 'performance', 'benchmark', 'eval',
        '评测', '精度', '质量', 'leaderboard', 'humaneval', 'mmlu'
    ],
    'Agent-Capability': [
        'agent', 'capability', 'reasoning', 'planning', 'memory',
        'autonomy', '智能体', '能力', 'multi-agent', 'tool use',
        'reasoning', 'planning', 'reflection'
    ],
}

TECH_TO_KEYWORDS = {
    'KV Cache': ['kv cache', 'kvcache', 'paged attention', 'pagedattention', 'cache'],
    'Speculative Decoding': ['speculative', 'specdec', 'draft model', 'medusa', 'eagle', 'lookahead', 'multi-token prediction'],
    'MoE': ['mixture of experts', 'moe', 'mixtral', 'expert'],
    'Quantization': ['quantize', 'quantization', 'int8', 'int4', 'fp8', 'awq', 'gptq', 'gguf', 'quant'],
    'PD Separation': ['prefill', 'decode', 'pd separation', 'disaggregation', 'prefill-decoding'],
    'Distributed Inference': ['distributed', 'tensor parallel', 'pipeline parallel', 'data parallel'],
    'Continuous Batching': ['continuous batching', 'iteration scheduling', 'batch scheduling'],
    'vLLM': ['vllm', 'paged attention'],
    'SGLang': ['sglang', 'radix attention'],
}


@dataclass
class PaperMatch:
    """论文匹配结果"""
    title: str
    abstract: str
    authors: List[str]
    venue: str
    year: int
    url: str
    pdf_url: str
    citation_count: int
    primary_area: str
    matched_problems: List[str] = field(default_factory=list)
    matched_techs: List[str] = field(default_factory=list)
    relevance_score: float = 0.0
    read_time_minutes: int = 30


@dataclass
class ReadingPyramid:
    """阅读金字塔"""
    top10_cards: List[PaperMatch] = field(default_factory=list)
    top3_skeleton: List[PaperMatch] = field(default_factory=list)
    top1_deep: Optional[PaperMatch] = None


class PaperSearchEngine:
    """
    增强版论文搜索引擎

    能力:
    1. 多Venue搜索 (ICLR/NeurIPS/ICML/CVPR/ACL/EMNLP/CoRL)
    2. 问题导向搜索 (Latency/Throughput/Memory/Scalability/Cost)
    3. 技术关键词扩展
    4. 阅读时间估算
    5. 阅读金字塔输出
    """

    def __init__(self, conference_store=None, use_index: bool = True):
        self.conference_store = conference_store
        self.scoring_engine = ScoringEngine()
        self._paper_cache = {}
        self._index = None
        if use_index:
            from layers.paper_analysis.paper_index import PaperIndex
            self._index = PaperIndex()
            self._index.load()

    def _load_all_conferences(self, venues: List[str] = None) -> Dict[str, List[Dict]]:
        """加载多个会议的论文"""
        if venues is None:
            venues = list(PAPER_VENUES.keys())

        all_papers = {}

        def load_venue(venue_key):
            venue_info = PAPER_VENUES.get(venue_key, {})
            if not venue_info:
                return venue_key, []
            year = venue_info['year']
            try:
                if self.conference_store:
                    papers = self.conference_store.load_papers_from_url(venue_key, year)
                else:
                    from layers.paper_analysis.conference_papers import ConferencePaperStore
                    store = ConferencePaperStore()
                    papers = store.load_papers_from_url(venue_key, year)
                return venue_key, papers
            except Exception as e:
                logger.warning(f"Failed to load {venue_key}{year}: {e}")
                return venue_key, []

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(load_venue, v): v for v in venues}
            for future in as_completed(futures):
                venue_key, papers = future.result()
                all_papers[venue_key] = papers
                logger.info(f"Loaded {len(papers)} papers from {venue_key.upper()}")

        return all_papers

    def _expand_keywords(self, query: str) -> List[str]:
        """扩展查询关键词"""
        query_lower = query.lower()
        expanded = [query_lower]

        for problem, keywords in PROBLEM_TO_KEYWORDS.items():
            if any(kw in query_lower for kw in keywords) or problem.lower() in query_lower:
                expanded.extend(keywords[:5])

        for tech, keywords in TECH_TO_KEYWORDS.items():
            if any(kw in query_lower for kw in keywords) or tech.lower() in query_lower:
                expanded.extend(keywords[:3])

        return list(set(expanded))

    def _calculate_relevance(self, paper: Dict, query_keywords: List[str], problems: List[str], techs: List[str]) -> float:
        """计算论文相关性分数"""
        title = paper.get('title', '').lower()
        abstract = paper.get('abstract', '').lower()
        keywords = paper.get('keywords', [])
        if isinstance(keywords, list):
            keywords = ' '.join(keywords).lower()
        primary_area = paper.get('primary_area', '').lower()

        text = f"{title} {abstract} {keywords} {primary_area}"

        score = 0.0

        for kw in query_keywords:
            if kw in title:
                score += 10.0
            if kw in abstract:
                score += 5.0
            if kw in keywords:
                score += 3.0
            if kw in primary_area:
                score += 2.0

        for problem in problems:
            problem_kws = PROBLEM_TO_KEYWORDS.get(problem, [])
            for kw in problem_kws:
                if kw in text:
                    score += 3.0
                    break

        for tech in techs:
            tech_kws = TECH_TO_KEYWORDS.get(tech, [])
            for kw in tech_kws:
                if kw in text:
                    score += 5.0
                    break

        citation = paper.get('citation_count', 0)
        if citation > 0:
            score += min(citation * 0.1, 10.0)

        return score

    def _estimate_read_time(self, paper: Dict) -> int:
        """估算阅读时间（分钟）"""
        abstract_len = len(paper.get('abstract', ''))
        title = paper.get('title', '').lower()

        base_time = 5
        if abstract_len > 500:
            base_time += 10
        elif abstract_len > 300:
            base_time += 5

        if any(kw in title for kw in ['survey', 'review', 'benchmark']):
            base_time += 15

        return base_time

    def search(
        self,
        query: str,
        problems: List[str] = None,
        techs: List[str] = None,
        venues: List[str] = None,
        min_relevance: float = 5.0,
        limit: int = 100
    ) -> List[PaperMatch]:
        """
        搜索论文

        Args:
            query: 搜索查询
            problems: 问题标签列表 (Latency/Throughput/Memory/Scalability/Cost/Reliability/Accuracy/Agent-Capability)
            techs: 技术标签列表 (KV Cache/Speculative Decoding/MoE/Quantization/PD Separation等)
            venues: 会议列表 (iclr/neurips/icml/cvpr/emnlp/acl/corl)
            min_relevance: 最低相关性分数
            limit: 返回结果数量

        Returns:
            论文匹配列表
        """
        problems = problems or []
        techs = techs or []
        venues = venues or list(PAPER_VENUES.keys())

        expanded_keywords = self._expand_keywords(query)
        logger.info(f"Expanded keywords: {expanded_keywords[:10]}...")

        all_papers = self._load_all_conferences(venues)

        matches = []
        for venue_key, papers in all_papers.items():
            for paper in papers:
                score = self._calculate_relevance(paper, expanded_keywords, problems, techs)

                if score >= min_relevance:
                    matched_problems = [p for p in problems if any(kw in (paper.get('title', '') + paper.get('abstract', '')).lower() for kw in PROBLEM_TO_KEYWORDS.get(p, []))]
                    matched_techs = [t for t in techs if any(kw in (paper.get('title', '') + paper.get('abstract', '')).lower() for kw in TECH_TO_KEYWORDS.get(t, []))]

                    match = PaperMatch(
                        title=paper.get('title', ''),
                        abstract=paper.get('abstract', ''),
                        authors=paper.get('authors', [])[:5],
                        venue=venue_key.upper(),
                        year=PAPER_VENUES.get(venue_key, {}).get('year', 0),
                        url=paper.get('url', ''),
                        pdf_url=paper.get('pdf', ''),
                        citation_count=paper.get('citation_count', 0),
                        primary_area=paper.get('primary_area', ''),
                        matched_problems=matched_problems,
                        matched_techs=matched_techs,
                        relevance_score=score,
                        read_time_minutes=self._estimate_read_time(paper)
                    )
                    matches.append(match)

        matches.sort(key=lambda x: x.relevance_score, reverse=True)
        logger.info(f"Found {len(matches)} papers, returning top {limit}")

        return matches[:limit]

    def fast_search(
        self,
        problems: List[str] = None,
        techs: List[str] = None,
        limit: int = 50
    ) -> List[PaperMatch]:
        """
        快速搜索（使用预建索引，毫秒级响应）

        Args:
            problems: 问题标签列表
            techs: 技术标签列表
            limit: 返回结果数量

        Returns:
            论文匹配列表
        """
        if self._index is None:
            logger.warning("Index not available, falling back to full search")
            return self.search('', problems=problems, techs=techs, limit=limit)

        problems = problems or []
        techs = techs or []

        if problems:
            indexed_papers = self._index.search_by_problems(problems, limit=limit * 2)
        elif techs:
            indexed_papers = self._index.search_by_techs(techs, limit=limit * 2)
        else:
            indexed_papers = list(self._index._index.values())[:limit]

        matches = []
        for ip in indexed_papers:
            matched_problems = [p for p in problems if p in ip.problems]
            matched_techs = [t for t in techs if t in ip.techs]

            score = len(matched_problems) * 3.0 + len(matched_techs) * 5.0
            score += ip.citation_count * 0.1

            match = PaperMatch(
                title=ip.title,
                abstract='',
                authors=[],
                venue=ip.venue,
                year=ip.year,
                url=ip.url,
                pdf_url='',
                citation_count=ip.citation_count,
                primary_area='',
                matched_problems=matched_problems,
                matched_techs=matched_techs,
                relevance_score=score,
                read_time_minutes=30
            )
            matches.append(match)

        matches.sort(key=lambda x: x.relevance_score, reverse=True)
        return matches[:limit]

    def search_by_problem(self, problem: str, limit: int = 50) -> List[PaperMatch]:
        """按问题搜索论文"""
        if problem not in PROBLEM_TO_KEYWORDS:
            logger.warning(f"Unknown problem: {problem}")
            return []

        return self.search(
            query=problem,
            problems=[problem],
            min_relevance=10.0,
            limit=limit
        )

    def search_by_tech(self, tech: str, limit: int = 50) -> List[PaperMatch]:
        """按技术搜索论文"""
        if tech not in TECH_TO_KEYWORDS:
            logger.warning(f"Unknown tech: {tech}")
            return []

        return self.search(
            query=tech,
            techs=[tech],
            min_relevance=10.0,
            limit=limit
        )

    def build_reading_pyramid(
        self,
        query: str,
        problems: List[str] = None,
        techs: List[str] = None,
        venues: List[str] = None
    ) -> ReadingPyramid:
        """
        构建阅读金字塔

        Returns:
            ReadingPyramid with:
            - top10_cards: 10篇论文卡片 (30秒/篇)
            - top3_skeleton: 3篇骨架阅读 (3分钟/篇)
            - top1_deep: 1篇深度精读 (30分钟)
        """
        results = self.search(
            query=query,
            problems=problems,
            techs=techs,
            venues=venues,
            min_relevance=5.0,
            limit=30
        )

        if not results:
            return ReadingPyramid()

        pyramid = ReadingPyramid()

        pyramid.top10_cards = results[:10]

        top15 = results[:15]
        for paper in top15:
            if paper.read_time_minutes <= 15 and len(pyramid.top3_skeleton) < 3:
                pyramid.top3_skeleton.append(paper)

        if len(pyramid.top3_skeleton) < 3:
            pyramid.top3_skeleton = top15[:3]

        if results:
            pyramid.top1_deep = results[0]

        return pyramid

    def generate_paper_card(self, paper: PaperMatch) -> str:
        """生成论文速读卡片"""
        card = f"""
## 📄 {paper.title}

**Venue:** {paper.venue} {paper.year}
**Area:** {paper.primary_area}
**Citations:** {paper.citation_count}

### 🎯 一句话总结
{paper.abstract[:300]}...

### 🏷️ 匹配标签
{" / ".join([f"`{p}`" for p in paper.matched_problems])}
{" / ".join([f"`{t}`" for t in paper.matched_techs])}

### ⏱️ 预估阅读时间
{paper.read_time_minutes} 分钟

### 🔗 链接
[Paper]({paper.url}) | [PDF]({paper.pdf_url})
"""
        return card

    def generate_skeleton_reading(self, paper: PaperMatch) -> str:
        """生成骨架阅读指南"""
        skeleton = f"""
## 📑 骨架阅读: {paper.title}

**Venue:** {paper.venue} {paper.year} | **Citations:** {paper.citation_count}

### 📝 摘要
{paper.abstract[:500]}...

### 🔑 关键问题
- 这篇论文解决了什么问题？
- 使用了什么方法？
- 结果如何？

### 💡 技术要点
1. **核心创新点:** (从摘要提取)
2. **关键技术:** {" / ".join(paper.matched_techs)}
3. **解决问题:** {" / ".join(paper.matched_problems)}

### 🎯 是否值得深度阅读?
- 阅读价值: {'⭐⭐⭐' if paper.relevance_score > 20 else '⭐⭐'} (分数: {paper.relevance_score:.1f})
- 预估时间: {paper.read_time_minutes} 分钟

### 🔗 链接
[Paper]({paper.url}) | [PDF]({paper.pdf_url})
"""
        return skeleton

    def print_search_results(self, results: List[PaperMatch], top_n: int = 10):
        """打印搜索结果"""
        print(f"\n{'='*80}")
        print(f"找到 {len(results)} 篇相关论文")
        print(f"{'='*80}\n")

        for i, paper in enumerate(results[:top_n], 1):
            print(f"[{i}] {paper.title[:70]}...")
            print(f"    Venue: {paper.venue} {paper.year} | Citations: {paper.citation_count}")
            print(f"    Score: {paper.relevance_score:.1f} | Read: {paper.read_time_minutes}min")
            print(f"    Tags: {' / '.join(paper.matched_problems + paper.matched_techs[:3])}")
            print()

    def print_reading_pyramid(self, pyramid: ReadingPyramid):
        """打印阅读金字塔"""
        print(f"\n{'='*80}")
        print("📚 阅读金字塔")
        print(f"{'='*80}\n")

        print("### 🏆 Top 1 深度精读 (30分钟)")
        if pyramid.top1_deep:
            p = pyramid.top1_deep
            print(f"    {p.title[:60]}...")
            print(f"    {p.venue} {p.year} | Citations: {p.citation_count}")
            print(f"    Tags: {' / '.join(p.matched_problems + p.matched_techs)}")
        print()

        print("### 📖 Top 3 骨架阅读 (3分钟/篇)")
        for i, p in enumerate(pyramid.top3_skeleton, 1):
            print(f"    [{i}] {p.title[:60]}...")
            print(f"        {p.venue} {p.year} | {p.read_time_minutes}min")
        print()

        print(f"### 📝 Top 10 论文卡片 (30秒/篇)")
        print(f"    (生成详细卡片请使用 generate_paper_card() 方法)")
        for i, p in enumerate(pyramid.top10_cards, 1):
            print(f"    [{i}] {p.title[:50]}... | {p.venue}")
