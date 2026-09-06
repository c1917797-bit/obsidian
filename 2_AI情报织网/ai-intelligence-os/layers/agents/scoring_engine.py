"""
Scoring Engine - 技术信号评分与过滤
基于规则的标签 + 兴趣权重 + 评分排序
实现 Metadata First 架构的第二层和第三层
"""
import re
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from datetime import datetime

from core.logger import get_logger

logger = get_logger("ScoringEngine")


@dataclass
class TechInterestWeights:
    """技术方向兴趣权重配置"""
    agent_runtime: int = 10
    agent_memory: int = 8
    agent_planning: int = 7
    agent_communication: int = 7
    mcp: int = 9
    a2a: int = 7
    multi_agent: int = 8

    kv_cache: int = 10
    prefix_cache: int = 9
    speculative_decoding: int = 9
    moe: int = 7
    quantization: int = 7
    quantization_aware: int = 7
    scheduling: int = 6
    inference_runtime: int = 8
    serving: int = 7
    gpu_kernel: int = 8

    pd_separation: int = 9
    disagg: int = 8
    cache_sharing: int = 8
    rdma: int = 7
    nvlink: int = 7
    distributed_inference: int = 10
    communication_optimization: int = 7
    load_balance: int = 6

    training: int = 2
    fine_tuning: int = 5
    rlhf: int = 5
    alignment: int = 5

    multimodal: int = 6
    vision: int = 5
    image_generation: int = 3
    video_generation: int = 4
    tts: int = 3

    paper: int = 4
    benchmark: int = 5
    opensource: int = 6
    release: int = 5


TECH_TAGS = {
    'Agent Runtime': ['agent runtime', 'agentic', 'agent system', 'runtime', 'execution'],
    'Agent Memory': ['agent memory', 'context management', 'session', 'memory', 'retrieval'],
    'Agent Planning': ['agent planning', 'task planning', 'reasoning', 'plan', 'reflect'],
    'Agent Communication': ['agent communication', 'a2a', 'agent to agent', 'multi-agent'],
    'MCP': ['mcp', 'model context protocol', 'anthropic mcp', 'mcp server'],
    'A2A': ['a2a protocol', 'agent to agent'],
    'Multi-Agent': ['multi-agent', 'multi agent', 'agent collaboration', 'agent swarm'],

    'KV Cache': ['kv cache', 'kvcache', 'kv-cache', 'pagedattention', 'paged attention'],
    'Prefix Cache': ['prefix cache', 'prefix caching', 'cache'],
    'Speculative Decoding': ['speculative', 'specdec', 'speculative decoding', 'draft model', 'medusa', 'eagle', 'lookahead'],
    'MoE': ['moe', 'mixture of experts', 'mixtral', 'deepseek moe', 'expert'],
    'Quantization': ['quantize', 'quantization', 'quant', 'int8', 'int4', 'fp8', 'awq', 'gptq', 'gguf'],
    'Quantization-Aware': ['qat', 'quantization aware'],
    'Scheduling': ['schedule', 'scheduling', 'batch', 'continuous batching', 'prefix batching'],
    'Inference Runtime': ['inference', 'serving', 'llm inference', 'inference engine'],
    'GPU Kernel': ['kernel', 'cuda', 'triton', 'flashattention', 'flash attention', 'kernel fusion'],
    'vLLM': ['vllm', 'v_l_l_m'],
    'SGLang': ['sglang', 'sgl'],
    'TensorRT': ['tensorrt', 'trt', 'trt-llm'],
    'llama.cpp': ['llama.cpp', 'llama-cpp', 'gguf'],

    'PD Separation': ['prefill', 'decode', 'pd separation', 'prefill_decode', ' disaggregat'],
    'Disaggregation': ['disaggregation', 'disaggregate', 'prefill decode'],
    'Cache Sharing': ['cache sharing', 'shared cache', 'cross requests'],
    'RDMA': ['rdma', 'remote direct memory'],
    'NVLink': ['nvlink', 'nv link'],
    'Distributed Inference': ['distributed', 'multi-gpu', 'tensor parallel', 'pipeline parallel', 'data parallel'],
    'Communication': ['nccl', 'communication', 'allreduce', 'allgather'],
    'Load Balance': ['load balance', 'load balancing', 'request distribution'],

    'Training': ['training', 'train', 'pretrain', 'pre-training'],
    'Fine-tuning': ['fine-tune', 'finetune', 'fine tuning', 'lora', 'rlora', 'adalora'],
    'RLHF': ['rlhf', 'reward model', 'reinforcement learning', 'ppo', 'dpo'],
    'Alignment': ['alignment', 'safety', 'rlhf', 'constitutional'],

    'Multimodal': ['multimodal', 'multi-modal', 'vision language', 'vlmodel'],
    'Vision': ['computer vision', 'cv', 'image understand'],
    'Image Generation': ['image generation', 'stable diffusion', 'sdxl', 'flux', 'image gen'],
    'Video Generation': ['video generation', 'sora', 'video gen', 'runway', 'kling'],
    'TTS': ['tts', 'text to speech', 'voice synthesis'],

    'Paper': ['paper', 'arxiv', 'research', 'study', 'acl', 'cvpr', 'neurips', 'icml', 'iclr', 'emnlp'],
    'Benchmark': ['benchmark', 'eval', 'evaluation', 'leaderboard', 'mt-bench', 'humaneval', 'mmlu'],
    'OpenSource': ['open source', 'opensource', 'open-source', 'github', 'release', 'released'],
    'Product Launch': ['launch', 'announce', 'release', 'unveil', 'debut', 'new model', 'new feature'],
}


