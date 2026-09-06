"""
Quality Gate - 质量门禁层
在报告生成前进行质量检查
参考 Paper-Analysis-Renew 的 quality local-ci 设计
"""
import os
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional

from core.models import TechEvent, Report
from core.storage import UnifiedStore
from core.logger import get_logger

logger = get_logger("QualityGate")

# OFF_TOPIC 关键词 — 匹配到这些关键词的事件会被降级或过滤
OFF_TOPIC_PATTERNS = [
    "老年", "养老", "居家看护", "健康监测",
    "植纤皮革", "环保材料", "可持续材料",
    "融资", "pre-A", "pre-B", "series", "IPO",
    "电动汽车", "电动车", "动力电池",
    "消费电子", "手机发布", "电脑发布",
    "智能家居", "IoT", "智能音箱",
    "游戏", "元宇宙", "VR/AR", "区块链", "NFT",
    "教育", "在线教育", "STEAM教育",
    "医疗", "手术机器人", "制药", "药物发现",
    "农业", "智慧农业", "精准农业",
    "时尚", "服装", "美妆",
    "文旅", "旅游", "酒店", "民宿",
    "招聘", "人事", "职场", "裁员",
    "宏观经济", "GDP", "利率", "通胀",
    "地缘政治", "中美", "关税",
    "地震", "气象", "自然灾害",
]

# Agent/Infra 核心关键词 — 命中这些关键词的事件优先级提升
RELEVANCE_BOOST_PATTERNS = [
    "agent", "multi-agent", "agentic", "tool call", "function call",
    "controller", "planner", "orchestrator", "coordinator",
    "inference", "inference optimization", "kv cache", "vllm", "sglang",
    "tensorrt", "triton", "llama.cpp", "speculative decoding",
    "quantization", "quantize", "distill", "prune", "model compress",
    "llm runtime", "serving", "throughput", "latency", "batch",
    "reasoning model", "chain-of-thought", "cot", "system prompt",
    "reward model", "rlhf", "post-training", "fine-tuning",
    "memory", "context window", "long context", "retrieval",
    "rag", "embedding", "vector search", "chunking",
    "agent protocol", "mcp", "a2a", "agent communication",
    "multi-modal", "vision language", "audio agent", "video generation",
    "llm", "gpt", "claude", "gemini", "deepseek", "qwen",
    "moe", "mixture of experts", "sparse",
    "benchmark", "eval", "agent benchmark", "inference benchmark",
    "safety", "jailbreak", "prompt inject", "alignment",
    "agentic rpa", "browser agent", "computer use", "web agent",
    "build 2026", "microsoft build", "nvidia", "anthropic", "openai",
    "arxiv", "neurips", "icml", "iclr", "acl", "cvpr",
    "kv cache", "prefix cache", "pagedattention",
    "disaggregated", "pd separation", "prefill decode",
]


def _is_off_topic(event: TechEvent) -> bool:
    """判断事件是否明显 OFF_TOPIC（基于关键词匹配，无LLM开销）"""
    text = (
        getattr(event, 'title', '') + ' ' +
        getattr(event, 'summary', '') + ' ' +
        getattr(event, 'entity', '') + ' ' +
        getattr(event, 'source', '') + ' ' +
        getattr(event, 'innovation', '') + ' ' +
        getattr(event, 'problem_solved', '')
    ).lower()

    for pattern in OFF_TOPIC_PATTERNS:
        if pattern.lower() in text:
            return True

    has_relevance = any(kw.lower() in text for kw in RELEVANCE_BOOST_PATTERNS)
    entity = getattr(event, 'entity', '') or ''
    ai_entities = ['openai', 'anthropic', 'google', 'meta', 'nvidia', 'microsoft',
                  'deepseek', 'mistral', 'cohere', 'hugging face', 'stability ai',
                  'xai', 'apple', 'amazon', 'byteDance', 'tencent', 'alibaba', 'baidu',
                  'huawei', 'bytedance', 'tencent', 'baidu', 'kimi', 'minimax',
                  'zhipu', 'stepfun', '01ai', 'qwen']
    is_ai_entity = any(e.lower() in entity.lower() for e in ai_entities if e)

    if not has_relevance and not is_ai_entity:
        return True

    return False


