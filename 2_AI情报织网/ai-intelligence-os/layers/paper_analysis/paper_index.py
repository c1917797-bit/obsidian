"""
Paper Index - 论文索引预计算
避免每次查询都扫描27,800篇论文
"""
import os
import json
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Set
from dataclasses import dataclass, asdict
from collections import defaultdict

from core.logger import get_logger

logger = get_logger("PaperIndex")


PROBLEM_KEYWORDS = {
    'Latency': ['latency', 'delay', 'ttft', 'time to first token', 'response time', '首字延迟', '实时', '低延迟'],
    'Throughput': ['throughput', 'tps', 'qps', '吞吐', '并发', 'bandwidth'],
    'Memory': ['memory', '显存', 'vram', 'kv cache', 'cache', '内存', 'oom', 'paged attention'],
    'Scalability': ['scalability', 'scale', 'distributed', 'multi-gpu', 'tensor parallel', '多卡', '扩展'],
    'Cost': ['cost', 'flops', 'compute efficiency', 'energy', '成本', '性价比'],
    'Reliability': ['reliability', 'fault tolerance', '容错', '可用性'],
    'Accuracy': ['accuracy', 'benchmark', 'eval', '评测', '精度', 'performance'],
    'Agent-Capability': ['agent', 'multi-agent', 'planning', 'reasoning', 'memory', '智能体'],
}

TECH_KEYWORDS = {
    'KV Cache': ['kv cache', 'paged attention', 'pagedattention', 'kvcache'],
    'Speculative Decoding': ['speculative', 'draft model', 'medusa', 'eagle', 'lookahead', 'multi-token prediction'],
    'MoE': ['mixture of experts', 'moe', 'mixtral'],
    'Quantization': ['quantize', 'quantization', 'int8', 'int4', 'fp8', 'awq', 'gptq', 'gguf'],
    'PD Separation': ['prefill', 'decode', 'pd separation', 'disaggregation', 'prefill-decoding'],
    'Distributed Inference': ['tensor parallel', 'pipeline parallel', 'data parallel', 'distributed serving'],
    'Continuous Batching': ['continuous batching', 'iteration scheduling', 'batch scheduling'],
    'vLLM': ['vllm'],
    'SGLang': ['sglang'],
    'Attention': ['attention', 'transformer', 'self-attention'],
    'FlashAttention': ['flash attention', 'flashattention', 'flash'],
}


@dataclass
class IndexedPaper:
    """索引后的论文"""
    paper_id: str
    title: str
    title_lower: str
    venue: str
    year: int
    url: str
    citation_count: int
    problems: List[str]
    techs: List[str]
    relevance_buckets: Set[str]

    def to_dict(self) -> Dict:
        return {
            'paper_id': self.paper_id,
            'title': self.title,
            'title_lower': self.title_lower,
            'venue': self.venue,
            'year': self.year,
            'url': self.url,
            'citation_count': self.citation_count,
            'problems': list(self.problems),
            'techs': list(self.techs),
            'relevance_buckets': list(self.relevance_buckets)
        }

    @classmethod
    def from_dict(cls, d: Dict) -> 'IndexedPaper':
        d['problems'] = set(d['problems'])
        d['techs'] = set(d['techs'])
        d['relevance_buckets'] = set(d['relevance_buckets'])
        return cls(**d)


