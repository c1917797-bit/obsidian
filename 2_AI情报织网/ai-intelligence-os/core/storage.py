"""
统一存储层 - SQLite
消除数据孤岛，统一事件和信号存储
"""
import os
import json
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
from pathlib import Path
from dataclasses import asdict

from core.models import Signal, TechEvent, EventType, Importance

class UnifiedStore:
    """
    统一存储层
    - Signals: 原始采集数据
    - Events: 分类Enrichment后的事件
    - Reports: 生成的报告
    """

    def __init__(self, db_path: str = None):
        self.db_path = db_path or os.path.join(
            os.path.dirname(__file__), '..', 'db', 'intelligence.db'
        )
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        self._init_db()
        self.stats = {
            'signals_stored': 0,
            'events_stored': 0,
            'reports_stored': 0,
            'queries': 0
        }

    def _init_db(self):
        """初始化数据库schema"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        # Signals 表 - 原始信号存储
        c.execute('''
            CREATE TABLE IF NOT EXISTS signals (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                url TEXT,
                source TEXT,
                source_id TEXT,
                source_type TEXT DEFAULT 'rss',
                category TEXT,
                priority TEXT DEFAULT 'P1',
                published TEXT,
                published_timestamp REAL,
                summary TEXT,
                content TEXT,
                authors TEXT,
                tags TEXT,
                fetched_at TEXT,
                language TEXT DEFAULT 'en',
                metadata TEXT,
                processed INTEGER DEFAULT 0,
                event_id TEXT,
                created_at TEXT
            )
        ''')

        # Events 表 - 分类Enrichment后的事件
        c.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id TEXT PRIMARY KEY,
                time TEXT NOT NULL,
                event_type TEXT NOT NULL,
                entity TEXT NOT NULL,
                entity_type TEXT DEFAULT 'project',
                tech_categories TEXT,
                title TEXT,
                summary TEXT,
                signals TEXT,
                innovation TEXT DEFAULT '',
                problem_solved TEXT DEFAULT '',
                importance TEXT DEFAULT 'P1',
                confidence REAL DEFAULT 0.5,
                source TEXT,
                url TEXT,
                authors TEXT,
                related_events TEXT DEFAULT '[]',
                related_techs TEXT DEFAULT '[]',
                created_at TEXT,
                novelty_score REAL DEFAULT 0.0,
                heat_score REAL DEFAULT 0.0,
                stage TEXT DEFAULT 'emerging',
                company TEXT DEFAULT '',
                direction TEXT DEFAULT '',
                metadata TEXT DEFAULT '{}'
            )
        ''')

        # Reports 表 - 生成的报告
        c.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT,
                report_type TEXT NOT NULL,
                period TEXT,
                created_at TEXT,
                events TEXT,
                trends TEXT,
                insights TEXT,
                metadata TEXT
            )
        ''')

        # Sources 表 - 信源配置和状态
        c.execute('''
            CREATE TABLE IF NOT EXISTS sources (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                url TEXT,
                source_type TEXT,
                category TEXT,
                priority TEXT DEFAULT 'P1',
                language TEXT DEFAULT 'en',
                enabled INTEGER DEFAULT 1,
                last_crawled TEXT,
                last_success TEXT,
                error_count INTEGER DEFAULT 0,
                last_error TEXT,
                crawl_interval INTEGER DEFAULT 3600,
                metadata TEXT
            )
        ''')

        # Indices
        c.execute('CREATE INDEX IF NOT EXISTS idx_signal_source ON signals(source)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_signal_published ON signals(published)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_signal_processed ON signals(processed)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_event_time ON events(time)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_event_type ON events(event_type)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_event_entity ON events(entity)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_event_importance ON events(importance)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_report_type ON reports(report_type)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_report_created ON reports(created_at)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_source_enabled ON sources(enabled)')

        conn.commit()
        conn.close()

    def _json_encode(self, obj: Any) -> str:
        """JSON序列化"""
        if obj is None:
            return '{}'
        if isinstance(obj, str):
            return obj
        try:
            return json.dumps(obj, ensure_ascii=False, default=str)
        except:
            return '{}'

    def _json_decode(self, text: str) -> Any:
        """JSON反序列化"""
        if not text:
            return {} if isinstance(text, str) and text == '{}' else []
        if isinstance(text, list):
            return text
        try:
            return json.loads(text)
        except:
            return {} if text == '{}' else []

    # ==================== Signal Operations ====================

    def save_signal(self, signal: Signal) -> bool:
        """保存单个信号"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        try:
            c.execute('''
                INSERT OR REPLACE INTO signals
                (id, title, url, source, source_id, source_type, category, priority,
                 published, published_timestamp, summary, content, authors, tags,
                 fetched_at, language, metadata, processed, event_id, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                signal.id, signal.title, signal.url, signal.source, signal.source_id,
                signal.source_type, signal.category, signal.priority,
                signal.published, signal.published_timestamp, signal.summary,
                signal.content, self._json_encode(signal.authors),
                self._json_encode(signal.tags), signal.fetched_at, signal.language,
                self._json_encode(signal.metadata), 0, None, datetime.now().isoformat()
            ))
            conn.commit()
            self.stats['signals_stored'] += 1
            return True
        except Exception as e:
            print(f"Save signal failed: {e}")
            return False
        finally:
            conn.close()

    def save_signals(self, signals: List[Signal]) -> int:
        """批量保存信号"""
        count = 0
        for signal in signals:
            if self.save_signal(signal):
                count += 1
        return count

    def get_signal(self, signal_id: str) -> Optional[Signal]:
        """获取单个信号"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('SELECT * FROM signals WHERE id = ?', (signal_id,))
        row = c.fetchone()
        conn.close()

        if row:
            return self._row_to_signal(row)
        return None

    def get_unprocessed_signals(self, limit: int = 100) -> List[Signal]:
        """获取未处理的信号"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('''
            SELECT * FROM signals
            WHERE processed = 0
            ORDER BY published_timestamp DESC
            LIMIT ?
        ''', (limit,))

        rows = c.fetchall()
        conn.close()

        return [self._row_to_signal(row) for row in rows]

    def mark_signal_processed(self, signal_id: str, event_id: str = None):
        """标记信号已处理"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        if event_id:
            c.execute('UPDATE signals SET processed = 1, event_id = ? WHERE id = ?', (event_id, signal_id))
        else:
            c.execute('UPDATE signals SET processed = 1 WHERE id = ?', (signal_id,))
        conn.commit()
        conn.close()

    def _row_to_signal(self, row: Tuple) -> Signal:
        """行转Signal对象"""
        columns = ['id', 'title', 'url', 'source', 'source_id', 'source_type', 'category',
                   'priority', 'published', 'published_timestamp', 'summary', 'content',
                   'authors', 'tags', 'fetched_at', 'language', 'metadata', 'processed',
                   'event_id', 'created_at']

        data = {}
        for i, col in enumerate(columns):
            val = row[i]
            if col in ['authors', 'tags']:
                data[col] = self._json_decode(val) if val else []
            elif col == 'metadata':
                data[col] = self._json_decode(val) if val else {}
            else:
                data[col] = val

        return Signal(**{k: v for k, v in data.items() if k in Signal.__dataclass_fields__})

    # ==================== Event Operations ====================

    def save_event(self, event: TechEvent) -> bool:
        """保存单个事件"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        try:
            c.execute('''
                INSERT OR REPLACE INTO events
                (id, time, event_type, entity, entity_type, tech_categories, title, summary,
                 signals, innovation, problem_solved, importance, confidence, source, url,
                 authors, related_events, related_techs, created_at, novelty_score, heat_score,
                 stage, company, direction, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                event.id, event.time, event.event_type, event.entity, event.entity_type,
                self._json_encode(event.tech_categories),
                event.title, event.summary,
                self._json_encode(event.signals),
                event.innovation, event.problem_solved, event.importance, event.confidence,
                event.source, event.url,
                self._json_encode(event.authors),
                self._json_encode(event.related_events),
                self._json_encode(event.related_techs),
                event.created_at, event.novelty_score, event.heat_score,
                event.stage, event.company, event.direction,
                self._json_encode(event.metadata)
            ))
            conn.commit()
            self.stats['events_stored'] += 1
            return True
        except Exception as e:
            print(f"Save event failed: {e}")
            return False
        finally:
            conn.close()

    def save_events(self, events: List[TechEvent]) -> int:
        """批量保存事件"""
        count = 0
        for event in events:
            if self.save_event(event):
                count += 1
        return count

    def get_event(self, event_id: str) -> Optional[TechEvent]:
        """获取单个事件"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('SELECT * FROM events WHERE id = ?', (event_id,))
        row = c.fetchone()
        conn.close()

        if row:
            return self._row_to_event(row)
        return None

    def get_events(
        self,
        event_type: str = None,
        entity: str = None,
        importance: str = None,
        since: str = None,
        until: str = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[TechEvent]:
        """查询事件列表"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = 'SELECT * FROM events WHERE 1=1'
        params = []

        if event_type:
            query += ' AND event_type = ?'
            params.append(event_type)
        if entity:
            query += ' AND entity = ?'
            params.append(entity)
        if importance:
            query += ' AND importance = ?'
            params.append(importance)
        if since:
            query += ' AND time >= ?'
            params.append(since)
        if until:
            query += ' AND time <= ?'
            params.append(until)

        query += ' ORDER BY time DESC LIMIT ? OFFSET ?'
        params.extend([limit, offset])

        c.execute(query, params)
        rows = c.fetchall()
        conn.close()

        return [self._row_to_event(row) for row in rows]

    def get_recent_events(self, days: int = 7, limit: int = 100) -> List[TechEvent]:
        """获取最近的事件"""
        since = (datetime.now() - timedelta(days=days)).isoformat()
        return self.get_events(since=since, limit=limit)

    def get_events_by_tech(self, tech_category: str, days: int = 30, limit: int = 50) -> List[TechEvent]:
        """按技术类别查询事件"""
        since = (datetime.now() - timedelta(days=days)).isoformat()

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('''
            SELECT * FROM events
            WHERE tech_categories LIKE ? AND time >= ?
            ORDER BY time DESC LIMIT ?
        ''', (f'%{tech_category}%', since, limit))

        rows = c.fetchall()
        conn.close()

        return [self._row_to_event(row) for row in rows]

    def _row_to_event(self, row: Tuple) -> TechEvent:
        """行转TechEvent对象"""
        columns = [
            'id', 'time', 'event_type', 'entity', 'entity_type', 'tech_categories',
            'title', 'summary', 'signals', 'innovation', 'problem_solved', 'importance',
            'confidence', 'source', 'url', 'authors', 'related_events', 'related_techs',
            'created_at', 'novelty_score', 'heat_score', 'stage', 'company', 'direction', 'metadata'
        ]

        data = {}
        for i, col in enumerate(columns):
            val = row[i]
            if col in ['tech_categories', 'signals', 'related_events', 'related_techs', 'authors']:
                data[col] = self._json_decode(val) if val else []
            elif col == 'metadata':
                data[col] = self._json_decode(val) if val else {}
            else:
                data[col] = val

        return TechEvent(**{k: v for k, v in data.items() if k in TechEvent.__dataclass_fields__})

    # ==================== Report Operations ====================

    def save_report(self, report: 'Report') -> bool:
        """保存报告"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        try:
            c.execute('''
                INSERT OR REPLACE INTO reports
                (id, title, content, report_type, period, created_at, events, trends, insights, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                report.id, report.title, report.content, report.report_type,
                report.period, report.created_at,
                self._json_encode(report.events),
                self._json_encode(report.trends),
                self._json_encode(report.insights),
                self._json_encode(report.metadata)
            ))
            conn.commit()
            self.stats['reports_stored'] += 1
            return True
        except Exception as e:
            print(f"Save report failed: {e}")
            return False
        finally:
            conn.close()

    def get_reports(self, report_type: str = None, limit: int = 10) -> List[Dict]:
        """获取报告列表"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        if report_type:
            c.execute('''
                SELECT * FROM reports
                WHERE report_type = ?
                ORDER BY created_at DESC LIMIT ?
            ''', (report_type, limit))
        else:
            c.execute('SELECT * FROM reports ORDER BY created_at DESC LIMIT ?', (limit,))

        rows = c.fetchall()
        conn.close()

        columns = ['id', 'title', 'content', 'report_type', 'period', 'created_at',
                   'events', 'trends', 'insights', 'metadata']

        reports = []
        for row in rows:
            report = {}
            for i, col in enumerate(columns):
                val = row[i]
                if col in ['events', 'trends', 'insights']:
                    report[col] = self._json_decode(val) if val else []
                elif col == 'metadata':
                    report[col] = self._json_decode(val) if val else {}
                else:
                    report[col] = val
            reports.append(report)

        return reports

    # ==================== Source Operations ====================

    def save_source(self, source: Dict) -> bool:
        """保存信源配置"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        try:
            c.execute('''
                INSERT OR REPLACE INTO sources
                (id, name, url, source_type, category, priority, language, enabled,
                 last_crawled, last_success, error_count, last_error, crawl_interval, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                source.get('id'), source.get('name'), source.get('url'),
                source.get('type'), source.get('category'), source.get('priority'),
                source.get('language', 'en'), source.get('enabled', 1),
                source.get('last_crawled'), source.get('last_success'),
                source.get('error_count', 0), source.get('last_error'),
                source.get('crawl_interval', 3600),
                self._json_encode(source.get('metadata', {}))
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Save source failed: {e}")
            return False
        finally:
            conn.close()

    def get_enabled_sources(self) -> List[Dict]:
        """获取启用的信源列表"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('SELECT * FROM sources WHERE enabled = 1 ORDER BY priority, name')
        rows = c.fetchall()
        conn.close()

        return self._rows_to_sources(rows)

    def update_source_status(self, source_id: str, success: bool, error: str = None):
        """更新信源状态"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        now = datetime.now().isoformat()
        if success:
            c.execute('''
                UPDATE sources
                SET last_crawled = ?, last_success = ?, error_count = 0
                WHERE id = ?
            ''', (now, now, source_id))
        else:
            c.execute('''
                UPDATE sources
                SET last_crawled = ?, error_count = error_count + 1, last_error = ?
                WHERE id = ?
            ''', (now, error, source_id))

        conn.commit()
        conn.close()

    def _rows_to_sources(self, rows: List[Tuple]) -> List[Dict]:
        """行转信源字典"""
        columns = ['id', 'name', 'url', 'source_type', 'category', 'priority', 'language',
                   'enabled', 'last_crawled', 'last_success', 'error_count', 'last_error',
                   'crawl_interval', 'metadata']

        sources = []
        for row in rows:
            source = {}
            for i, col in enumerate(columns):
                val = row[i]
                if col == 'metadata':
                    source[col] = self._json_decode(val) if val else {}
                elif col == 'enabled':
                    source[col] = bool(val)
                else:
                    source[col] = val
            sources.append(source)

        return sources

    # ==================== Statistics ====================

    def get_stats(self) -> Dict:
        """获取统计信息"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        stats = {}

        # Signal counts
        c.execute('SELECT COUNT(*) FROM signals')
        stats['total_signals'] = c.fetchone()[0]

        c.execute('SELECT COUNT(*) FROM signals WHERE processed = 1')
        stats['processed_signals'] = c.fetchone()[0]

        c.execute('SELECT COUNT(*) FROM signals WHERE published >= ?',
                   ((datetime.now() - timedelta(days=7)).isoformat(),))
        stats['signals_this_week'] = c.fetchone()[0]

        # Event counts
        c.execute('SELECT COUNT(*) FROM events')
        stats['total_events'] = c.fetchone()[0]

        c.execute('SELECT COUNT(*) FROM events WHERE time >= ?',
                   ((datetime.now() - timedelta(days=7)).isoformat(),))
        stats['events_this_week'] = c.fetchone()[0]

        # Event type distribution
        c.execute('SELECT event_type, COUNT(*) FROM events GROUP BY event_type')
        stats['events_by_type'] = {row[0]: row[1] for row in c.fetchall()}

        # Importance distribution
        c.execute('SELECT importance, COUNT(*) FROM events GROUP BY importance')
        stats['events_by_importance'] = {row[0]: row[1] for row in c.fetchall()}

        # Reports count
        c.execute('SELECT COUNT(*) FROM reports')
        stats['total_reports'] = c.fetchone()[0]

        # Sources count
        c.execute('SELECT COUNT(*) FROM sources WHERE enabled = 1')
        stats['enabled_sources'] = c.fetchone()[0]

        # Pipeline stats
        stats['pipeline'] = self.stats.copy()

        conn.close()
        return stats

    def count_events(self, event_type: str = None, since: str = None) -> int:
        """统计事件数量"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        query = 'SELECT COUNT(*) FROM events WHERE 1=1'
        params = []

        if event_type:
            query += ' AND event_type = ?'
            params.append(event_type)
        if since:
            query += ' AND time >= ?'
            params.append(since)

        c.execute(query, params)
        count = c.fetchone()[0]
        conn.close()

        return count

    def get_trending_techs(self, days: int = 14, limit: int = 10) -> List[Dict]:
        """获取热门技术"""
        since = (datetime.now() - timedelta(days=days)).isoformat()

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('''
            SELECT tech_categories, COUNT(*) as cnt
            FROM events
            WHERE time >= ?
            GROUP BY tech_categories
            ORDER BY cnt DESC
            LIMIT ?
        ''', (since, limit))

        rows = c.fetchall()
        conn.close()

        results = []
        for row in rows:
            cats = self._json_decode(row[0])
            results.append({
                'tech': cats[0] if cats else 'unknown',
                'category': cats[1] if len(cats) > 1 else 'unknown',
                'count': row[1]
            })

        return results

    def backup_to_json(self, filepath: str = None) -> str:
        """备份数据库到JSON"""
        if not filepath:
            filepath = os.path.join(
                os.path.dirname(self.db_path),
                f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            )

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        # Export signals
        c.execute('SELECT * FROM signals ORDER BY published DESC')
        signals = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]

        # Export events
        c.execute('SELECT * FROM events ORDER BY time DESC')
        events = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]

        # Export reports
        c.execute('SELECT * FROM reports ORDER BY created_at DESC')
        reports = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]

        conn.close()

        backup = {
            'exported_at': datetime.now().isoformat(),
            'signals_count': len(signals),
            'events_count': len(events),
            'reports_count': len(reports),
            'signals': signals,
            'events': events,
            'reports': reports
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(backup, f, ensure_ascii=False, indent=2)

        return filepath