class QualityGate:
    """
    质量门禁
    在报告生成前检查数据质量和完整性
    """

    def __init__(self, store: UnifiedStore = None):
        self.store = store or UnifiedStore()
        self.min_events_threshold = 3   # 降低门槛：OFF_TOPIC过滤后仍保证足够候选
        self.min_signal_threshold = 10
        self.max_event_age_days = 3
        # 加载关键词列表（用于评分）
        self._boost_keywords = RELEVANCE_BOOST_PATTERNS
        self._offtopic_keywords = OFF_TOPIC_PATTERNS

    def check_events_quality(self, events: List[TechEvent]) -> Tuple[bool, Dict]:
        """
        检查事件质量
        返回: (是否通过, 检查结果详情)
        """
        results = {
            'total_events': len(events),
            'fresh_events': 0,
            'high_priority_events': 0,
            'diversity_score': 0,
            'issues': []
        }

        if len(events) < self.min_events_threshold:
            results['issues'].append(f"事件数量不足: {len(events)} < {self.min_events_threshold}")

        now = datetime.now()
        fresh_count = 0
        high_priority_count = 0
        entities = set()
        event_types = set()

        for event in events:
            try:
                event_time = datetime.fromisoformat(event.time)
                age = (now - event_time).total_seconds() / 86400

                if age <= self.max_event_age_days:
                    fresh_count += 1

                if hasattr(event, 'importance') and event.importance in ['P0', 'P1']:
                    high_priority_count += 1

                if hasattr(event, 'entity') and event.entity:
                    entities.add(event.entity)

                if hasattr(event, 'event_type') and event.event_type:
                    event_types.add(event.event_type)

            except:
                pass

        results['fresh_events'] = fresh_count
        results['high_priority_events'] = high_priority_count
        results['diversity_score'] = len(entities) / max(len(events), 1)

        if fresh_count < 3:
            results['issues'].append(f"新鲜事件不足: {fresh_count} < 3")

        if len(event_types) < 2:
            results['issues'].append(f"事件类型单一: 只有 {len(event_types)} 种类型")

        passed = len(results['issues']) == 0

        logger.info(f"Quality check: {'PASSED' if passed else 'FAILED'}", issues=len(results['issues']))
        return passed, results

    def check_signals_quality(self, signals_count: int) -> Tuple[bool, Dict]:
        """
        检查信号质量
        """
        results = {
            'signal_count': signals_count,
            'threshold': self.min_signal_threshold,
            'issues': []
        }

        if signals_count < self.min_signal_threshold:
            results['issues'].append(f"信号数量不足: {signals_count} < {self.min_signal_threshold}")

        passed = len(results['issues']) == 0
        return passed, results

    def check_source_health(self) -> Tuple[bool, Dict]:
        """
        检查信源健康状态
        """
        sources = self.store.get_enabled_sources() if hasattr(self.store, 'get_enabled_sources') else []

        results = {
            'total_sources': len(sources),
            'healthy_sources': 0,
            'failed_sources': 0,
            'issues': []
        }

        # 首次运行：信源表尚未初始化，不算失败
        if len(sources) == 0:
            results['message'] = '信源未初始化（首次运行），跳过健康检查'
            return True, results

        for source in sources:
            last_success = source.get('last_success')
            error_count = source.get('error_count', 0)

            if error_count > 5:
                results['failed_sources'] += 1
            else:
                results['healthy_sources'] += 1

        if results['failed_sources'] > len(sources) * 0.5:
            results['issues'].append(f"超过50%的信源失败: {results['failed_sources']}/{len(sources)}")

        passed = len(results['issues']) == 0 and results['healthy_sources'] >= 3
        return passed, results

    def run_quality_gates(self, events: List[TechEvent] = None, signals_count: int = 0) -> Tuple[bool, Dict]:
        """
        运行所有质量门禁
        返回: (是否通过所有检查, 详细结果)
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'event_check': {'passed': False, 'details': {}},
            'signal_check': {'passed': False, 'details': {}},
            'source_check': {'passed': False, 'details': {}},
            'overall_passed': False,
            'recommendations': []
        }

        # === 相关性过滤：移除 OFF_TOPIC 内容 ===
        original_count = len(events) if events else 0
        if events:
            before_filter = len(events)
            events = [e for e in events if not _is_off_topic(e)]
            filtered_count = before_filter - len(events)
            if filtered_count > 0:
                logger.info(f"[QualityGate] 过滤 OFF_TOPIC 事件: {filtered_count}/{before_filter} 条，剩余 {len(events)} 条")

        if events:
            before_filter = len(events)
            events = [e for e in events if not _is_off_topic(e)]
            filtered_count = before_filter - len(events)
            if filtered_count > 0:
                logger.info(f'[QualityGate] OFF_TOPIC过滤: {filtered_count}/{before_filter}条移除，剩余{len(events)}条')
            results['event_check']['details']['off_topic_filtered'] = filtered_count
            results['event_check']['details']['original_count'] = before_filter

        if events:
            # === Agent/Infra 相关性评分：命中的事件优先级提升 ===
            for event in events:
                text = (
                    getattr(event, 'title', '') + ' ' +
                    getattr(event, 'summary', '') + ' ' +
                    getattr(event, 'entity', '') + ' ' +
                    getattr(event, 'innovation', '') + ' ' +
                    getattr(event, 'problem_solved', '')
                ).lower()
                boost = sum(1 for kw in self._boost_keywords if kw.lower() in text)
                # 将 boost 写入 event 的内部评分属性（供后续排序使用）
                event._relevance_boost = boost

            # 按 (importance级别, -relevance_boost, 时间) 排序，确保最相关的事件排前面
            priority_order = {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}
            events = sorted(events, key=lambda e: (
                priority_order.get(getattr(e, 'importance', 'P2') or 'P2', 2),
                -getattr(e, '_relevance_boost', 0),
                getattr(e, 'time', '')
            ))

            event_passed, event_details = self.check_events_quality(events)
            results['event_check'] = {'passed': event_passed, 'details': event_details}
            results['event_check']['details']['original_count'] = original_count
            results['event_check']['details']['off_topic_filtered'] = original_count - len(events) if events else original_count
        elif original_count > 0:
            # 所有事件都被过滤掉了
            results['event_check'] = {
                'passed': False,
                'details': {
                    'total_events': 0,
                    'original_count': original_count,
                    'off_topic_filtered': original_count,
                    'issues': [f'所有事件({original_count}条)均被判定为 OFF_TOPIC，请检查信源配置']
                }
            }

        if signals_count > 0:
            signal_passed, signal_details = self.check_signals_quality(signals_count)
            results['signal_check'] = {'passed': signal_passed, 'details': signal_details}

        source_passed, source_details = self.check_source_health()
        results['source_check'] = {'passed': source_passed, 'details': source_details}

        # 如果信源数量为0（首次运行，数据库尚未初始化），不视为失败
        if results['source_check']['details'].get('total_sources', 0) == 0:
            results['source_check']['passed'] = True
            results['source_check']['details']['issues'] = []

            results['source_check']['details']['message'] = '信源未初始化，首次运行跳过此检查'

        results['overall_passed'] = (
            results['event_check']['passed'] and
            results['signal_check']['passed'] and
            results['source_check']['passed']
        )

        if not results['event_check']['passed']:
            results['recommendations'].append('事件数量或质量不足，建议等待更多数据')

        if not results['signal_check']['passed']:
            results['recommendations'].append('信号采集不足，检查信源配置')

        if not results['source_check']['passed']:
            results['recommendations'].append('信源健康度不佳，优先处理失败信源')

        return results['overall_passed'], results

    def get_quality_report(self, events: List[TechEvent]) -> str:
        """
        生成质量报告（供LLM分析）
        """
        passed, results = self.run_quality_gates(events)

        report = f"""## 质量门禁报告

