"""
Classifier Agent - 分类与Enrichment层
对原始信号进行分类、打标、评分
"""
import os
import json
from datetime import datetime
from typing import List, Dict, Optional, Any, Tuple

from core.models import Signal, TechEvent, EventType, Importance, ContentType, TechStage
from core.storage import UnifiedStore
from core.logger import get_logger
from core.minimax_client import get_client

logger = get_logger("ClassifierAgent")

TECH_ONTOLOGY = {
    "inference_optimization": {
        "description": "推理性能优化技术",
        "subcategories": {
            "speculative_decoding": {"description": "投机解码", "stage": "peak"},
            "kv_cache": {"description": "KV Cache优化", "stage": "peak"},
            "flash_attention": {"description": "Flash Attention系列", "stage": "converging"},
            "quantization": {"description": "模型量化", "stage": "converging"},
            "batch_optimization": {"description": "批处理优化", "stage": "growing"},
            "pruning": {"description": "模型剪枝", "stage": "mature"}
        }
    },
    "agent_runtime": {
        "description": "Agent运行时技术",
        "subcategories": {
            "multi_agent": {"description": "多Agent协作", "stage": "growing"},
            "tool_use": {"description": "工具使用", "stage": "peak"},
            "reasoning": {"description": "推理能力", "stage": "growing"},
            "memory": {"description": "记忆系统", "stage": "emerging"},
            "session_management": {"description": "会话管理", "stage": "peak"}
        }
    },
    "cost_optimization": {
        "description": "成本与效率优化",
        "subcategories": {
            "moe": {"description": "混合专家模型", "stage": "peak"},
            "distillation": {"description": "模型蒸馏", "stage": "mature"},
            "compile_optimization": {"description": "编译优化", "stage": "growing"}
        }
    },
    "research": {
        "description": "基础研究",
        "subcategories": {
            "architecture": {"description": "模型架构", "stage": "growing"},
            "training": {"description": "训练方法", "stage": "growing"},
            "evaluation": {"description": "评测方法", "stage": "emerging"}
        }
    },
    "industry": {
        "description": "产业动态",
        "subcategories": {
            "product_launch": {"description": "产品发布", "stage": "growing"},
            "funding": {"description": "融资动态", "stage": "growing"},
            "partnership": {"description": "合作并购", "stage": "emerging"}
        }
    }
}

KNOWN_COMPANIES = [
    'OpenAI', 'Anthropic', 'DeepSeek', 'Google', 'Meta', 'Microsoft',
    'NVIDIA', 'Amazon', 'Apple', 'xAI', 'Mistral', 'Cohere',
    'vllm', 'sglang', 'huggingface', 'meta', 'stabilityai'
]

KNOWN_PROJECTS = [
    'vllm', 'sglang', 'tensorrt-llm', 'flash-attention', 'llama.cpp',
    'langchain', 'llamaindex', 'autogen', 'dspy', 'transformers',
    'deepspeed', 'accelerate', 'peft', 'triton'
]

