"""
Social Media Crawler - 社交媒体采集
支持：
- HackerNews (API)
- Reddit (热门帖子RSS)
- Twitter/X (通过第三方API或RSS)
"""
import os
import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from core.models import Signal
from core.storage import UnifiedStore
from core.logger import get_logger

logger = get_logger("SocialMediaCrawler")


class SocialMediaCrawler:
    """
    社交媒体采集器
    通过公开API和RSS采集社交媒体上的AI热点
    """

    HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
    HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
    HN_MAX_ITEMS = 30

    REDDIT_POPULAR_URL = "https://www.reddit.com/r/MachineLearning/hot.rss"
    REDDIT_AI_URL = "https://www.reddit.com/r/ArtificialIntelligence/hot.rss"

    def __init__(self, store: UnifiedStore = None):
        self.store = store or UnifiedStore()
        self.stats = {'crawled': 0, 'new': 0}

    def crawl_hackernews(self, keywords: List[str] = None, limit: int = 20) -> List[Signal]:
        """
        采集HackerNews AI相关帖子
        keywords: 匹配的关键词列表
        """
        if keywords is None:
            keywords = ['AI', 'LLM', 'GPT', 'neural', 'machine learning', 'language model',
                       'inference', 'agent', 'transformer', 'deep learning']

        signals = []
        try:
            resp = requests.get(self.HN_TOP_STORIES_URL, timeout=10)
            resp.encoding = 'utf-8'
            story_ids = json.loads(resp.text)[:50]

            for story_id in story_ids[:limit]:
                try:
                    item_resp = requests.get(self.HN_ITEM_URL.format(story_id), timeout=5)
                    item_resp.encoding = 'utf-8'
                    item = json.loads(item_resp.text)

                    title = item.get('title', '')
                    url = item.get('url', f"https://news.ycombinator.com/item?id={story_id}")

                    title_lower = title.lower()
                    if not any(kw in title_lower for kw in keywords):
                        continue

                    signal_id = hashlib.md5(str(story_id).encode()).hexdigest()[:16]

                    signal = Signal(
                        id=signal_id,
                        title=title[:300],
                        url=url,
                        source='HackerNews',
                        source_id=f'hn_{story_id}',
                        source_type='social',
                        category='social',
                        priority='P1' if item.get('score', 0) > 50 else 'P2',
                        published=datetime.fromtimestamp(item.get('time', 0)).isoformat() if item.get('time') else '',
                        summary=f"Score: {item.get('score', 0)} | Comments: {item.get('descendants', 0)}",
                        tags=['hackernews', 'tech'],
                        language='en'
                    )
                    signals.append(signal)
                    self.stats['crawled'] += 1

                    time.sleep(0.1)
                except Exception as e:
                    logger.debug(f"HN story error: {e}")
                    continue

        except Exception as e:
            logger.error(f"HN crawl error: {e}")

        return signals

    def crawl_reddit(self, subreddits: List[str] = None, limit_per_sub: int = 15) -> List[Signal]:
        """
        采集Reddit热门帖子
        """
        if subreddits is None:
            subreddits = ['MachineLearning', 'ArtificialIntelligence', 'LocalLLaMA', 'deeplearning']

        signals = []
        for subreddit in subreddits:
            try:
                url = f"https://www.reddit.com/r/{subreddit}/hot.rss"
                resp = requests.get(url, timeout=15, headers={'User-Agent': 'IntelligenceOS/1.0'})
                resp.raise_for_status()
                resp.encoding = 'utf-8'

                import feedparser
                feed = feedparser.parse(resp.text)

                for entry in feed.entries[:limit_per_sub]:
                    try:
                        signal_id = hashlib.md5(entry.get('id', entry.get('link', '')).encode()).hexdigest()[:16]

                        published = ''
                        if hasattr(entry, 'published_parsed') and entry.published_parsed:
                            published = datetime(*entry.published_parsed[:6]).isoformat()

                        summary = ''
                        if hasattr(entry, 'summary'):
                            summary = entry.summary[:500] if len(entry.summary) > 500 else entry.summary

                        signal = Signal(
                            id=signal_id,
                            title=entry.get('title', 'No Title')[:300],
                            url=entry.get('link', ''),
                            source=f'reddit/{subreddit}',
                            source_id=f'reddit_{entry.get("id", "")}',
                            source_type='social',
                            category='social',
                            priority='P1' if hasattr(entry, 'score') and entry.score > 100 else 'P2',
                            published=published,
                            summary=summary,
                            tags=['reddit', subreddit.lower()],
                            language='en'
                        )
                        signals.append(signal)
                        self.stats['crawled'] += 1

                    except Exception as e:
                        logger.debug(f"Reddit entry error: {e}")
                        continue

                time.sleep(1)

            except Exception as e:
                logger.error(f"Reddit r/{subreddit} error: {e}")
                continue

        return signals

    def crawl_all(self) -> List[Signal]:
        """采集所有社交媒体"""
        all_signals = []

        logger.info("Crawling HackerNews...")
        hn_signals = self.crawl_hackernews()
        all_signals.extend(hn_signals)
        logger.info(f"  HN: +{len(hn_signals)} signals")

        logger.info("Crawling Reddit...")
        reddit_signals = self.crawl_reddit()
        all_signals.extend(reddit_signals)
        logger.info(f"  Reddit: +{len(reddit_signals)} signals")

        for sig in all_signals:
            if self.store.save_signal(sig):
                self.stats['new'] += 1

        logger.info(f"Social media crawl complete: {self.stats['crawled']} crawled, {self.stats['new']} new")
        return all_signals