**检查时间**: {results['timestamp']}
**总体状态**: {'✅ 通过' if passed else '❌ 未通过'}

### 事件质量检查
- 总事件数: {results['event_check']['details'].get('total_events', 0)}
- 新鲜事件(3天内): {results['event_check']['details'].get('fresh_events', 0)}
- 高优先级事件: {results['event_check']['details'].get('high_priority_events', 0)}
- 多样性得分: {results['event_check']['details'].get('diversity_score', 0):.2f}
- **状态**: {'✅ 通过' if results['event_check']['passed'] else '❌ 未通过'}

### 信号质量检查
- 信号总数: {results['signal_check']['details'].get('signal_count', 0)}
- 阈值: {results['signal_check']['details'].get('threshold', 0)}
- **状态**: {'✅ 通过' if results['signal_check']['passed'] else '❌ 未通过'}

### 信源健康检查
- 总信源数: {results['source_check']['details'].get('total_sources', 0)}
- 健康信源: {results['source_check']['details'].get('healthy_sources', 0)}
- 失败信源: {results['source_check']['details'].get('failed_sources', 0)}
- **状态**: {'✅ 通过' if results['source_check']['passed'] else '❌ 未通过'}

### 问题列表
"""
        if results['event_check']['details'].get('issues'):
            for issue in results['event_check']['details']['issues']:
                report += f"- {issue}\n"

        if results['signal_check']['details'].get('issues'):
            for issue in results['signal_check']['details']['issues']:
                report += f"- {issue}\n"

        if results['source_check']['details'].get('issues'):
            for issue in results['source_check']['details']['issues']:
                report += f"- {issue}\n"

        report += "\n### 建议\n"
        if results['recommendations']:
            for rec in results['recommendations']:
                report += f"- {rec}\n"
        else:
            report += "- 数据质量良好，可以生成报告\n"

        return report