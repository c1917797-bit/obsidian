"""
Obsidian Sink - 输出层
将报告输出到Obsidian vault
"""
import os
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from core.models import Report, TechEvent
from core.logger import get_logger

try:
    from layers.output.html_sink import convert_report as _convert_html
    HTML_ENABLED = True
except Exception:
    HTML_ENABLED = False

logger = get_logger("ObsidianSink")

class ObsidianSink:
    """
    Obsidian数据沉没器
    将报告写入Obsidian vault

    目录结构:
    - Daily/          日报
    - Weekly/         周报
    - Monthly/        月报
    - Inbox/          收件箱（临时）
    - ???/         未分类技术事件
    """

    def __init__(self, vault_path: str = None):
        self.vault_path = vault_path or os.environ.get(
            'OBSIDIAN_VAULT_PATH',
            r"C:\Users\Huawei\Documents\code\Obsidian\3_AI情报日历"
        )

        self._ensure_dirs()

    def _ensure_dirs(self):
        """确保目录存在"""
        self.daily_dir = os.path.join(self.vault_path, "Daily")
        self.weekly_dir = os.path.join(self.vault_path, "Weekly")
        self.monthly_dir = os.path.join(self.vault_path, "Monthly")
        self.inbox_dir = os.path.join(self.vault_path, "Inbox")

        for d in [self.daily_dir, self.weekly_dir, self.monthly_dir, self.inbox_dir]:
            os.makedirs(d, exist_ok=True)

    def save_report(self, report: Report) -> str:
        """保存报告到Obsidian"""
        try:
            if report.report_type == 'daily':
                md_path = self._save_daily_report(report)
            elif report.report_type == 'weekly':
                md_path = self._save_weekly_report(report)
            elif report.report_type == 'monthly':
                md_path = self._save_monthly_report(report)
            elif report.report_type == 'convergence':
                md_path = self._save_technical_report(report, "技术收敛")
            elif report.report_type == 'company_strategy':
                md_path = self._save_company_report(report)
            elif report.report_type == 'tech_roadmap':
                md_path = self._save_technical_report(report, "技术路线图")
            else:
                md_path = self._save_generic_report(report)

            # 同时导出HTML
            if HTML_ENABLED and md_path:
                try:
                    html_path = md_path.replace('.md', '.html')
                    _convert_html(md_path, html_path)
                except Exception as html_err:
                    logger.warning(f"HTML export failed: {html_err}")

            return md_path
        except Exception as e:
            logger.error(f"Failed to save report to Obsidian: {e}")
            return ""

    def _save_daily_report(self, report: Report) -> str:
        """保存日报 - 直接写入Daily目录，文件名格式: YYYY-MM-DD.md"""
        date_str = report.period or datetime.now().strftime('%Y-%m-%d')
        filename = f"{date_str}.md"
        filepath = os.path.join(self.daily_dir, filename)

        content = self._build_daily_content(report)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved daily report: {filepath}")
        return filepath

    def _build_daily_content(self, report: Report) -> str:
        """构建日报内容"""
        date_str = report.period or datetime.now().strftime('%Y-%m-%d')

        events_text = ""
        if hasattr(report, 'events') and report.events:
            events_text = f"\n## 关联事件\n\n"
            for event_id in report.events[:10]:
                events_text += f"- {event_id}\n"

        categories_text = ""
        if hasattr(report, 'trends') and report.trends:
            by_category = report.trends.get('by_category', {})
            if by_category:
                categories_text = "\n## 分类统计\n\n"
                for cat, count in by_category.items():
                    categories_text += f"- {cat}: {count} 条\n"

        content = f"""---
type: daily-report
date: {date_str}
created: {report.created_at}
tags: [AI-Intelligence, Daily]
---

# AI Infra Daily - {date_str}

## 今日概要

{report.content}

{categories_text}
{events_text}

## 反向链接

> [!info] 相关笔记
> - [[Weekly_{self._get_week_str()}|本周周报]]
> - [[技术收敛_{date_str[:7]}|本月技术收敛]]
> - [[4_AI情报洞察/技术洞察/多卡协同/多卡极致推理系统技术规划报告---以终为始版|多卡协同技术洞察]]

---

**生成时间**: {report.created_at}
**Report ID**: {report.id}
"""

        return content

    def _save_weekly_report(self, report: Report) -> str:
        """保存周报"""
        week_str = report.period or self._get_week_str()
        filename = f"Weekly_{week_str}.md"
        filepath = os.path.join(self.weekly_dir, filename)

        trends_text = ""
        if hasattr(report, 'trends') and report.trends:
            trending = report.trends.get('trending', [])
            if trending:
                trends_text = f"\n## 本周热门技术\n\n"
                for tech in trending:
                    trends_text += f"- {tech}\n"

        events_text = ""
        if hasattr(report, 'events') and report.events:
            events_text = f"\n## 事件统计\n\n共记录 {len(report.events)} 条事件\n"

        content = f"""---
type: weekly-report
period: {week_str}
created: {report.created_at}
tags: [AI-Intelligence, Weekly]
---

# Weekly Report - {week_str}

## 本周技术演化

{report.content}

{trends_text}
{events_text}

## 反向链接

> [!info] 相关笔记
> - [[Daily/{datetime.now().strftime('%Y-%m-%d')}|今日日报]]
> - [[Monthly/Monthly_{datetime.now().strftime('%Y-%m')}|本月月报]]
> - [[技术收敛_{datetime.now().strftime('%Y-%m')}|技术收敛报告]]

---

**生成时间**: {report.created_at}
**Report ID**: {report.id}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved weekly report: {filepath}")
        return filepath

    def _save_monthly_report(self, report: Report) -> str:
        """保存月报"""
        month_str = report.period or datetime.now().strftime('%Y-%m')
        filename = f"Monthly_{month_str}.md"
        filepath = os.path.join(self.monthly_dir, filename)

        content = f"""---
