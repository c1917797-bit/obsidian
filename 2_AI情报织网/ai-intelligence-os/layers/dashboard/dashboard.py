"""
Intelligence Dashboard - 可视化仪表板
技术雷达、趋势热图、统计面板
"""
import os
import json
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict

from core.logger import get_logger

logger = get_logger("Dashboard")


class TechRadar:
    """
    技术雷达
    可视化技术在不同阶段的分布
    """

    def __init__(self, trend_engine=None):
        self.trend_engine = trend_engine

    def generate_radar_data(self, days: int = 30) -> Dict:
        """生成技术雷达数据"""
        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            from core.storage import UnifiedStore
            self.trend_engine = TrendEngine(store=UnifiedStore())

        all_techs = self.trend_engine.get_trending_techs(days=days, limit=50)

        radar = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'days': days,
                'tech_count': len(all_techs)
            },
            'rings': {
                'adopt': [],
                'trial': [],
                'assess': [],
                'hold': []
            },
            'quadrants': {
                'inference': [],
                'agent': [],
                'tools': [],
                'research': []
            }
        }

        category_map = {
            'inference_optimization': 'inference',
            'agent_runtime': 'agent',
            'cost_optimization': 'inference',
            'research': 'research',
            'industry': 'tools',
            'framework': 'tools'
        }

        for tech_data in all_techs:
            tech = tech_data['tech']
            heat = tech_data['heat_score']
            stage = tech_data.get('stage', 'growing')

            entry = {
                'tech': tech,
                'heat': heat,
                'events': tech_data.get('count', 0)
            }

            if heat >= 0.7:
                ring = 'adopt'
            elif heat >= 0.5:
                ring = 'trial'
            elif heat >= 0.3:
                ring = 'assess'
            else:
                ring = 'hold'

            radar['rings'][ring].append(entry)

            quadrant = category_map.get(tech_data.get('category', ''), 'research')
            radar['quadrants'][quadrant].append(entry)

        return radar

    def render_ascii_radar(self, days: int = 30) -> str:
        """渲染ASCII雷达图"""
        radar_data = self.generate_radar_data(days)

        lines = [
            "=" * 60,
            "TECHNOLOGY RADAR",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"Period: Last {days} days",
            "=" * 60,
            ""
        ]

        lines.append("  ADOPT (high heat, ready for production)")
        for item in radar_data['rings']['adopt'][:5]:
            lines.append(f"    ● {item['tech']} ({item['heat']:.2f})")

        lines.append("\n  TRIAL (good heat, worth trying)")
        for item in radar_data['rings']['trial'][:5]:
            lines.append(f"    ◐ {item['tech']} ({item['heat']:.2f})")

        lines.append("\n  ASSESS (emerging, worth exploring)")
        for item in radar_data['rings']['assess'][:5]:
            lines.append(f"    ○ {item['tech']} ({item['heat']:.2f})")

        lines.append("\n  HOLD (low heat or immature)")
        for item in radar_data['rings']['hold'][:5]:
            lines.append(f"    · {item['tech']} ({item['heat']:.2f})")

        lines.append("\n" + "=" * 60)
        lines.append("QUADRANTS")
        for quadrant, items in radar_data['quadrants'].items():
            lines.append(f"\n  [{quadrant.upper()}]")
            for item in items[:3]:
                lines.append(f"    {item['tech']}")

        return '\n'.join(lines)


