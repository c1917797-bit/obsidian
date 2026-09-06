"""
Academic Paper Tracker - 自动化学术论文追踪
基于问题空间 (problem_spaces) 的主动论文发现

功能:
1. arXiv API 关键词搜索
2. Semantic Scholar 论文 enrichment
3. 自动生成 Paper Card 保存到 _corpus
4. 与 IntelligenceOS pipeline 集成

用法:
    python academic_tracker.py --problems "KV Cache,Agent" --limit 20
    python academic_tracker.py --run-daily  # 每日自动追踪模式
"""
import os
import sys
import json
import re
import time
import hashlib
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field, asdict
from pathlib import Path
import urllib.parse

# 路径常量
SCRIPT_DIR = Path(__file__).parent
OBSIDIAN_ROOT = Path("C:/Users/Huawei/Documents/code/Obsidian")
AI_OS_ROOT = SCRIPT_DIR.parent.parent
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"
PAPER_CARDS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/Daily"
CONFIG_DIR = AI_OS_ROOT / "config"

# 导入 MiniMax client
sys.path.insert(0, str(AI_OS_ROOT))
try:
    from core.minimax_client import get_client
    from core.logger import get_logger
    MINIMAX_AVAILABLE = True
except ImportError:
    MINIMAX_AVAILABLE = False
    print("⚠️  MiniMax client 不可用")

logger = get_logger("AcademicTracker") if MINIMAX_AVAILABLE else None


# 问题空间 → arXiv 搜索关键词映射
PROBLEM_TO_ARXIV_QUERY = {
    'Latency': 'ti:(latency OR "inference speed" OR "response time" OR "first token") AND abs:(inference OR LLM OR transformer)',
    'Throughput': 'ti:(throughput OR "tokens per second" OR serving) AND abs:(inference OR LLM)',
    'Memory': 'ti:(memory OR "kv cache" OR "paged attention" OR compression) AND abs:(LLM OR inference)',
    'Scalability': 'ti:(scalability OR "multi-gpu" OR distributed OR parallel) AND abs:(inference OR LLM)',
    'Agent-Capability': 'ti:(agent OR "multi-agent" OR planning OR reasoning) AND abs:(LLM OR language model)',
    'Distributed Inference': 'ti:("distributed inference" OR "tensor parallel" OR "pipeline parallel") AND abs:(LLM)',
    'Speculative Decoding': 'ti:("speculative" OR "draft model" OR "specdec") AND abs:(decoding OR inference)',
    'KV Cache': 'ti:("kv cache" OR "paged attention" OR cache) AND abs:(LLM OR transformer)',
}

# 技术关键词
TECH_KEYWORDS = [
    'KV Cache', 'Speculative Decoding', 'MoE', 'Quantization',
    'PD Separation', 'Continuous Batching', 'vLLM', 'SGLang',
    'Tensor Parallel', 'Pipeline Parallel'
]


@dataclass
class ArxivPaper:
    """arXiv 论文"""
    arxiv_id: str
    title: str
    authors: List[str]
    abstract: str
    published: str
    updated: str
    categories: List[str]
    pdf_url: str
    citation_count: int = 0
    semantic_scholar_id: str = ""


@dataclass
class TrackedPaper:
    """追踪的论文"""
    paper_id: str
    citekey: str
    title: str
    authors: List[str]
    year: int
    venue: str  # arXiv 或会议
    doi: str = ""
    url: str = ""
    pdf_url: str = ""
    abstract: str = ""
    citation_count: int = 0
    relevance_score: float = 0.0
    matched_problems: List[str] = field(default_factory=list)
    matched_techs: List[str] = field(default_factory=list)
    relevance_score_breakdown: str = ""
    tracked_at: str = ""
    source: str = "arxiv"  # arxiv / semantic_scholar / conference