PROBLEM_TAGS = {
    'Latency': ['latency', 'delay', 'response time', 'time to first token', 'ttft', '首字', '延迟', '响应速度'],
    'Throughput': ['throughput', 'tokens per second', 'tps', 'qps', 'output speed', '吞吐', '并发', '带宽'],
    'Memory': ['memory', '显存', 'vram', 'gpu memory', 'oom', 'out of memory', 'memory efficiency', '内存'],
    'Scalability': ['scalability', 'scale', 'multi-gpu', 'multi-node', 'distributed', '扩展', '扩展性', '多卡'],
    'Cost': ['cost', 'price', 'cheap', 'expensive', 'compute', 'flops', '费用', '成本', '性价比'],
    'Reliability': ['reliability', 'availability', 'fault tolerance', 'recovery', '可用性', '可靠性', '容错'],
    'Accuracy': ['accuracy', 'quality', 'performance', 'benchmark', 'eval', '评测', '精度', '质量'],
    'Agent-Capability': ['agent', 'capability', 'reasoning', 'planning', 'memory', 'autonomy', '智能体', '能力'],
}

SYSTEM_LAYER_TAGS = {
    'Runtime': ['runtime', 'serving', 'inference engine', 'execution', '运行时', '推理引擎'],
    'Scheduler': ['scheduler', 'scheduling', 'batch', 'queue', '调度', '调度器'],
    'Memory-System': ['memory', 'cache', 'kv cache', '显存', '缓存', '内存管理'],
    'Network': ['network', 'rdma', 'nccl', 'bandwidth', '通信', '网络'],
    'Model': ['model', 'architecture', 'transformer', 'llm', '模型', '架构'],
    'Agent': ['agent', 'multi-agent', 'mcp', 'a2a', '智能体', '多智能体'],
}


@dataclass
class ScoredSignal:
    """带评分的信号"""
    signal_id: str
    title: str
    summary: str
    source: str
    source_id: str
    url: str
    category: str
    priority: str
    published: str
    language: str
    tags: List[str] = field(default_factory=list)
    problem_tags: List[str] = field(default_factory=list)
    layer_tags: List[str] = field(default_factory=list)
    score: float = 0.0
    tag_scores: Dict[str, int] = field(default_factory=dict)
    event_score: float = 0.0
    tech_score: float = 0.0
    trend_score: float = 0.0

    @property
    def title_lower(self) -> str:
        return self.title.lower()