class TrendHeatmap:
    """
    趋势热图
    显示技术随时间的活跃度变化
    """

    def __init__(self, store=None):
        self.store = store

    def generate_heatmap_data(self, techs: List[str], days: int = 30) -> Dict:
        """生成热图数据"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        heatmap = {
            'metadata': {
                'techs': techs,
                'days': days,
                'generated_at': datetime.now().isoformat()
            },
            'cells': [],
            'row_labels': techs,
            'col_labels': []
        }

        today = datetime.now()
        for i in range(days):
            date = today - timedelta(days=i)
            heatmap['col_labels'].append(date.strftime('%m-%d'))

        for tech in techs:
            row = {'tech': tech, 'values': []}
            events = self.store.get_events_by_tech(tech, days=days, limit=100)

            daily_counts = defaultdict(int)
            for event in events:
                try:
                    event_date = datetime.fromisoformat(event.time)
                    day_key = (today - event_date).days
                    if 0 <= day_key < days:
                        daily_counts[day_key] += 1
                except:
                    pass

            for i in range(days):
                count = daily_counts.get(i, 0)
                intensity = min(count / 5.0, 1.0)
                row['values'].append({
                    'day_offset': i,
                    'count': count,
                    'intensity': intensity
                })

            heatmap['cells'].append(row)

        return heatmap

    def render_ascii_heatmap(self, techs: List[str], days: int = 14) -> str:
        """渲染ASCII热图"""
        heatmap = self.generate_heatmap_data(techs, days)

        lines = [
            "=" * 60,
            "TREND HEATMAP",
            f"Period: Last {days} days",
            "=" * 60,
            ""
        ]

        header = "TECH            " + "".join([f"{d:>5}" for d in range(days)])
        lines.append(header)
        lines.append("-" * len(header))

        for row in heatmap['cells']:
            tech_name = row['tech'][:14].ljust(14)
            values_str = "".join([f"{int(c['intensity'] * 9):>5}" for c in row['values']])
            lines.append(f"{tech_name} {values_str}")

        lines.append("\nIntensity: 0=none, 1-3=low, 4-6=medium, 7-9=high")
        lines.append("=" * 60)

        return '\n'.join(lines)


class StatsPanel:
    """
    统计面板
    系统运行统计可视化
    """

    def __init__(self, store=None, trend_engine=None):
        self.store = store
        self.trend_engine = trend_engine

    def generate_stats(self) -> Dict:
        """生成统计面板数据"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        stats = self.store.get_stats()

        panel = {
            'overview': {
                'total_signals': stats.get('total_signals', 0),
                'total_events': stats.get('total_events', 0),
                'reports_generated': stats.get('total_reports', 0),
                'active_sources': stats.get('enabled_sources', 0)
            },
            'recent_activity': {
                'signals_this_week': stats.get('signals_this_week', 0),
                'events_this_week': stats.get('events_this_week', 0)
            },
            'distribution': {
                'by_type': stats.get('events_by_type', {}),
                'by_importance': stats.get('events_by_importance', {})
            }
        }

        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            self.trend_engine = TrendEngine(store=self.store)

        trend_summary = self.trend_engine.get_trend_summary(days=7)
        panel['trending'] = {
            'top_5': trend_summary.get('trending_techs', [])[:5],
            'converging_count': len(trend_summary.get('converging_techs', [])),
            'production_ready_count': len(trend_summary.get('production_ready', []))
        }

        return panel

    def render_ascii_stats(self) -> str:
        """渲染ASCII统计面板"""
        stats = self.generate_stats()

        lines = [
            "=" * 60,
            "INTELLIGENCE OS STATISTICS",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "=" * 60,
            "",
            "┌─────────────────┬─────────────────┐",
            "│ OVERVIEW        │ VALUE           │",
            "├─────────────────┼─────────────────┤",
            f"│ Total Signals   │ {stats['overview']['total_signals']:>15} │",
            f"│ Total Events    │ {stats['overview']['total_events']:>15} │",
            f"│ Reports Gen.    │ {stats['overview']['reports_generated']:>15} │",
            f"│ Active Sources  │ {stats['overview']['active_sources']:>15} │",
            "└─────────────────┴─────────────────┘",
            "",
            "┌─────────────────┬─────────────────┐",
            "│ RECENT (7 days) │ VALUE           │",
            "├─────────────────┼─────────────────┤",
            f"│ Signals         │ {stats['recent_activity']['signals_this_week']:>15} │",
            f"│ Events          │ {stats['recent_activity']['events_this_week']:>15} │",
            "└─────────────────┴─────────────────┘",
            "",
            "TRENDING TECHNOLOGIES:"
        ]

        for i, tech in enumerate(stats['trending']['top_5'], 1):
            lines.append(f"  {i}. {tech}")

        lines.extend([
            "",
            f"Converging: {stats['trending']['converging_count']} technologies",
            f"Production Ready: {stats['trending']['production_ready_count']} projects",
            "",
            "=" * 60
        ])

        return '\n'.join(lines)


