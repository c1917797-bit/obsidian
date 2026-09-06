"""
Trend Engine - 趋势分析层
基于事件数据计算技术趋势、热点、收敛度
"""
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

from core.storage import UnifiedStore
from core.logger import get_logger

logger = get_logger("TrendEngine")

class TrendEngine:
    """
    趋势分析引擎
    负责任务：
    1. 计算技术热度（heat_score）
    2. 识别热门技术（trending）
    3. 识别收敛技术（converging）
    4. 识别生产就绪技术（production_ready）
    5. 生成技术演化链
    """

    def __init__(self, store: UnifiedStore = None):
        self.store = store or UnifiedStore()

        self.TECH_STAGES = {
            'emerging': {'score_range': (0, 0.3), 'velocity': 'slow'},
            'growing': {'score_range': (0.3, 0.6), 'velocity': 'fast'},
            'peak': {'score_range': (0.6, 0.8), 'velocity': 'stable'},
            'converging': {'score_range': (0.8, 0.95), 'velocity': 'slowing'},
            'mature': {'score_range': (0.95, 1.0), 'velocity': 'stable'}
        }

    def calculate_heat_score(self, tech_category: str, days: int = 7) -> float:
        """
        计算技术热度分数
        基于：
        - 事件数量（activity）
        - 重要性分布（quality）
        - 时间衰减（recency）
        """
        since = (datetime.now() - timedelta(days=days)).isoformat()

        events = self.store.get_events_by_tech(tech_category, days=days, limit=100)

        if not events:
            return 0.0

        activity_score = min(len(events) / 20.0, 1.0)

        importance_scores = {'P0': 1.0, 'P1': 0.7, 'P2': 0.4, 'P3': 0.2}
        quality_score = 0.0
        for event in events:
            imp = event.importance if hasattr(event, 'importance') else 'P1'
            quality_score += importance_scores.get(imp, 0.5)
        quality_score = min(quality_score / (len(events) * 1.0), 1.0)

        recency_score = 0.0
        now = datetime.now().timestamp()
        for event in events:
            try:
                event_time = datetime.fromisoformat(event.time).timestamp()
                age_days = (now - event_time) / 86400
                recency_score += max(0, 1 - age_days / days)
            except:
                pass
        recency_score = min(recency_score / len(events), 1.0) if events else 0.0

        heat_score = (
            activity_score * 0.3 +
            quality_score * 0.4 +
            recency_score * 0.3
        )

        return round(heat_score, 3)

    def get_trending_techs(self, days: int = 7, limit: int = 10) -> List[Dict]:
        """获取热门技术"""
        trending = self.store.get_trending_techs(days=days, limit=20)

        results = []
        for item in trending:
            tech = item['tech']
            count = item['count']
            heat = self.calculate_heat_score(tech, days)

            if heat > 0.3:
                results.append({
                    'tech': tech,
                    'category': item.get('category', 'unknown'),
                    'count': count,
                    'heat_score': heat,
                    'stage': self._get_stage_from_score(heat)
                })

        results.sort(key=lambda x: x['heat_score'], reverse=True)
        return results[:limit]

    def get_converging_techs(self, days: int = 30) -> List[Dict]:
        """
        获取收敛技术
        收敛 = 技术迭代放缓，标准趋于统一
        识别标准：
        - 事件数量稳定或下降
        - 新项目/实现减少
        - 讨论焦点转向"最佳实践"
        """
        trending = self.store.get_trending_techs(days=days, limit=30)

        converging = []
        for item in trending:
            tech = item['tech']

            current_events = self.store.get_events_by_tech(tech, days=7, limit=20)
            older_events = self.store.get_events_by_tech(tech, days=28, limit=50)

            current_count = len(current_events)
            older_count = len(older_events)

            if older_count > 0:
                ratio = current_count / max(older_count / 4, 1)

                if ratio < 0.7 and current_count >= 3:
                    converging.append({
                        'tech': tech,
                        'category': item.get('category', 'unknown'),
                        'current_activity': current_count,
                        'activity_ratio': round(ratio, 2),
                        'stage': 'converging',
                        'heat_score': item.get('count', 0) / older_count
                    })

        converging.sort(key=lambda x: x['activity_ratio'])
        return converging[:10]

    def get_production_ready(self, days: int = 14) -> List[Dict]:
        """
        获取生产就绪技术
        标准：
        - 头部项目有正式release
        - 多个独立实现
        - 文档完善
        """
        from layers.agents.classifier_agent import KNOWN_PROJECTS

        production_ready = []

        for project in KNOWN_PROJECTS:
            events = self.store.get_events_by_tech(project, days=days, limit=10)

            if len(events) >= 2:
                has_release = any(
                    'release' in e.title.lower() or 'announce' in e.title.lower()
                    for e in events
                )
                has_industry = any(
                    e.event_type == 'product_announcement' or e.event_type == 'runtime_feature'
                    for e in events
                )

                if has_release or has_industry:
                    production_ready.append({
                        'project': project,
                        'events_count': len(events),
                        'has_release': has_release,
                        'heat_score': self.calculate_heat_score(project, days)
                    })

        production_ready.sort(key=lambda x: x['heat_score'], reverse=True)
        return production_ready[:10]

    def get_evolution_chain(self, tech: str) -> Dict:
        """
        获取技术演化链
        从历史事件中推断技术发展阶段
        """
        events = self.store.get_events_by_tech(tech, days=90, limit=50)

        if len(events) < 3:
            return {'tech': tech, 'evolution': [], 'current_stage': 'unknown'}

        stage_events = {'emerging': [], 'growing': [], 'peak': [], 'converging': [], 'mature': []}

        for event in events:
            try:
                event_time = datetime.fromisoformat(event.time)
                stage = event.stage if hasattr(event, 'stage') and event.stage else 'emerging'
                if stage in stage_events:
                    stage_events[stage].append(event_time)
            except:
                pass

        evolution = []
        for stage_name, times in stage_events.items():
            if times:
                evolution.append({
                    'stage': stage_name,
                    'count': len(times),
                    'first_seen': min(times).isoformat(),
                    'last_seen': max(times).isoformat()
                })

        current_stage = 'emerging'
        if evolution:
            current_stage = evolution[-1]['stage']

        return {
            'tech': tech,
            'evolution': evolution,
            'current_stage': current_stage,
            'total_events': len(events)
        }

    def get_trend_summary(self, days: int = 7) -> Dict:
        """获取趋势摘要"""
        trending = self.get_trending_techs(days=days, limit=10)
        converging = self.get_converging_techs(days=days)
        production_ready = self.get_production_ready(days=days)

        return {
            'trending_techs': [t['tech'] for t in trending[:5]],
            'converging_techs': [t['tech'] for t in converging[:5]],
            'production_ready': [p['project'] for p in production_ready[:5]],
            'trending_details': trending,
            'converging_details': converging,
            'production_details': production_ready,
            'generated_at': datetime.now().isoformat()
        }

    def _get_stage_from_score(self, score: float) -> str:
        """根据分数确定stage"""
        if score >= 0.8:
            return 'converging'
        elif score >= 0.6:
            return 'peak'
        elif score >= 0.3:
            return 'growing'
        else:
            return 'emerging'

    def detect_anomalies(self, days: int = 7) -> List[Dict]:
        """
        检测异常信号
        - 突然出现的新技术方向
        - 突然冷却的曾经常见技术
        - 异常高热度的技术
        """
        trending = self.store.get_trending_techs(days=days, limit=30)
        older_trending = self.store.get_trending_techs(days=30, limit=50)

        anomalies = []

        for item in trending:
            tech = item['tech']
            heat = item.get('count', 0)

            if heat > 10:
                for old_item in older_trending:
                    if old_item['tech'] == tech:
                        if item.get('count', 0) > old_item.get('count', 0) * 3:
                            anomalies.append({
                                'type': 'spike',
                                'tech': tech,
                                'current_count': heat,
                                'previous_count': old_item.get('count', 0),
                                'description': f'热度突然增长 {heat/old_item.get("count",1):.1f}x'
                            })
                        break
            else:
                is_new = True
                for old_item in older_trending:
                    if old_item['tech'] == tech:
                        is_new = False
                        break
                if is_new and heat >= 3:
                    anomalies.append({
                        'type': 'new_emerging',
                        'tech': tech,
                        'count': heat,
                        'description': '新兴技术方向'
                    })

        return anomalies

    def get_tech_radar(self, days: int = 30) -> Dict:
        """
        生成技术雷达数据
        用于可视化
        """
        all_techs = self.store.get_trending_techs(days=days, limit=50)

        radar = {
            'inference_optimization': [],
            'agent_runtime': [],
            'cost_optimization': [],
            'research': [],
            'industry': []
        }

        category_map = {
            'inference_optimization': ['speculative_decoding', 'kv_cache', 'flash_attention', 'quantization', 'batch_optimization'],
            'agent_runtime': ['multi_agent', 'tool_use', 'reasoning', 'memory', 'session_management'],
            'cost_optimization': ['moe', 'distillation', 'compile_optimization'],
            'research': ['architecture', 'training', 'evaluation'],
            'industry': ['product_launch', 'funding', 'partnership']
        }

        for item in all_techs:
            tech = item['tech']
            for domain, techs in category_map.items():
                if tech in techs or any(t in tech for t in techs):
                    heat = self.calculate_heat_score(tech, days)
                    radar[domain].append({
                        'tech': tech,
                        'heat': heat,
                        'stage': self._get_stage_from_score(heat),
                        'events': item.get('count', 0)
                    })
                    break

        return radar