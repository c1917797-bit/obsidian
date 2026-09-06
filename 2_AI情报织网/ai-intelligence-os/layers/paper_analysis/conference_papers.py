"""
Conference Papers Integration - 顶会论文集成
集成 paperlists 数据: ICLR/NeurIPS/ICML/CVPR 等38个顶会

能力:
- 顶会论文JSON读取
- 论文搜索/筛选
- 论文元数据提取
- 论文信号生成
"""
import os
import json
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

from core.logger import get_logger

logger = get_logger("ConferencePapers")

@dataclass
class PaperMetadata:
    """论文元数据"""
    paper_id: str
    title: str
    authors: List[str] = field(default_factory=list)
    abstract: str = ""
    keywords: List[str] = field(default_factory=list)
    primary_area: str = ""
    venue: str = ""
    year: int = 0
    url: str = ""
    pdf_url: str = ""
    code_url: str = ""
    citation_count: int = 0
    influence_score: float = 0.0

    def to_signal_dict(self) -> Dict:
        return {
            'id': self.paper_id,
            'title': self.title,
            'authors': self.authors,
            'abstract': self.abstract,
            'keywords': self.keywords,
            'primary_area': self.primary_area,
            'venue': self.venue,
            'year': self.year,
            'url': self.url,
            'source': f'{self.venue}_{self.year}',
            'category': 'research_paper',
            'source_type': 'conference_paper',
            'published': f'{self.year}-01-01'
        }


VENUES = {
    'iclr': 'International Conference on Learning Representations',
    'neurips': 'Neural Information Processing Systems',
    'icml': 'International Conference on Machine Learning',
    'cvpr': 'Conference on Computer Vision and Pattern Recognition',
    'iccv': 'International Conference on Computer Vision',
    'eccv': 'European Conference on Computer Vision',
    'nips': 'Neural Information Processing Systems',
    'emnlp': 'Empirical Methods in Natural Language Processing',
    'acl': 'Association for Computational Linguistics',
    'aaai': 'Association for the Advancement of Artificial Intelligence',
    'ijcai': 'International Joint Conference on Artificial Intelligence',
    'kdd': 'Knowledge Discovery and Data Mining',
    'siggraph': 'Special Interest Group on Computer Graphics',
    'siggraphasia': 'SIGGRAPH Asia',
    'corl': 'Conference on Robot Learning',
    'uai': 'Uncertainty in Artificial Intelligence',
    'aistats': 'Artificial Intelligence and Statistics',
    'wacv': 'Winter Conference on Applications of Computer Vision',
    'iro': 'International Conference on Intelligent Robots',
    'icra': 'International Conference on Robotics and Automation',
    'colt': 'Conference on Learning Theory',
    'alt': 'Algorithmic Learning Theory',
    'acml': 'Asian Conference on Machine Learning',
    'naacl': 'North American Chapter of the Association for Computational Linguistics',
    'coling': 'International Conference on Computational Linguistics',
    'acmmm': 'ACM Multimedia Conference',
    'www': 'The Web Conference',
    '3dv': 'International Conference on 3D Vision',
    'ai4x': 'AI for Science Workshop',
    'automl': 'International Conference on Automated Machine Learning',
    'rl': 'Reinforcement Learning Conference',
}

PAPERLISTS_BASE = "https://raw.githubusercontent.com/Papercopilot/paperlists/main"