class DashboardGenerator:
    """
    综合仪表板生成器
    生成完整的可视化报告
    """

    def __init__(self, store=None, trend_engine=None):
        self.store = store
        self.trend_engine = trend_engine
        self.tech_radar = TechRadar(trend_engine)
        self.heatmap = TrendHeatmap(store)
        self.stats_panel = StatsPanel(store, trend_engine)

    def generate_full_dashboard(self, days: int = 30) -> str:
        """生成完整仪表板"""
        lines = [
            "=" * 70,
            "║       AI INTELLIGENCE OS - DASHBOARD                        ║",
            f"║       Generated: {datetime.now().strftime('%Y-%m-%d %H:%M'):<40}║",
            "=" * 70,
            ""
        ]

        lines.append("[ SYSTEM STATISTICS ]")
        lines.append(self.stats_panel.render_ascii_stats())
        lines.append("")

        lines.append("[ TECHNOLOGY RADAR ]")
        lines.append(self.tech_radar.render_ascii_radar(days))
        lines.append("")

        top_techs = ['speculative_decoding', 'kv_cache', 'flash_attention', 'moe', 'multi-agent', 'vllm', 'sglang']
        lines.append("[ ACTIVITY HEATMAP ]")
        lines.append(self.heatmap.render_ascii_heatmap(top_techs, days=14))
        lines.append("")

        lines.append("=" * 70)
        lines.append("END OF DASHBOARD")
        lines.append("=" * 70)

        return '\n'.join(lines)

    def export_dashboard_json(self, filepath: str = None) -> str:
        """导出JSON格式的仪表板数据"""
        if not filepath:
            data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
            os.makedirs(data_dir, exist_ok=True)
            filepath = os.path.join(data_dir, f"dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

        dashboard_data = {
            'generated_at': datetime.now().isoformat(),
            'stats': self.stats_panel.generate_stats(),
            'radar': self.tech_radar.generate_radar_data(),
            'heatmap': {
                'techs': ['speculative_decoding', 'kv_cache', 'flash_attention', 'moe', 'multi-agent'],
                'days': 14,
                'data': self.heatmap.generate_heatmap_data(
                    ['speculative_decoding', 'kv_cache', 'flash_attention', 'moe', 'multi-agent'],
                    days=14
                )
            }
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

        logger.info(f"Dashboard exported to: {filepath}")
        return filepath

    def generate_obsidian_dashboard_note(self) -> str:
        """生成Obsidian仪表板笔记"""
        stats = self.stats_panel.generate_stats()
        radar = self.tech_radar.generate_radar_data()

        content = f"""---
type: dashboard
date: {datetime.now().strftime('%Y-%m-%d')}
created: {datetime.now().isoformat()}
tags: [AI-Intelligence, Dashboard]
---

# AI Intelligence OS Dashboard

> [!info] Last Updated
> {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 系统概览

| 指标 | 数值 |
|------|------|
| 总信号数 | {stats['overview']['total_signals']} |
| 总事件数 | {stats['overview']['total_events']} |
| 生成报告 | {stats['overview']['reports_generated']} |
| 活跃信源 | {stats['overview']['active_sources']} |

## 本周活跃

| 类型 | 数量 |
|------|------|
| 信号 | {stats['recent_activity']['signals_this_week']} |
| 事件 | {stats['recent_activity']['events_this_week']} |

## 技术雷达

### ADOPT - 可采用
"""
        for item in radar['rings']['adopt'][:5]:
            content += f"- [[{item['tech']}]] (热度: {item['heat']:.2f})\n"

        content += """
### TRIAL - 可试用
"""
        for item in radar['rings']['trial'][:5]:
            content += f"- [[{item['tech']}]] (热度: {item['heat']:.2f})\n"

        content += """
### ASSESS - 可评估
"""
        for item in radar['rings']['assess'][:5]:
            content += f"- [[{item['tech']}]] (热度: {item['heat']:.2f})\n"

        content += """
### HOLD - 暂缓
"""
        for item in radar['rings']['hold'][:5]:
            content += f"- [[{item['tech']}]] (热度: {item['heat']:.2f})\n"

        content += """
## 热门技术

"""
        for i, tech in enumerate(stats['trending']['top_5'], 1):
            content += f"{i}. {tech}\n"

        content += f"""
## 技术收敛

- 收敛中技术: {stats['trending']['converging_count']} 个
- 生产就绪: {stats['trending']['production_ready_count']} 个

---

> [!tip] Quick Links
> - [[Daily/{datetime.now().strftime('%Y-%m-%d')}|今日日报]]
> - [[Weekly_{self._get_week_str()}|本周周报]]
> - [[技术收敛_{datetime.now().strftime('%Y-%m')}|技术收敛报告]]
"""

        return content

    def _get_week_str(self) -> str:
        """获取当前周字符串"""
        today = datetime.now()
        week_num = today.isocalendar()[1]
        return f"{today.year}-W{week_num:02d}"

    def save_dashboard_note(self) -> str:
        """保存仪表板笔记到Obsidian"""
        from layers.output.obsidian_sink import ObsidianSink

        sink = ObsidianSink()
        content = self.generate_obsidian_dashboard_note()

        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"Dashboard_{date_str}.md"
        filepath = os.path.join(sink.daily_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Dashboard note saved: {filepath}")
        return filepath


def create_dashboard(store=None, trend_engine=None) -> DashboardGenerator:
    """创建仪表板生成器"""
    return DashboardGenerator(store=store, trend_engine=trend_engine)


def generate_and_print_dashboard():
    """生成并打印仪表板"""
    from core.storage import UnifiedStore
    from layers.trends.trend_engine import TrendEngine

    store = UnifiedStore()
    trend_engine = TrendEngine(store=store)

    dashboard = create_dashboard(store=store, trend_engine=trend_engine)
    output = dashboard.generate_full_dashboard()

    print(output)
    return output