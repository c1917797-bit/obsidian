"""
Twitter Source Adapter - Twitter/X 推特数据采集
使用 Nitter (开源推特替代) 无需认证即可采集

支持的采集方式：
1. 用户时间线: ?endpoint=user&user=username
2. 搜索结果: ?endpoint=search&query=keyword
3. 标签/话题: ?endpoint=hashtag&hashtag=AI
"""
import re
import time
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass

from core.logger import get_logger

logger = get_logger("TwitterSource")


NITTER_INSTANCES = [
    'nitter.net',
    'nitter.privacydev.net',
    'xcancel.com'
]


@dataclass
class Tweet:
    """推文数据"""
    id: str
    text: str
    author: str
    author_handle: str
    created_at: str
    url: str
    reply_count: int = 0
    retweet_count: int = 0
    like_count: int = 0
    is_retweet: bool = False
    is_reply: bool = False


class TwitterSourceAdapter:
    """
    Twitter数据采集适配器

    使用Nitter实例将Twitter时间线转换为RSS-like的格式
    无需Twitter API认证
    """

    def __init__(self, instance: str = 'nitter.net'):
        self.instance = instance
        self.base_url = f'https://{instance}'
        self._session = None

    def _make_session(self):
        import requests
        if self._session is None:
            self._session = requests.Session()
            self._session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
        return self._session

    def _parse_tweets_from_html(self, html: str) -> List[Tweet]:
        """从Nitter HTML页面解析推文"""
        from bs4 import BeautifulSoup

        tweets = []
        soup = BeautifulSoup(html, 'html.parser')

        timeline = soup.find('div', class_='timeline')
        if not timeline:
            return tweets

        for item in timeline.find_all('div', class_='timeline-item'):
            try:
                # 提取推文内容
                content_div = item.find('div', class_='tweet-content')
                if not content_div:
                    continue

                # 提取作者信息
                author_div = item.find('a', class_='author')
                author_name = author_div.find('span', class_='fullname').text.strip() if author_div else ''
                author_handle = author_div.get('href', '').strip('/') if author_div else ''

                # 提取时间
                time_elem = item.find('span', class_='tweet-date')
                created_at = time_elem.get('title', '') if time_elem else ''

                # 提取统计
                stats_div = item.find('div', class_='tweet-stats')
                reply_count = retweet_count = like_count = 0
                if stats_div:
                    for stat in stats_div.find_all('span', class_='tweet-stat'):
                        count_elem = stat.find('span', class_='tweet-stat-count')
                        if count_elem:
                            count = int(count_elem.text.replace(',', ''))
                            if 'reply' in stat.get('class', []):
                                reply_count = count
                            elif 'retweet' in stat.get('class', []):
                                retweet_count = count
                            elif 'heart' in stat.get('class', []):
                                like_count = count

                # 提取链接
                link_elem = item.find('a', class_='post-date')
                url = ''
                if link_elem:
                    url = 'https://twitter.com' + link_elem.get('href', '')

                # 生成ID
                tweet_id = url.split('/')[-1] if url else ''

                tweet = Tweet(
                    id=tweet_id,
                    text=content_div.text.strip(),
                    author=author_name,
                    author_handle=author_handle,
                    created_at=created_at,
                    url=url,
                    reply_count=reply_count,
                    retweet_count=retweet_count,
                    like_count=like_count
                )
                tweets.append(tweet)

            except Exception as e:
                continue

        return tweets

    def fetch_user_timeline(self, username: str, limit: int = 20) -> List[Tweet]:
        """
        获取用户时间线

        Args:
            username: Twitter用户名（不含@）
            limit: 返回数量

        Returns:
            推文列表
        """
        url = f'{self.base_url}/{username}/rss'
        try:
            session = self._make_session()
            resp = session.get(url, timeout=15)
            resp.raise_for_status()
            resp.encoding = 'utf-8'

            return self._parse_rss(resp.text)

        except Exception as e:
            logger.warning(f"Failed to fetch timeline for {username}: {e}")
            return []

    def search(self, query: str, limit: int = 20) -> List[Tweet]:
        """
        搜索推文（通过Nitter搜索页）

        注意: Nitter搜索功能可能不可用，改用RSS时间线采集
        """
        # Nitter没有搜索RSS，改用用户时间线采集
        logger.warning("Nitter搜索不可用，请使用用户时间线采集")
        return []

    def _parse_rss(self, rss_text: str) -> List[Tweet]:
        """解析Nitter RSS"""
        import xml.etree.ElementTree as ET

        tweets = []
        try:
            root = ET.fromstring(rss_text)
            for item in root.findall('.//item'):
                title = item.find('title')
                link = item.find('link')
                pub_date = item.find('pubDate')
                description = item.find('description')

                if title is not None and link is not None:
                    text = title.text or ''
                    # 清理HTML实体
                    text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')

                    # 提取作者（从title格式 "用户名 @handle"）
                    author_match = re.search(r'^(.+?)\s*@(\w+)', text)
                    author = author_match.group(1) if author_match else ''
                    handle = author_match.group(2) if author_match else ''

                    # 移除用户信息，只保留正文
                    if author_match:
                        text = text.split(')', 1)[-1].strip() if ')' in text else text
                        text = re.sub(r'^.+?\s*@\w+\s*:\s*', '', text)

                    tweet_id = link.text.split('/')[-1] if link.text else ''

                    tweet = Tweet(
                        id=tweet_id,
                        text=text.strip(),
                        author=author,
                        author_handle=handle,
                        created_at=pub_date.text if pub_date is not None else '',
                        url=link.text or '',
                        reply_count=0,
                        retweet_count=0,
                        like_count=0
                    )
                    tweets.append(tweet)

        except Exception as e:
            logger.warning(f"Failed to parse RSS: {e}")

        return tweets

    def to_signal_format(self, tweet: Tweet, source_id: str) -> Dict:
        """转换为Signal格式"""
        return {
            'id': f'twitter_{tweet.id}',
            'source_id': source_id,
            'title': f"@{tweet.author_handle}: {tweet.text[:100]}...",
            'content': tweet.text,
            'url': tweet.url,
            'author': tweet.author,
            'author_handle': tweet.author_handle,
            'published_at': tweet.created_at,
            'type': 'twitter',
            'category': 'social',
            'language': 'en',
            'engagement': {
                'replies': tweet.reply_count,
                'retweets': tweet.retweet_count,
                'likes': tweet.like_count
            }
        }