class ScoringEngine:
    """
    评分引擎 - 实现规则标签 + 兴趣权重评分

    流程：
    1. 规则打标签 (无需LLM)
    2. 分维度评分（热点事件/热点技术/行业趋势）
    3. 来源优先级加分
    4. 时效性加分
    5. 返回Top N（每个维度单独排序）
    """

    def __init__(self, weights: TechInterestWeights = None):
        self.weights = weights or TechInterestWeights()
        self._build_tag_keyword_map()

    def _build_tag_keyword_map(self):
        """构建标签 -> 关键词映射（用于快速匹配）"""
        self.tag_keywords = {}
        self.keyword_tags = {}

        for tag, keywords in TECH_TAGS.items():
            self.tag_keywords[tag] = keywords
            for kw in keywords:
                if kw not in self.keyword_tags:
                    self.keyword_tags[kw] = []
                self.keyword_tags[kw].append(tag)

    def _extract_tags(self, title: str, summary: str = '', tags: List[str] = None) -> Dict[str, List[str]]:
        """基于规则提取标签 - 返回三层标签"""
        text = (title + ' ' + (summary or '')).lower()
        result = {
            'tech': set(),
            'problem': set(),
            'layer': set()
        }

        for keyword, tag_list in self.keyword_tags.items():
            if keyword in text:
                for tag in tag_list:
                    result['tech'].add(tag)

        for problem_tag, keywords in PROBLEM_TAGS.items():
            for kw in keywords:
                if kw in text:
                    result['problem'].add(problem_tag)
                    break

        for layer_tag, keywords in SYSTEM_LAYER_TAGS.items():
            for kw in keywords:
                if kw in text:
                    result['layer'].add(layer_tag)
                    break

        if tags:
            for t in tags:
                t_lower = t.lower()
                if t_lower in self.tag_keywords:
                    result['tech'].add(t_lower)

        return result

    def _calculate_tag_score(self, tags: List[str]) -> Dict[str, int]:
        """计算每个标签的得分"""
        scores = {}
        weight_map = {
            'Agent Runtime': self.weights.agent_runtime,
            'Agent Memory': self.weights.agent_memory,
            'Agent Planning': self.weights.agent_planning,
            'Agent Communication': self.weights.agent_communication,
            'MCP': self.weights.mcp,
            'A2A': self.weights.a2a,
            'Multi-Agent': self.weights.multi_agent,
            'KV Cache': self.weights.kv_cache,
            'Prefix Cache': self.weights.prefix_cache,
            'Speculative Decoding': self.weights.speculative_decoding,
            'MoE': self.weights.moe,
            'Quantization': self.weights.quantization,
            'Quantization-Aware': self.weights.quantization_aware,
            'Scheduling': self.weights.scheduling,
            'Inference Runtime': self.weights.inference_runtime,
            'Serving': self.weights.serving,
            'GPU Kernel': self.weights.gpu_kernel,
            'PD Separation': self.weights.pd_separation,
            'Disaggregation': self.weights.disagg,
            'Cache Sharing': self.weights.cache_sharing,
            'RDMA': self.weights.rdma,
            'NVLink': self.weights.nvlink,
            'Distributed Inference': self.weights.distributed_inference,
            'Communication': self.weights.communication_optimization,
            'Load Balance': self.weights.load_balance,
            'Training': self.weights.training,
            'Fine-tuning': self.weights.fine_tuning,
            'RLHF': self.weights.rlhf,
            'Alignment': self.weights.alignment,
            'Multimodal': self.weights.multimodal,
            'Vision': self.weights.vision,
            'Image Generation': self.weights.image_generation,
            'Video Generation': self.weights.video_generation,
            'TTS': self.weights.tts,
            'Paper': self.weights.paper,
            'Benchmark': self.weights.benchmark,
            'OpenSource': self.weights.opensource,
            'Product Launch': self.weights.release,
            'vLLM': 9,
            'SGLang': 9,
            'TensorRT': 8,
            'llama.cpp': 7,
        }

        for tag in tags:
            scores[tag] = weight_map.get(tag, 5)

        return scores

    def _get_source_priority_bonus(self, source: str, source_id: str, category: str, source_type: str = '') -> float:
        """来源优先级加分"""
        source_lower = source.lower()
        source_id_lower = source_id.lower()
        category_lower = category.lower() if category else ''
        source_type_lower = source_type.lower() if source_type else ''

        priority_map = {
            'github': 5,
            'arxiv': 4,
            'huggingface': 4,
            'paper': 4,
            'academic': 4,
            'tech_blog': 6,
            'inference': 6,
            'agent': 6,
            'training': 5,
            'benchmark': 5,
            'social': 7,
            'news': 6,
            'news_cn': 15,  # 中文新闻大幅提高
        }

        bonus = priority_map.get(category_lower, 3)

        # Twitter/社交媒体来源获得更高基础分
        if source_type_lower == 'twitter_rss':
            bonus = max(bonus, 12)
        if 'twitter' in source_id_lower:
            bonus = max(bonus, 12)

        # 中文新闻给予更高基础分
        if category_lower == 'news_cn':
            bonus = max(bonus, 20)
        if any(ns in source for ns in ['量子位', '机器之心', '36kr', '虎嗅', '爱范儿']):
            bonus = max(bonus, 20)

        if 'arxiv' in source_id_lower or 'arxiv' in source_lower:
            bonus = max(bonus, 5)
        if 'github' in source_id_lower or 'github' in source_lower:
            bonus = max(bonus, 5)
        if source_lower in ['vllm', 'sglang', 'deepseek', 'qwen', 'llama.cpp', 'tensorrt']:
            bonus = max(bonus, 7)

        return bonus

    def _get_recency_bonus(self, published: str) -> float:
        """时效性加分 - 近期内容加分"""
        if not published:
            return 1.0

        try:
            if isinstance(published, str):
                dt = datetime.fromisoformat(published.replace('Z', '+00:00'))
            else:
                dt = published

            hours_old = (datetime.now() - dt).total_seconds() / 3600

            if hours_old < 24:
                return 3.0
            elif hours_old < 48:
                return 2.0
            elif hours_old < 72:
                return 1.5
            elif hours_old < 168:
                return 1.0
            else:
                return 0.5
        except:
            return 1.0

    def score_signal(self, signal_dict: Dict) -> ScoredSignal:
        """对单个信号评分"""
        title = signal_dict.get('title', '')
        summary = signal_dict.get('summary', '')
        source = signal_dict.get('source', '')
        source_id = signal_dict.get('source_id', '')
        url = signal_dict.get('url', '')
        category = signal_dict.get('category', '')
        priority = signal_dict.get('priority', 'P1')
        published = signal_dict.get('published', '')
        language = signal_dict.get('language', 'en')
        existing_tags = signal_dict.get('tags', [])
        source_type = signal_dict.get('source_type', '')

        tags = self._extract_tags(title, summary, existing_tags)
        tech_tags = tags['tech']
        problem_tags = tags['problem']
        layer_tags = tags['layer']

        tech_scores = self._calculate_tag_score(list(tech_tags))
        tag_score_sum = sum(tech_scores.values())

        problem_bonus = len(problem_tags) * 3
        layer_bonus = len(layer_tags) * 2

        source_bonus = self._get_source_priority_bonus(source, source_id, category, source_type)
        recency_bonus = self._get_recency_bonus(published)

        priority_map = {'P0': 5, 'P1': 3, 'P2': 1, 'P3': 0}
        priority_bonus = priority_map.get(priority, 2)

        total_score = (tag_score_sum + source_bonus + priority_bonus + problem_bonus + layer_bonus) * recency_bonus

        event_score = self._calculate_event_score(signal_dict, recency_bonus)
        tech_score = self._calculate_tech_score(signal_dict, tech_tags, tag_score_sum, problem_tags, layer_tags, recency_bonus)
        trend_score = self._calculate_trend_score(signal_dict, recency_bonus)

        return ScoredSignal(
            signal_id=signal_dict.get('id', ''),
            title=title,
            summary=summary,
            source=source,
            source_id=source_id,
            url=url,
            category=category,
            priority=priority,
            published=published,
            language=language,
            tags=list(tech_tags),
            problem_tags=list(problem_tags),
            layer_tags=list(layer_tags),
            score=total_score,
            tag_scores={**tech_scores, **{p: 3 for p in problem_tags}, **{l: 2 for l in layer_tags}},
            event_score=event_score,
            tech_score=tech_score,
            trend_score=trend_score
        )

    def _calculate_event_score(self, signal_dict: Dict, recency_bonus: float) -> float:
        """计算热点事件分数 - 基于新闻事件特征（行业/公司动态）"""
        title = signal_dict.get('title', '').lower()
        summary = signal_dict.get('summary', '').lower()
        source = signal_dict.get('source', '').lower()
        category = signal_dict.get('category', '').lower()
        source_type = signal_dict.get('source_type', '').lower()

        score = 0.0
        text = title + ' ' + summary

        event_keywords = [
            'launch', 'release', 'announce', 'unveil', 'debut', 'introduce',
            'acquisition', 'funding', 'raises', 'investment', 'ipo',
            'ceo', 'cto', 'founder', 'hires', 'joins', 'leaves', 'appointed',
            '挖走', '入职', '加盟', '任命', '融资', '收购', '发布', '推出', '重磅',
            '开招', '扩张', '核心岗位', '重返', '进入', '布局'
        ]

        for kw in event_keywords:
            if kw in text:
                score += 5.0

        if category in ['news_cn', 'news'] and not any(k in text for k in ['arxiv', 'paper', 'research', 'study', '论文']):
            score += 15.0
        if source_type == 'twitter_rss':
            score += 10.0
        if any(ns in source for ns in ['量子位', '机器之心', '36kr', 'techcrunch']):
            score += 12.0

        company_in_news = sum(1 for c in ['openai', 'anthropic', 'google', 'meta', 'nvidia', 'amazon', 'microsoft', 'deepseek'] if c in text)
        if company_in_news > 0 and category in ['news_cn', 'news']:
            score += company_in_news * 5.0

        if any(k in text for k in ['arxiv', 'paper', 'research', 'study', '论文', 'iclr', 'neurips', 'icml', 'cvpr']):
            score *= 0.3

        return score * recency_bonus

    def _calculate_tech_score(self, signal_dict: Dict, tech_tags: set, tag_score_sum: float,
                                problem_tags: set, layer_tags: set, recency_bonus: float) -> float:
        """计算热点技术分数 - 基于技术特征（论文、技术突破）"""
        title = signal_dict.get('title', '').lower()
        summary = signal_dict.get('summary', '').lower()
        source_type = signal_dict.get('source_type', '').lower()
        category = signal_dict.get('category', '').lower()

        score = 0.0
        text = title + ' ' + summary

        score += tag_score_sum

        tech_keywords = [
            'agent', 'multi-agent', 'llm', 'inference', 'kv cache', 'speculative',
            'quantization', 'moe', 'mixture', 'attention', 'transformer',
            'benchmark', 'eval', 'leaderboard', 'sota',
            'arxiv', 'paper', 'research', 'study', 'iclr', 'neurips', 'icml', 'cvpr', 'acl', 'emnlp',
            'novel', 'state-of-the-art', 'breakthrough', 'improve', 'propose', 'introduce'
        ]

        for kw in tech_keywords:
            if kw in text:
                score += 3.0

        problem_bonus = len(problem_tags) * 3
        layer_bonus = len(layer_tags) * 2
        score += problem_bonus + layer_bonus

        if 'agent' in tech_tags or 'Agent' in tech_tags:
            score += 5.0
        if 'Inference Runtime' in tech_tags or 'KV Cache' in tech_tags:
            score += 5.0

        if any(k in text for k in ['arxiv', 'paper', 'research', 'huggingface']):
            score *= 1.5

        if source_type == 'atom' or source_type == 'hf_api':
            score *= 1.3

        return score * recency_bonus

    def _calculate_trend_score(self, signal_dict: Dict, recency_bonus: float) -> float:
        """计算行业趋势分数 - 基于行业动态特征（市场、生态、合作伙伴）"""
        title = signal_dict.get('title', '').lower()
        summary = signal_dict.get('summary', '').lower()
        source = signal_dict.get('source', '').lower()
        category = signal_dict.get('category', '').lower()

        score = 0.0
        text = title + ' ' + summary

        if any(k in text for k in ['arxiv', 'paper', 'research', 'study', '论文', 'iclr', 'neurips']):
            score *= 0.3

        trend_keywords = [
            'startup', 'company', 'industry', 'market', 'trend', 'growth', 'adoption',
            'partnership', 'collaboration', 'ecosystem', 'platform', 'integration',
            'enterprise', 'business', 'revenue', 'customer', 'deployment',
            'open source', 'community', 'adoption', 'adopt',
            '合作', '生态', '平台', '市场', '行业', '企业', '部署', '落地'
        ]

        for kw in trend_keywords:
            if kw in text:
                score += 4.0

        if category in ['industry', 'tech_blog']:
            score += 10.0
        if 'github' in source:
            score += 8.0

        company_mentions = sum(1 for c in ['openai', 'anthropic', 'google', 'meta', 'nvidia', 'amazon', 'microsoft', 'deepseek'] if c in text)
        score += company_mentions * 3.0

        return score * recency_bonus

    def score_signals(self, signals: List[Dict], top_n: int = 50) -> List[ScoredSignal]:
        """
        对信号列表评分并排序

        Args:
            signals: 信号字典列表
            top_n: 返回前N条

        Returns:
            排序后的ScoredSignal列表
        """
        if not signals:
            return []

        scored = []
        for sig in signals:
            try:
                scored_sig = self.score_signal(sig)
                scored.append(scored_sig)
            except Exception as e:
                logger.warning(f"Scoring failed for signal: {e}")
                continue

        scored.sort(key=lambda x: x.score, reverse=True)

        logger.info(f"Scored {len(scored)} signals, top score: {scored[0].score if scored else 0:.1f}")

        return scored[:top_n]

    def filter_and_rank(self, signals: List[Dict], min_score: float = 5.0, top_n: int = 50) -> List[ScoredSignal]:
        """
        过滤低分信号并返回Top N

        Args:
            signals: 信号字典列表
            min_score: 最低分数阈值
            top_n: 返回前N条

        Returns:
            高分信号列表
        """
        scored = self.score_signals(signals, top_n=top_n * 2)

        filtered = [s for s in scored if s.score >= min_score]

        filtered.sort(key=lambda x: x.score, reverse=True)

        return filtered[:top_n]

    def get_top_signals(self, signals: List[Dict], top_n: int = 30) -> List[ScoredSignal]:
        """
        获取Top N信号（用于后续LLM处理）

        默认返回Top 30，进入两阶段抓取的高分内容
        """
        return self.score_signals(signals, top_n=top_n)

    def get_top_signals_by_dimension(self, signals: List[Dict], top_n: int = 10) -> Dict[str, List[ScoredSignal]]:
        """
        按维度获取Top N信号

        Returns:
            dict with keys: 'event', 'tech', 'trend'
        """
        scored = self.score_signals(signals, top_n=len(signals))

        events = sorted(scored, key=lambda x: x.event_score, reverse=True)[:top_n]
        techs = sorted(scored, key=lambda x: x.tech_score, reverse=True)[:top_n]
        trends = sorted(scored, key=lambda x: x.trend_score, reverse=True)[:top_n]

        return {
            'event': events,
            'tech': techs,
            'trend': trends
        }

    def explain_score(self, scored_signal: ScoredSignal) -> str:
        """解释评分原因（用于调试）"""
        lines = [
            f"Title: {scored_signal.title[:60]}...",
            f"Score: {scored_signal.score:.1f}",
            f"Tags: {', '.join(scored_signal.tags) or 'None'}",
            f"Tag Scores: {scored_signal.tag_scores}",
            f"Source: {scored_signal.source} ({scored_signal.category})",
            f"Published: {scored_signal.published}",
        ]
        return '\n'.join(lines)
