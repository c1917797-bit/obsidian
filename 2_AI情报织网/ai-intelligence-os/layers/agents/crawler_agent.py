"""
Crawler Agent - 数据采集层
从RSS、GitHub、arXiv等渠道采集原始信号

支持两种模式：
1. Legacy模式 (crawl_all): 全量采集 + LLM总结
2. Metadata First模式 (crawl_all_metadata_first): 元数据优先 + 规则评分 + Top N抓全文
"""
import os
import json
import re
import time
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
from dataclasses import asdict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import feedparser
from bs4 import BeautifulSoup

from core.models import Signal
from core.storage import UnifiedStore
from core.logger import get_logger
from layers.agents.scoring_engine import ScoringEngine, ScoredSignal

logger = get_logger("CrawlerAgent")

class SourceManager:
    """信源管理器"""

    DEFAULT_SOURCES = [
        {"id": "hf_daily_papers", "name": "HuggingFace Daily Papers", "url": "https://huggingface.co/api/papers?sort=trending&limit=20", "type": "hf_api", "category": "tech_papers", "priority": "P0", "language": "en"},
        {"id": "arxiv_cs_LG", "name": "arXiv cs.LG", "url": "http://export.arxiv.org/api/query?search_query=cat:cs.LG&max_results=20&sortBy=submittedDate&sortOrder=descending", "type": "atom", "category": "tech_papers", "priority": "P0", "language": "en"},
        {"id": "arxiv_cs_CL", "name": "arXiv cs.CL", "url": "http://export.arxiv.org/api/query?search_query=cat:cs.CL&max_results=20&sortBy=submittedDate&sortOrder=descending", "type": "atom", "category": "tech_papers", "priority": "P0", "language": "en"},
        {"id": "arxiv_cs_AI", "name": "arXiv cs.AI", "url": "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=20&sortBy=submittedDate&sortOrder=descending", "type": "atom", "category": "tech_papers", "priority": "P0", "language": "en"},
        {"id": "arxiv_cs_DC", "name": "arXiv cs.DC", "url": "http://export.arxiv.org/api/query?search_query=cat:cs.DC&max_results=20&sortBy=submittedDate&sortOrder=descending", "type": "atom", "category": "tech_papers", "priority": "P1", "language": "en"},
        {"id": "arxiv_cs_MA", "name": "arXiv cs.MA", "url": "http://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending", "type": "atom", "category": "tech_papers", "priority": "P1", "language": "en"},
        {"id": "vllm_releases", "name": "vLLM Releases", "url": "https://github.com/vllm-project/vllm/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en"},
        {"id": "sglang_releases", "name": "SGLang Releases", "url": "https://github.com/sgl-project/sglang/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en"},
        {"id": "deepseek_releases", "name": "DeepSeek Releases", "url": "https://github.com/deepseek-ai/DeepSeek-V3/releases.atom", "type": "atom", "category": "industry", "priority": "P0", "language": "en"},
        {"id": "qwen_releases", "name": "Qwen Releases", "url": "https://github.com/QwenLM/Qwen1.5/releases.atom", "type": "atom", "category": "industry", "priority": "P0", "language": "en"},
        {"id": "pytorch_blog", "name": "PyTorch Blog", "url": "https://pytorch.org/blog/feed.xml", "type": "rss", "category": "tech_blog", "priority": "P0", "language": "en"},
        {"id": "deepmind_blog", "name": "Google DeepMind Blog", "url": "https://deepmind.google/blog/rss.xml", "type": "rss", "category": "tech_blog", "priority": "P0", "language": "en"},
        {"id": "openai_blog", "name": "OpenAI Blog", "url": "https://openai.com/blog/rss.xml", "type": "rss", "category": "tech_blog", "priority": "P0", "language": "en"},
        {"id": "lmsys_releases", "name": "LMSYS Releases", "url": "https://github.com/lm-sys/FastChat/releases.atom", "type": "atom", "category": "benchmark", "priority": "P0", "language": "en"},
        {"id": "swe_bench", "name": "SWE-Bench Releases", "url": "https://github.com/princeton-nlp/SWE-bench/releases.atom", "type": "atom", "category": "benchmark", "priority": "P0", "language": "en"},
        {"id": "autogen_releases", "name": "AutoGen Releases", "url": "https://github.com/microsoft/autogen/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en"},
        {"id": "dspy_releases", "name": "DSPy Releases", "url": "https://github.com/stanfordnlp/dspy/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en"},
        {"id": "langchain_releases", "name": "LangChain Releases", "url": "https://github.com/langchain-ai/langchain/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en"},
        {"id": "llamaindex_releases", "name": "LlamaIndex Releases", "url": "https://github.com/run-llama/llama_index/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en"},
        {"id": "deepspeed_releases", "name": "DeepSpeed Releases", "url": "https://github.com/microsoft/DeepSpeed/releases.atom", "type": "atom", "category": "training", "priority": "P0", "language": "en"},
        {"id": "flashattention_releases", "name": "FlashAttention Releases", "url": "https://github.com/FlashAttention/FlashAttention/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en"},
        {"id": "tensorrt_llm_releases", "name": "TensorRT-LLM Releases", "url": "https://github.com/NVIDIA/TensorRT-LLM/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en"},
        {"id": "llama_cpp_releases", "name": "llama.cpp Releases", "url": "https://github.com/ggerganov/llama.cpp/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en"},
        {"id": "liangzibit", "name": "量子位", "url": "https://www.qbitai.com/rss", "type": "rss", "category": "news_cn", "priority": "P0", "language": "zh"},
        {"id": "techcrunch_ai", "name": "TechCrunch AI", "url": "https://techcrunch.com/category/artificial-intelligence/feed/", "type": "rss", "category": "news", "priority": "P1", "language": "en"},
        # Twitter Sources (via RSSHub - Nitter is defunct)
        {"id": "twitter_OpenAI", "name": "X/OpenAI", "url": "https://rsshub.app/twitter/user/OpenAI", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_AnthropicAI", "name": "X/Anthropic", "url": "https://rsshub.app/twitter/user/AnthropicAI", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_GoogleAI", "name": "X/Google AI", "url": "https://rsshub.app/twitter/user/GoogleAI", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_GoogleDeepMind", "name": "X/Google DeepMind", "url": "https://rsshub.app/twitter/user/GoogleDeepMind", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_HuggingFace", "name": "X/HuggingFace", "url": "https://rsshub.app/twitter/user/huggingface", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_xai", "name": "X/xAI", "url": "https://rsshub.app/twitter/user/xai", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_MistralAI", "name": "X/Mistral AI", "url": "https://rsshub.app/twitter/user/MistralAI", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_NVIDIA", "name": "X/NVIDIA", "url": "https://rsshub.app/twitter/user/NVIDIA", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_ylecun", "name": "X/Yann LeCun", "url": "https://rsshub.app/twitter/user/ylecun", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_AndrewYNg", "name": "X/Andrew Ng", "url": "https://rsshub.app/twitter/user/AndrewYNg", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_jimfan", "name": "X/Jim Fan", "url": "https://rsshub.app/twitter/user/jimfan", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_swyx", "name": "X/Swyx", "url": "https://rsshub.app/twitter/user/swyx", "type": "rss", "category": "social", "priority": "P1", "language": "en"},
        {"id": "twitter_ak_akhaliq", "name": "X/AK (AI News)", "url": "https://rsshub.app/twitter/user/_akhaliq", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_emollick", "name": "X/Ethan Mollick", "url": "https://rsshub.app/twitter/user/emollick", "type": "rss", "category": "social", "priority": "P1", "language": "en"},
        {"id": "twitter_DeepSeekAI", "name": "X/DeepSeek", "url": "https://rsshub.app/twitter/user/deepseek_ai", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
        {"id": "twitter_QwenAI", "name": "X/Qwen", "url": "https://rsshub.app/twitter/user/Qwen_AI", "type": "rss", "category": "social", "priority": "P0", "language": "en"},
    ]

    def __init__(self, sources_file: str = None, store: UnifiedStore = None):
        self.store = store
        self.sources_file = sources_file
        self.sources = self._load_sources()

    def _load_sources(self) -> List[Dict]:
        """从配置文件或数据库加载信源"""
        if self.sources_file and os.path.exists(self.sources_file):
            try:
                with open(self.sources_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_feeds = data.get('rss_feeds', self.DEFAULT_SOURCES)
                    # 只返回 enabled=True 的信源
                    enabled_feeds = [s for s in all_feeds if s.get('enabled', True)]
                    return enabled_feeds
            except Exception as e:
                logger.warning(f"Failed to load sources from file: {e}")

        if self.store:
            db_sources = self.store.get_enabled_sources()
            if db_sources:
                return db_sources

        return self.DEFAULT_SOURCES

    def get_by_priority(self, priority: str) -> List[Dict]:
        return [s for s in self.sources if s.get('priority') == priority]


    def get_by_category(self, category: str) -> List[Dict]:
        return [s for s in self.sources if s.get('category') == category]

    def filter_by_categories(self, categories: List[str]) -> List[Dict]:
        """只返回指定分类的信源（用于过滤掉news等非技术类信源）"""
        if not categories:
            return self.sources
        return [s for s in self.sources if s.get('category') in categories]

class CrawlerAgent:
    """
    采集Agent
    负责任务：
    1. 从配置的源采集原始信号
    2. 解析RSS/Atom/API响应
    3. 转换为Signal对象
    4. 存储到UnifiedStore
    """

    def __init__(self, store: UnifiedStore = None, sources_file: str = None,
                 max_workers: int = 8, request_delay: float = 0.5):
        self.store = store or UnifiedStore()
        self.source_manager = SourceManager(sources_file, self.store)
        self.max_retries = 3
        self.request_delay = request_delay
        self.max_workers = max_workers
        self.stats = {'crawled': 0, 'new': 0, 'failed': 0}
        self.scoring_engine = ScoringEngine()

    def _make_session(self) -> requests.Session:
        """创建新的 HTTP Session（每个线程独立）"""
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        return session

    def _generate_id(self, text: str) -> str:
        """生成信号唯一ID"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()[:16]

    def _clean_html(self, html: str) -> str:
        """清理HTML标签"""
        if not html:
            return ''
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text(separator=' ', strip=True)

    def _get(self, url: str, timeout: int = 30) -> Optional[str]:
        """带重试的HTTP GET（每次调用创建独立session，线程安全）"""
        for retry in range(self.max_retries):
            try:
                session = self._make_session()
                resp = session.get(url, timeout=timeout)
                resp.raise_for_status()
                # ── FIX: Force UTF-8 decoding before accessing .text ──
                # requests defaults to ISO-8859-1/Windows-1252 when the server sends no
                # explicit charset, corrupting Chinese/emoji content from WeChat, RSS, etc.
                resp.encoding = 'utf-8'
                time.sleep(self.request_delay)
                return resp.text
            except Exception as e:
                logger.warning(f"Request failed ({retry+1}/{self.max_retries}): {url} - {e}")
                if retry < self.max_retries - 1:
                    time.sleep(2 ** retry)
        return None

    def _parse_time(self, time_str: str) -> str:
        """解析时间字符串"""
        if not time_str:
            return datetime.now().isoformat()
        try:
            dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            return dt.isoformat()
        except:
            return datetime.now().isoformat()

    def collect_rss(self, source: Dict) -> List[Signal]:
        """采集RSS/Atom源"""
        url = source['url']
        content = self._get(url)
        if not content:
            return []

        signals = []
        feed = feedparser.parse(content)

        for entry in feed.entries[:30]:
            try:
                signal_id = self._generate_id(entry.get('id', entry.get('link', '')))

                published = ''
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6]).isoformat()
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    published = datetime(*entry.updated_parsed[:6]).isoformat()

                summary = ''
                if hasattr(entry, 'summary'):
                    summary = self._clean_html(entry.summary)
                elif hasattr(entry, 'description'):
                    summary = self._clean_html(entry.description)

                authors = []
                if hasattr(entry, 'authors'):
                    authors = [a.get('name', '') for a in entry.authors]

                tags = []
                if hasattr(entry, 'tags'):
                    tags = [t.get('term', '') for t in entry.tags]

                signal = Signal(
                    id=signal_id,
                    title=entry.get('title', '无标题').strip(),
                    url=entry.get('link', ''),
                    source=source.get('name', source['id']),
                    source_id=source['id'],
                    source_type=source.get('type', 'rss'),
                    category=source.get('category', ''),
                    priority=source.get('priority', 'P1'),
                    published=published,
                    summary=summary[:1000],
                    authors=authors,
                    tags=tags,
                    language=source.get('language', 'en')
                )
                signals.append(signal)
            except Exception as e:
                logger.error(f"Failed to parse RSS entry: {e}")
                continue

        return signals

    def collect_huggingface(self, source: Dict) -> List[Signal]:
        """采集HuggingFace Daily Papers API"""
        url = source['url']
        content = self._get(url)
        if not content:
            return []

        signals = []
        try:
            data = json.loads(content)
            papers = data.get('papers', []) if isinstance(data, dict) else data

            for item in papers[:20]:
                try:
                    paper_id = item.get('id', '')
                    title = item.get('title', 'No Title')
                    paper_url = item.get('url', f'https://huggingface.co/papers/{paper_id}')
                    summary = item.get('summary', item.get('description', ''))
                    published = item.get('published', datetime.now().isoformat())

                    signal_id = self._generate_id(paper_id or title)

                    signal = Signal(
                        id=signal_id,
                        title=title.strip(),
                        url=paper_url,
                        source='HuggingFace Papers',
                        source_id=source['id'],
                        source_type='hf_api',
                        category=source.get('category', 'tech_papers'),
                        priority=source.get('priority', 'P0'),
                        published=published if isinstance(published, str) else datetime.now().isoformat(),
                        summary=summary[:1000] if summary else '',
                        tags=[t.get('name', '') for t in item.get('tags', [])[:5]] if isinstance(item.get('tags'), list) else [],
                        language='en'
                    )
                    signals.append(signal)
                except Exception as e:
                    logger.error(f"Failed to parse HF paper: {e}")
                    continue
        except Exception as e:
            logger.error(f"HF API parse error: {e}")

        return signals

    def collect_github(self, repo: str) -> List[Signal]:
        """采集GitHub仓库动态"""
        signals = []
        try:
            api_url = f"https://api.github.com/repos/{repo}/events"
            resp = self.session.get(api_url, timeout=30)
            resp.encoding = 'utf-8'
            if resp.status_code == 200:
                events = json.loads(resp.text)
                for event in events[:10]:
                    signal_id = self._generate_id(f"{repo}_{event.get('type', '')}_{event.get('created_at', '')}")
                    signal = Signal(
                        id=signal_id,
                        title=f"{repo}: {event.get('type', '')}",
                        url=event.get('payload', {}).get('html_url', f"https://github.com/{repo}"),
                        source=repo,
                        source_id=f"github_{repo}",
                        source_type='github',
                        category='inference',
                        priority='P0',
                        published=event.get('created_at', ''),
                        summary=event.get('payload', {}).get('description', '')[:500]
                    )
                    signals.append(signal)
        except Exception as e:
            logger.error(f"GitHub采集失败 {repo}: {e}")
        return signals

    def collect_arxiv(self, query: str = "LLM", max_results: int = 10) -> List[Signal]:
        """采集arXiv论文（关键词搜索）"""
        signals = []
        try:
            url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
            content = self._get(url)
            if not content:
                return signals

            entries = re.findall(r'<entry>(.*?)</entry>', content, re.DOTALL)
            for entry in entries:
                try:
                    title_match = re.search(r'<title>(.*?)</title>', entry)
                    link_match = re.search(r'<id>(.*?)</id>', entry)
                    published_match = re.search(r'<published>(.*?)</published>', entry)
                    summary_match = re.search(r'<summary>(.*?)</summary>', entry)
                    author_matches = re.findall(r'<name>(.*?)</name>', entry)

                    if title_match:
                        signal_id = self._generate_id(title_match.group(1))
                        signal = Signal(
                            id=signal_id,
                            title=title_match.group(1).strip().replace('\n', ' '),
                            url=link_match.group(1) if link_match else '',
                            source='arXiv',
                            source_id='arxiv',
                            source_type='arxiv',
                            category='tech_papers',
                            priority='P0',
                            published=published_match.group(1) if published_match else '',
                            summary=summary_match.group(1)[:1000] if summary_match else '',
                            authors=author_matches[:5] if author_matches else [],
                            tags=['arxiv', query[:50]],
                            language='en'
                        )
                        signals.append(signal)
                except Exception as e:
                    continue
        except Exception as e:
            logger.error(f"arXiv采集失败: {e}")
        return signals

    def collect_arxiv_keyword(self, source: Dict) -> List[Signal]:
        """采集arXiv Scholar Alert关键词源

        source配置格式:
        {
            "id": "scholar_alert_03",
            "name": "KV Cache Compression",
            "type": "arxiv_keyword",
            "query": "KV cache compression offloading LLM long context",
            "max_results": 15,
            "priority": "P0",
            "category": "scholar_alert",
            "language": "en"
        }
        """
        query = source.get('query', source.get('name', ''))
        max_results = source.get('max_results', 15)
        signals = self.collect_arxiv(query=query, max_results=max_results)

        for sig in signals:
            sig.source = source.get('name', 'arXiv Scholar Alert')
            sig.source_id = source.get('id', 'arxiv_keyword')
            sig.source_type = 'arxiv_keyword'
            sig.category = source.get('category', 'scholar_alert')
            sig.priority = source.get('priority', 'P0')

        logger.info(f"arXiv keyword [{query[:40]}...]: {len(signals)} papers")
        return signals

    def collect_source(self, source: Dict) -> List[Signal]:
        """根据源类型调用对应采集方法"""
        feed_type = source.get('type', 'rss')

        if feed_type == 'hf_api' or feed_type == 'hf_api_filtered':
            signals = self.collect_huggingface(source)
            if feed_type == 'hf_api_filtered' and source.get('keywords'):
                kw_list = [k.lower() for k in source['keywords']]
                filtered = [sig for sig in signals if any(kw in (sig.title + ' ' + sig.summary).lower() for kw in kw_list)]
                logger.info(f"HF filtered: {len(signals)} -> {len(filtered)}")
                signals = filtered
            return signals
        elif feed_type == 'arxiv_keyword':
            return self.collect_arxiv_keyword(source)
        elif feed_type == 'paperlists_json':
            return self.collect_paperlists(source)
        elif feed_type == 'web':
            return self.collect_web(source)
        elif feed_type == 'twitter_rss':
            return self.collect_twitter_rss(source)
        elif feed_type == 'openreview':
            return self.collect_openreview(source)
        elif 'arxiv.org' in source.get('url', ''):
            return self.collect_rss(source)
        else:
            return self.collect_rss(source)

    def collect_openreview(self, source: Dict) -> List[Signal]:
        """采集 OpenReview 论文（under-review）"""
        signals = []
        try:
            url = source['url']
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; AI-Intelligence-OS/1.0)',
                'Accept': 'application/json'
            }
            resp = requests.get(url, timeout=30, headers=headers)
            if resp.status_code != 200:
                logger.warning(f"OpenReview API {resp.status_code}: {source.get('id')}")
                return signals

            data = json.loads(resp.text)
            notes = data.get('notes', [])
            logger.info(f"OpenReview: {len(notes)} notes from {source.get('name')}")

            for note in notes[:30]:
                try:
                    note_id = note.get('id', '')
                    title = note.get('title', 'No Title')
                    abstract = note.get('abstract', '')
                    authors = note.get('authors', [])
                    if isinstance(authors, list) and len(authors) > 0:
                        if isinstance(authors[0], dict):
                            authors = [a.get('name', '') for a in authors[:5]]
                        else:
                            authors = authors[:5]
                    else:
                        authors = []
                    metarev = note.get('metarevision', 0) or 0
                    reply_count = note.get('replyCount', 0) or 0
                    tc = note.get('tcconf', {}) or {}
                    venue = tc.get('venue', 'NeurIPS/ICML 2026')
                    cdate = tc.get('cdate', '')

                    signal_id = self._generate_id(note_id or title)
                    signal = Signal(
                        id=signal_id,
                        title=title.strip()[:200] if title else 'No Title',
                        url=f"https://openreview.net/forum?id={note_id}" if note_id else '',
                        source=source.get('name', 'OpenReview'),
                        source_id=source.get('id', 'openreview'),
                        source_type='openreview',
                        category='academic',
                        priority='P1',
                        published=cdate,
                        summary=abstract[:500] if abstract else '',
                        authors=authors,
                        tags=['openreview', 'under-review', f'metarev:{metarev}'],
                        language='en'
                    )
                    signals.append(signal)
                except Exception as e:
                    logger.error(f"Failed to parse OpenReview note: {e}")
                    continue

            logger.info(f"OpenReview: {len(signals)} papers from {source.get('name')}")
        except Exception as e:
            logger.error(f"OpenReview采集失败 {source.get('id')}: {e}")
        return signals

    def collect_twitter_rss(self, source: Dict) -> List[Signal]:
        """采集Twitter RSS (通过Nitter)"""
        signals = []
        try:
            content = self._get(source['url'], timeout=15)
            if not content:
                return signals

            entries = re.findall(r'<item>(.*?)</item>', content, re.DOTALL)
            for entry in entries[:10]:
                try:
                    title_match = re.search(r'<title>(.*?)</title>', entry)
                    link_match = re.search(r'<link>(.*?)</link>', entry)
                    pub_match = re.search(r'<pubDate>(.*?)</pubDate>', entry)
                    desc_match = re.search(r'<description>(.*?)</description>', entry)

                    if not title_match:
                        continue

                    title = title_match.group(1)
                    link = link_match.group(1) if link_match else ''

                    # 清理HTML实体
                    title = title.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')

                    # 提取作者和内容
                    author = ''
                    text = title
                    author_match = re.search(r'^(.+?)\s*@\w+\s*', title)
                    if author_match:
                        author = author_match.group(1).strip()

                    # 移除"用户 @handle: "前缀
                    text = re.sub(r'^.+?\s*@\w+\s*:\s*', '', title)

                    # 生成ID
                    tweet_id = link.split('/')[-1] if link else self._generate_id(title)

                    signal = Signal(
                        id=f'twitter_{tweet_id}',
                        title=text[:200],
                        url=link,
                        source=f"Twitter/{author}" if author else source.get('name', 'Twitter'),
                        source_id=source['id'],
                        source_type='twitter_rss',
                        category='social',
                        priority=source.get('priority', 'P0'),
                        published=pub_match.group(1) if pub_match else datetime.now().isoformat(),
                        summary=text[:500] if text else '',
                        language='en'
                    )
                    signals.append(signal)

                except Exception as e:
                    continue

        except Exception as e:
            logger.warning(f"Twitter RSS采集失败 {source.get('id')}: {e}")

        return signals

    def collect_paperlists(self, source: Dict) -> List[Signal]:
        """采集顶会论文JSON (paperlists)"""
        url = source['url']
        content = self._get(url)
        if not content:
            return []

        signals = []
        try:
            papers = json.loads(content)
            if not isinstance(papers, list):
                logger.warning(f"Unexpected paperlists format for {source.get('id')}")
                return []

            venue = source.get('id', '').replace('_', ' ').upper()
            for paper in papers[:50]:
                try:
                    paper_id = paper.get('id', paper.get('paper_id', ''))
                    if not paper_id:
                        continue

                    signal_id = self._generate_id(paper_id)

                    title = paper.get('title', 'No Title')
                    paper_url = paper.get('url', '')

                    authors = paper.get('authors', [])
                    if isinstance(authors, list) and len(authors) > 0:
                        if isinstance(authors[0], dict):
                            authors = [a.get('name', '') for a in authors[:5]]
                        else:
                            authors = authors[:5]
                    else:
                        authors = []

                    published = paper.get('published', paper.get('year', ''))
                    if published and isinstance(published, int):
                        published = f"{published}-01-01"

                    abstract = paper.get('abstract', '')
                    if len(abstract) > 500:
                        abstract = abstract[:500] + '...'

                    signal = Signal(
                        id=signal_id,
                        title=title.strip() if title else 'No Title',
                        url=paper_url,
                        source=f"{venue} Papers",
                        source_id=source.get('id', 'paperlists'),
                        source_type='paperlists_json',
                        category='academic',
                        priority='P0',
                        published=published,
                        summary=abstract,
                        authors=authors,
                        tags=paper.get('keywords', [])[:5],
                        language='en'
                    )
                    signals.append(signal)
                except Exception as e:
                    logger.error(f"Failed to parse paperlists entry: {e}")
                    continue

            logger.info(f"paperlists: {len(signals)} papers from {source.get('name', source.get('id'))}")

        except Exception as e:
            logger.error(f"paperlists parse error {source.get('id')}: {e}")

        return signals

    def collect_web(self, source: Dict) -> List[Signal]:
        """采集Web页面 - 提取链接+正文摘要"""
        url = source['url']
        content = self._get(url)
        if not content:
            return []

        signals = []
        soup = BeautifulSoup(content, 'html.parser')
        article_links = soup.find_all('a', href=True)
        seen_links = set()

        for link in article_links[:15]:
            href = link.get('href', '')
            if not href or href in seen_links:
                continue
            if href.startswith('#') or '/tag' in href or '/category' in href:
                continue

            from urllib.parse import urljoin
            full_url = href if href.startswith('http') else urljoin(url, href)
            seen_links.add(full_url)

            title = ''.join(s.strip() for s in link.contents if isinstance(s, str)).strip()
            if not title or len(title) < 10:
                continue

            signal_id = self._generate_id(full_url)
            signal = Signal(
                id=signal_id,
                title=title[:200],
                url=full_url,
                source=source.get('name', source['id']),
                source_id=source['id'],
                source_type='web',
                category=source.get('category', ''),
                priority=source.get('priority', 'P1'),
                published=datetime.now().isoformat(),
                language=source.get('language', 'en')
            )
            signals.append(signal)

        return signals

    def extract_article_text(self, url: str) -> str:
        """使用trafilatura提取网页正文（用于后续LLM总结）

        Args:
            url: 文章URL

        Returns:
            提取的正文文本（最多2000字符），失败返回空字符串
        """
        try:
            import trafilatura
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                text = trafilatura.extract(downloaded, max_length=2000, include_comments=False)
                return text or ''
        except ImportError:
            logger.warning("trafilatura not installed. Install with: pip install trafilatura")
        except Exception as e:
            logger.debug(f"trafilatura extraction failed for {url}: {e}")
        return ''

    def crawl_all(self, exclude_categories: List[str] = None, max_workers: int = None) -> List[Signal]:
        """从所有配置的源采集（并行）
        exclude_categories: 要排除的分类列表，如 ['news'] 过滤掉 TechCrunch 等商业新闻
        max_workers: 并行工作线程数（默认使用 self.max_workers）
        """
        all_signals = []
        sources = self.source_manager.sources

        # 过滤掉非技术类信源（news类）
        if exclude_categories:
            original_count = len(sources)
            sources = [s for s in sources if s.get('category') not in exclude_categories]
            logger.info(f"过滤信源: {original_count} -> {len(sources)} (排除 {exclude_categories})")

        logger.info(f"开始采集 {len(sources)} 个信源... (并行数: {max_workers or self.max_workers})")

        # 使用线程池并行采集
        workers = max_workers or self.max_workers
        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_source = {
                executor.submit(self._crawl_single_source, source): source
                for source in sources
            }

            for future in as_completed(future_to_source):
                source = future_to_source[future]
                source_id = source.get('id', 'unknown')
                try:
                    signals, error = future.result()
                    if error:
                        logger.error(f"  -> {source.get('name', source_id)} 失败: {error}")
                        self.stats['failed'] += 1
                        if self.store:
                            self.store.update_source_status(source_id, success=False, error=str(error))
                    else:
                        new_count = 0
                        for sig in signals:
                            if self.store.save_signal(sig):
                                new_count += 1
                        if self.store:
                            self.store.update_source_status(source_id, success=True)
                        all_signals.extend(signals)
                        self.stats['crawled'] += len(signals)
                        self.stats['new'] += new_count
                        logger.info(f"  -> {source.get('name', source_id)}: {len(signals)} 条 (新增 {new_count})")
                except Exception as e:
                    logger.error(f"  -> {source.get('name', source_id)} 异常: {e}")
                    self.stats['failed'] += 1

        logger.log_metric('crawled', self.stats['crawled'])
        logger.log_metric('new_signals', self.stats['new'])

        return all_signals

    def crawl_all_metadata_first(self, exclude_categories: List[str] = None,
                                   max_workers: int = None,
                                   top_n: int = 30,
                                   min_score: float = 5.0) -> Tuple[List[Signal], List[ScoredSignal]]:
        """
        两阶段采集：Metadata First + 规则评分 + Top N抓全文

        Phase 1: 元数据采集 (快速，10秒内完成所有信源)
        Phase 2: 规则评分 + Top N

        Returns:
            (all_signals, top_scored_signals)
        """
        all_signals = []
        sources = self.source_manager.sources

        if exclude_categories:
            original_count = len(sources)
            sources = [s for s in sources if s.get('category') not in exclude_categories]
            logger.info(f"过滤信源: {original_count} -> {len(sources)} (排除 {exclude_categories})")

        logger.info(f"[Phase 1] 开始元数据采集 {len(sources)} 个信源...")

        workers = max_workers or self.max_workers
        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_source = {
                executor.submit(self._crawl_single_source, source): source
                for source in sources
            }

            for future in as_completed(future_to_source):
                source = future_to_source[future]
                source_id = source.get('id', 'unknown')
                try:
                    signals, error = future.result()
                    if error:
                        logger.error(f"  -> {source.get('name', source_id)} 失败: {error}")
                        self.stats['failed'] += 1
                    else:
                        new_count = 0
                        for sig in signals:
                            if self.store.save_signal(sig):
                                new_count += 1
                        all_signals.extend(signals)
                        self.stats['crawled'] += len(signals)
                        self.stats['new'] += new_count
                        logger.info(f"  -> {source.get('name', source_id)}: {len(signals)} 条 (新增 {new_count})")
                except Exception as e:
                    logger.error(f"  -> {source.get('name', source_id)} 异常: {e}")
                    self.stats['failed'] += 1

        logger.info(f"[Phase 1] 元数据采集完成: {len(all_signals)} 条信号")

        logger.info(f"[Phase 2] 开始规则评分 + 分维度Top N筛选...")
        signal_dicts = [self.to_event_dict(sig) for sig in all_signals]

        dimension_signals = self.scoring_engine.get_top_signals_by_dimension(
            signal_dicts,
            top_n=top_n
        )

        event_signals = dimension_signals['event']
        tech_signals = dimension_signals['tech']
        trend_signals = dimension_signals['trend']

        logger.info(f"[Phase 2] 评分完成:")
        logger.info(f"  热点事件: {len([s for s in event_signals if s.event_score > 0])} 条")
        logger.info(f"  热点技术: {len([s for s in tech_signals if s.tech_score > 0])} 条")
        logger.info(f"  行业趋势: {len([s for s in trend_signals if s.trend_score > 0])} 条")

        for scored in event_signals[:3]:
            if scored.event_score > 0:
                logger.debug(f"  Event: {scored.title[:40]}... (score={scored.event_score:.1f})")
        for scored in tech_signals[:3]:
            if scored.tech_score > 0:
                logger.debug(f"  Tech: {scored.title[:40]}... (score={scored.tech_score:.1f})")
        for scored in trend_signals[:3]:
            if scored.trend_score > 0:
                logger.debug(f"  Trend: {scored.title[:40]}... (score={scored.trend_score:.1f})")

        logger.log_metric('crawled', self.stats['crawled'])
        logger.log_metric('new_signals', self.stats['new'])

        return all_signals, event_signals, tech_signals, trend_signals

    def _crawl_single_source(self, source: Dict) -> tuple:
        """采集单个信源，返回 (signals, error) """
        source_id = source.get('id', 'unknown')
        try:
            signals = self.collect_source(source)
            return signals, None
        except Exception as e:
            return [], str(e)

    def crawl_source(self, source_id: str) -> List[Signal]:
        """采集指定信源"""
        source = None
        for s in self.source_manager.sources:
            if s.get('id') == source_id:
                source = s
                break

        if not source:
            logger.error(f"Source not found: {source_id}")
            return []

        signals = self.collect_source(source)
        for sig in signals:
            self.store.save_signal(sig)

        return signals

    def to_event_dict(self, signal: Signal) -> Dict:
        """将Signal转换为事件字典（供分类使用）"""
        return {
            'id': signal.generate_id(),
            'time': signal.published or signal.fetched_at,
            'title': signal.title,
            'summary': signal.summary,
            'source': signal.source,
            'url': signal.url,
            'category': signal.category,
            'published': signal.published,
            'tags': signal.tags,
            'language': signal.language
        }