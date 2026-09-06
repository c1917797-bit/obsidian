"""
Signal Source Tracker - 信号源关联追踪
按 source 统计事件分布，识别首发媒体和信源能力
"""
import os
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from collections import defaultdict

from core.logger import get_logger

logger = get_logger("SignalSourceTracker")


class SignalSourceTracker:
    """
    信号源关联追踪器
    负责：
    1. 按 source 统计事件分布
    2. 识别哪些 source 最先报道重大技术
    3. 写入信号源关联.md
    """

    def __init__(self, store=None):
        self.store = store

    def _get_db_conn(self):
        """获取数据库连接"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()
        return sqlite3.connect(self.store.db_path)

    def get_source_stats(self, days: int = 7) -> Dict:
        """按 source 统计事件分布"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        since = (datetime.now() - timedelta(days=days)).isoformat()

        try:
            conn = self._get_db_conn()
            cursor = conn.execute("""
                SELECT source, COUNT(*) as cnt,
                       SUM(CASE WHEN importance = 'P0' THEN 1 ELSE 0 END) as p0_count,
                       SUM(CASE WHEN importance = 'P1' THEN 1 ELSE 0 END) as p1_count
                FROM events
                WHERE time >= ?
                GROUP BY source
                ORDER BY cnt DESC
            """, (since,))
            rows = cursor.fetchall()
            conn.close()
        except Exception as e:
            logger.error(f"Failed to get source stats: {e}")
            return {}

        source_stats = []
        total_events = 0
        for row in rows:
            source_stats.append({
                'source': row[0] or 'unknown',
                'count': row[1],
                'p0_count': row[2] or 0,
                'p1_count': row[3] or 0
            })
            total_events += row[1]

        # 计算占比
        for s in source_stats:
            s['ratio'] = round(s['count'] / total_events, 3) if total_events > 0 else 0

        return {
            'sources': source_stats,
            'total_events': total_events,
            'days': days,
            'generated_at': datetime.now().isoformat()
        }

    def get_first_sources(self, days: int = 30) -> List[Dict]:
        """识别哪些 source 最先报道重大技术（首发能力分析）"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        since = (datetime.now() - timedelta(days=days)).isoformat()

        try:
            conn = self._get_db_conn()
            cursor = conn.execute("""
                SELECT entity, source, MIN(time) as first_time
                FROM events
                WHERE time >= ? AND entity IS NOT NULL AND entity != ''
                GROUP BY entity, source
                ORDER BY entity, first_time
            """, (since,))
            rows = cursor.fetchall()
            conn.close()
        except Exception as e:
            logger.error(f"Failed to get first sources: {e}")
            return []

        # 按 entity 找第一个报道的 source
        entity_first = {}
        for row in rows:
            entity, source, first_time = row[0], row[1], row[2]
            if entity not in entity_first:
                entity_first[entity] = {'source': source, 'first_time': first_time}

        # 统计每个 source 的首发次数
        first_counts = defaultdict(int)
        for entity, info in entity_first.items():
            first_counts[info['source']] += 1

        result = []
        for source, count in sorted(first_counts.items(), key=lambda x: -x[1]):
            result.append({'source': source, 'first_count': count})

        return result[:10]

    def save_correlation_report(self, correlation: Dict) -> str:
        """写入信号源关联.md"""
        vault_base = r"C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网"
        filepath = os.path.join(vault_base, "识别", "信号源关联", "信号源关联.md")
        date_str = datetime.now().strftime('%Y-%m-%d')

        sources = correlation.get('sources', [])
        first_sources = correlation.get('first_sources', [])

        # 构建信源统计表
        source_rows = ""
        for s in sources[:20]:
            source_rows += f"| {s['source']} | {s['count']} | {s['p0_count']} | {s['p1_count']} | {s['ratio']:.1%} |\n"

        # 构建首发能力表
        first_rows = ""
        for f in first_sources[:10]:
            first_rows += f"| {f['source']} | {f['first_count']} |\n"

        nl = "\n"
        content = f"""---
type: source-correlation
created: {date_str}
updated: {date_str}
tags: [AI-Intelligence, 信号, 信源]
---

# 信号源关联

> [!info] 自动生成
> 由 AI Intelligence OS SignalSourceTracker 自动更新 | 更新时间: {date_str}

## 信源统计（7日）

| 信源 | 事件数 | P0数 | P1数 | 占比 |
|------|--------|------|------|------|
{source_rows if source_rows else f"| - | - | - | - |{nl}"}

## 首发能力（30日）

| 信源 | 首发次数 |
|------|----------|
{first_rows if first_rows else f"| - | - |{nl}"}

## 生成信息

- 统计周期: 最近 {correlation.get('days', 7)} 天
- 总事件数: {correlation.get('total_events', 0)}
- 生成时间: {correlation.get('generated_at', date_str)}
- 数据来源: AI Intelligence OS UnifiedStore
"""

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"信号源关联已更新: {filepath}")
        return filepath