type: monthly-report
period: {month_str}
created: {report.created_at}
tags: [AI-Intelligence, Monthly]
---

# Monthly Report - {month_str}

## 本月技术战略总结

{report.content}

---

**生成时间**: {report.created_at}
**Report ID**: {report.id}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved monthly report: {filepath}")
        return filepath

    def _save_technical_report(self, report: Report, category: str) -> str:
        """保存技术报告"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        safe_category = self._sanitize_filename(category)
        filename = f"{safe_category}_{date_str}_{report.id[:8]}.md"

        if category == "技术收敛":
            filepath = os.path.join(self.weekly_dir, filename)
        else:
            filepath = os.path.join(self.inbox_dir, filename)

        content = f"""---
type: {report.report_type}
category: {category}
date: {date_str}
created: {report.created_at}
tags: [AI-Intelligence, {category}]
---

# {report.title}

{report.content}

---

**生成时间**: {report.created_at}
**Report ID**: {report.id}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved technical report: {filepath}")
        return filepath

    def _save_company_report(self, report: Report) -> str:
        """保存公司战略报告"""
        company_name = report.title.split(' ')[0] if report.title else "Unknown"
        month_str = datetime.now().strftime('%Y-%m')
        filename = f"{company_name}_{month_str}.md"
        filepath = os.path.join(self.inbox_dir, filename)

        content = f"""---
type: company-strategy
company: {company_name}
period: {report.period or month_str}
created: {report.created_at}
tags: [AI-Intelligence, Company, {company_name}]
---

# {report.title}

{report.content}

---
**生成时间**: {report.created_at}
**Report ID**: {report.id}
**关联事件**: {len(report.events) if hasattr(report, 'events') else 0}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved company report: {filepath}")
        return filepath

    def _save_generic_report(self, report: Report) -> str:
        """保存通用报告"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"{report.report_type}_{date_str}_{report.id[:8]}.md"
        filepath = os.path.join(self.inbox_dir, filename)

        content = f"""---
type: {report.report_type}
date: {date_str}
created: {report.created_at}
tags: [AI-Intelligence]
---

# {report.title}

{report.content}

---
**生成时间**: {report.created_at}
**Report ID**: {report.id}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Saved generic report: {filepath}")
        return filepath

    def save_event(self, event: TechEvent) -> str:
        """保存单个事件到Inbox"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        safe_entity = self._sanitize_filename(event.entity or 'unknown')
        filename = f"Event_{safe_entity}_{event.id[:8]}.md"
        filepath = os.path.join(self.inbox_dir, filename)

        content = f"""---
type: tech-event
event_type: {event.event_type}
entity: {event.entity}
entity_type: {event.entity_type}
tech_categories: {', '.join(event.tech_categories) if event.tech_categories else 'unknown'}
importance: {event.importance}
confidence: {event.confidence}
stage: {event.stage}
date: {event.time}
created: {event.created_at}
tags: [AI-Intelligence, Event, {event.entity}]
---

# {event.title or '技术事件'}

## 基本信息

- **实体**: {event.entity}
- **类型**: {event.event_type}
- **技术分类**: {', '.join(event.tech_categories) if event.tech_categories else '未知'}
- **重要性**: {event.importance}
- **阶段**: {event.stage}

## 摘要

{event.summary or '无'}

## 创新点

{event.innovation or '未知'}

## 解决的问题

{event.problem_solved or '未知'}

## 原始链接

{event.url or '无'}

## 来源

{event.source}

---
**Event ID**: {event.id}
**Heat Score**: {event.heat_score}
**Novelty Score**: {event.novelty_score}
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filepath

    def save_events_batch(self, events: List[TechEvent]) -> List[str]:
        """批量保存事件"""
        saved_paths = []
        for event in events:
            try:
                path = self.save_event(event)
                saved_paths.append(path)
            except Exception as e:
                logger.error(f"Failed to save event {event.id}: {e}")
        return saved_paths

    def create_daily_note(self, date: str = None) -> str:
        """创建或更新每日笔记"""
        date_str = date or datetime.now().strftime('%Y-%m-%d')
        filepath = os.path.join(self.daily_dir, f"{date_str}.md")

        if os.path.exists(filepath):
            return filepath

        content = f"""---