class NewsAggregatorCrawler:
    """
    新闻聚合采集器
    补充更多高质量AI新闻源
    """

    NEWS_SOURCES = [
        {"id": "hn_ai", "name": "HackerNews AI", "url": "https://hnrss.org/frontpage", "type": "rss", "category": "social", "priority": "P1", "enabled": True},
        {"id": "reddit_ml", "name": "Reddit ML", "url": "https://www.reddit.com/r/MachineLearning/hot.rss", "type": "rss", "category": "social", "priority": "P1", "enabled": True},
        {"id": "reddit_ai", "name": "Reddit AI", "url": "https://www.reddit.com/r/ArtificialIntelligence/hot.rss", "type": "rss", "category": "social", "priority": "P1", "enabled": True},
    ]

    def __init__(self, store: UnifiedStore = None):
        self.store = store or UnifiedStore()

    def crawl_rss(self, source: Dict) -> List[Signal]:
        """采集单个RSS源"""
        signals = []
        try:
            resp = requests.get(source['url'], timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
            resp.raise_for_status()
            resp.encoding = 'utf-8'

            import feedparser
            feed = feedparser.parse(resp.text)

            for entry in feed.entries[:20]:
                signal_id = hashlib.md5(entry.get('id', entry.get('link', '')).encode()).hexdigest()[:16]

                published = ''
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6]).isoformat()

                summary = ''
                if hasattr(entry, 'summary'):
                    summary = entry.summary[:500]
                elif hasattr(entry, 'description'):
                    summary = entry.description[:500]

                signal = Signal(
                    id=signal_id,
                    title=entry.get('title', 'No Title')[:300],
                    url=entry.get('link', ''),
                    source=source['name'],
                    source_id=source['id'],
                    source_type='rss',
                    category=source.get('category', 'social'),
                    priority=source.get('priority', 'P2'),
                    published=published,
                    summary=summary,
                    tags=source.get('tags', []),
                    language='en'
                )
                signals.append(signal)

        except Exception as e:
            logger.error(f"RSS crawl error ({source['name']}): {e}")

        return signals

    def crawl_all(self) -> List[Signal]:
        """采集所有新闻源"""
        all_signals = []
        for source in self.NEWS_SOURCES:
            if not source.get('enabled', True):
                continue
            signals = self.crawl_rss(source)
            all_signals.extend(signals)
            for sig in signals:
                self.store.save_signal(sig)
            logger.info(f"  {source['name']}: +{len(signals)} signals")
        return all_signals


def create_social_crawler(store=None) -> SocialMediaCrawler:
    """创建社交媒体采集器"""
    return SocialMediaCrawler(store=store)


def create_news_aggregator(store=None) -> NewsAggregatorCrawler:
    """创建新闻聚合器"""
    return NewsAggregatorCrawler(store=store)