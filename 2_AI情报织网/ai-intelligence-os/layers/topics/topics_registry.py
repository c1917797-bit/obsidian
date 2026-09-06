"""
TopicsRegistry - 情报靶点追踪器
根据 topics_registry.json 定义，持续跟踪方向并给事件打标签
"""
import os
import json
from typing import List, Dict, Set, Optional
from datetime import datetime

from core.logger import get_logger

logger = get_logger("TopicsRegistry")


class TopicsRegistry:
    """
    情报靶点注册表
    功能：
    1. 加载课题配置
    2. 判断事件/信号属于哪个课题
    3. 给事件打课题标签
    """

    def __init__(self, config_path: str = None):
        if config_path is None:
            config_path = os.path.join(
                os.path.dirname(__file__),
                '..', '..', 'config', 'topics_registry.json'
            )
        self.config_path = config_path
        self.topics = []
        self.all_keywords = []  # 扁平化所有关键词
        self._load()

    def _load(self):
        """加载配置"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.topics = data.get('topics', [])
            self._build_keyword_index()
            logger.info(f"已加载 {len(self.topics)} 个情报靶点")
        except Exception as e:
            logger.error(f"加载 topics_registry 失败: {e}")
            self.topics = []

    def _build_keyword_index(self):
        """扁平化所有课题的关键词"""
        self.all_keywords = []
        for topic in self.topics:
            for kw in topic.get('keywords', []):
                self.all_keywords.append((kw.lower(), topic['name']))
            # 递归子课题
            for child in topic.get('children', []):
                for kw in child.get('keywords', []):
                    self.all_keywords.append((kw.lower(), child['name']))

    def match_topic(self, text: str) -> List[str]:
        """
        判断文本属于哪些课题
        @param text: 标题或内容
        @return: 匹配的课题名称列表
        """
        text_lower = text.lower()
        matched = []
        for kw, topic_name in self.all_keywords:
            if kw in text_lower:
                if topic_name not in matched:
                    matched.append(topic_name)
        return matched

    def match_all(self, title: str, content: str = "", summary: str = "") -> Dict[str, any]:
        """
        综合匹配标题+内容+摘要
        @return: {
            'matched_topics': [...],
            'topic_details': [{'name': ..., 'matched_keywords': [...]}],
            'is_strategic': bool  # 是否是战略级课题(P0)
        }
        """
        text = f"{title} {content} {summary}".lower()
        matched_topics = []
        topic_details = []

        seen_topics = set()
        for kw, topic_name in self.all_keywords:
            if kw in text and topic_name not in seen_topics:
                seen_topics.add(topic_name)
                matched_topics.append(topic_name)
                # 找关键词所属的课题对象
                topic_obj = self._find_topic(topic_name)
                if topic_obj:
                    matched_kws = [k for k in topic_obj.get('keywords', []) if k.lower() in text.lower()]
                    topic_details.append({
                        'name': topic_name,
                        'matched_keywords': matched_kws,
                        'priority': topic_obj.get('priority', 'P1')
                    })

        is_strategic = any(t.get('priority') == 'P0' for t in topic_details)

        return {
            'matched_topics': matched_topics,
            'topic_details': topic_details,
            'is_strategic': is_strategic
        }

    def _find_topic(self, name: str) -> Optional[Dict]:
        """根据名称找课题对象"""
        for topic in self.topics:
            if topic['name'] == name:
                return topic
            for child in topic.get('children', []):
                if child['name'] == name:
                    return child
        return None

    def get_topic_tree(self) -> List[Dict]:
        """获取课题树结构"""
        return self.topics

    def get_strategic_topics(self) -> List[str]:
        """获取所有 P0 课题"""
        return [t['name'] for t in self.topics if t.get('priority') == 'P0']

    def tag_event(self, event) -> Dict:
        """
        给事件打课题标签
        @param event: TechEvent 对象
        @return: 标签字典
        """
        title = getattr(event, 'title', '') or ''
        summary = getattr(event, 'summary', '') or ''
        content = getattr(event, 'content', '') or ''

        match_result = self.match_all(title, content, summary)

        return {
            'topics': match_result['matched_topics'],
            'is_strategic': match_result['is_strategic'],
            'topic_details': match_result['topic_details']
        }


def load_registry() -> TopicsRegistry:
    """加载课题注册表"""
    return TopicsRegistry()