class ConferencePaperStore:
    """
    顶会论文仓库
    支持38个顶会的历年论文JSON
    """

    def __init__(self, cache_dir: str = None):
        self.cache_dir = cache_dir or os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'data', 'conference_papers'
        )
        os.makedirs(self.cache_dir, exist_ok=True)
        self._paper_cache = {}

    def get_paper_json_url(self, venue: str, year: int) -> str:
        """获取论文JSON的GitHub Raw URL"""
        venue_lower = venue.lower()
        return f"{PAPERLISTS_BASE}/{venue_lower}/{venue_lower}{year}.json"

    def get_local_json_path(self, venue: str, year: int) -> str:
        """本地缓存路径"""
        return os.path.join(self.cache_dir, f'{venue.lower()}{year}.json')

    def load_papers_from_url(self, venue: str, year: int, force: bool = False) -> List[Dict]:
        """从GitHub加载论文JSON"""
        import requests

        local_path = self.get_local_json_path(venue, year)
        cache_key = f"{venue}_{year}"

        if not force and cache_key in self._paper_cache:
            return self._paper_cache[cache_key]

        if not force and os.path.exists(local_path):
            try:
                with open(local_path, 'r', encoding='utf-8') as f:
                    papers = json.load(f)
                    self._paper_cache[cache_key] = papers
                    return papers
            except Exception as e:
                logger.warning(f"Failed to load local cache for {venue}{year}: {e}")

        try:
            url = self.get_paper_json_url(venue, year)
            logger.info(f"Fetching {venue}{year} papers from {url}")

            import time
            for retry in range(3):
                try:
                    resp = requests.get(url, timeout=30)
                    resp.raise_for_status()
                    resp.encoding = 'utf-8'
                    break
                except Exception as retry_err:
                    if retry < 2:
                        wait = 2 ** retry
                        logger.warning(f"Retry {retry+1}/3 for {venue}{year} after {wait}s: {retry_err}")
                        time.sleep(wait)
                    else:
                        raise

            papers = json.loads(resp.text)

            with open(local_path, 'w', encoding='utf-8') as f:
                json.dump(papers, f, ensure_ascii=False, indent=2)

            self._paper_cache[cache_key] = papers
            logger.info(f"Loaded {len(papers)} papers for {venue}{year}")
            return papers

        except Exception as e:
            logger.error(f"Failed to load papers for {venue}{year}: {e}")
            return []

    def search_papers(
        self,
        venue: str,
        year: int,
        keyword: str = None,
        area: str = None,
        limit: int = 50
    ) -> List[PaperMetadata]:
        """搜索论文"""
        papers = self.load_papers_from_url(venue, year)
        if not papers:
            return []

        results = []
        for paper in papers:
            if keyword:
                kw_lower = keyword.lower()
                title = paper.get('title', '').lower()
                abstract = paper.get('abstract', '').lower()
                keywords = paper.get('keywords', [])
                if kw_lower not in title and kw_lower not in abstract:
                    if not any(kw_lower in str(k).lower() for k in keywords):
                        continue

            if area:
                paper_area = paper.get('primary_area', '')
                if area.lower() not in paper_area.lower():
                    continue

            meta = PaperMetadata(
                paper_id=paper.get('id', paper.get('paper_id', '')),
                title=paper.get('title', ''),
                authors=paper.get('authors', []),
                abstract=paper.get('abstract', ''),
                keywords=paper.get('keywords', []),
                primary_area=paper.get('primary_area', ''),
                venue=venue.upper(),
                year=year,
                url=paper.get('url', ''),
                pdf_url=paper.get('pdf', ''),
                code_url=paper.get('code', ''),
                citation_count=paper.get('citation_count', 0)
            )
            results.append(meta)

            if len(results) >= limit:
                break

        return results

    def get_trending_papers(
        self,
        venues: List[str] = None,
        years: List[int] = None,
        limit: int = 20
    ) -> List[PaperMetadata]:
        """获取热门/高引用论文"""
        if venues is None:
            venues = ['iclr', 'neurips', 'icml']
        if years is None:
            years = [2025, 2024]

        all_papers = []
        for venue in venues:
            for year in years:
                papers = self.load_papers_from_url(venue, year)
                for p in papers:
                    if p.get('citation_count', 0) > 10:
                        all_papers.append(p)

        all_papers.sort(key=lambda x: x.get('citation_count', 0), reverse=True)

        results = []
        for paper in all_papers[:limit]:
            venue = paper.get('venue', '').lower()
            year = paper.get('year', 2024)
            meta = PaperMetadata(
                paper_id=paper.get('id', ''),
                title=paper.get('title', ''),
                authors=paper.get('authors', []),
                abstract=paper.get('abstract', ''),
                keywords=paper.get('keywords', []),
                primary_area=paper.get('primary_area', ''),
                venue=venue.upper(),
                year=year,
                url=paper.get('url', ''),
                citation_count=paper.get('citation_count', 0)
            )
            results.append(meta)

        return results

    def generate_paper_signals(self, venue: str, year: int, topic: str = None) -> List[Dict]:
        """生成论文信号"""
        papers = self.search_papers(venue, year, keyword=topic, limit=20)

        signals = []
        for paper in papers:
            signals.append({
                'id': hashlib.md5(paper.title.encode()).hexdigest()[:16],
                'title': paper.title,
                'url': paper.url or paper.pdf_url,
                'source': f'{venue.upper()} {year}',
                'source_id': f'{venue}_{year}_{paper.paper_id}',
                'source_type': 'conference_paper',
                'category': 'research_paper',
                'priority': 'P0' if paper.citation_count > 50 else 'P1',
                'published': f'{year}-01-01',
                'summary': paper.abstract[:500] if paper.abstract else '',
                'authors': paper.authors,
                'tags': paper.keywords + [paper.primary_area],
                'metadata': {
                    'venue': venue.upper(),
                    'year': year,
                    'citation_count': paper.citation_count,
                    'primary_area': paper.primary_area
                }
            })

        return signals


def get_available_venues() -> List[str]:
    """获取支持的所有顶会"""
    return list(VENUES.keys())


def get_venue_display_name(venue: str) -> str:
    """获取顶会全名"""
    return VENUES.get(venue.lower(), venue.upper())


if __name__ == '__main__':
    store = ConferencePaperStore()

    print("=" * 60)
    print("Conference Paper Store - 测试")
    print("=" * 60)

    print("\n支持顶会:")
    for v in get_available_venues()[:10]:
        print(f"  - {v}: {get_venue_display_name(v)}")

    print("\n搜索 ICLR 2025 关于 transformers 的论文:")
    papers = store.search_papers('iclr', 2025, keyword='transformer', limit=5)
    for p in papers:
        print(f"\n  [{p.paper_id}] {p.title}")
        print(f"  作者: {', '.join(p.authors[:3])}")
        print(f"  引用: {p.citation_count}")
        print(f"  领域: {p.primary_area}")

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)