class ClassifierAgent:
    """
    分类Agent
    负责任务：
    1. 对Signal进行分类（event_type, tech_categories）
    2. 提取实体（entity, company）
    3. 评分（importance, confidence, novelty_score）
    4. 生成enrichment数据（innovation, problem_solved）
    """

    def __init__(self, store: UnifiedStore = None, use_llm: bool = True):
        self.store = store or UnifiedStore()
        self.client = get_client() if use_llm else None
        self.use_llm = use_llm
        self.stats = {'classified': 0, 'errors': 0}

    def classify(self, signal: Signal) -> Dict:
        """分类单个信号 - 优先规则，LLM增强"""
        title = signal.title
        summary = signal.summary
        source = signal.source

        # 优先使用规则分类（快速）
        result = self._classify_rule_based(title, summary, source)

        # 只有在信号质量高且有时间预算时才尝试LLM
        if self.use_llm and len(summary) > 100:
            try:
                llm_result = self._classify_with_llm(title, summary, source)
                if llm_result:
                    # LLM结果覆盖规则结果
                    result.update(llm_result)
            except Exception as e:
                # LLM失败不影响规则结果
                pass

        return result

    def _classify_with_llm(self, title: str, summary: str, source: str, timeout: int = 30) -> Optional[Dict]:
        """使用LLM进行分类（带超时）"""
        if not self.client:
            return None

        prompt = f"""分析以下AI技术信号，输出JSON：

标题：{title[:200]}
摘要：{summary[:300]}
来源：{source}

输出格式：
{{"event_type":"runtime_feature|inference_opt|agent_framework|cost_opt|research_paper","tech_categories":["domain","subcategory"],"entity":"实体名","importance":"P0|P1|P2","confidence":0.0-1.0,"innovation":"创新点","problem_solved":"解决的问题"}}

直接输出JSON，不要解释。"""

        messages = [{"role": "user", "content": prompt}]
        try:
            result = self.client.chat_json(messages)
            if result and 'event_type' in result:
                return result
        except Exception as e:
            logger.error(f"LLM classification error: {e}")

        return None

    def _classify_rule_based(self, title: str, summary: str, source: str) -> Dict:
        """基于规则的分类（fallback）"""
        title_lower = (title + summary).lower()

        event_type = 'runtime_feature'
        tech_domain = 'inference_optimization'
        tech_sub = 'runtime_feature'
        importance = 'P1'
        stage = 'growing'

        if any(k in title_lower for k in ['speculative', 'decoding', 'eagle', 'medusa', 'hydra', 'specdec']):
            tech_domain = 'inference_optimization'
            tech_sub = 'speculative_decoding'
            stage = 'peak'
        elif any(k in title_lower for k in ['kv cache', 'pagedattention', 'flashinfer']):
            tech_domain = 'inference_optimization'
            tech_sub = 'kv_cache'
            stage = 'peak'
        elif any(k in title_lower for k in ['flash attention', 'flashattn', 'fa3', 'fa2']):
            tech_domain = 'inference_optimization'
            tech_sub = 'flash_attention'
            stage = 'converging'
        elif any(k in title_lower for k in ['quantization', 'quantize', 'int8', 'fp8', 'nf4', 'awq', 'gptq']):
            tech_domain = 'inference_optimization'
            tech_sub = 'quantization'
            stage = 'converging'
        elif any(k in title_lower for k in ['moe', 'mixture of experts', 'mixtral', 'deepseek-moe']):
            tech_domain = 'cost_optimization'
            tech_sub = 'moe'
            stage = 'peak'
        elif any(k in title_lower for k in ['multi-agent', 'multi agent', 'multiagent', 'collaboration']):
            tech_domain = 'agent_runtime'
            tech_sub = 'multi_agent'
            stage = 'growing'
        elif any(k in title_lower for k in ['tool use', 'tool_calling', 'function calling']):
            tech_domain = 'agent_runtime'
            tech_sub = 'tool_use'
            stage = 'peak'
        elif any(k in title_lower for k in ['memory', 'persistent', 'session']):
            tech_domain = 'agent_runtime'
            tech_sub = 'memory'
            stage = 'emerging'
        elif any(k in title_lower for k in ['arxiv', 'paper', 'research', 'study']):
            event_type = 'research_paper'
            tech_domain = 'research'
            tech_sub = 'architecture'
        elif any(k in title_lower for k in ['benchmark', 'leaderboard', 'eval', 'chatbot arena']):
            event_type = 'benchmark_update'
            tech_domain = 'research'
            tech_sub = 'evaluation'
        elif any(k in title_lower for k in ['release', 'launch', 'announce']):
            event_type = 'product_announcement'
            tech_domain = 'industry'
            tech_sub = 'product_launch'
            importance = 'P0'

        entity = self._extract_entity(title, source)
        company = self._extract_company(title)

        return {
            'event_type': event_type,
            'tech_categories': [tech_domain, tech_sub],
            'entity': entity,
            'entity_type': 'project' if entity.lower() in [p.lower() for p in KNOWN_PROJECTS] else 'project',
            'importance': importance,
            'confidence': 0.6,
            'innovation': self._extract_innovation(title, summary),
            'problem_solved': self._extract_problem(title, summary),
            'company': company,
            'stage': stage
        }

    def _extract_entity(self, title: str, source: str) -> str:
        """提取实体"""
        title_lower = title.lower()
        for proj in KNOWN_PROJECTS:
            if proj in title_lower:
                return proj
        return source.split('/')[-1] if '/' in source else source

    def _extract_company(self, title: str) -> str:
        """提取公司名"""
        title_lower = title.lower()
        for comp in ['openai', 'anthropic', 'deepseek', 'google', 'meta', 'microsoft', 'nvidia', 'amazon']:
            if comp in title_lower:
                return comp.capitalize()
        return ''

    def _extract_innovation(self, title: str, summary: str) -> str:
        """提取创新点"""
        text = (title + ' ' + summary)[:300]
        if any(k in text.lower() for k in ['new', 'novel', 'introduce', 'propose', 'improve', 'achieve']):
            return text.split('.')[0][:100]
        return title[:100]

    def _extract_problem(self, title: str, summary: str) -> str:
        """提取解决的问题"""
        text = (title + ' ' + summary)[:300]
        if any(k in text.lower() for k in ['solve', 'address', 'problem', 'bottleneck', 'optimize']):
            for sent in text.split('.'):
                if any(k in sent.lower() for k in ['solve', 'address', 'problem', 'bottleneck']):
                    return sent[:100]
        return ''

    def classify_all(self, signals: List[Signal], use_llm: bool = False) -> List[TechEvent]:
        """
        批量分类
        use_llm: 是否使用LLM增强（默认False，规则优先）
        """
        self.use_llm = use_llm
        events = []
        for i, signal in enumerate(signals):
            try:
                classification = self.classify(signal)
                event = TechEvent.from_signal(signal, classification)
                events.append(event)
                self.stats['classified'] += 1

                # 标记信号已处理
                self.store.mark_signal_processed(signal.id, event.id)

                # 每50条保存一次
                if len(events) >= 50:
                    saved = self.store.save_events(events)
                    logger.info(f"已保存 {saved} 条事件 (进度 {i+1}/{len(signals)})")
                    events = []

            except Exception as e:
                logger.error(f"Failed to classify signal {signal.id}: {e}")
                self.stats['errors'] += 1
                continue

        # 保存剩余的事件
        if events:
            saved = self.store.save_events(events)
            logger.info(f"已保存最后 {saved} 条事件")

        logger.log_metric('classified', self.stats['classified'])
        logger.info(f"分类完成: {self.stats['classified']} 条事件, 错误 {self.stats['errors']} 条")

        return events

    def classify_and_save(self, signals: List[Signal]) -> int:
        """分类并保存到存储"""
        events = self.classify_all(signals)
        return self.store.save_events(events)

    def get_event_type_stats(self, days: int = 7) -> Dict:
        """获取事件类型统计"""
        from datetime import timedelta
        since = (datetime.now() - timedelta(days=days)).isoformat()

        stats = {}
        for et in EventType:
            count = self.store.count_events(event_type=et.value, since=since)
            stats[et.value] = count

        return stats

    def get_importance_distribution(self, days: int = 7) -> Dict:
        """获取重要性分布"""
        from datetime import timedelta
        since = (datetime.now() - timedelta(days=days)).isoformat()

        events = self.store.get_events(since=since, limit=1000)
        distribution = {'P0': 0, 'P1': 0, 'P2': 0, 'P3': 0}

        for event in events:
            imp = event.importance if hasattr(event, 'importance') else 'P1'
            if imp in distribution:
                distribution[imp] += 1

        return distribution