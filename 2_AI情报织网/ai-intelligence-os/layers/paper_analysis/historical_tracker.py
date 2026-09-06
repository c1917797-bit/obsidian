"""
Historical Paper Scanner - 历史高价值论文扫描
专门扫描 2025 年高引用论文

用法:
    python historical_tracker.py --problems "KV Cache" --min-citations 10
    python historical_tracker.py --all-problems --min-citations 5
"""
import os
import sys
import json
import re
import time
import requests
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
try:
    from core.minimax_client import get_client
    from core.logger import get_logger
except ImportError:
    get_client = None
    get_logger = None

SCRIPT_DIR = Path(__file__).parent
OBSIDIAN_ROOT = Path("C:/Users/Huawei/Documents/code/Obsidian")
AI_OS_ROOT = SCRIPT_DIR.parent.parent.parent
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"
CONFIG_DIR = AI_OS_ROOT / "config"

logger = get_logger("HistoricalTracker") if get_logger else None


# 问题空间 → 2025年搜索关键词
PROBLEM_QUERIES_2025 = {
    'KV Cache': 'ti:("kv cache" OR "paged attention" OR "memory management") AND all:2025',
    'Distributed Inference': 'ti:("tensor parallel" OR "pipeline parallel" OR "distributed inference") AND all:2025',
    'Agent-Capability': 'ti:(agent OR "multi-agent" OR planning OR reasoning) AND all:2025',
    'Latency': 'ti:(latency OR "inference speed" OR "response time") AND all:2025',
    'Throughput': 'ti:(throughput OR "tokens per second" OR serving) AND all:2025',
    'Scalability': 'ti:(scalability OR "multi-gpu" OR distributed) AND all:2025',
    'Speculative Decoding': 'ti:("speculative" OR "draft model" OR specdec) AND all:2025',
    'MoE': 'ti:("mixture of experts" OR moe) AND all:2025',
    'Quantization': 'ti:(quantize OR quantization) AND all:2025',
}

ARXIV_API = "http://export.arxiv.org/api/query"


class HistoricalTracker:
    """
    历史高价值论文扫描器

    策略：
    1. 先用 2025 年搜索（包含年份过滤）
    2. 再用 Semantic Scholar 补充引用数
    3. 按引用数排序，过滤低引用
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 IntelligenceOS/1.0'
        })
        self.client = get_client() if get_client else None
        self.tracked = 0

    def search_2025_papers(
        self,
        query: str,
        max_results: int = 50,
        min_citations: int = 5
    ) -> List[Dict]:
        """搜索 2025 年论文"""
        params = {
            'search_query': query,
            'max_results': min(max_results, 100),
            'sortBy': 'relevance',  # 按相关性排序
            'sortOrder': 'descending'
        }

        url = f"{ARXIV_API}?{urlencode(params)}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return self._parse_entries(response.text)
        except Exception as e:
            if logger:
                logger.error(f"Search failed: {e}")
            return []

    def _parse_entries(self, xml_text: str) -> List[Dict]:
        """解析 ATOM 响应"""
        papers = []
        entries = re.findall(r'<entry>(.*?)</entry>', xml_text, re.DOTALL)

        for entry in entries:
            try:
                title = re.sub(r'\s+', ' ', re.search(r'<title>(.*?)</title>', entry, re.DOTALL).group(1)).strip()
                authors = re.findall(r'<name>(.*?)</name>', entry)
                abstract = re.sub(r'\s+', ' ', re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL).group(1)).strip()

                published = re.search(r'<published>(.*?)</published>', entry)
                published = published.group(1)[:10] if published else ""

                arxiv_id = re.search(r'<id>(.*?)</id>', entry)
                arxiv_id = arxiv_id.group(1).split('/abs/')[-1] if arxiv_id else ""

                categories = re.findall(r'<category term="([^"]+)"', entry)

                papers.append({
                    'arxiv_id': arxiv_id,
                    'title': title,
                    'authors': authors,
                    'abstract': abstract,
                    'published': published,
                    'categories': categories,
                    'pdf_url': f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                    'url': f"https://arxiv.org/abs/{arxiv_id}",
                    'citation_count': 0  # 待 enrichment
                })
            except Exception:
                continue

        return papers

    def enrich_citations(self, papers: List[Dict], limit: int = 30) -> List[Dict]:
        """用 Semantic Scholar 获取引用数"""
        import urllib.parse

        S2_API = "https://api.semanticscholar.org/graph/v1/paper/arXiv:"

        enriched = 0
        for paper in papers[:limit]:
            try:
                paper_id = f"arXiv:{paper['arxiv_id']}"
                url = f"{S2_API}{urllib.parse.quote(paper['arxiv_id'])}?fields=citationCount,year,venue"

                resp = self.session.get(url, timeout=15)
                if resp.status_code == 200:
                    data = resp.json()
                    paper['citation_count'] = data.get('citationCount', 0)
                    paper['year'] = data.get('year', 2025)
                    paper['venue'] = data.get('venue', 'arXiv')
                    enriched += 1

                time.sleep(0.3)  # 限速
            except Exception:
                continue

        return papers

    def scan_problem(
        self,
        problem: str,
        query: str,
        min_citations: int = 5,
        max_save: int = 20
    ) -> List[Dict]:
        """扫描单个问题空间"""
        print(f"\n🔍 问题: {problem}")
        print(f"   查询: {query[:60]}...")

        papers = self.search_2025_papers(query, max_results=50)
        print(f"   arXiv 返回: {len(papers)} 篇")

        if not papers:
            return []

        # Enrich 引用数
        papers = self.enrich_citations(papers, limit=30)

        # 按引用数排序
        papers.sort(key=lambda x: x['citation_count'], reverse=True)

        # 过滤
        high_quality = [p for p in papers if p['citation_count'] >= min_citations]
        print(f"   引用≥{min_citations}: {len(high_quality)} 篇")

        return high_quality[:max_save]

    def save_to_corpus(self, paper: Dict, citekey: str) -> bool:
        """保存到 _corpus"""
        CORPUS_DIR.mkdir(parents=True, exist_ok=True)

        filepath = CORPUS_DIR / f"{citekey}.md"
        if filepath.exists():
            return False

        # 生成 citekey
        if not citekey:
            words = re.findall(r'[a-zA-Z]+', paper['title'].lower())
            meaningful = [w for w in words if len(w) > 4][:4]
            citekey = ''.join(w[0] for w in meaningful)[:6] + str(paper.get('year', 2025))

        content = self._format_entry(paper, citekey)
        filepath.write_text(content, encoding='utf-8')
        self.tracked += 1
        return True

    def _format_entry(self, paper: Dict, citekey: str) -> str:
        """格式化 corpus 条目"""
        authors_str = '; '.join(paper.get('authors', [])[:5])
        year = paper.get('year', paper.get('published', '2025')[:4])

        return f"""---