class PaperIndex:
    """
    论文索引 - 预计算所有论文的问题/技术标签
    支持快速查询，无需每次扫描全量论文
    """

    def __init__(self, cache_dir: str = None):
        if cache_dir is None:
            cache_dir = os.path.join(
                os.path.dirname(__file__),
                '..', 'data', 'paper_index'
            )
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.index_file = os.path.join(cache_dir, 'paper_index.json')
        self._index: Dict[str, IndexedPaper] = {}
        self._problem_index: Dict[str, Set[str]] = defaultdict(set)
        self._tech_index: Dict[str, Set[str]] = defaultdict(set)
        self._venue_index: Dict[str, List[str]] = defaultdict(list)
        self._loaded = False

    def _extract_paper_id(self, paper: Dict) -> str:
        """生成论文ID"""
        title = paper.get('title', '')
        venue = paper.get('venue', paper.get('id', ''))
        key = f"{venue}_{title}"
        return hashlib.md5(key.encode()).hexdigest()[:16]

    def _tag_problems(self, title: str, abstract: str = '') -> List[str]:
        """标签问题"""
        text = (title + ' ' + (abstract or '')).lower()
        matched = []
        for problem, keywords in PROBLEM_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                matched.append(problem)
        return matched

    def _tag_techs(self, title: str, abstract: str = '') -> List[str]:
        """标签技术"""
        text = (title + ' ' + (abstract or '')).lower()
        matched = []
        for tech, keywords in TECH_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                matched.append(tech)
        return matched

    def _build_index(self, papers: List[Dict]):
        """构建索引"""
        self._index.clear()
        self._problem_index.clear()
        self._tech_index.clear()
        self._venue_index.clear()

        for paper in papers:
            try:
                paper_id = self._extract_paper_id(paper)
                title = paper.get('title', '')
                venue = paper.get('venue', paper.get('source', '')).upper()
                year = paper.get('year', 0) or paper.get('published', '')[:4]
                if year:
                    try:
                        year = int(year)
                    except:
                        year = 0
                url = paper.get('url', paper.get('pdf', ''))
                citation_count = paper.get('citation_count', 0)
                abstract = paper.get('abstract', '')

                problems = self._tag_problems(title, abstract)
                techs = self._tag_techs(title, abstract)

                indexed = IndexedPaper(
                    paper_id=paper_id,
                    title=title,
                    title_lower=title.lower(),
                    venue=venue,
                    year=year,
                    url=url,
                    citation_count=citation_count,
                    problems=problems,
                    techs=techs,
                    relevance_buckets=set(problems + techs)
                )

                self._index[paper_id] = indexed

                for p in problems:
                    self._problem_index[p].add(paper_id)
                for t in techs:
                    self._tech_index[t].add(paper_id)
                self._venue_index[venue].append(paper_id)

            except Exception as e:
                continue

        logger.info(f"Indexed {len(self._index)} papers")
        for p, c in self._problem_index.items():
            logger.info(f"  {p}: {len(c)} papers")
        for t, c in self._tech_index.items():
            logger.info(f"  {t}: {len(c)} papers")

    def save(self):
        """保存索引到文件"""
        data = {
            'papers': {k: v.to_dict() for k, v in self._index.items()},
            'problem_index': {k: list(v) for k, v in self._problem_index.items()},
            'tech_index': {k: list(v) for k, v in self._tech_index.items()},
            'venue_index': {k: list(v) for k, v in self._venue_index.items()},
            'saved_at': datetime.now().isoformat()
        }
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        logger.info(f"Index saved to {self.index_file}")

    def load(self) -> bool:
        """从文件加载索引"""
        if not os.path.exists(self.index_file):
            return False

        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self._index = {k: IndexedPaper.from_dict(v) for k, v in data['papers'].items()}
            self._problem_index = {k: set(v) for k, v in data['problem_index'].items()}
            self._tech_index = {k: set(v) for k, v in data['tech_index'].items()}
            self._venue_index = {k: list(v) for k, v in data['venue_index'].items()}

            logger.info(f"Loaded index with {len(self._index)} papers")
            self._loaded = True
            return True
        except Exception as e:
            logger.warning(f"Failed to load index: {e}")
            return False

    def needs_refresh(self, max_age_hours: int = 24) -> bool:
        """检查是否需要刷新"""
        if not os.path.exists(self.index_file):
            return True
        mtime = os.path.getmtime(self.index_file)
        age_hours = (datetime.now().timestamp() - mtime) / 3600
        return age_hours > max_age_hours

    def search_by_problems(
        self,
        problems: List[str],
        min_problems: int = 1,
        limit: int = 50
    ) -> List[IndexedPaper]:
        """按问题搜索（使用预建索引）"""
        if not self._loaded:
            return []

        if not problems:
            return list(self._index.values())[:limit]

        candidate_ids = None
        for p in problems:
            if p in self._problem_index:
                if candidate_ids is None:
                    candidate_ids = set(self._problem_index[p])
                else:
                    candidate_ids &= self._problem_index[p]

        if candidate_ids is None:
            return []

        results = []
        for pid in candidate_ids:
            paper = self._index[pid]
            match_count = sum(1 for p in problems if p in paper.problems)
            if match_count >= min_problems:
                results.append(paper)

        results.sort(key=lambda x: x.citation_count, reverse=True)
        return results[:limit]

    def search_by_techs(
        self,
        techs: List[str],
        min_techs: int = 1,
        limit: int = 50
    ) -> List[IndexedPaper]:
        """按技术搜索（使用预建索引）"""
        if not self._loaded:
            return []

        if not techs:
            return list(self._index.values())[:limit]

        candidate_ids = None
        for t in techs:
            if t in self._tech_index:
                if candidate_ids is None:
                    candidate_ids = set(self._tech_index[t])
                else:
                    candidate_ids &= self._tech_index[t]

        if candidate_ids is None:
            return []

        results = []
        for pid in candidate_ids:
            paper = self._index[pid]
            match_count = sum(1 for t in techs if t in paper.techs)
            if match_count >= min_techs:
                results.append(paper)

        results.sort(key=lambda x: x.citation_count, reverse=True)
        return results[:limit]

    def search_by_buckets(
        self,
        buckets: List[str],
        limit: int = 50
    ) -> List[IndexedPaper]:
        """按问题+技术组合搜索（快速）"""
        if not self._loaded:
            return []

        results = []
        for paper in self._index.values():
            if any(b in paper.relevance_buckets for b in buckets):
                results.append(paper)

        results.sort(key=lambda x: x.citation_count, reverse=True)
        return results[:limit]

    def build_from_conferences(self, conference_store):
        """从会议数据构建索引"""
        logger.info("Building index from conference papers...")

        all_papers = []
        venues = ['iclr', 'nips', 'icml', 'cvpr', 'emnlp', 'acl', 'corl']
        years = {'iclr': 2025, 'nips': 2025, 'icml': 2024, 'cvpr': 2024, 'emnlp': 2024, 'acl': 2024, 'corl': 2024}

        for venue in venues:
            year = years.get(venue, 2024)
            try:
                papers = conference_store.load_papers_from_url(venue, year)
                all_papers.extend(papers)
                logger.info(f"Loaded {len(papers)} from {venue.upper()}")
            except Exception as e:
                logger.warning(f"Failed to load {venue}: {e}")

        self._build_index(all_papers)
        self._loaded = True
        self.save()

    def get_stats(self) -> Dict:
        """获取索引统计"""
        return {
            'total_papers': len(self._index),
            'problem_distribution': {p: len(ids) for p, ids in self._problem_index.items()},
            'tech_distribution': {t: len(ids) for t, ids in self._tech_index.items()},
            'venue_distribution': {v: len(ids) for v, ids in self._venue_index.items()},
        }
