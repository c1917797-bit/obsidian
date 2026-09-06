"""
Insight Agent - 战略洞察层
生成符合「每日前沿科技简报」格式的高质量报告
"""
import os
import time
import json
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from core.models import TechEvent, Report
from core.storage import UnifiedStore
from core.logger import get_logger
from core.minimax_client import get_client

logger = get_logger("InsightAgent")

CATEGORIES = ['AI-Agent', 'LLM推理', '多模态推理', '模型压缩', '推理框架', '行业趋势', '热点事件', '热点技术', '热点方向']

DEFAULT_OUTPUT_FORMAT = """[{category}]：{title}@{entity}

[一句话总结]：{summary}

[关键词]：{keywords}

[业务启示]：
{business_insight}

[背景介绍]：
{background}

[技术和创新点描述]：
{tech_innovation}

[效果总结]：
{results}"""


class InsightAgent:
    """
    洞察Agent
    生成高质量的每日/周度技术简报
    """

    def __init__(self, store: UnifiedStore = None, trend_engine = None):
        self.store = store or UnifiedStore()
        self.trend_engine = trend_engine
        self.client = get_client()
        self.max_retries = 5
        self.retry_delay = 5
        self._load_output_format_config()

    def _load_output_format_config(self):
        """加载输出格式配置"""
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'output_formats.json')
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    self.output_config = json.load(f)
                logger.info(f"Loaded output format config with {len(self.output_config.get('output_formats', {}))} categories")
            except Exception as e:
                logger.warning(f"Failed to load output format config: {e}")
                self.output_config = {'output_formats': {}}
        else:
            self.output_config = {'output_formats': {}}

    def _generate_with_retry(self, prompt: str, temperature: float = 0.6, max_tokens: int = 2048) -> str:
        """带重试的LLM生成"""
        messages = [{"role": "user", "content": prompt}]

        for attempt in range(self.max_retries):
            try:
                content = self.client.chat(messages, temperature=temperature, max_tokens=max_tokens)
                if content and len(content) > 50:
                    return content
                logger.warning(f"Attempt {attempt+1}: Empty or short response, retrying...")
            except Exception as e:
                logger.warning(f"Attempt {attempt+1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))

        return ""

    def _generate_with_retry_with_system(self, prompt: str, system_prompt: str = None, temperature: float = 0.6, max_tokens: int = 2048) -> str:
        """带系统提示的LLM生成"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        for attempt in range(self.max_retries):
            try:
                content = self.client.chat(messages, temperature=temperature, max_tokens=max_tokens)
                if content and len(content) > 50:
                    return content
                logger.warning(f"Attempt {attempt+1}: Empty or short response, retrying...")
            except Exception as e:
                logger.warning(f"Attempt {attempt+1} failed: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))

        return ""

    def _is_ai_related_content(self, event: TechEvent) -> bool:
        """检查内容是否与AI相关"""
        title = getattr(event, 'title', '') or ''
        summary = getattr(event, 'summary', '') or ''
        source = getattr(event, 'source', '') or ''
        text = (title + ' ' + summary).lower()

        ai_keywords = [
            'ai', 'artificial intelligence', 'machine learning', 'deep learning',
            'llm', 'gpt', 'gemma', 'claude', 'chatgpt', 'openai', 'anthropic',
            'model', 'models', 'neural', 'network', 'transformer',
            'agent', 'multi-agent', 'rag', 'retrieval', 'embedding',
            'inference', 'training', 'fine-tuning', 'alignment',
            'nlp', 'nlu', 'cv', 'computer vision', 'speech', 'tts', 'asr',
            'stable diffusion', 'diffusion', 'gan', '生成式', '大模型',
            '模型', '人工智能', '智能', '神经网络', '深度学习', '机器学习',
            'arXiv', 'arxiv', 'paper', '论文', 'research', '研究',
            'tech', 'technology', '技术', 'algorithm', '算法',
            '框架', 'framework', '开源', 'open source',
            'nvidia', 'gpu', 'tpu', 'chip', '芯片', 'hardware', '硬件',
            'runtime', '推理', '训练', '优化', 'optimization',
            'api', 'cloud', '云端', '部署', 'deploy',
            'semantic', '向量', '检索', '搜索',
            'benchmark', '评估', '评测', '性能', 'accuracy',
            'vllm', 'sglang', 'tensorrt', 'llama', 'gemma', 'mistral',
            'langchain', 'llamaindex', 'autogen', 'dspy', 'crewai',
            'robot', '机器人', '自动驾驶', '智能驾驶', '智能汽车',
            'hacker news', 'huggingface', 'github', 'ssm', 'rw kv',
            'speculative', 'decoding', 'batch', 'serving', 'inference',
            'token', 'latency', 'throughput', 'gpu',
            'release', 'launch', 'announce', 'debut', 'unveil',
            'startup', 'funding', 'investor', 'acquisition',
            'developer', 'programming', 'coding', 'software',
            'virtual', 'digital', 'assistant', 'assistant',
            'claude', 'gemini', 'copilot', 'cursor', 'windsurf'
        ]

        company_keywords = [
            'openai', 'anthropic', 'google', 'meta', 'nvidia', 'microsoft',
            'deepseek', 'mistral', 'cohere', 'hugging face', 'stability ai',
            'x.ai', 'waymo', 'tesla', '小鹏', '蔚来', '理想', '比亚迪',
            '华为', '阿里', '腾讯', '百度', '字节',
            'amazon', 'apple', 'apple', 'facebook', 'netflix'
        ]

        if any(k in text for k in ai_keywords):
            return True
        if any(k in source.lower() for k in company_keywords):
            return True
        if any(k in title for k in ['LLM', 'GPT', 'AI', 'AGI', 'RAG', 'Agent']):
            return True

        return False

    def _filter_ai_events(self, events: List[TechEvent]) -> List[TechEvent]:
        """过滤掉非AI相关的事件"""
        filtered = []
        for event in events:
            if self._is_ai_related_content(event):
                filtered.append(event)
            else:
                logger.info(f"过滤非AI内容: {getattr(event, 'title', 'Unknown')[:50]}")
        return filtered

    def _categorize_event(self, event: TechEvent) -> str:
        """为事件分配分类标签 - 基于信号来源类型和内容特征"""
        title = getattr(event, 'title', '') or ''
        summary = getattr(event, 'summary', '') or ''
        source = getattr(event, 'source', '') or ''
        entity = getattr(event, 'entity', '') or ''
        metadata = getattr(event, 'metadata', {}) or {}
        source_type = metadata.get('source_type', '') or ''
        url = getattr(event, 'url', '') or ''

        title_lower = title.lower()
        text = title_lower + ' ' + summary.lower()

        # === Twitter来源 -> 优先作为热点事件/行业趋势 ===
        if source_type == 'twitter_rss':
            # 产品发布/公司动态 -> 热点事件
            twitter_event_keywords = ['release', 'launch', 'announce', 'unveil', 'new model', 'new version',
                                     'openai', 'anthropic', 'google', 'meta', 'deepseek', 'nvidia', 'mistral',
                                     'hugging face', 'vllm', 'sglang', 'xai', 'breaking', 'just in']
            if any(k in text for k in twitter_event_keywords):
                return '热点事件'
            # 技术讨论/论文 -> 热点技术
            tech_keywords = ['paper', 'research', 'study', 'arxiv', 'new method', 'technique', 'algorithm']
            if any(k in text for k in tech_keywords):
                return '热点技术'
            # 默认 -> 行业趋势（捕捉AI圈动态）
            return '行业趋势'

        # === GitHub Releases -> 热点技术（产品发布/版本更新）===
        if source_type == 'atom' or 'github.com' in source.lower():
            return '热点技术'

        # === 新闻来源检测 (最高优先级) ===
        # 中文新闻源：量子位、机器之心、通心粉等 -> 行业/产业新闻
        news_cn_sources = ['量子位', '机器之心', '通心粉', '虎嗅', '36kr', '雷锋网', '爱范儿']
        if any(ns in source for ns in news_cn_sources):
            # 检测人物/职位变动新闻 (热点事件)
            person_change_keywords = ['加盟', '入职', '任命', '挖来', '聘请', '离职', '创业', '加入',
                                       '新老师', '新教授', '新院长', '导师', '讲师', '全职', '加入',
                                       '重返', '进入', '布局', '核心岗位', '开招', '扩张']
            if any(k in text for k in person_change_keywords):
                return '热点事件'
            # 检测产业动态
            industry_keywords = ['合作', '收购', '融资', '产品', '战略', '发布', '推出', '上线']
            if any(k in text for k in industry_keywords):
                return '行业趋势'
            # 检测技术动态
            tech_keywords = ['论文', '研究', '技术', '模型', '算法', '框架', '系统']
            if any(k in text for k in tech_keywords):
                return '热点技术'
            return '行业趋势'

        # 英文新闻源：TechCrunch, VentureBeat, Import AI等
        news_en_sources = ['techcrunch', 'venturebeat', 'import ai', 'the information', 'wired', 'arstechnica']
        if any(ns in source.lower() for ns in news_en_sources):
            # 产品发布/新功能 -> 热点事件
            new_product_keywords = ['launch', 'release', 'announce', 'unveil', 'rolling out', 'now lets',
                                    'new model', 'new feature', 'new tool', 'debuts', 'introduces', 'new music']
            if any(k in text for k in new_product_keywords):
                return '热点事件'
            # 融资/收购/合作 -> 行业趋势
            business_keywords = ['startup', 'funding', 'acquisition', 'partnership', 'raises', 'Series']
            if any(k in text for k in business_keywords):
                return '行业趋势'
            return '行业趋势'

        # === 公司/人物新闻检测 (跨来源) ===
        person_news_keywords = ['ceo', 'cto', 'founder', 'joins', 'leaves', 'appointed', 'hires',
                                 'jensen', '黄仁勋', 'nvidia ceo']
        if any(k in text for k in person_news_keywords):
            return '热点事件'

        # === 论文/研究检测 (paperlists来源优先) ===
        if source_type in ['paperlists_json', 'paper']:
            # 检查是否是技术突破
            breakthrough_keywords = ['new', 'novel', 'introduce', 'propose', 'achieve', 'state-of-the-art', 'sota',
                                     'breakthrough', 'improve', 'performance']
            if any(k in text for k in breakthrough_keywords):
                return '热点技术'
            return '热点方向'

        # === 技术分类 ===
        if any(k in text for k in ['agent', 'multi-agent', 'agentic', 'tool use', 'tool_calling', 'function calling']):
            return 'AI-Agent'
        elif any(k in text for k in ['inference', 'speculative', 'decoding', 'kv cache', 'batch', 'vllm', 'sglang']):
            return 'LLM推理'
        elif any(k in text for k in ['multimodal', 'vision', 'image', 'audio', 'video', 'video generation']):
            return '多模态推理'
        elif any(k in text for k in ['quantize', 'quantization', 'prune', 'distill', 'compress', 'pruning']):
            return '模型压缩'
        elif any(k in text for k in ['llama.cpp', 'tensorrt', 'triton', 'deepspeed', 'accelerate']):
            return '推理框架'
        elif any(k in text for k in ['openai', 'anthropic', 'google', 'meta', 'deepseek', 'nvidia', 'microsoft']):
            return '行业趋势'

        # === 论文/研究检测 (其他来源) ===
        paper_keywords = ['paper', 'arxiv', 'research', 'study', 'acl', 'cvpr', 'neurips', 'emnlp', 'iclr']
        if any(k in text for k in paper_keywords):
            if any(k in text for k in ['new', 'novel', 'introduce', 'propose', 'achieve', 'state-of-the-art', 'sota']):
                return '热点技术'
            return '热点方向'

        # === 产品发布检测 ===
        release_keywords = ['release', 'launch', 'announce', 'unveil', 'version', 'beta', '正式发布', '推出',
                            'b9354', 'v0.5.0', '更新', '新版']
        if any(k in text for k in release_keywords):
            return '热点技术'

        # === 默认分类 ===
        return '热点方向'

    def _build_brief_entry(self, event: TechEvent) -> str:
        """构建单条简报条目"""
        category = self._categorize_event(event)
        title = getattr(event, 'title', 'Unknown')[:100]

        # 防御性清理：修复被爬虫合并的标题
        # 例如 "ResearchApr 24, 2026Project Deal" -> "Project Deal"
        # 或 "AlignmentMay 8, 2026Teaching Claude why" -> "Teaching Claude why"
        # 匹配：月份名（全称或缩写）+ 日期 + 年份，年份后必须是字母才截断
        MONTH_PATTERN = 'January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'
        m = re.search(r'(' + MONTH_PATTERN + r')\s+\d{1,2},?\s+\d{4}(\w)', title)
        if m and len(m.group(2)) == 1:
            # 年份后的下一个字母就是新标题的起点
            cleaned = title[m.start(2):].lstrip(':： ')
            if len(cleaned) >= 10:
                title = cleaned
        summary = getattr(event, 'summary', '')[:500]
        url = getattr(event, 'url', '')
        entity = getattr(event, 'entity', 'Unknown') or getattr(event, 'company', 'Unknown') or self._extract_entity_from_title(title)
        importance = getattr(event, 'importance', 'P1')
        confidence = '高' if importance == 'P0' else '中'

        if category == '热点技术':
            return self._build_tech_insight_entry(event, category, title, summary, url, entity, confidence)
        elif category == '热点事件':
            return self._build_event_insight_entry(event, category, title, summary, url, entity, confidence)
        elif category == '热点方向':
            return self._build_trend_insight_entry(event, category, title, summary, url, entity, confidence)
        else:
            return self._build_standard_entry(category, title, summary, url, entity, confidence)

    def _build_event_insight_entry(self, event: TechEvent, category: str, title: str, summary: str, url: str, entity: str, confidence: str) -> str:
        """构建热点事件的富格式条目 - 按照 日报格式.md 的模板"""
        full_summary = summary if len(summary) > 50 else self._get_enhanced_summary(event)

        prompt = f"""请根据以下事件信息，生成符合格式的热点事件洞察报告。

标题：{title}
来源：{getattr(event, 'source', '未知')}
实体：{entity}
摘要：{full_summary[:300]}
URL：{url}

严格按以下格式输出，生成中文报告，直接输出不要解释：

[热点事件]：{title}@{entity}

[一句话总结]：【主体】做了【什么】，【效果/价值】（50-100字）

[关键词]：关键词1、关键词2、关键词3、关键词4、关键词5（5-8个，用中文顿号分隔）

[业务启示]：
【维度名1】：2-3句话（维度名要基于内容自拟，如【组织管理】、【技术战略】、【市场影响】等）
【维度名2】：2-3句话
（2-4个维度，用【自拟维度名】：格式）

[背景介绍]：
【技术/事件名】是【发布者】推出的【类型】，用于【目的】。此前【历史背景】，现在【新进展】。（100-150字）

[技术和创新点]：
技术点1名称: 详细描述（一句话）
技术点2名称: 详细描述（一句话）
（3-6个技术点，格式为「名称: 描述」，用中文冒号）

[效果总结]：
【技术/事件名称】在【领域】方面有【效果描述】。（80-120字）

---
- **来源**: {url if url else '<primary source URL>'}
- **置信度**: {confidence}
- **信号等级**: 🔴核心 / 🟡关注 / 🟢观察
- **行动**: 观察

直接输出报告内容，不要输出任何其他文字。"""

        try:
            insight = self._generate_with_retry(prompt, temperature=0.6, max_tokens=2000)
            if insight and len(insight) > 100:
                # Clean up any thinking content
                insight = re.sub(r'<think>.*?', '', insight, flags=re.DOTALL)
                insight = re.sub(r'<think>.*?', '', insight, flags=re.DOTALL)
                insight = insight.strip()
                # Ensure it starts with [热点事件]
                if not insight.startswith('[热点事件]'):
                    insight = f'[热点事件]：{title}@{entity}\n\n' + insight
                return insight
        except Exception as e:
            logger.warning(f"Failed to generate event insight: {e}")

        return self._build_standard_entry(category, title, summary, url, entity, confidence)

    def _build_trend_insight_entry(self, event: TechEvent, category: str, title: str, summary: str, url: str, entity: str, confidence: str) -> str:
        """构建热点方向的富格式条目（产业动态）- 按照 日报格式.md 的模板"""
        full_summary = summary if len(summary) > 50 else self._get_enhanced_summary(event)

        prompt = f"""请根据以下产业动态信息，生成符合格式的热点方向洞察报告。

标题：{title}
来源：{getattr(event, 'source', '未知')}
实体：{entity}
摘要：{full_summary[:300]}
URL：{url}

严格按以下格式输出，生成中文报告，直接输出不要解释：

[热点方向]：{title}@{entity}

[一句话总结]：【领域】正在发生【趋势描述】，反映出【核心变化】。（50-100字）

[关键信号]：
1. 【信号1】：具体事实（来源）
2. 【信号2】：具体事实（来源）
3. 【信号3】：具体事实（来源）
（3-5个关键事实，每个包含具体数据或事件）

[玩家动态]：
- 【玩家1】：动作+影响
- 【玩家2】：动作+影响
（主要玩家及最新动态，2-4个）

[趋势研判]：
根据上述信号，【领域】正在发生【趋势描述】，预计将在【时间范围】内产生以下影响：1）...2）...（2-3句话的趋势判断）

[战略启示]：
1. 【企业】：应该关注/行动...
2. 【开发者】：应该关注/行动...
（2-3个维度的战略建议）

---
- **来源**: {url if url else '<primary source URL>'}
- **置信度**: {confidence}
- **信号等级**: 🔴核心 / 🟡关注 / 🟢观察
- **行动**: 观察

直接输出报告内容，不要输出任何其他文字。"""

        try:
            insight = self._generate_with_retry(prompt, temperature=0.6, max_tokens=2000)
            if insight and len(insight) > 100:
                # Clean up any thinking content
                insight = re.sub(r'<think>.*?', '', insight, flags=re.DOTALL)
                insight = re.sub(r'<think>.*?', '', insight, flags=re.DOTALL)
                insight = insight.strip()
                # Ensure it starts with [热点方向]
                if not insight.startswith('[热点方向]'):
                    insight = f'[热点方向]：{title}@{entity}\n\n' + insight
                return insight
        except Exception as e:
            logger.warning(f"Failed to generate trend insight: {e}")

        return self._build_standard_entry(category, title, summary, url, entity, confidence)

    def _build_tech_insight_entry(self, event: TechEvent, category: str, title: str, summary: str, url: str, entity: str, confidence: str) -> str:
        """构建热点技术的富格式条目 - 按照 日报格式.md 的模板"""
        full_summary = summary if len(summary) > 50 else self._get_enhanced_summary(event)

        prompt = f"""请根据以下技术信息，生成符合格式的热点技术洞察报告。

标题：{title}
来源：{getattr(event, 'source', '未知')}
实体：{entity}
摘要：{full_summary[:300]}
URL：{url}

严格按以下格式输出，生成中文报告，直接输出不要解释：

[热点技术]：{title}@{entity}

[一句话总结]：【主体】做了【什么】，【效果/价值】（50-100字）

[关键词]：关键词1、关键词2、关键词3、关键词4、关键词5（5-8个，用中文顿号分隔）
[业务启示]：
【维度名1】：2-3句话（维度名要基于内容自拟，如【模型设计】、【训练策略】、【部署优化】、【安全隐私】等）
【维度名2】：2-3句话
（2-4个维度，用【自拟维度名】：格式）

[背景介绍]：
【技术名】是【发布者】推出的【类型】，用于【目的】。此前【历史背景】，现在【新进展】。（100-150字）

[技术和创新点]：
技术点1名称: 详细描述（一句话）
技术点2名称: 详细描述（一句话）
（3-6个技术点，格式为「名称: 描述」，用中文冒号）

[效果总结]：
【技术名称】在【性能/效率/能力】方面有显著提升。（80-120字）

---
- **来源**: {url if url else '<primary source URL>'}
- **置信度**: {confidence}
- **信号等级**: 🔴核心 / 🟡关注 / 🟢观察
- **行动**: 观察 / 深读 / 试玩

直接输出报告内容，不要输出任何其他文字。"""

        try:
            insight = self._generate_with_retry(prompt, temperature=0.6, max_tokens=2000)
            if insight and len(insight) > 100:
                # Clean up any thinking content
                insight = re.sub(r'<think>.*?', '', insight, flags=re.DOTALL)
                insight = re.sub(r'<think>.*?', '', insight, flags=re.DOTALL)
                insight = insight.strip()
                # Ensure it starts with [热点技术]
                if not insight.startswith('[热点技术]'):
                    insight = f'[热点技术]：{title}@{entity}\n\n' + insight
                return insight
        except Exception as e:
            logger.warning(f"Failed to generate tech insight: {e}")

        return self._build_standard_entry(category, title, summary, url, entity, confidence)

    def _get_enhanced_summary(self, event: TechEvent) -> str:
        """获取增强的摘要信息"""
        parts = []
        if getattr(event, 'summary', ''):
            parts.append(event.summary)
        if getattr(event, 'innovation', ''):
            parts.append(f"创新点：{event.innovation}")
        if getattr(event, 'problem_solved', ''):
            parts.append(f"解决问题：{event.problem_solved}")
        if getattr(event, 'metadata', {}):
            venue = event.metadata.get('venue', '')
            year = event.metadata.get('year', '')
            if venue:
                parts.append(f"发表在：{venue} {year}")
        return ' '.join(parts)[:500] if parts else ''

    def _extract_entity_from_title(self, title: str) -> str:
        """从标题中提取实体/公司名"""
        known_companies = ['Google', 'OpenAI', 'Anthropic', 'Meta', 'Microsoft', 'NVIDIA', 'DeepSeek',
                          'Meta', 'Amazon', 'Apple', 'xAI', 'Mistral', 'Cohere', '字节跳动', '百度', '阿里巴巴']
        for company in known_companies:
            if company.lower() in title.lower():
                return company
        return 'Unknown'

    def _build_standard_entry(self, category: str, title: str, summary: str, url: str, entity: str, confidence: str) -> str:
        """构建标准格式的简报条目"""
        return f"""【{category}】{title}

- **来源**: {url if url else '待补充'}
- **置信度**: {confidence}"""

    def generate_daily_brief(self, events: List[TechEvent] = None) -> Report:
        """生成每日简报"""
        if not events:
            events = self.store.get_recent_events(days=1, limit=20)

        if not events:
            return Report(
                title="每日简报 - 无数据",
                content="今日无新的技术事件记录。",
                report_type="daily",
                period=datetime.now().strftime('%Y-%m-%d')
            )

        events = self._filter_ai_events(events)

        date_str = datetime.now().strftime('%Y-%m-%d')
        week_str = self._get_week_period()

        events_by_category = {}
        for event in events:
            cat = self._categorize_event(event)
            if cat not in events_by_category:
                events_by_category[cat] = []
            events_by_category[cat].append(event)

        content = f"""📡 前沿科技简报 · {date_str}

## 🔥 热点事件
"""

        hot_events = events_by_category.get('热点事件', [])[:4]
        if not hot_events:
            hot_events = [e for e in events if getattr(e, 'importance', 'P1') == 'P0'][:3]
        for event in hot_events:
            content += self._build_brief_entry(event) + "\n\n"

        content += "## 💡 热点技术\n"
        tech_events = events_by_category.get('热点技术', [])
        if not tech_events:
            tech_events = [e for e in events if 'model' in getattr(e, 'title', '').lower() or 'paper' in getattr(e, 'title', '').lower()][:4]
        for event in tech_events[:4]:
            content += self._build_brief_entry(event) + "\n\n"

        content += "## 📊 行业趋势\n"
        industry_events = events_by_category.get('行业趋势', [])[:3]
        for event in industry_events:
            content += self._build_brief_entry(event) + "\n\n"

        content += "## 🤖 AI-Agent\n"
        agent_events = events_by_category.get('AI-Agent', [])[:3]
        for event in agent_events:
            content += self._build_brief_entry(event) + "\n\n"

        content += "## ⚡ LLM推理\n"
        inference_events = events_by_category.get('LLM推理', [])[:3]
        for event in inference_events:
            content += self._build_brief_entry(event) + "\n\n"

        content += f"""---
📌 文末汇总
- 今日最值得深读: {'; '.join([getattr(e, 'title', 'Unknown')[:50] for e in events[:2]])}
- 今日可跳过: 无
- 待观察趋势(跨条目): 推理优化技术持续迭代，Agent框架正在整合

## 反向链接

> [!info] 相关笔记
> - [[Weekly_{week_str}|本周周报]]
> - [[技术收敛_{date_str[:7]}|本月技术收敛]]
> - [[4_AI情报洞察/技术洞察/多卡协同/多卡极致推理系统技术规划报告---以终为始版|多卡协同技术洞察]]
"""

        report = Report(
            title=f"📡 前沿科技简报 · {date_str}",
            content=content,
            report_type="daily",
            period=date_str
        )

        for event in events[:10]:
            report.add_event(event.id)

        report.trends = {
            'events_count': len(events),
            'by_category': {cat: len(es) for cat, es in events_by_category.items()}
        }

        self.store.save_report(report)
        logger.log_metric('reports_generated', 1)

        return report

    def generate_weekly_evolution_report(self, events: List[TechEvent] = None) -> Report:
        """生成周度技术演化报告"""
        if not events:
            events = self.store.get_recent_events(days=7, limit=200)

        if not events:
            return Report(
                title="周度技术演化报告 - 无数据",
                content="本周无新的技术事件记录。",
                report_type="weekly",
                period=self._get_week_period()
            )

        events = self._filter_ai_events(events)

        week_str = self._get_week_period()

        events_by_category = {}
        for event in events:
            cat = self._categorize_event(event)
            if cat not in events_by_category:
                events_by_category[cat] = []
            events_by_category[cat].append(event)

        content = f"""📡 前沿科技简报 · {week_str} 周报

## 本周技术主线

本周共记录 {len(events)} 条技术事件，分类分布：
"""

        for cat, events in sorted(events_by_category.items(), key=lambda x: len(x[1]), reverse=True):
            content += f"- {cat}: {len(events)} 条\n"

        order_map = {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}
        content += "\n## 🔥 热点事件\n"
        hot_events = sorted(events, key=lambda e: (order_map.get(getattr(e, 'importance', 'P2') or 'P2', 3), getattr(e, 'created_at', '')))[:5]
        for event in hot_events:
            entry = self._build_brief_entry(event)
            content += entry + "\n\n"

        content += "## 💡 热点技术\n"
        tech_events = [e for e in events if 'model' in getattr(e, 'title', '').lower() or 'paper' in getattr(e, 'title', '').lower()][:5]
        for event in tech_events:
            entry = self._build_brief_entry(event)
            content += entry + "\n\n"

        content += "## 📊 热点方向\n"
        for cat, cat_events in list(events_by_category.items())[:3]:
            content += f"### {cat}\n"
            for event in cat_events[:2]:
                entry = self._build_brief_entry(event)
                content += entry + "\n\n"

        content += """## 深读推荐

本周深读论文：
"""
        for event in events[:3]:
            title = getattr(event, 'title', 'Unknown')[:80]
            url = getattr(event, 'url', '')
            content += f"- {title}\n  来源: {url}\n"

        content += f"""
---
📌 文末汇总
- 本周最值得深读: {'; '.join([getattr(e, 'title', 'Unknown')[:50] for e in events[:2]])}
- 本周可跳过: 无
- 下周重点关注: 推理框架新版本、Agent架构演进、成本优化技术
"""

        report = Report(
            title=f"📡 前沿科技简报 · {week_str} 周报",
            content=content,
            report_type="weekly",
            period=week_str
        )

        report.trends = {
            'events_count': len(events),
            'by_category': events_by_category,
            'by_type': self._count_by_type(events)
        }

        for event in events:
            report.add_event(event.id)

        self.store.save_report(report)
        logger.log_metric('reports_generated', 1)

        return report

    def generate_convergence_report(self) -> Report:
        """生成技术收敛报告"""
        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            self.trend_engine = TrendEngine(self.store)

        converging = self.trend_engine.get_converging_techs(days=30)
        production_ready = self.trend_engine.get_production_ready(days=14)

        date_str = datetime.now().strftime('%Y-%m')

        content = f"""📡 技术收敛报告 · {date_str}

## 技术收敛概览

本周观察到以下技术正在收敛：

"""

        if converging:
            for t in converging[:5]:
                content += f"""### {t['tech']}
- **活跃度**: {t['current_activity']} 条事件/周 (比率 {t['activity_ratio']})
- **阶段**: {t['stage']}
- **分析**: 技术迭代正在放缓，标准趋于统一

"""
        else:
            content += "无明显收敛中的技术。\n"

        content += """
## 生产就绪技术

"""
        if production_ready:
            for p in production_ready[:5]:
                content += f"""### {p['project']}
- **事件数**: {p['events_count']}
- **正式Release**: {'是' if p['has_release'] else '否'}
- **热度**: {p['heat_score']}

"""
        else:
            content += "无生产就绪技术。\n"

        content += """## 战略建议

1. **关注收敛技术**: 技术收敛意味着生态稳定，可以考虑投入
2. **评估生产就绪**: 有正式Release的技术可考虑小规模试点
3. **避免过早投入**: 仍在快速迭代的技术不适合大规模投入

"""

        report = Report(
            title=f"📡 技术收敛报告 · {date_str}",
            content=content,
            report_type="convergence",
            period=date_str
        )

        report.trends = {
            'converging': [t['tech'] for t in converging],
            'production_ready': [p['project'] for p in production_ready]
        }

        self.store.save_report(report)
        logger.log_metric('reports_generated', 1)

        return report

    def generate_company_strategy_report(self, company: str) -> Report:
        """生成公司战略分析报告"""
        company_lower = company.lower()

        events = self.store.get_recent_events(days=30, limit=100)
        company_events = [
            e for e in events
            if company_lower in (getattr(e, 'entity', '') or '').lower()
            or company_lower in (getattr(e, 'title', '') or '').lower()
            or company_lower in (getattr(e, 'company', '') or '').lower()
        ]

        if not company_events:
            return Report(
                title=f"{company} 战略分析 - 无数据",
                content=f"近期无 {company} 相关技术事件记录。",
                report_type="company_strategy",
                period=datetime.now().strftime('%Y-%m')
            )

        content = f"""📡 {company} 战略分析 · {datetime.now().strftime('%Y-%m')}

## 技术布局概览

{company} 近期有 {len(company_events)} 条相关技术事件。

"""

        for event in company_events[:5]:
            entry = self._build_brief_entry(event)
            content += entry + "\n\n"

        content += """
## 关键动作分析

"""
        releases = [e for e in company_events if 'release' in getattr(e, 'title', '').lower()]
        if releases:
            content += f"本周有 {len(releases)} 个Release:\n"
            for r in releases[:3]:
                content += f"- {getattr(r, 'title', 'Unknown')}\n"

        content += """
## 竞争态势

"""
        content += f"{company} 在AI领域持续投入，重点方向包括：\n"
        for cat, count in self._count_by_category(company_events).items():
            content += f"- {cat}: {count} 条\n"

        content += """
## 短期预测

1. 预计将继续发布新版本或新模型
2. 重点投入方向可能集中在推理优化或Agent架构
3. 关注与云服务商的合作动态

"""

        report = Report(
            title=f"📡 {company} 战略分析 · {datetime.now().strftime('%Y-%m')}",
            content=content,
            report_type="company_strategy",
            period=datetime.now().strftime('%Y-%m')
        )

        for event in company_events:
            report.add_event(event.id)

        self.store.save_report(report)
        logger.log_metric('reports_generated', 1)

        return report

    def generate_tech_roadmap(self, tech_area: str) -> Report:
        """生成技术路线图"""
        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            self.trend_engine = TrendEngine(self.store)

        evolution = self.trend_engine.get_evolution_chain(tech_area)

        content = f"""📡 {tech_area} 技术路线图 · {datetime.now().strftime('%Y-%m')}

## 技术概览

{tech_area} 是当前AI基础设施的重要方向。

## 发展阶段

"""

        for e in evolution.get('evolution', []):
            content += f"- **{e['stage']}**: {e['count']} 条事件 ({e['first_seen'][:10]} ~ {e['last_seen'][:10]})\n"

        content += f"""
当前阶段: {evolution.get('current_stage', 'unknown')}
总事件数: {evolution.get('total_events', 0)}

## 发展趋势

### 短期(1-3个月)
- 技术将继续快速迭代
- 新版本/新实现持续发布

### 中期(3-6个月)
- 部分技术可能进入收敛阶段
- 生产级应用将逐步落地

## 战略建议

1. 密切关注头部项目动态
2. 评估技术成熟度后再大规模投入
3. 关注社区生态和文档完善程度

"""

        report = Report(
            title=f"📡 {tech_area} 技术路线图",
            content=content,
            report_type="tech_roadmap",
            period=datetime.now().strftime('%Y-%m')
        )

        report.trends = evolution

        self.store.save_report(report)
        logger.log_metric('reports_generated', 1)

        return report

    def _count_by_type(self, events: List[TechEvent]) -> Dict:
        """统计事件类型分布"""
        counts = {}
        for event in events:
            et = getattr(event, 'event_type', 'unknown') if event else 'unknown'
            counts[et] = counts.get(et, 0) + 1
        return counts

    def _count_by_category(self, events: List[TechEvent]) -> Dict:
        """统计事件分类分布"""
        counts = {}
        for event in events:
            cat = self._categorize_event(event)
            counts[cat] = counts.get(cat, 0) + 1
        return counts

    def _get_week_period(self) -> str:
        """获取当前周 period"""
        today = datetime.now()
        week_num = today.isocalendar()[1]
        return f"{today.year}-W{week_num:02d}"

    def save_report(self, report: Report, output_dir: str = None) -> str:
        """保存报告到文件"""
        if not output_dir:
            output_dir = os.path.join(
                os.path.dirname(__file__), '..', '..', 'reports'
            )
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{report.report_type}_{report.period}_{report.id}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Title: {report.title}\n")
            f.write(f"Type: {report.report_type}\n")
            f.write(f"Period: {report.period}\n")
            f.write(f"Created: {report.created_at}\n")
            f.write(f"Events: {len(report.events)}\n")
            f.write("\n" + "=" * 60 + "\n\n")
            f.write(report.content)

        return filepath