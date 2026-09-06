"""
Enhanced Crawler Agent - 增强版采集层
改进：
1. 更好的重试和退避策略（特别是arXiv）
2. 更多的GitHub RSS信源
3. 社交媒体支持
4. 更快的失败检测
"""
import os
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import feedparser
from bs4 import BeautifulSoup

from core.models import Signal
from core.storage import UnifiedStore
from core.logger import get_logger

logger = get_logger("EnhancedCrawler")


NEW_SOURCES = [
    # === 重要框架/工具 GitHub Releases ===
    {"id": "transformers_releases", "name": "HuggingFace Transformers", "url": "https://github.com/huggingface/transformers/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en", "enabled": True},
    {"id": "accelerate_releases", "name": "HuggingFace Accelerate", "url": "https://github.com/huggingface/accelerate/releases.atom", "type": "atom", "category": "training", "priority": "P0", "language": "en", "enabled": True},
    {"id": "peft_releases", "name": "HuggingFace PEFT", "url": "https://github.com/huggingface/peft/releases.atom", "type": "atom", "category": "training", "priority": "P0", "language": "en", "enabled": True},
    {"id": "trl_releases", "name": "TRL (Transformer Reinforcement Learning)", "url": "https://github.com/allenai/trl/releases.atom", "type": "atom", "category": "training", "priority": "P0", "language": "en", "enabled": True},
    {"id": "vllm_chat_releases", "name": "vLLM Chat", "url": "https://github.com/vllm-project/llamaflow/releases.atom", "type": "atom", "category": "inference", "priority": "P1", "language": "en", "enabled": True},

    # === 新增 Agent 框架 ===
    {"id": "mastra_releases", "name": "Mastra Releases", "url": "https://github.com/mastra-ai/mastra/releases.atom", "type": "atom", "category": "agent", "priority": "P1", "language": "en", "enabled": True},
    {"id": "graphiti_releases", "name": "Graphiti Releases", "url": "https://github.com/蒸汽 Reality/graphiti/releases.atom", "type": "atom", "category": "agent", "priority": "P1", "language": "en", "enabled": True},

    # === 推理优化新工具 ===
    {"id": "sglang_backend_releases", "name": "SGLang Backend", "url": "https://github.com/sgl-project/sglang/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en", "enabled": True},
    {"id": "lightllm_releases", "name": "LightLLM Releases", "url": "https://github.com/ModelTC/lightllm/releases.atom", "type": "atom", "category": "inference", "priority": "P1", "language": "en", "enabled": True},
    {"id": "lmdeploy_releases", "name": "LMDeploy Releases", "url": "https://github.com/InternLM/lmdeploy/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en", "enabled": True},

    # === 本地推理框架 ===
    {"id": "ollama_releases", "name": "Ollama Releases", "url": "https://github.com/ollama/ollama/releases.atom", "type": "atom", "category": "inference", "priority": "P0", "language": "en", "enabled": True},
    {"id": "llamaedge_releases", "name": "LlamaEdge Releases", "url": "https://github.com/asuride/llamaedge/releases.atom", "type": "atom", "category": "inference", "priority": "P2", "language": "en", "enabled": True},

    # === MCP相关 ===
    {"id": "modelcontextprotocol_releases", "name": "MCP SDK Releases", "url": "https://github.com/modelcontextprotocol/python-sdk/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en", "enabled": True},
    {"id": "fastmcp_releases", "name": "FastMCP Releases", "url": "https://github.com/jlowin/fastmcp/releases.atom", "type": "atom", "category": "agent", "priority": "P1", "language": "en", "enabled": True},

    # === 国产框架 ===
    {"id": "qwen_releases", "name": "Qwen Releases", "url": "https://github.com/QwenLM/Qwen/releases.atom", "type": "atom", "category": "industry", "priority": "P0", "language": "en", "enabled": True},
    {"id": "chatglm_releases", "name": "ChatGLM Releases", "url": "https://github.com/THUDM/ChatGLM3/releases.atom", "type": "atom", "category": "industry", "priority": "P0", "language": "en", "enabled": True},
    {"id": "kimi_releases", "name": "Kimi Releases", "url": "https://github.com/MoonshotAI/kimi-native-api/releases.atom", "type": "atom", "category": "industry", "priority": "P1", "language": "en", "enabled": True},

    # === 云厂商AI ===
    {"id": "groq_releases", "name": "Groq Releases", "url": "https://github.com/groq/groq-sdk/releases.atom", "type": "atom", "category": "inference", "priority": "P1", "language": "en", "enabled": True},
    {"id": "cerebras_releases", "name": "Cerebras Releases", "url": "https://github.com/Cerebras/cerebras-sdk/releases.atom", "type": "atom", "category": "inference", "priority": "P1", "language": "en", "enabled": True},

    # === 新兴Agent框架 ===
    {"id": "agentnet_releases", "name": "AgentNet Releases", "url": "https://github.com/baidu/agentnet/releases.atom", "type": "atom", "category": "agent", "priority": "P1", "language": "en", "enabled": True},
    {"id": "openagents_releases", "name": "OpenAgents Releases", "url": "https://github.com/xingyaoww/open-agents/releases.atom", "type": "atom", "category": "agent", "priority": "P1", "language": "en", "enabled": True},

    # === 数据库/向量存储 ===
    {"id": "milvus_releases", "name": "Milvus Releases", "url": "https://github.com/milvus-io/milvus/releases.atom", "type": "atom", "category": "storage", "priority": "P1", "language": "en", "enabled": True},
    {"id": "qdrant_releases", "name": "Qdrant Releases", "url": "https://github.com/qdrant/qdrant/releases.atom", "type": "atom", "category": "storage", "priority": "P1", "language": "en", "enabled": True},
    {"id": "chroma_releases", "name": "Chroma Releases", "url": "https://github.com/chroma-core/chroma/releases.atom", "type": "atom", "category": "storage", "priority": "P1", "language": "en", "enabled": True},

    # === 观测性/调试 ===
    {"id": "langfuse_releases", "name": "Langfuse Releases", "url": "https://github.com/langfuse/langfuse/releases.atom", "type": "atom", "category": "observability", "priority": "P1", "language": "en", "enabled": True},
    {"id": "opentelemetry_releases", "name": "OpenTelemetry Releases", "url": "https://github.com/open-telemetry/opentelemetry-python/releases.atom", "type": "atom", "category": "observability", "priority": "P1", "language": "en", "enabled": True},

    # === AI搜索/研究 ===
    {"id": "perplexica_releases", "name": "Perplexica Releases", "url": "https://github.com/ItzLeroy/Perplexica/releases.atom", "type": "atom", "category": "agent", "priority": "P2", "language": "en", "enabled": True},
    {"id": "fastgpt_releases", "name": "FastGPT Releases", "url": "https://github.com/chatgpt-cn/fastgpt/releases.atom", "type": "atom", "category": "agent", "priority": "P1", "language": "zh", "enabled": True},

    # === RAG框架 ===
    {"id": "llamaparse_releases", "name": "LlamaParse Releases", "url": "https://github.com/run-llama/llama_parse/releases.atom", "type": "atom", "category": "agent", "priority": "P0", "language": "en", "enabled": True},
    {"id": "disaggregated_rag_releases", "name": "Disaggregated RAG", "url": "https://github.com/neuml/disaggregated-rag/releases.atom", "type": "atom", "category": "agent", "priority": "P2", "language": "en", "enabled": True},
]