type: literature-corpus-entry
citekey: {citekey}
title: "{paper['title']}"
authors: {authors_str}
year: {year}
venue: {paper.get('venue', 'arXiv')}
url: {paper.get('url', '')}
pdf_url: {paper.get('pdf_url', '')}
abstract: |
{paper.get('abstract', '')[:2000]}
citation_count: {paper.get('citation_count', 0)}
relevance_score: {min(paper.get('citation_count', 0) * 2 + 30, 100)}
matched_problems: []
matched_techs: []
pre_screened_status: Included
source: historical-scan-2025
created: {datetime.now().strftime('%Y-%m-%d')}
---

# {paper['title']}

**{paper.get('venue', 'arXiv')} | {year}** | Citations: {paper.get('citation_count', 0)}

## 作者
{authors_str}

## 摘要
{paper.get('abstract', '无')[:1000]}...

## 链接
- [arXiv]({paper.get('url', '')}) | [PDF]({paper.get('pdf_url', '')})

---

*由 Historical Tracker 扫描 | 2025-06-03*
"""

    def run_all(
        self,
        problems: Dict[str, str] = None,
        min_citations: int = 5,
        max_per_problem: int = 15,
        dry_run: bool = False
    ) -> Dict:
        """
        运行全量扫描

        Args:
            problems: 问题→查询 dict
            min_citations: 最低引用数
            max_per_problem: 每个问题最多保存数
            dry_run: 只打印不保存
        """
        problems = problems or PROBLEM_QUERIES_2025

        print("\n" + "=" * 70)
        print("📚 Historical Paper Scanner - 2025 高价值论文扫描")
        print("=" * 70)
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"最低引用数: {min_citations}")
        print(f"每问题最多保存: {max_per_problem}")
        print(f"模式: {'DRY-RUN' if dry_run else 'LIVE'}")
        print("=" * 70)

        total_saved = 0
        total_found = 0

        for problem, query in problems.items():
            papers = self.scan_problem(problem, query, min_citations, max_per_problem)
            total_found += len(papers)

            if not dry_run:
                for paper in papers:
                    citekey = self._generate_citekey(paper)
                    if self.save_to_corpus(paper, citekey):
                        print(f"   💾 保存: {paper['title'][:50]}... (cite={paper['citation_count']})")
                        total_saved += 1

        print("\n" + "=" * 70)
        print("📊 扫描结果")
        print("=" * 70)
        print(f"发现高价值论文: {total_found} 篇")
        print(f"保存到 _corpus: {total_saved} 篇")
        print("=" * 70)

        return {
            'found': total_found,
            'saved': total_saved,
            'problems': len(problems)
        }

    def _generate_citekey(self, paper: Dict) -> str:
        words = re.findall(r'[a-zA-Z]+', paper['title'].lower())
        meaningful = [w for w in words if len(w) > 4 and w not in
                     ('the', 'with', 'from', 'that', 'this', 'based', 'using', 'learning', 'network', 'model')]
        prefix = ''.join(w[0] for w in meaningful[:4])[:6]
        year = paper.get('year', '2025')
        return f"{prefix}{year}"


def urlencode(params: Dict) -> str:
    import urllib.parse
    return urllib.parse.urlencode(params)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Historical Paper Scanner')
    parser.add_argument('--problems', '-p', help='问题空间 (逗号分隔)')
    parser.add_argument('--min-citations', '-c', type=int, default=5, help='最低引用数')
    parser.add_argument('--max', '-m', type=int, default=15, help='每问题最多保存数')
    parser.add_argument('--dry-run', '-n', action='store_true', help='只打印不保存')

    args = parser.parse_args()

    # 构建问题 dict
    if args.problems:
        problem_list = [p.strip() for p in args.problems.split(',')]
        problems = {p: PROBLEM_QUERIES_2025.get(p, f'all:{p}') for p in problem_list}
    else:
        problems = PROBLEM_QUERIES_2025

    tracker = HistoricalTracker()
    result = tracker.run_all(
        problems=problems,
        min_citations=args.min_citations,
        max_per_problem=args.max,
        dry_run=args.dry_run
    )

    return result


if __name__ == "__main__":
    main()