class ArxivClient:
    """arXiv API 客户端"""

    ARXIV_API = "http://export.arxiv.org/api/query"

    def __init__(self, delay: float = 3.0):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) IntelligenceOS/1.0'
        })

    def search(
        self,
        query: str,
        max_results: int = 20,
        sort_by: str = "submittedDate",
        sort_order: str = "descending"
    ) -> List[ArxivPaper]:
        """
        搜索 arXiv

        Args:
            query: arXiv 查询语法
            max_results: 最大结果数
            sort_by: submittedDate / lastUpdatedDate / relevance
            sort_order: descending / ascending

        Returns:
            ArxivPaper 列表
        """
        params = {
            'search_query': query,
            'max_results': min(max_results, 100),
            'sortBy': sort_by,
            'sortOrder': sort_order
        }

        url = f"{self.ARXIV_API}?{urllib.parse.urlencode(params)}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return self._parse_atom_response(response.text)
        except Exception as e:
            if logger:
                logger.error(f"arXiv search failed: {e}")
            return []

    def _parse_atom_response(self, xml_text: str) -> List[ArxivPaper]:
        """解析 ATOM 响应"""
        papers = []

        # 简单的 XML 解析（不用 lxml）
        entries = re.findall(r'<entry>(.*?)</entry>', xml_text, re.DOTALL)

        for entry in entries:
            try:
                title = self._extract_tag(entry, 'title')
                title = re.sub(r'\s+', ' ', title).strip()

                authors = re.findall(r'<name>(.*?)</name>', entry)
                abstract = self._extract_tag(entry, 'summary')
                abstract = re.sub(r'\s+', ' ', abstract).strip()

                published = self._extract_tag(entry, 'published')
                updated = self._extract_tag(entry, 'updated')

                arxiv_id = self._extract_tag(entry, 'id')
                if '/abs/' in arxiv_id:
                    arxiv_id = arxiv_id.split('/abs/')[-1]

                categories = re.findall(r'<category term="([^"]+)"', entry)
                pdf_url = ""
                for link in re.findall(r'<link[^>]+>', entry):
                    if 'title="pdf"' in link or 'type="application/pdf"' in link:
                        href = re.search(r'href="([^"]+)"', link)
                        if href:
                            pdf_url = href.group(1)
                            break

                paper = ArxivPaper(
                    arxiv_id=arxiv_id,
                    title=title,
                    authors=authors,
                    abstract=abstract,
                    published=published[:10] if published else "",
                    updated=updated[:10] if updated else "",
                    categories=categories,
                    pdf_url=pdf_url,
                    citation_count=0
                )
                papers.append(paper)

            except Exception as e:
                if logger:
                    logger.warning(f"Failed to parse entry: {e}")
                continue

        return papers

    def _extract_tag(self, text: str, tag: str) -> str:
        """提取 XML 标签内容"""
        match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
        return match.group(1) if match else ""