def get_twitter_default_accounts() -> List[Dict]:
    """获取Twitter上最重要的AI相关账号"""
    return [
        # AI Labs & Companies
        {'handle': 'AndrewYNg', 'name': 'Andrew Ng', 'category': 'AI_Lab'},
        {'handle': 'ylecun', 'name': 'Yann LeCun', 'category': 'AI_Lab'},
        {'handle': 'jimfan', 'name': 'Jim Fan (NVIDIA)', 'category': 'AI_Lab'},
        {'handle': 'DrJimFan', 'name': 'Jim Fan', 'category': 'AI_Lab'},
        {'handle': 'kaborothy', 'name': 'Yann LeCun', 'category': 'AI_Lab'},

        # Researchers
        {'handle': 'hardmaru', 'name': 'David Ha', 'category': 'Researcher'},
        {'handle': 'svpino', 'name': 'Santiago', 'category': 'Researcher'},
        {'handle': 'prince_canuma', 'name': 'Prince Canuma', 'category': 'Researcher'},

        # AI Companies
        {'handle': 'OpenAI', 'name': 'OpenAI', 'category': 'Company'},
        {'handle': 'AnthropicAI', 'name': 'Anthropic', 'category': 'Company'},
        {'handle': 'GoogleAI', 'name': 'Google AI', 'category': 'Company'},
        {'handle': 'DeepMind', 'name': 'DeepMind', 'category': 'Company'},
        {'handle': 'MistralAI', 'name': 'Mistral AI', 'category': 'Company'},
        {'handle': 'metaai', 'name': 'Meta AI', 'category': 'Company'},
        {'handle': 'xai', 'name': 'xAI', 'category': 'Company'},

        # AI Infrastructure
        {'handle': 'nvidia', 'name': 'NVIDIA', 'category': 'Infra'},
        {'handle': 'GPUCompute', 'name': 'NVIDIA GPU', 'category': 'Infra'},
        {'handle': 'huggingface', 'name': 'HuggingFace', 'category': 'Infra'},

        # AI News
        {'handle': '_akhaliq', 'name': 'AK (AI News)', 'category': 'News'},
        {'handle': 'osanseviero', 'name': 'Omar (HuggingFace)', 'category': 'News'},
        {'handle': 'ylecun', 'name': 'Yann LeCun', 'category': 'News'},

        # Agents & Coding
        {'handle': 'emollick', 'name': 'Ethan Mollick', 'category': 'Education'},
        {'handle': 'simonw', 'name': 'Simon Willison', 'category': 'Developer'},
        {'handle': 'swyx', 'name': 'Swyx', 'category': 'Developer'},

        # Chinese AI (英文动态)
        {'handle': 'deepseek_ai', 'name': 'DeepSeek', 'category': 'Company'},
        {'handle': 'Qwen_AI', 'name': 'Qwen', 'category': 'Company'},
    ]