class EnhancedCrawler:
    """
    增强版采集Agent
    改进：
    - 更智能的重试策略（特别是arXiv）
    - 指数退避+抖动
    - 并行度更高
    - 更好的错误处理
    """

    def __init__(self, store: UnifiedStore = None, sources_file: str = None, max_workers: int = 16):
        self.store = store or UnifiedStore()
        self.sources_file = sources_file
        self.max_workers = max_workers
        self.stats = {'crawled': 0, 'new': 0, 'failed': 0, 'skipped': 0}
        self._load_sources()

    def _load_sources(self):
        """加载信源配置"""
        self.sources = list(NEW_SOURCES)

        if self.sources_file and os.path.exists(self.sources_file):
            try:
                with open(self.sources_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    existing = {s['id'] for s in self.sources}
                    for s in data.get('rss_feeds', []):
                        if s.get('enabled', False) and s['id'] not in existing:
                            self.sources.append(s)
            except Exception as e:
                logger.warning(f"Failed to load sources: {e}")

        self.enabled_sources = [s for s in self.sources if s.get('enabled', True)]
        logger.info(f"Loaded {len(self.enabled_sources)} enabled sources")

    def _make_session(self) -> requests.Session:
        """创建HTTP Session"""
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/rss+xml, application/xml, text/xml, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        })
        return session

    def _get_with_adaptive_retry(self, url: str, source_type: str = "atom", max_retries: int = 4) -> Optional[str]:
        """
        自适应重试策略
        - arXiv: 更保守的请求频率
        - GitHub: 标准重试
        - 其他: 快速失败
        """
        base_delay = 2
        if 'arxiv' in url.lower():
            base_delay = 5
        elif 'github' in url.lower():
            base_delay = 1

        for attempt in range(max_retries):
            session = self._make_session()
            timeout = 15 if 'arxiv' in url.lower() else 20

            try:
                resp = session.get(url, timeout=timeout)
                resp.raise_for_status()
                resp.encoding = 'utf-8'

                time.sleep(base_delay * (0.5 + hash(url) % 100 / 200))
                return resp.text

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:
                    wait_time = base_delay * (2 ** attempt) + (hash(url) % 10)
                    logger.warning(f"Rate limited, waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
                elif e.response.status_code >= 500:
                    delay = base_delay * (2 ** attempt)
                    logger.warning(f"Server error {e.response.status_code}, retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    return None

            except requests.exceptions.Timeout:
                if 'arxiv' in url.lower():
                    logger.warning(f"arXiv timeout (attempt {attempt+1}), trying alternative...")
                    time.sleep(base_delay * 2)
                else:
                    if attempt < max_retries - 1:
                        time.sleep(base_delay)

            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(base_delay * (attempt + 1))
                else:
                    logger.error(f"Request failed permanently: {e}")
                    return None

        return None

    def collect_rss(self, source: Dict) -> List[Signal]:
        """采集RSS/Atom源"""
        url = source['url']
        content = self._get_with_adaptive_retry(url, source.get('type', 'atom'))

        if not content:
            return []

        signals = []
        try:
            feed = feedparser.parse(content)
            for entry in feed.entries[:25]:
                try:
                    signal = self._parse_entry(entry, source)
                    if signal:
                        signals.append(signal)
                except Exception as e:
                    logger.error(f"Failed to parse entry: {e}")
                    continue
        except Exception as e:
            logger.error(f"Feed parse error for {source['name']}: {e}")

        return signals

    def _parse_entry(self, entry, source: Dict) -> Optional[Signal]:
        """解析单个RSS条目"""
        import hashlib

        entry_id = entry.get('id', entry.get('link', ''))
        signal_id = hashlib.md5(entry_id.encode()).hexdigest()[:16]

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

        return Signal(
            id=signal_id,
            title=entry.get('title', '无标题').strip()[:300],
            url=entry.get('link', ''),
            source=source.get('name', source['id']),
            source_id=source['id'],
            source_type=source.get('type', 'rss'),
            category=source.get('category', ''),
            priority=source.get('priority', 'P1'),
            published=published,
            summary=summary[:800],
            tags=[t.get('term', '') for t in getattr(entry, 'tags', [])[:5]],
            language=source.get('language', 'en')
        )

    def _clean_html(self, html: str) -> str:
        """清理HTML"""
        if not html:
            return ''
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text(separator=' ', strip=True)[:1000]

    def _crawl_single(self, source: Dict) -> tuple:
        """采集单个信源"""
        try:
            signals = self.collect_rss(source)
            return signals, None
        except Exception as e:
            return [], str(e)

    def crawl_all(self, exclude_categories: List[str] = None) -> List[Signal]:
        """并行采集所有信源"""
        all_signals = []
        sources = [s for s in self.enabled_sources if s.get('enabled', True)]

        if exclude_categories:
            sources = [s for s in sources if s.get('category') not in exclude_categories]

        logger.info(f"Starting crawl: {len(sources)} sources, {self.max_workers} workers")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_source = {
                executor.submit(self._crawl_single, source): source
                for source in sources
            }

            for future in as_completed(future_to_source):
                source = future_to_source[future]
                try:
                    signals, error = future.result()
                    if error:
                        logger.warning(f"  {source['name']}: {error}")
                        self.stats['failed'] += 1
                    else:
                        for sig in signals:
                            if self.store.save_signal(sig):
                                self.stats['new'] += 1
                        all_signals.extend(signals)
                        self.stats['crawled'] += len(signals)
                        if signals:
                            logger.info(f"  {source['name']}: +{len(signals)}")
                except Exception as e:
                    logger.error(f"  {source['name']} exception: {e}")
                    self.stats['failed'] += 1

        logger.info(f"Crawl complete: {self.stats['crawled']} signals, {self.stats['new']} new")
        return all_signals


def get_enhanced_crawler(store=None) -> EnhancedCrawler:
    """获取增强版采集器"""
    return EnhancedCrawler(store=store)