date: {date_str}
tags: [Daily, AI-Intelligence]
type: daily-note
---

# {date_str}

## 今日工作

## 今日发现

## 明日计划

"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Created daily note: {filepath}")
        return filepath

    def _get_week_str(self) -> str:
        """获取当前周字符串"""
        today = datetime.now()
        week_num = today.isocalendar()[1]
        return f"{today.year}-W{week_num:02d}"

    def _sanitize_filename(self, name: str) -> str:
        """清理文件名，移除不合法字符"""
        name = name.replace('/', '_').replace('\\', '_')
        name = re.sub(r'[<>:"|?*]', '', name)
        return name[:50]

    def get_recent_reports(self, report_type: str = None, limit: int = 10) -> List[str]:
        """获取最近的报告文件"""
        if report_type == 'daily':
            directory = self.daily_dir
        elif report_type == 'weekly':
            directory = self.weekly_dir
        elif report_type == 'monthly':
            directory = self.monthly_dir
        else:
            directory = self.vault_path

        if not os.path.exists(directory):
            return []

        files = []
        for f in os.listdir(directory):
            if f.endswith('.md'):
                filepath = os.path.join(directory, f)
                files.append((os.path.getmtime(filepath), filepath))

        files.sort(reverse=True)
        return [f[1] for f in files[:limit]]

    def sync_to_obsidian(self, reports: List[Report], events: List[TechEvent] = None) -> Dict:
        """同步报告和事件到Obsidian"""
        results = {
            'reports_saved': 0,
            'events_saved': 0,
            'paths': []
        }

        for report in reports:
            try:
                path = self.save_report(report)
                if path:
                    results['reports_saved'] += 1
                    results['paths'].append(path)
            except Exception as e:
                logger.error(f"Failed to sync report: {e}")

        if events:
            event_paths = self.save_events_batch(events)
            results['events_saved'] = len(event_paths)
            results['paths'].extend(event_paths)

        logger.info(f"Synced to Obsidian: {results['reports_saved']} reports, {results['events_saved']} events")
        return results

    def get_vault_stats(self) -> Dict:
        """获取Vault统计信息"""
        stats = {
            'vault_path': self.vault_path,
            'daily_count': 0,
            'weekly_count': 0,
            'monthly_count': 0,
            'inbox_count': 0
        }

        for dir_path, stats_key in [
            (self.daily_dir, 'daily_count'),
            (self.weekly_dir, 'weekly_count'),
            (self.monthly_dir, 'monthly_count'),
            (self.inbox_dir, 'inbox_count')
        ]:
            if os.path.exists(dir_path):
                count = len([f for f in os.listdir(dir_path) if f.endswith('.md')])
                stats[stats_key] = count

        return stats

    def save_trend_report(self, trend_summary: Dict) -> str:
        """保存趋势追踪报告到 识别/趋势追踪/趋势追踪.md"""
        vault_base = r"C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网"
        filepath = os.path.join(vault_base, "识别", "趋势追踪", "趋势追踪.md")
        date_str = datetime.now().strftime('%Y-%m-%d')

        trending_details = trend_summary.get('trending_details', [])
        stage_emoji = {'emerging': '🟢', 'growing': '🟡', 'peak': '🟠', 'converging': '🔴', 'mature': '⚪'}
        trending_rows = ""
        for t in trending_details[:10]:
            emoji = stage_emoji.get(t.get('stage', 'emerging'), '⚪')
            trending_rows += f"| {t['tech']} | {t.get('heat_score', 0):.3f} | {emoji} {t.get('stage', '')} | {t.get('count', 0)} |\n"

        converging_details = trend_summary.get('converging_details', [])
        converging_rows = ""
        for t in converging_details[:10]:
            converging_rows += f"| {t['tech']} | {t.get('activity_ratio', 0):.2f} | {t.get('current_activity', 0)} |\n"

        nl = "\n"
        content = f"""---
type: signal-tracker
created: {date_str}
updated: {date_str}
tags: [AI-Intelligence, 信号, 趋势]
---

# 趋势追踪

> [!info] 自动生成
> 由 AI Intelligence OS TrendEngine 自动更新 | 更新时间: {date_str}

## 活跃趋势（7日热门）

| 技术 | 热度分数 | 阶段 | 事件数 |
|------|----------|------|--------|
{trending_rows if trending_rows else f"| - | - | - | - |{nl}"}

## 收敛中的技术（30日）

| 技术 | 活跃度比率 | 周事件数 |
|------|------------|----------|
{converging_rows if converging_rows else f"| - | - | - |{nl}"}

## 趋势摘要

- **热门技术**: {', '.join(trend_summary.get('trending_techs', [])[:5]) or '无'}
- **收敛技术**: {', '.join(trend_summary.get('converging_techs', [])[:5]) or '无'}
- **生产就绪**: {', '.join(trend_summary.get('production_ready', [])[:5]) or '无'}

## 生成信息

- 生成时间: {trend_summary.get('generated_at', date_str)}
- 数据来源: AI Intelligence OS TrendEngine
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"趋势追踪已更新: {filepath}")
        return filepath
