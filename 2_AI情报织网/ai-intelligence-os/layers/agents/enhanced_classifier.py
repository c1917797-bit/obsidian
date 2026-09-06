"""
Enhanced Classifier Agent - 优化版分类层
改进：
1. 规则优先，减少LLM调用
2. 智能缓存相同来源的分类结果
3. 批量处理减少开销
4. 更精确的P0/P1分类
"""
import os
import json
from datetime import datetime
from typing import List, Dict, Optional, Set
from collections import defaultdict

from core.models import Signal, TechEvent
from core.storage import UnifiedStore
from core.logger import get_logger

logger = get_logger("EnhancedClassifier")


CLASSIFIER_CACHE = {}


class EnhancedClassifier:
    """
    增强版分类器
    策略：规则为主，LLM为辅
    - 高优先级来源 → LLM增强
    - 低优先级来源 → 纯规则
    - 缓存避免重复LLM调用
    """

    HIGH_PRIORITY_SOURCES = {
        'HuggingFace Papers', 'arXiv', 'Google DeepMind Blog', 'OpenAI Blog',
        'Anthropic News', 'DeepMind', 'TechCrunch', '量子位', '机器之心',
        'vllm', 'sglang', 'autogen', 'langchain', 'dspy'
    }

    TECH_KEYWORDS = {
        'speculative_decoding': ['speculative', 'specdec', 'decoding', 'eagle', 'medusa', 'hydra', 'lookahead'],
        'kv_cache': ['kv cache', 'pagedattention', 'flashinfer', 'paged', 'cache'],
        'flash_attention': ['flash attention', 'flashattn', 'flash-attn', 'fa3', 'fa2'],
        'quantization': ['quantize', 'quantization', 'int8', 'fp8', 'nf4', 'awq', 'gptq', 'quark'],
        'moe': ['moe', 'mixture of experts', 'mixtral', 'deepseek-moe', 'expert'],
        'multi_agent': ['multi-agent', 'multi agent', 'multiagent', 'agent collaboration'],
        'tool_use': ['tool use', 'tool calling', 'function calling', 'tool_calling'],
        'long_context': ['long context', '1m context', '1m token', '百万 token', 'extended context'],
        'reasoning': ['reasoning', 'chain-of-thought', 'cot', 'thinking', 'reasoner'],
        'agentic': ['agentic', 'agentic ai', '代理式'],
        'mcp': ['mcp', 'model context protocol', 'modelcontextprotocol'],
        'memory': ['memory', 'persistent memory', 'session memory'],
        'batch': ['batch', 'batching', 'continuous batching', 'iteration'],
        'serving': ['serving', 'inference', 'deployment', 'production']
    }

    COMPANY_KEYWORDS = {
        'OpenAI': ['openai', 'gpt', 'chatgpt'],
        'Anthropic': ['anthropic', 'claude', 'artificial'],
        'DeepSeek': ['deepseek', 'deep seek'],
        'Google': ['google', 'gemini', 'deepmind', 'alphabet'],
        'Meta': ['meta', 'llama', 'facebook'],
        'Microsoft': ['microsoft', 'azure', 'bing'],
        'NVIDIA': ['nvidia', 'cuda', 'gpu', 'h100', 'h200'],
        'Mistral': ['mistral', 'mixtral'],
        'vllm': ['vllm', 'v LLm'],
        'SGLang': ['sglang', 'sgl-project'],
        'HuggingFace': ['huggingface', 'hf ', 'transformers'],
        'Cohere': ['cohere'],
        'xAI': ['xai', 'x.ai', 'grok']
    }

    def __init__(self, store: UnifiedStore = None):
        self.store = store or UnifiedStore()
        self.stats = {'classified': 0, 'llm_used': 0, 'cached': 0}

    def classify(self, signal: Signal) -> TechEvent:
        """分类单个信号"""
        cache_key = f"{signal.source_id}:{signal.title[:50]}"

        if cache_key in CLASSIFIER_CACHE:
            cached = CLASSIFIER_CACHE[cache_key].copy()
            cached['id'] = signal.id
            return TechEvent.from_signal(signal, cached)

        result = self._classify_rule_based(signal)

        if signal.source in self.HIGH_PRIORITY_SOURCES and len(signal.summary) > 100:
            try:
                llm_result = self._classify_with_llm(signal)
                if llm_result:
                    result.update(llm_result)
                    self.stats['llm_used'] += 1
            except Exception as e:
                logger.debug(f"LLM fallback: {e}")

        CLASSIFIER_CACHE[cache_key] = result.copy()
        self.stats['classified'] += 1

        return TechEvent.from_signal(signal, result)

    def _classify_rule_based(self, signal: Signal) -> Dict:
        """基于规则的快速分类"""
        title = signal.title.lower()
        summary = signal.summary.lower()
        source = signal.source.lower()
        text = f"{title} {summary}"

        event_type = 'runtime_feature'
        tech_categories = ['research', 'general']
        importance = 'P2'
        stage = 'growing'
        entity = signal.source

        if any(k in text for k in ['release', 'launch', 'announce', 'unveil', 'introduce']):
            event_type = 'product_announcement'
            importance = 'P0' if signal.source in self.HIGH_PRIORITY_SOURCES else 'P1'

        if any(k in text for k in ['paper', 'arxiv', 'research', 'study', ' preprint']):
            event_type = 'research_paper'
            tech_categories = ['research', 'architecture']

        if any(k in text for k in ['benchmark', 'eval', 'leaderboard', 'score']):
            event_type = 'benchmark_update'

        for tech, keywords in self.TECH_KEYWORDS.items():
            if any(k in text for k in keywords):
                tech_categories = ['inference_optimization' if tech in ['speculative_decoding', 'kv_cache', 'flash_attention', 'quantization', 'batch'] else 'agent_runtime']
                tech_categories.append(tech)

                if tech in ['flash_attention', 'quantization', 'moe']:
                    stage = 'converging'
                    importance = 'P1'
                elif tech in ['speculative_decoding', 'kv_cache']:
                    stage = 'peak'
                    importance = 'P0'
                elif tech in ['multi_agent', 'tool_use', 'reasoning']:
                    stage = 'growing'
                    importance = 'P1'
                break

        for company, keywords in self.COMPANY_KEYWORDS.items():
            if any(k in text for k in keywords):
                entity = company
                if importance == 'P2':
                    importance = 'P1'
                break

        return {
            'event_type': event_type,
            'tech_categories': tech_categories[:2],
            'entity': entity,
            'entity_type': 'company' if entity in self.COMPANY_KEYWORDS else 'project',
            'importance': importance,
            'confidence': 0.8 if importance == 'P0' else 0.7,
            'innovation': self._extract_innovation(signal),
            'problem_solved': self._extract_problem(signal),
            'company': entity if entity in self.COMPANY_KEYWORDS else '',
            'stage': stage
        }

    def _classify_with_llm(self, signal: Signal) -> Optional[Dict]:
        """使用LLM增强分类（可选）"""
        try:
            from core.minimax_client import get_client
            client = get_client()

            prompt = f"""分析以下AI技术信息，输出JSON：

标题：{signal.title[:150]}
摘要：{signal.summary[:200]}
来源：{signal.source}

输出：{{"event_type":"runtime_feature|product_announcement|research_paper","tech_category":"inference_optimization|agent_runtime|cost_optimization|research","entity":"公司/项目名","importance":"P0|P1|P2"}}

直接输出JSON。"""

            result = client.chat_json([{"role": "user", "content": prompt}])
            if result and 'event_type' in result:
                return result
        except:
            pass
        return None

    def _extract_innovation(self, signal: Signal) -> str:
        """提取创新点"""
        text = f"{signal.title} {signal.summary}"
        for phrase in ['introduces', 'proposes', 'achieves', 'state-of-the-art', 'new method', 'improves']:
            if phrase.lower() in text.lower():
                sentences = text.split('.')
                for s in sentences:
                    if phrase.lower() in s.lower():
                        return s.strip()[:100]
        return signal.title[:80]

    def _extract_problem(self, signal: Signal) -> str:
        """提取解决的问题"""
        text = f"{signal.title} {signal.summary}"
        for phrase in ['solve', 'address', 'bottleneck', 'challenge', 'problem with']:
            if phrase.lower() in text.lower():
                sentences = text.split('.')
                for s in sentences:
                    if phrase.lower() in s.lower():
                        return s.strip()[:100]
        return ''

    def classify_batch(self, signals: List[Signal]) -> List[TechEvent]:
        """批量分类"""
        events = []
        for signal in signals:
            try:
                event = self.classify(signal)
                events.append(event)
            except Exception as e:
                logger.error(f"Failed to classify {signal.id}: {e}")
                continue

        if events:
            saved = self.store.save_events(events)
            logger.info(f"Saved {saved} events from {len(events)} signals")

        return events

    def get_stats(self) -> Dict:
        """获取分类统计"""
        return self.stats.copy()


def get_enhanced_classifier(store=None) -> EnhancedClassifier:
    """获取增强分类器"""
    return EnhancedClassifier(store=store)