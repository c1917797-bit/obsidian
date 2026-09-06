"""
Beliefs Evolution System - 自演进认知系统
Learned from Pulsar: https://github.com/sou350121/Pulsar
"""
import os
import json
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum

from core.logger import get_logger

logger = get_logger("BeliefsEvolution")


class BeliefState(Enum):
    """信念状态"""
    EMERGING = "emerging"
    GROWING = "growing"
    CONFIRMED = "confirmed"
    CONVERGING = "converging"
    DECLINING = "declining"
    REJECTED = "rejected"


@dataclass
class Belief:
    """信念"""
    id: str
    concept: str
    state: BeliefState
    confidence: float
    evidence_count: int
    supporting_sources: List[str] = field(default_factory=list)
    opposing_sources: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    first_evidence_at: str = ""
    confirmed_at: str = ""
    notes: str = ""


@dataclass
class BeliefEvidence:
    """证据"""
    id: str
    belief_id: str
    source: str
    evidence_text: str
    polarity: float
    event_id: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class BeliefEvolutionEngine:
    """
    信念演化引擎
    跟踪技术认知的演进过程
    """

    def __init__(self, store=None):
        self.store = store
        self.beliefs: Dict[str, Belief] = {}
        self.evidence: Dict[str, List[BeliefEvidence]] = {}
        self._load_beliefs()

    def _beliefs_file_path(self) -> str:
        """获取信念存储文件路径"""
        data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        return os.path.join(data_dir, 'beliefs_evolution.json')

    def _load_beliefs(self):
        """从文件加载信念"""
        filepath = self._beliefs_file_path()
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.beliefs = {}
            for b_data in data.get('beliefs', []):
                state = BeliefState(b_data['state'])
                belief = Belief(
                    id=b_data['id'],
                    concept=b_data['concept'],
                    state=state,
                    confidence=b_data['confidence'],
                    evidence_count=b_data['evidence_count'],
                    supporting_sources=b_data.get('supporting_sources', []),
                    opposing_sources=b_data.get('opposing_sources', []),
                    created_at=b_data['created_at'],
                    updated_at=b_data['updated_at'],
                    first_evidence_at=b_data.get('first_evidence_at', ''),
                    confirmed_at=b_data.get('confirmed_at', ''),
                    notes=b_data.get('notes', '')
                )
                self.beliefs[belief.id] = belief

            self.evidence = {}
            for ev_data in data.get('evidence', []):
                evidence = BeliefEvidence(
                    id=ev_data['id'],
                    belief_id=ev_data['belief_id'],
                    source=ev_data['source'],
                    evidence_text=ev_data['evidence_text'],
                    polarity=ev_data['polarity'],
                    event_id=ev_data['event_id'],
                    created_at=ev_data['created_at']
                )
                if evidence.belief_id not in self.evidence:
                    self.evidence[evidence.belief_id] = []
                self.evidence[evidence.belief_id].append(evidence)

            logger.info(f"Loaded {len(self.beliefs)} beliefs, {len(self.evidence)} evidence items")

        except Exception as e:
            logger.error(f"Failed to load beliefs: {e}")

    def _save_beliefs(self):
        """保存信念到文件"""
        filepath = self._beliefs_file_path()

        data = {
            'beliefs': [
                {
                    'id': b.id,
                    'concept': b.concept,
                    'state': b.state.value,
                    'confidence': b.confidence,
                    'evidence_count': b.evidence_count,
                    'supporting_sources': b.supporting_sources,
                    'opposing_sources': b.opposing_sources,
                    'created_at': b.created_at,
                    'updated_at': b.updated_at,
                    'first_evidence_at': b.first_evidence_at,
                    'confirmed_at': b.confirmed_at,
                    'notes': b.notes
                }
                for b in self.beliefs.values()
            ],
            'evidence': [
                {
                    'id': ev.id,
                    'belief_id': ev.belief_id,
                    'source': ev.source,
                    'evidence_text': ev.evidence_text,
                    'polarity': ev.polarity,
                    'event_id': ev.event_id,
                    'created_at': ev.created_at
                }
                for evidences in self.evidence.values()
                for ev in evidences
            ],
            'saved_at': datetime.now().isoformat()
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        logger.info(f"Saved {len(self.beliefs)} beliefs to {filepath}")

    def create_belief(self, concept: str, initial_evidence: str = "", source: str = "") -> Belief:
        """创建新信念"""
        belief_id = f"belief_{concept.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        belief = Belief(
            id=belief_id,
            concept=concept,
            state=BeliefState.EMERGING,
            confidence=0.5,
            evidence_count=0,
            first_evidence_at=datetime.now().isoformat()
        )

        self.beliefs[belief_id] = belief

        if initial_evidence:
            self.add_evidence(belief_id, initial_evidence, source, polarity=1.0)

        self._save_beliefs()
        logger.info(f"Created belief: {concept}")
        return belief

    def add_evidence(self, belief_id: str, evidence_text: str, source: str, polarity: float = 1.0, event_id: str = "") -> BeliefEvidence:
        """为信念添加证据"""
        if belief_id not in self.beliefs:
            logger.warning(f"Belief not found: {belief_id}")
            return None

        evidence_id = f"ev_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        evidence = BeliefEvidence(
            id=evidence_id,
            belief_id=belief_id,
            source=source,
            evidence_text=evidence_text,
            polarity=polarity,
            event_id=event_id
        )

        if belief_id not in self.evidence:
            self.evidence[belief_id] = []
        self.evidence[belief_id].append(evidence)

        belief = self.beliefs[belief_id]
        belief.evidence_count = len(self.evidence[belief_id])
        belief.updated_at = datetime.now().isoformat()

        if polarity > 0:
            if source not in belief.supporting_sources:
                belief.supporting_sources.append(source)
        else:
            if source not in belief.opposing_sources:
                belief.opposing_sources.append(source)

        self._update_belief_confidence(belief)
        self._update_belief_state(belief)
        self._save_beliefs()

        return evidence

    def _update_belief_confidence(self, belief: Belief):
        """更新信念置信度"""
        if belief_id := belief.id and self.evidence.get(belief_id):
            evds = self.evidence[belief_id]
            if not evds:
                return

            total_polarity = sum(e.polarity for e in evds)
            evidence_factor = min(len(evds) / 10.0, 1.0)

            base_confidence = (total_polarity / len(evds) + 1) / 2

            belief.confidence = min(0.95, max(0.05, base_confidence * (0.7 + 0.3 * evidence_factor)))

    def _update_belief_state(self, belief: Belief):
        """更新信念状态"""
        evidence_count = len(self.evidence.get(belief.id, []))

        if evidence_count >= 5 and belief.confidence >= 0.7:
            if belief.state != BeliefState.CONFIRMED:
                belief.state = BeliefState.CONFIRMED
                belief.confirmed_at = datetime.now().isoformat()
                logger.info(f"Belief confirmed: {belief.concept}")
        elif evidence_count >= 3 and belief.confidence >= 0.6:
            belief.state = BeliefState.GROWING
        elif evidence_count >= 1:
            belief.state = BeliefState.EMERGING

        if belief.confidence < 0.3 and evidence_count >= 3:
            belief.state = BeliefState.DECLINING

    def get_belief(self, concept: str) -> Optional[Belief]:
        """获取概念相关的信念"""
        concept_lower = concept.lower()
        for belief in self.beliefs.values():
            if concept_lower in belief.concept.lower():
                return belief
        return None

    def get_all_beliefs(self, state: BeliefState = None) -> List[Belief]:
        """获取所有信念"""
        if state:
            return [b for b in self.beliefs.values() if b.state == state]
        return list(self.beliefs.values())

    def get_belief_timeline(self, belief_id: str) -> List[Dict]:
        """获取信念的时间线"""
        if belief_id not in self.evidence:
            return []

        timeline = []
        for ev in self.evidence[belief_id]:
            timeline.append({
                'time': ev.created_at,
                'type': 'evidence',
                'source': ev.source,
                'polarity': ev.polarity,
                'summary': ev.evidence_text[:100]
            })

        belief = self.beliefs[belief_id]
        timeline.append({
            'time': belief.created_at,
            'type': 'created',
            'concept': belief.concept
        })

        if belief.confirmed_at:
            timeline.append({
                'time': belief.confirmed_at,
                'type': 'confirmed',
                'confidence': belief.confidence
            })

        timeline.sort(key=lambda x: x['time'])
        return timeline

    def evolve_beliefs_from_events(self, events: List) -> List[Belief]:
        """
        从事件演化信念
        分析事件，更新或创建相关信念
        """
        updated_beliefs = []

        keywords_map = {
            'speculative decoding': ['speculative', 'specdec', '推测解码'],
            'kv cache': ['kv cache', 'kv-cache', 'key value cache'],
            'flash attention': ['flash attention', 'flashattn', '快注意力'],
            'moe': ['mixture of experts', 'moe', '混合专家'],
            'multi-agent': ['multi-agent', 'multiagent', '多智能体'],
            'agentic': ['agentic', '代理式'],
            'long context': ['long context', '长上下文', '1m context'],
            'quantization': ['quantize', 'quantization', '量化'],
            'vllm': ['vllm', 'vLLM'],
            'sglang': ['sglang', 'SGLang'],
            'tensorrt': ['tensorrt', 'TensorRT'],
            'mcp': ['mcp', 'model context protocol']
        }

        for event in events:
            event_text = ' '.join([
                getattr(event, 'title', ''),
                getattr(event, 'summary', ''),
                getattr(event, 'entity', '')
            ]).lower()

            for concept, keywords in keywords_map.items():
                if any(kw in event_text for kw in keywords):
                    belief = self.get_belief(concept)
                    if not belief:
                        belief = self.create_belief(
                            concept=concept,
                            initial_evidence=getattr(event, 'summary', '')[:500],
                            source=getattr(event, 'source', 'event')
                        )

                    polarity = 1.0 if getattr(event, 'importance', 'P1') in ['P0', 'P1'] else 0.5

                    self.add_evidence(
                        belief_id=belief.id,
                        evidence_text=getattr(event, 'summary', '')[:500],
                        source=getattr(event, 'source', 'event'),
                        polarity=polarity,
                        event_id=getattr(event, 'id', '')
                    )

                    updated_beliefs.append(belief)

        return updated_beliefs

    def get_converging_beliefs(self) -> List[Tuple[Belief, float]]:
        """
        获取正在收敛的信念
        高置信度 + 大量证据 = 技术成熟
        """
        converging = []

        for belief in self.beliefs.values():
            evidence_count = len(self.evidence.get(belief.id, []))

            if belief.state in [BeliefState.CONFIRMED, BeliefState.CONVERGING]:
                score = belief.confidence * 0.6 + min(evidence_count / 20.0, 1.0) * 0.4
                converging.append((belief, score))

        converging.sort(key=lambda x: x[1], reverse=True)
        return converging

    def get_emerging_beliefs(self) -> List[Belief]:
        """获取新兴信念"""
        return [b for b in self.beliefs.values() if b.state == BeliefState.EMERGING]

    def generate_beliefs_report(self) -> str:
        """生成信念演化报告"""
        lines = ["# AI技术信念演化报告\n"]
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        lines.append(f"**信念总数**: {len(self.beliefs)}\n\n")

        confirmed = [b for b in self.beliefs.values() if b.state == BeliefState.CONFIRMED]
        growing = [b for b in self.beliefs.values() if b.state == BeliefState.GROWING]
        emerging = [b for b in self.beliefs.values() if b.state == BeliefState.EMERGING]

        lines.append(f"## 确认的信念 ({len(confirmed)})\n")
        for b in confirmed:
            lines.append(f"- **{b.concept}**: 置信度 {b.confidence:.0%}, 证据 {b.evidence_count} 条")

        lines.append(f"\n## 增长中的信念 ({len(growing)})\n")
        for b in growing:
            lines.append(f"- **{b.concept}**: 置信度 {b.confidence:.0%}, 证据 {b.evidence_count} 条")

        lines.append(f"\n## 新兴的信念 ({len(emerging)})\n")
        for b in emerging[:5]:
            lines.append(f"- **{b.concept}**: 置信度 {b.confidence:.0%}, 证据 {b.evidence_count} 条")

        return '\n'.join(lines)


class BeliefAwareInsightAgent:
    """
    信念感知洞察Agent
    在生成洞察时考虑信念演化状态
    """

    def __init__(self, belief_engine: BeliefEvolutionEngine):
        self.belief_engine = belief_engine

    def incorporate_beliefs(self, events: List) -> List[Dict]:
        """将信念状态融入事件分析"""
        result = []

        for event in events:
            event_dict = {
                'id': getattr(event, 'id', ''),
                'title': getattr(event, 'title', ''),
                'entity': getattr(event, 'entity', ''),
                'importance': getattr(event, 'importance', 'P2'),
                'belief_state': None,
                'belief_confidence': None
            }

            for belief in self.belief_engine.beliefs.values():
                if belief.concept.lower() in event_dict['title'].lower():
                    event_dict['belief_state'] = belief.state.value
                    event_dict['belief_confidence'] = belief.confidence
                    break

            result.append(event_dict)

        return result


def create_belief_engine(store=None) -> BeliefEvolutionEngine:
    """创建信念演化引擎"""
    return BeliefEvolutionEngine(store=store)