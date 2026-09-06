"""
Article Scraper - 内容抓取层
参考 paperlists 的多源抓取设计
支持 arXiv API、GitHub Releases、RSS 等多源抓取
"""
import os
import re
import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

import requests
import feedparser
from bs4 import BeautifulSoup

from core.models import Signal
from core.logger import get_logger

logger = get_logger("ArticleScraper")

@dataclass
class ArticleMetadata:
    """文章元数据"""
    title: str
    url: str
    authors: List[str] = field(default_factory=list)
    published: str = ""
    abstract: str = ""
    categories: List[str] = field(default_factory=list)
    citation_count: int = 0
    influence_score: float = 0.0
    pdf_url: str = ""
    venue: str = ""
    keywords: List[str] = field(default_factory=list)

class ArticleScraper:
    """
    文章抓取器
    统一处理多源内容抓取
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.max_retries = 3
        self.request_delay = 1.5

    def _get(self, url: str, timeout: int = 30) -> Optional[str]:
        """带重试的HTTP GET"""
        for retry in range(self.max_retries):
            try:
                resp = self.session.get(url, timeout=timeout)
                resp.raise_for_status()
                # ── FIX: Force UTF-8 decoding before accessing .text ──
                resp.encoding = 'utf-8'
                time.sleep(self.request_delay)
                return resp.text
            except Exception as e:
                logger.warning(f"Request failed ({retry+1}/{self.max_retries}): {url} - {e}")
                if retry < self.max_retries - 1:
                    time.sleep(2 ** retry)
        return None

    def scrape_arxiv_article(self, article_id: str) -> Optional[ArticleMetadata]:
        """
        抓取arXiv论文详情
        article_id: arXiv ID (如 "2401.12345")
        """
        url = f"http://export.arxiv.org/api/query?id_list={article_id}"
        content = self._get(url)
        if not content:
            return None

        try:
            feed = feedparser.parse(content)
            entry = feed.entries[0] if feed.entries else None
            if not entry:
                return None

            categories = [tag.term for tag in entry.get('tags', [])]

            metadata = ArticleMetadata(
                title=entry.title.strip(),
                url=entry.id,
                authors=[a.name for a in entry.get('authors', [])],
                published=entry.get('published', ''),
                abstract=entry.get('summary', '')[:1000],
                categories=categories,
                pdf_url=entry.get('pdf', ''),
                keywords=[t.term for t in entry.get('tags', [])[:5]]
            )
            return metadata

        except Exception as e:
            logger.error(f"Failed to parse arXiv article {article_id}: {e}")
            return None

    def scrape_huggingface_paper(self, paper_id: str) -> Optional[ArticleMetadata]:
        """
        抓取HuggingFace Paper详情
        """
        url = f"https://huggingface.co/api/papers/{paper_id}"
        content = self._get(url)
        if not content:
            return None

        try:
            data = json.loads(content)
            metadata = ArticleMetadata(
                title=data.get('title', ''),
                url=data.get('url', ''),
                authors=data.get('authors', []),
                published=data.get('published', ''),
                abstract=data.get('summary', ''),
                categories=data.get('tags', []),
                citation_count=data.get('citation_count', 0),
                keywords=data.get('topics', [])
            )
            return metadata

        except Exception as e:
            logger.error(f"Failed to parse HF paper {paper_id}: {e}")
            return None

    def scrape_github_release(self, repo: str, limit: int = 10) -> List[Dict]:
        """
        抓取GitHub Release
        """
        url = f"https://api.github.com/repos/{repo}/releases?per_page={limit}"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        resp = self.session.get(url, headers=headers, timeout=30)
        resp.encoding = 'utf-8'

        if resp.status_code != 200:
            logger.warning(f"GitHub API failed for {repo}: {resp.status_code}")
            return []

        try:
            resp.encoding = 'utf-8'
            releases = json.loads(resp.text)
            results = []
            for rel in releases:
                results.append({
                    'tag_name': rel.get('tag_name', ''),
                    'name': rel.get('name', ''),
                    'body': rel.get('body', '')[:500],
                    'published_at': rel.get('published_at', ''),
                    'html_url': rel.get('html_url', ''),
                    'assets': len(rel.get('assets', []))
                })
            return results

        except Exception as e:
            logger.error(f"Failed to parse GitHub releases for {repo}: {e}")
            return []

    def scrape_github_commits(self, repo: str, days: int = 7) -> List[Dict]:
        """
        抓取GitHub最近提交
        """
        since = (datetime.now() - timedelta(days=days)).isoformat()
        url = f"https://api.github.com/repos/{repo}/commits?since={since}"
        headers = {'Accept': 'application/vnd.github.v3+json'}

        resp = self.session.get(url, headers=headers, timeout=30)
        resp.encoding = 'utf-8'
        if resp.status_code != 200:
            return []

        try:
            commits = json.loads(resp.text)
            results = []
            for commit in commits[:20]:
                results.append({
                    'sha': commit.get('sha', '')[:7],
                    'message': commit.get('commit', {}).get('message', '').split('\n')[0],
                    'author': commit.get('commit', {}).get('author', {}).get('name', ''),
                    'date': commit.get('commit', {}).get('author', {}).get('date', '')
                })
            return results

        except Exception as e:
            logger.error(f"Failed to parse GitHub commits for {repo}: {e}")
            return []

    def extract_keywords_from_text(self, text: str, max_keywords: int = 10) -> List[str]:
        """
        从文本中提取关键词
        用于在没有元数据时分析内容
        """
        text_lower = text.lower()

        ai_keywords = [
            'transformer', 'llm', 'gpt', 'bert', 'attention', 'neural',
            'reinforcement', 'multimodal', 'diffusion', 'generative',
            'agent', 'reasoning', 'chain-of-thought', 'rag', 'fine-tuning',
            'inference', 'optimization', 'quantization', 'distillation',
            'speculative', 'batch', 'serving', 'deployment', 'runtime'
        ]

        found = []
        for kw in ai_keywords:
            if kw in text_lower:
                found.append(kw)

        return found[:max_keywords]

    def build_paper_summary(self, metadata: ArticleMetadata) -> str:
        """
        构建论文摘要（用于报告）
        """
        summary = f"**{metadata.title}**\n\n"

        if metadata.authors:
            summary += f"作者: {', '.join(metadata.authors[:3])}"
            if len(metadata.authors) > 3:
                summary += f" 等{len(metadata.authors)}人"
            summary += "\n\n"

        if metadata.venue:
            summary += f"会议/期刊: {metadata.venue}\n\n"

        if metadata.categories:
            summary += f"分类: {' > '.join(metadata.categories[:3])}\n\n"

        if metadata.abstract:
            summary += f"摘要: {metadata.abstract[:300]}...\n\n"

        if metadata.citation_count > 0:
            summary += f"引用数: {metadata.citation_count}\n"

        if metadata.keywords:
            summary += f"关键词: {', '.join(metadata.keywords[:5])}\n"

        return summary

class SourceManager:
    """
    信源管理器
    参考 paperlists 的多源配置设计
    """

    def __init__(self, config_path: str = None):
        self.config_path = config_path
        self.sources = self._load_sources()

    def _load_sources(self) -> Dict[str, List[Dict]]:
        """加载信源配置"""
        default_sources = {
            'arxiv': [
                {'id': 'arxiv_cs_AI', 'name': 'arXiv cs.AI', 'url': 'http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=20', 'category': 'research'},
                {'id': 'arxiv_cs_LG', 'name': 'arXiv cs.LG', 'url': 'http://export.arxiv.org/api/query?search_query=cat:cs.LG&max_results=20', 'category': 'research'},
                {'id': 'arxiv_cs_CL', 'name': 'arXiv cs.CL', 'url': 'http://export.arxiv.org/api/query?search_query=cat:cs.CL&max_results=20', 'category': 'research'},
            ],
            'github': [
                {'id': 'vllm_releases', 'name': 'vLLM', 'repo': 'vllm-project/vllm', 'type': 'releases'},
                {'id': 'sglang_releases', 'name': 'SGLang', 'repo': 'sgl-project/sglang', 'type': 'releases'},
                {'id': 'deepseek_releases', 'name': 'DeepSeek', 'repo': 'deepseek-ai/DeepSeek-V3', 'type': 'releases'},
            ],
            'huggingface': [
                {'id': 'hf_daily', 'name': 'HuggingFace Daily', 'url': 'https://huggingface.co/api/papers?sort=trending&limit=20', 'type': 'api'},
            ],
            'rss': [
                {'id': 'liangzibit', 'name': '量子位', 'url': 'https://www.qbitai.com/rss', 'type': 'rss'},
                {'id': 'pytorch_blog', 'name': 'PyTorch Blog', 'url': 'https://pytorch.org/blog/feed.xml', 'type': 'rss'},
            ]
        }

        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    return loaded.get('sources', default_sources)
            except Exception as e:
                logger.error(f"Failed to load sources config: {e}")

        return default_sources

    def get_sources(self, source_type: str = None) -> List[Dict]:
        """获取信源列表"""
        if source_type:
            return self.sources.get(source_type, [])
        all_sources = []
        for sources in self.sources.values():
            all_sources.extend(sources)
        return all_sources

    def get_source_by_id(self, source_id: str) -> Optional[Dict]:
        """根据ID获取信源"""
        for sources in self.sources.values():
            for source in sources:
                if source.get('id') == source_id:
                    return source
        return None