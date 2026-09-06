"""
ResearchTopicAnalyzer - 研究课题分解与信源路由
将用户输入的课题分解为可搜索的研究问题，并确定信源优先级
"""
import re
from typing import List, Dict, Tuple

from core.logger import get_logger
from layers.research import ResearchQuestion, ResearchTopic

logger = get_logger("ResearchTopicAnalyzer")


class ResearchTopicAnalyzer:
    """
    研究课题分析器
    功能：
    1. 课题分解为研究问题
    2. 生成多个搜索 query 变体
    3. 信源路由优先级判断
    """

    def __init__(self):
        # 技术关键词 → 相关研究问题类型
        self.TECH_QUESTION_MAP = {
            'kv cache': [
                'KV Cache 淘汰策略',
                'KV Cache 压缩方法',
                'KV Cache 内存优化',
                '长上下文下的 KV Cache'
            ],
            'speculative decoding': [
                '投机解码算法优化',
                '投机解码效果评估',
                '推测解码延迟分析',
                '投机解码在分布式系统的应用'
            ],
            'multi-agent': [
                '多智能体协作机制',
                'Agent 通信协议',
                '多Agent任务调度',
                'Agent 状态管理'
            ],
            'quantization': [
                '量化方法对比',
                'INT4/INT8 量化精度损失',
                '量化感知训练 vs 量化后训练',
                '端侧量化部署'
            ],
            'inference optimization': [
                '推理延迟优化',
                '吞吐量提升方法',
                '推理成本优化',
                '批处理策略优化'
            ],
            'memory': [
                'Agent 记忆系统',
                '长期记忆存储架构',
                '记忆检索机制',
                '上下文窗口扩展'
            ],
            'distributed': [
                '分布式推理架构',
                '多卡并行策略',
                '通信优化',
                '模型并行 vs 数据并行'
            ]
        }

        # 信源类型优先级映射
        self.SOURCE_PRIORITY = {
            'academic': ['arxiv', 'paper', 'conference', 'iclr', 'neurips', 'icml'],
            'engineering': ['github', 'release', 'framework', 'vllm', 'sglang'],
            'industry': ['news', 'blog', 'company', 'announcement', 'funding']
        }

        # 学科领域关键词 → 信源类型倾向
        self.DOMAIN_SOURCE_TENDENCY = {
            'agent': 'engineering',  # Agent 方向工程实现强
            'runtime': 'engineering',
            'memory': 'academic',  # Memory 系统学术深度高
            'kv cache': 'academic',
            'speculative': 'academic',
            'quantization': 'engineering',  # 量化工程落地快
            'distributed': 'engineering',
            'multi-agent': 'both',
            'benchmark': 'academic',
            'evaluation': 'academic'
        }

    def analyze(self, topic: str) -> 'ResearchTopic':
        """
        入口：分析课题，返回分解后的 ResearchTopic

        Args:
            topic: 用户输入的研究课题

        Returns:
            ResearchTopic: 分解后的课题结构
        """
        from layers.research import ResearchTopic, ResearchQuestion

        logger.info(f"分析课题: {topic}")

        # 分解研究问题
        questions = self.decompose_research_questions(topic)

        # 生成搜索 query
        queries = self.generate_search_queries(topic, questions)

        # 判断信源优先级
        source_priority = self.route_sources(topic, questions)

        # 判断研究深度
        depth = self.estimate_depth(questions)

        return ResearchTopic(
            original_topic=topic,
            decomposed_questions=questions,
            search_queries=queries,
            source_priority=source_priority,
            estimated_depth=depth
        )

    def decompose_research_questions(self, topic: str) -> List[ResearchQuestion]:
        """
        将课题分解为多个可搜索的研究问题
        """
        from layers.research import ResearchQuestion

        topic_lower = topic.lower()
        questions = []
        q_id = 1

        # 核心问题：这个课题要解决什么问题？
        core_keyword = self._extract_core_keyword(topic_lower)
        questions.append(ResearchQuestion(
            id=f"q{q_id}",
            question=f"{topic} 的核心问题是什么？",
            keywords=self._extract_keywords(topic),
            priority="P0",
            source_type=self._guess_source_type(topic_lower)
        ))
        q_id += 1

        # 如果匹配已知技术领域，添加具体研究问题
        for tech_pattern, sub_questions in self.TECH_QUESTION_MAP.items():
            if tech_pattern in topic_lower:
                for sq in sub_questions:
                    questions.append(ResearchQuestion(
                        id=f"q{q_id}",
                        question=sq,
                        keywords=[tech_pattern],
                        priority="P1",
                        source_type=self._guess_source_type(tech_pattern)
                    ))
                    q_id += 1

        # 方法对比问题
        questions.append(ResearchQuestion(
            id=f"q{q_id}",
            question=f"现有方法对比：各方法的优劣是什么？",
            keywords=self._extract_keywords(topic),
            priority="P0",
            source_type="academic"
        ))
        q_id += 1

        # 评估指标问题
        questions.append(ResearchQuestion(
            id=f"q{q_id}",
            question=f"该方向的评估指标和基准是什么？",
            keywords=self._extract_keywords(topic) + ['benchmark', 'evaluation'],
            priority="P1",
            source_type="academic"
        ))
        q_id += 1

        # 开放问题/未解决方向
        questions.append(ResearchQuestion(
            id=f"q{q_id}",
            question=f"该方向有哪些未解决的研究空白？",
            keywords=self._extract_keywords(topic) + ['open problem', 'future'],
            priority="P1",
            source_type="academic"
        ))

        logger.info(f"分解为 {len(questions)} 个研究问题")
        return questions

    def generate_search_queries(self, topic: str, questions: List[ResearchQuestion]) -> List[str]:
        """
        生成多个搜索 query 变体
        """
        queries = []

        # 原始课题作为 query
        queries.append(topic)

        # 从研究问题生成 query
        for q in questions:
            queries.append(q.question)

        # 生成关键词组合 query
        keywords = self._extract_keywords(topic)

        # 两两组合生成复合 query
        if len(keywords) >= 2:
            for i in range(len(keywords)):
                for j in range(i + 1, len(keywords)):
                    queries.append(f"{keywords[i]} {keywords[j]}")

        # 加入特定的后缀 query（针对不同类型的内容）
        for kw in keywords[:3]:
            queries.append(f"{kw} site:arxiv.org")
            queries.append(f"{kw} site:github.com")

        # 去重
        seen = set()
        unique_queries = []
        for q in queries:
            if q not in seen and len(q) > 3:
                seen.add(q)
                unique_queries.append(q)

        return unique_queries[:15]  # 最多15个query

    def route_sources(self, topic: str, questions: List[ResearchQuestion]) -> List[str]:
        """
        确定搜索优先级：哪些来源应该优先搜索
        返回优先级列表：['conference', 'arxiv', 'github', ...]
        """
        topic_lower = topic.lower()

        # 分析领域倾向
        domain_tendency = 'both'
        for domain, tendency in self.DOMAIN_SOURCE_TENDENCY.items():
            if domain in topic_lower:
                domain_tendency = tendency
                break

        priority_order = []

        if domain_tendency in ['academic', 'both']:
            priority_order.extend(['arxiv', 'conference', 'paper'])
        if domain_tendency in ['engineering', 'both']:
            priority_order.extend(['github', 'framework', 'release'])
        if domain_tendency in ['industry', 'both']:
            priority_order.extend(['news', 'company', 'blog'])

        # 始终包含 signals（已有的情报）
        if 'signals' not in priority_order:
            priority_order.append('signals')

        logger.info(f"信源优先级: {priority_order}")
        return priority_order

    def _extract_core_keyword(self, topic: str) -> str:
        """提取核心关键词"""
        keywords = self._extract_keywords(topic)
        return keywords[0] if keywords else topic

    def _extract_keywords(self, text: str) -> List[str]:
        """提取关键词"""
        # 移除常见停用词
        stop_words = {'the', 'a', 'an', 'of', 'in', 'for', 'on', 'with', 'to', 'and', 'is', 'are', 'or', 'for', 'based', 'using'}
        words = re.findall(r'\b[a-z]+\b', text.lower())
        return [w for w in words if w not in stop_words and len(w) > 2]

    def _guess_source_type(self, keyword: str) -> str:
        """根据关键词猜测主要信源类型"""
        if any(k in keyword for k in ['agent', 'runtime', 'framework', 'system']):
            return 'engineering'
        elif any(k in keyword for k in ['memory', 'cache', 'optimization', 'algorithm']):
            return 'academic'
        elif any(k in keyword for k in ['multi', 'collaborative', 'communication']):
            return 'both'
        return 'academic'

    def estimate_depth(self, questions: List[ResearchQuestion]) -> str:
        """估计研究深度"""
        if len(questions) >= 6:
            return 'deep'
        elif len(questions) >= 4:
            return 'medium'
        return 'shallow'