class SemanticScholarClient:
    """Semantic Scholar API 客户端"""

    S2_API = "https://api.semanticscholar.org/graph/v1"
    S2_FIELDS = "title,authors,abstract,year,venue,citationCount,externalIds,url,influentialCitationCount"

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('S2_API_KEY', '')
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({'x-api-key': self.api_key})
        self.session.headers.update({'User-Agent': 'IntelligenceOS/1.0'})

    def get_paper(self, paper_id: str, fields: str = None) -> Optional[Dict]:
        """
        获取论文详情

        Args:
            paper_id: arXiv ID (不带 arXiv:) 或 DOI
            fields: 要获取的字段

        Returns:
            论文详情 dict
        """
        fields = fields or self.S2_FIELDS
        endpoint = f"{self.S2_API}/paper/{paper_id}"

        try:
            response = self.session.get(
                endpoint,
                params={'fields': fields},
                timeout=30
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None
            else:
                if logger:
                    logger.warning(f"S2 API error: {response.status_code}")
                return None

        except Exception as e:
            if logger:
                logger.error(f"S2 get_paper failed: {e}")
            return None

    def get_citations(self, paper_id: str, limit: int = 10) -> List[Dict]:
        """获取引用"""
        endpoint = f"{self.S2_API}/paper/{paper_id}/citations"
        try:
            response = self.session.get(
                endpoint,
                params={'fields': 'title,year,venue,citationCount', 'limit': limit},
                timeout=30
            )
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
        except Exception:
            pass
        return []

    def search(self, query: str, limit: int = 20) -> List[Dict]:
        """搜索论文"""
        endpoint = f"{self.S2_API}/paper/search"
        try:
            response = self.session.get(
                endpoint,
                params={
                    'query': query,
                    'fields': self.S2_FIELDS,
                    'limit': limit
                },
                timeout=30
            )
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
        except Exception as e:
            if logger:
                logger.error(f"S2 search failed: {e}")
        return []


class AcademicTracker:
    """
    学术论文追踪器

    基于问题空间自动追踪 arXiv 和 Semantic Scholar
    """

    def __init__(self, client=None, s2_client=None):
        self.arxiv = client or ArxivClient()
        self.s2 = s2_client or SemanticScholarClient()
        self.client = get_client() if MINIMAX_AVAILABLE else None
        self.tracked_count = 0

    def load_problem_spaces(self) -> Dict[str, List[str]]:
        """加载问题空间配置"""
        config_file = CONFIG_DIR / "problem_spaces.json"

        if config_file.exists():
            try:
                data = json.loads(config_file.read_text(encoding='utf-8'))
                return data.get('problem_spaces', {})
            except Exception:
                pass

        # 默认配置
        return {
            'KV Cache': ['memory', 'cache', 'paged attention'],
            'Distributed Inference': ['distributed', 'multi-gpu', 'tensor parallel'],
            'Agent': ['agent', 'multi-agent', 'planning'],
            'Latency': ['latency', 'inference speed', 'optimization'],
            'Speculative Decoding': ['speculative', 'draft model'],
        }

    def generate_citekey(self, title: str, year: int) -> str:
        """生成 citekey"""
        # 取标题前3个有意义的词
        words = re.findall(r'[a-zA-Z]+', title.lower())
        meaningful = [w for w in words if len(w) > 3 and w not in
                     ('the', 'and', 'with', 'from', 'that', 'this', 'based', 'using')]
        prefix = ''.join(w[0] for w in meaningful[:4])[:6]
        return f"{prefix}{year}"

    def calculate_relevance(
        self,
        paper: ArxivPaper,
        problems: Dict[str, List[str]]
    ) -> tuple[float, List[str], List[str]]:
        """计算论文相关性分数"""
        text = f"{paper.title} {paper.abstract}".lower()
        score = 0.0
        matched_problems = []
        matched_techs = []

        # 问题匹配
        for problem, keywords in problems.items():
            for kw in keywords:
                if kw.lower() in text:
                    score += 5.0
                    if problem not in matched_problems:
                        matched_problems.append(problem)

        # 技术匹配
        for tech in TECH_KEYWORDS:
            if tech.lower() in text:
                score += 8.0
                if tech not in matched_techs:
                    matched_techs.append(tech)

        # 标题匹配加权
        for problem, keywords in problems.items():
            for kw in keywords:
                if kw.lower() in paper.title.lower():
                    score += 10.0

        # 引用数加成 (如果已 enrichment)
        if paper.citation_count > 0:
            score += min(paper.citation_count * 0.1, 10.0)

        return score, matched_problems, matched_techs

    def enrich_with_semantic_scholar(self, paper: ArxivPaper) -> ArxivPaper:
        """用 Semantic Scholar 丰富论文信息"""
        try:
            # 尝试用 arXiv ID 查询
            s2_paper = self.s2.get_paper(f"arXiv:{paper.arxiv_id}")

            if s2_paper:
                paper.citation_count = s2_paper.get('citationCount', 0)
                paper.semantic_scholar_id = s2_paper.get('paperId', '')
                if not paper.abstract and s2_paper.get('abstract'):
                    paper.abstract = s2_paper.get('abstract')
                if s2_paper.get('externalIds', {}).get('DOI'):
                    paper.doi = s2_paper['externalIds']['DOI']
            else:
                # 尝试用标题搜索
                search_results = self.s2.search(paper.title, limit=1)
                if search_results:
                    matched = search_results[0]
                    paper.citation_count = matched.get('citationCount', 0)
                    paper.semantic_scholar_id = matched.get('paperId', '')

        except Exception as e:
            if logger:
                logger.warning(f"Enrichment failed for {paper.arxiv_id}: {e}")

        return paper

    def search_problem_spaces(self, problems: Dict[str, List[str]] = None, limit_per_problem: int = 10) -> List[TrackedPaper]:
        """
        搜索所有问题空间的新论文

        Args:
            problems: 问题空间 dict
            limit_per_problem: 每个问题最多返回论文数

        Returns:
            TrackedPaper 列表
        """
        problems = problems or self.load_problem_spaces()
        all_papers = []
        seen_ids = set()

        print(f"\n🔍 搜索 {len(problems)} 个问题空间的最新论文...")
        print("=" * 60)

        for problem, keywords in problems.items():
            print(f"\n📚 问题: {problem}")

            # 构建 arXiv 查询
            keyword_query = ' OR '.join([f'"{kw}"' for kw in keywords[:3]])
            query = f'abs:({keyword_query}) AND (abs:(LLM) OR abs:(language model) OR abs:(neural network) OR abs:(transformer) OR abs:(inference))'

            try:
                papers = self.arxiv.search(
                    query=query,
                    max_results=limit_per_problem * 2,  # 多取一些，过滤重复
                    sort_by='submittedDate',
                    sort_order='descending'
                )

                print(f"   arXiv 返回: {len(papers)} 篇")

                # Enrich + 打分
                for paper in papers[:limit_per_problem]:
                    if paper.arxiv_id in seen_ids:
                        continue

                    # Semantic Scholar enrichment
                    paper = self.enrich_with_semantic_scholar(paper)

                    # 计算相关性
                    score, matched_probs, matched_techs = self.calculate_relevance(paper, problems)

                    if score >= 10.0:  # 最低阈值
                        seen_ids.add(paper.arxiv_id)

                        # 解析年份
                        try:
                            year = int(paper.published[:4])
                        except:
                            year = datetime.now().year

                        tracked = TrackedPaper(
                            paper_id=paper.arxiv_id,
                            citekey=self.generate_citekey(paper.title, year),
                            title=paper.title,
                            authors=paper.authors[:5],
                            year=year,
                            venue=f"arXiv:{paper.categories[0] if paper.categories else 'cs.AI'}",
                            doi=paper.doi,
                            url=f"https://arxiv.org/abs/{paper.arxiv_id}",
                            pdf_url=paper.pdf_url or f"https://arxiv.org/pdf/{paper.arxiv_id}.pdf",
                            abstract=paper.abstract[:1000] if paper.abstract else "",
                            citation_count=paper.citation_count,
                            relevance_score=score,
                            matched_problems=matched_probs,
                            matched_techs=matched_techs,
                            tracked_at=datetime.now().isoformat(),
                            source='arxiv'
                        )
                        all_papers.append(tracked)
                        print(f"   ✅ {paper.title[:50]}... (score={score:.1f})")

                time.sleep(self.arxiv.delay)

            except Exception as e:
                print(f"   ❌ 搜索失败: {e}")
                continue

        # 按相关性排序
        all_papers.sort(key=lambda x: x.relevance_score, reverse=True)

        print(f"\n📊 共发现 {len(all_papers)} 篇高相关论文")
        self.tracked_count = len(all_papers)

        return all_papers

    def save_to_corpus(self, paper: TrackedPaper, dry_run: bool = False) -> Optional[Path]:
        """保存论文到 _corpus 目录"""
        CORPUS_DIR.mkdir(parents=True, exist_ok=True)

        filename = f"{paper.citekey}.md"
        filepath = CORPUS_DIR / filename

        if filepath.exists():
            return None  # 已存在

        content = self._format_corpus_entry(paper)

        if not dry_run:
            filepath.write_text(content, encoding='utf-8')
            if logger:
                logger.info(f"Saved: {filepath}")

        return filepath

    def save_paper_card(self, paper: TrackedPaper, dry_run: bool = False) -> Optional[Path]:
        """保存论文卡片到 Daily 目录"""
        PAPER_CARDS_DIR.mkdir(parents=True, exist_ok=True)

        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"{date_str}_{paper.citekey}.md"
        filepath = PAPER_CARDS_DIR / filename

        if filepath.exists():
            return None

        # 生成 AI 摘要
        summary = self._generate_paper_summary(paper)

        content = self._format_paper_card(paper, summary)

        if not dry_run:
            filepath.write_text(content, encoding='utf-8')
            if logger:
                logger.info(f"Saved card: {filepath}")

        return filepath

    def _generate_paper_summary(self, paper: TrackedPaper) -> Dict[str, str]:
        """用 LLM 生成论文摘要"""
        if not self.client:
            return {
                'one_sentence': paper.abstract[:100] + "..." if paper.abstract else "无摘要",
                'contributions': ["需阅读原文获取"],
                'why_important': "相关性评分: " + str(paper.relevance_score)
            }

        prompt = f"""论文标题: {paper.title}

论文摘要: {paper.abstract[:800] if paper.abstract else '无'}

请生成:
1. 一句话总结 (不超过50字)
2. 三个核心贡献 (列表)
3. 为什么重要 (不超过100字)

JSON格式:
{{
    "one_sentence": "...",
    "contributions": ["...", "...", "..."],
    "why_important": "..."
}}"""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat(messages, temperature=0.3, max_tokens=500)
            data = json.loads(response)
            return data
        except Exception as e:
            if logger:
                logger.warning(f"LLM summary failed: {e}")
            return {
                'one_sentence': paper.abstract[:100] + "..." if paper.abstract else "无摘要",
                'contributions': ["需阅读原文获取"],
                'why_important': f"相关性评分: {paper.relevance_score:.1f}"
            }

    def _format_corpus_entry(self, paper: TrackedPaper) -> str:
        """格式化 corpus 条目"""
        authors_str = '; '.join(paper.authors) if paper.authors else 'Unknown'

        content = f"""---
type: literature-corpus-entry
citekey: {paper.citekey}
title: "{paper.title}"
authors: {authors_str}
year: {paper.year}
venue: {paper.venue}
doi: {paper.doi}
url: {paper.url}
pdf_url: {paper.pdf_url}
abstract: |
{paper.abstract[:2000] if paper.abstract else '无摘要'}
citation_count: {paper.citation_count}
relevance_score: {paper.relevance_score}
matched_problems: [{', '.join(paper.matched_problems)}]
matched_techs: [{', '.join(paper.matched_techs)}]
pre_screened_status: Included
contamination_signals:
  preprint_post_llm_inflection: false
  semantic_scholar_unmatched: null
  openalex_unmatched: null
  crossref_unmatched: null
source: {paper.source}
tracked_at: {paper.tracked_at}
created: {datetime.now().strftime('%Y-%m-%d')}
---

# {paper.title}

**{paper.venue} | {paper.year}** | Citations: {paper.citation_count}

## 作者
{authors_str}

## 摘要
{paper.abstract[:1000] if paper.abstract else '无摘要'}...

## 匹配问题
{', '.join([f'`{p}`' for p in paper.matched_problems])}

## 匹配技术
{', '.join([f'`{t}`' for t in paper.matched_techs])}

## 链接
- [arXiv]({paper.url}) | [PDF]({paper.pdf_url})

---

*由 Academic Tracker 自动追踪 | {datetime.now().strftime('%Y-%m-%d')}*
"""

        return content

    def _format_paper_card(self, paper: TrackedPaper, summary: Dict) -> str:
        """格式化论文卡片"""
        authors_str = ', '.join(paper.authors[:3]) if paper.authors else 'Unknown'
        contributions = '\n'.join([f"{i+1}. {c}" for i, c in enumerate(summary.get('contributions', []))])

        content = f"""---
title: "{paper.title}"
venue: {paper.venue}
year: {paper.year}
authors: "{authors_str}"
citations: {paper.citation_count}
relevance_score: {paper.relevance_score}
tags: [{', '.join(paper.matched_problems)}, {', '.join(paper.matched_techs)}]
date: {datetime.now().strftime('%Y-%m-%d')}
type: paper-card
citekey: {paper.citekey}
---

# {paper.title}

**{paper.venue} {paper.year}** | Citations: {paper.citation_count} | ⭐ {paper.relevance_score:.1f}

**作者:** {authors_str}{' et al.' if len(paper.authors) > 3 else ''}

## 一句话总结
{summary.get('one_sentence', paper.abstract[:80] + '...')}

## 核心贡献
{contributions}

## 为什么重要
{summary.get('why_important', '需进一步评估')}

## 匹配标签
- **问题:** {', '.join(paper.matched_problems)}
- **技术:** {', '.join(paper.matched_techs)}

## 链接
- [Paper]({paper.url}) | [PDF]({paper.pdf_url})

---

*由 Academic Tracker 自动生成 | {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""

        return content

    def run_daily_tracking(
        self,
        problems: Dict[str, List[str]] = None,
        min_score: float = 15.0,
        save_corpus: bool = True,
        save_cards: bool = True,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """
        运行每日追踪

        Args:
            problems: 问题空间
            min_score: 最低相关性分数
            save_corpus: 保存到 _corpus
            save_cards: 保存 Paper Card 到 Daily
            dry_run: 只打印不保存

        Returns:
            追踪结果统计
        """
        print("\n" + "=" * 70)
        print("📚 Academic Tracker - 每日学术论文追踪")
        print("=" * 70)
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"最低相关性分数: {min_score}")
        print(f"模式: {'DRY-RUN' if dry_run else 'LIVE'}")
        print("=" * 70)

        # Step 1: 搜索问题空间
        papers = self.search_problem_spaces(problems, limit_per_problem=15)

        if not papers:
            print("\n⚠️  未发现高相关论文")
            return {'found': 0, 'corpus': 0, 'cards': 0}

        # Step 2: 过滤
        filtered = [p for p in papers if p.relevance_score >= min_score]
        print(f"\n🎯 过滤后 ({min_score}分以上): {len(filtered)} 篇")

        # Step 3: 保存
        corpus_count = 0
        card_count = 0

        for paper in filtered:
            if save_corpus:
                path = self.save_to_corpus(paper, dry_run)
                if path:
                    corpus_count += 1

            if save_cards:
                path = self.save_paper_card(paper, dry_run)
                if path:
                    card_count += 1

        # 统计
        print("\n" + "=" * 70)
        print("📊 追踪结果")
        print("=" * 70)
        print(f"发现论文: {len(papers)} 篇")
        print(f"高相关 (≥{min_score}): {len(filtered)} 篇")
        print(f"保存到 _corpus: {corpus_count} 篇")
        print(f"生成 Paper Card: {card_count} 篇")
        print("=" * 70)

        return {
            'found': len(papers),
            'filtered': len(filtered),
            'corpus': corpus_count,
            'cards': card_count,
            'papers': [asdict(p) for p in filtered]
        }


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Academic Paper Tracker')
    parser.add_argument('--problems', '-p', help='问题空间 (逗号分隔)')
    parser.add_argument('--limit', '-l', type=int, default=15, help='每个问题搜索论文数')
    parser.add_argument('--min-score', '-s', type=float, default=15.0, help='最低相关性分数')
    parser.add_argument('--dry-run', '-n', action='store_true', help='只打印不保存')
    parser.add_argument('--run-daily', '-d', action='store_true', help='每日追踪模式')
    parser.add_argument('--no-corpus', action='store_true', help='不保存到 _corpus')
    parser.add_argument('--no-cards', action='store_true', help='不生成 Paper Card')

    args = parser.parse_args()

    tracker = AcademicTracker()

    # 解析问题空间
    problems = None
    if args.problems:
        problem_list = [p.strip() for p in args.problems.split(',')]
        problems = {p: [] for p in problem_list}

    # 运行追踪
    result = tracker.run_daily_tracking(
        problems=problems,
        min_score=args.min_score,
        save_corpus=not args.no_corpus,
        save_cards=not args.no_cards,
        dry_run=args.dry_run
    )

    return result


if __name__ == "__main__":
    main()