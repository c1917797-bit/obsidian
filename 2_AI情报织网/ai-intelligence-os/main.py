"""
重构后的完整流水线
Signal → Classify → Store → Trend → Insight → Output
"""
import os
os.environ['PYTHONUTF8'] = '1'

import sys
import io
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Optional

if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except:
        pass

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.models import Signal, TechEvent, Report
from core.storage import UnifiedStore
from core.logger import get_logger, logger
from core.minimax_client import get_client
from core.pipeline_lock import PipelineLock

from layers.agents.crawler_agent import CrawlerAgent
from layers.agents.classifier_agent import ClassifierAgent
from layers.trends.trend_engine import TrendEngine
from layers.trends.signal_source_tracker import SignalSourceTracker
from layers.insight.insight_agent import InsightAgent
from layers.output.obsidian_sink import ObsidianSink
from layers.quality.quality_gate import QualityGate
from layers.scraper.article_scraper import ArticleScraper
from layers.paper_analysis.conference_papers import ConferencePaperStore, get_available_venues
from layers.paper_analysis import PaperAnalysisIntegration, DrawIOIntegration
from layers.paper_analysis.deep_research import DeepResearchPipeline, ResearchQuery
from layers.paper_analysis.litrep_report import LiteraryProgrammingReport, ReportTemplates
from layers.notifications.notifications import NotificationCenter
from layers.topics import TopicsRegistry

class IntelligenceOS:
    """
    AI情报操作系统 - 统一协调器

    架构：
    [CrawlerAgent] → [ClassifierAgent] → [UnifiedStore] → [TrendEngine] → [InsightAgent] → [ObsidianSink]
         ↓               ↓                  ↓               ↓              ↓            ↓
      Signals        TechEvents         SQLite        Trends        Reports      Markdown

    支持模式：
    - daily: 每日流水线
    - weekly: 周报生成
    - query: 自然语言查询
    - stats: 查看统计信息
    - backup: 备份数据
    """

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('MINIMAX_API_KEY')

        if not self.api_key:
            raise ValueError("MINIMAX_API_KEY is not set. Please provide --api-key or set environment variable.")

        os.environ['MINIMAX_API_KEY'] = self.api_key

        self.store = UnifiedStore()
        sources_file = os.path.join(os.path.dirname(__file__), 'config', 'sources_comprehensive.json')
        self.crawler = CrawlerAgent(store=self.store, sources_file=sources_file)
        self.classifier = ClassifierAgent(store=self.store, use_llm=True)
        self.trend_engine = TrendEngine(store=self.store)
        self.insight_agent = InsightAgent(store=self.store, trend_engine=self.trend_engine)
        self.obsidian_sink = ObsidianSink()
        self.quality_gate = QualityGate(store=self.store)
        self.scraper = ArticleScraper()

        self.conference_store = ConferencePaperStore()
        self.paper_analysis = PaperAnalysisIntegration(conference_store=self.conference_store, store=self.store)
        self.drawio = DrawIOIntegration()
        self.deep_research = DeepResearchPipeline(store=self.store)
        self.litprog_report = LiteraryProgrammingReport()
        self.notification_center = NotificationCenter()
        self.topics_registry = TopicsRegistry()

        self.stats = {
            'signals_crawled': 0,
            'events_classified': 0,
            'reports_generated': 0,
            'errors': 0,
            'quality_check_passed': False
        }

        logger.info("IntelligenceOS initialized")

    def run_daily_pipeline(self, force: bool = False, use_metadata_first: bool = True) -> Dict:
        """
        执行每日流水线
        1. 采集信号 (Metadata First模式可选)
        2. 分类事件
        3. 趋势分析
        4. 生成报告
        5. 输出到Obsidian

        Args:
            force: 是否强制重新运行
            use_metadata_first: 是否使用Metadata First两阶段采集 (默认True)
        """
        logger.info("=" * 60)
        logger.info("AI Intelligence OS - 每日流水线")
        logger.info(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"采集模式: {'Metadata First (两阶段)' if use_metadata_first else 'Legacy (全量)'}")
        logger.info("=" * 60)

        start_time = datetime.now()
        top_scored_signals = []

        try:
            logger.log_step("CRAWL", "STARTED")
            if use_metadata_first:
                signals, event_signals, tech_signals, trend_signals = self.crawler.crawl_all_metadata_first(
                    exclude_categories=['news', 'news_cn'],
                    top_n=30,
                    min_score=5.0
                )
                top_scored_signals = event_signals + tech_signals + trend_signals
            else:
                signals = self.crawler.crawl_all(exclude_categories=['news', 'news_cn'])
                top_scored_signals = []
            self.stats['signals_crawled'] = len(signals)
            logger.info(f"采集完成: {len(signals)} 条信号")
            if top_scored_signals:
                logger.info(f"高分信号(Top 30): {len(top_scored_signals)} 条")
            logger.log_step("CRAWL", "COMPLETED", count=len(signals), top_n=len(top_scored_signals))

        except Exception as e:
            logger.error(f"Crawl阶段失败: {e}")
            self.stats['errors'] += 1
            signals = []

        try:
            logger.log_step("CLASSIFY", "STARTED")
            if signals:
                signals_for_classify = signals
                if top_scored_signals and use_metadata_first:
                    scored_ids = {s.signal_id for s in top_scored_signals}
                    signals_for_classify = [sig for sig in signals if sig.generate_id() in scored_ids]
                    logger.info(f"使用高分信号子集进行分类: {len(signals_for_classify)} 条 (来自 {len(top_scored_signals)} 高分)")
                else:
                    logger.info(f"使用全部信号进行分类: {len(signals)} 条")
                events = self.classifier.classify_all(signals_for_classify)
                saved_count = self.store.save_events(events)
                self.stats['events_classified'] = len(events)
                logger.info(f"分类完成: {len(events)} 条事件, 保存 {saved_count} 条")
                logger.log_step("CLASSIFY", "COMPLETED", count=len(events), saved=saved_count)

                # 课题靶点标注
                try:
                    from layers.topics.topics_registry import load_registry
                    registry = load_registry()
                    tagged_count = 0
                    for event in events:
                        tag_result = registry.tag_event(event)
                        if tag_result['matched_topics']:
                            # 将课题标签存入事件的 metadata
                            if not hasattr(event, 'metadata') or event.metadata is None:
                                event.metadata = {}
                            event.metadata['topics'] = tag_result['matched_topics']
                            event.metadata['is_strategic'] = tag_result['is_strategic']
                            tagged_count += 1
                    if tagged_count > 0:
                        # 重新保存带标签的事件
                        self.store.save_events(events)
                        logger.info(f"课题标注完成: {tagged_count} 条事件打标")
                except Exception as e:
                    logger.warning(f"课题标注失败（不影响主流程）: {e}")

            else:
                events = []
                logger.info("无新信号，跳过分类")
                logger.log_step("CLASSIFY", "SKIPPED", reason="no_signals")

        except Exception as e:
            logger.error(f"Classify阶段失败: {e}")
            self.stats['errors'] += 1
            events = []

        try:
            logger.log_step("INBOX", "STARTED")
            if events:
                event_paths = self.obsidian_sink.save_events_batch(events)
                logger.info(f"已写入 {len(event_paths)} 条事件到 Inbox")
                logger.log_step("INBOX", "COMPLETED", count=len(event_paths))
            else:
                logger.log_step("INBOX", "SKIPPED", reason="no_events")
        except Exception as e:
            logger.error(f"Inbox阶段失败: {e}")
            self.stats['errors'] += 1

        try:
            logger.log_step("TREND", "STARTED")
            trend_summary = self.trend_engine.get_trend_summary(days=7)
            logger.info(f"趋势分析: {len(trend_summary.get('trending_techs', []))} 热门技术")
            logger.log_step("TREND", "COMPLETED", trending=len(trend_summary.get('trending_techs', [])))

        except Exception as e:
            logger.error(f"Trend阶段失败: {e}")
            trend_summary = {}
            self.stats['errors'] += 1

        try:
            logger.log_step("SOURCE_CORRELATION", "STARTED")
            tracker = SignalSourceTracker(store=self.store)
            correlation = tracker.get_source_stats(days=7)
            tracker.save_correlation_report(correlation)
            logger.log_step("SOURCE_CORRELATION", "COMPLETED")
        except Exception as e:
            logger.error(f"Source correlation failed: {e}")

        try:
            logger.log_step("QUALITY", "STARTED")
            quality_passed, quality_results = self.quality_gate.run_quality_gates(
                events, signals_count=self.stats['signals_crawled']
            )
            self.stats['quality_check_passed'] = quality_passed

            if quality_passed:
                logger.info("质量门禁检查通过")
                logger.log_step("QUALITY", "PASSED", events_count=len(events))
            else:
                logger.warning(f"质量门禁未通过: {quality_results.get('recommendations', [])}")
                logger.log_step("QUALITY", "FAILED", issues=quality_results.get('issues', []))
                logger.log_step("QUALITY", "PROCEEDING", reason="force_or_partial")

        except Exception as e:
            logger.error(f"Quality阶段失败: {e}")
            self.stats['errors'] += 1

        # 预排序事件（避免在报告生成时重复排序导致比较错误）
        def _sort_key(e):
            priority_order = {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}
            imp = getattr(e, 'importance', 'P2') or 'P2'
            return (priority_order.get(imp, 2), getattr(e, 'time', ''))

        if events:
            events = sorted(events, key=_sort_key)

        # 初始化报告变量（确保OUTPUT阶段一定可以访问）
        daily_brief = None
        weekly_report = None

        try:
            logger.log_step("REPORT", "STARTED")
            daily_brief = self.insight_agent.generate_daily_brief(events)
            weekly_report = self.insight_agent.generate_weekly_evolution_report(events)
            self.stats['reports_generated'] += 2
            logger.info(f"报告生成: Daily + Weekly")
            logger.log_step("REPORT", "COMPLETED", daily=daily_brief.id, weekly=weekly_report.id)

        except Exception as e:
            logger.error(f"Report阶段失败: {e}")
            self.stats['errors'] += 1
            # daily_brief 和 weekly_report 保持 None，OUTPUT阶段会处理这种情况

        try:
            logger.log_step("OUTPUT", "STARTED")
            # 写入趋势追踪
            if trend_summary:
                trend_path = self.obsidian_sink.save_trend_report(trend_summary)
                logger.info(f"趋势追踪已更新: {trend_path}")
            if daily_brief:
                report_path = self.obsidian_sink.save_report(daily_brief)
                daily_brief.metadata['report_path'] = report_path
                logger.info(f"日报已输出到Obsidian: {report_path}")
            else:
                logger.warning("跳过日报输出：daily_brief为None")
            if weekly_report:
                self.obsidian_sink.save_report(weekly_report)
                logger.info("周报已输出到Obsidian")
            else:
                logger.warning("跳过周报输出：weekly_report为None")
            logger.log_step("OUTPUT", "COMPLETED")

        except Exception as e:
            logger.error(f"Output阶段失败: {e}")
            self.stats['errors'] += 1

        try:
            logger.log_step("NOTIFY", "STARTED")
            if daily_brief:
                # 用 send_feishu_digest 精选格式发飞书
                import sys
                sys.path.insert(0, r'C:\Users\Huawei\.openclaw\workspace')
                import send_feishu_digest as sfd
                report_path = os.path.join(
                    self.obsidian_sink.daily_dir,
                    f"{daily_brief.period}.md"
                )
                if os.path.exists(report_path):
                    sections = sfd.parse_sections(report_path)
                    feishu_content = sfd.format_digest(sections, daily_brief.period)
                else:
                    feishu_content = daily_brief.content  # fallback
                # 只发 telegram/wecom（不发飞书，飞书由 send_feishu_digest 精选摘要单独发）
                notify_result = self.notification_center.send_daily_report(feishu_content, channels=['telegram', 'wecom', 'email'])
                success_channels = [ch for ch, ok in notify_result.items() if ok]
                failed_channels = [ch for ch, ok in notify_result.items() if not ok]
                logger.info(f"推送完成: 成功 {len(success_channels)} 个渠道 ({', '.join(success_channels)})")
                if failed_channels:
                    logger.warning(f"推送失败: {', '.join(failed_channels)}")
                logger.log_step("NOTIFY", "COMPLETED", success=len(success_channels))
            else:
                logger.info("跳过推送：无日报内容")
                logger.log_step("NOTIFY", "SKIPPED", reason="no_daily_brief")

        except Exception as e:
            logger.error(f"Notify阶段失败: {e}")
            self.stats['errors'] += 1

        elapsed = (datetime.now() - start_time).total_seconds()

        result = {
            'status': 'success' if self.stats['errors'] == 0 else 'partial',
            'signals_crawled': self.stats['signals_crawled'],
            'events_classified': self.stats['events_classified'],
            'reports_generated': self.stats['reports_generated'],
            'quality_check_passed': self.stats['quality_check_passed'],
            'errors': self.stats['errors'],
            'elapsed_seconds': elapsed
        }

        logger.info("=" * 60)
        logger.info("每日流水线完成")
        logger.info(f"  采集: {self.stats['signals_crawled']} 条信号")
        logger.info(f"  分类: {self.stats['events_classified']} 条事件")
        logger.info(f"  质量门禁: {'通过' if self.stats['quality_check_passed'] else '未通过'}")
        logger.info(f"  报告: {self.stats['reports_generated']} 份")
        logger.info(f"  错误: {self.stats['errors']} 个")
        logger.info(f"  耗时: {elapsed:.1f} 秒")
        logger.info("=" * 60)

        logger.log_metric('daily_pipeline_completed', 1)

        return result

    def run_weekly_pipeline(self) -> Dict:
        """执行周报流水线"""
        logger.info("=" * 60)
        logger.info("AI Intelligence OS - 周报流水线")
        logger.info("=" * 60)

        try:
            events = self.store.get_recent_events(days=7, limit=200)
            logger.info(f"本周事件: {len(events)} 条")

            logger.log_step("WEEKLY_REPORT", "STARTED")
            weekly_report = self.insight_agent.generate_weekly_evolution_report(events)
            logger.log_step("WEEKLY_REPORT", "COMPLETED")

            logger.log_step("CONVERGENCE_REPORT", "STARTED")
            convergence_report = self.insight_agent.generate_convergence_report()
            logger.log_step("CONVERGENCE_REPORT", "COMPLETED")

            self.obsidian_sink.save_report(weekly_report)
            self.obsidian_sink.save_report(convergence_report)

            self.stats['reports_generated'] += 2

            logger.info("周报生成完成")
            logger.info(f"  Weekly: {weekly_report.id}")
            logger.info(f"  Convergence: {convergence_report.id}")

            return {
                'status': 'success',
                'weekly_report': weekly_report.id,
                'convergence_report': convergence_report.id,
                'reports_generated': 2
            }

        except Exception as e:
            logger.error(f"Weekly pipeline failed: {e}")
            return {'status': 'error', 'message': str(e)}

    def query(self, question: str) -> str:
        """
        自然语言查询
        支持：
        - trending/热门: 近期热门技术
        - convergence/收敛: 技术收敛状态
        - company/公司: 公司战略分析
        - roadmap/路线: 技术路线图
        - stats/统计: 系统统计
        """
        question_lower = question.lower().strip()

        if 'trending' in question_lower or '热门' in question:
            return self._query_trending()

        elif 'convergence' in question_lower or '收敛' in question:
            return self._query_convergence()

        elif 'company' in question_lower or '公司' in question:
            for company in ['OpenAI', 'Anthropic', 'DeepSeek', 'Google', 'Meta', 'Microsoft']:
                if company.lower() in question_lower:
                    return self._query_company(company)
            return "请指定公司名称: OpenAI, Anthropic, DeepSeek, Google, Meta, Microsoft"

        elif 'roadmap' in question_lower or '路线' in question:
            tech_area = self._extract_tech_area(question)
            return self._query_roadmap(tech_area)

        elif 'stats' in question_lower or '统计' in question:
            return self._query_stats()

        elif 'anomaly' in question_lower or '异常' in question:
            return self._query_anomalies()

        else:
            return self._query_general(question)

    def _query_trending(self) -> str:
        """查询热门技术"""
        trend_summary = self.trend_engine.get_trend_summary(days=7)
        trending = trend_summary.get('trending_techs', [])

        if not trending:
            return "本周无热门技术记录"

        response = "本周热门技术:\n\n"
        for i, tech in enumerate(trending[:5], 1):
            response += f"{i}. {tech}\n"

        response += f"\n共 {len(trend_summary.get('trending_details', []))} 个技术有热度变化"

        return response

    def _query_convergence(self) -> str:
        """查询技术收敛"""
        converging = self.trend_engine.get_converging_techs(days=30)

        if not converging:
            return "当前无明显收敛中的技术"

        response = "正在收敛的技术:\n\n"
        for item in converging[:5]:
            response += f"- {item['tech']}: 活跃度比率 {item['activity_ratio']}\n"
            response += f"  当前 {item['current_activity']} 条事件/周\n"

        return response

    def _query_company(self, company: str) -> str:
        """查询公司战略"""
        report = self.insight_agent.generate_company_strategy_report(company)
        return f"## {company} 战略分析\n\n{report.content}"

    def _query_roadmap(self, tech_area: str) -> str:
        """查询技术路线"""
        report = self.insight_agent.generate_tech_roadmap(tech_area)
        return f"## {tech_area} 技术路线图\n\n{report.content}"

    def _query_stats(self) -> str:
        """查询系统统计"""
        stats = self.store.get_stats()

        response = "## 系统统计\n\n"
        response += f"总信号数: {stats.get('total_signals', 0)}\n"
        response += f"本周信号: {stats.get('signals_this_week', 0)}\n"
        response += f"总事件数: {stats.get('total_events', 0)}\n"
        response += f"本周事件: {stats.get('events_this_week', 0)}\n"
        response += f"报告数: {stats.get('total_reports', 0)}\n"
        response += f"启用信源: {stats.get('enabled_sources', 0)}\n\n"

        response += "事件类型分布:\n"
        for et, count in stats.get('events_by_type', {}).items():
            response += f"  {et}: {count}\n"

        response += "\n重要性分布:\n"
        for imp, count in stats.get('events_by_importance', {}).items():
            response += f"  {imp}: {count}\n"

        return response

    def _query_anomalies(self) -> str:
        """查询异常信号"""
        anomalies = self.trend_engine.detect_anomalies(days=7)

        if not anomalies:
            return "本周无明显异常信号"

        response = "## 异常信号\n\n"
        for anomaly in anomalies[:5]:
            response += f"- [{anomaly['type']}] {anomaly['tech']}\n"
            response += f"  {anomaly['description']}\n"

        return response

    def _query_general(self, question: str) -> str:
        """通用查询"""
        events = self.store.get_recent_events(days=7, limit=20)

        prompt = f"""基于以下近期技术事件，回答用户问题。

用户问题: {question}

近期事件:
"""
        for e in events[:10]:
            prompt += f"- {e.title[:80]}\n"

        prompt += "\n请简洁回答用户问题，不要重复事件列表。"

        messages = [{"role": "user", "content": prompt}]
        try:
            client = get_client()
            return client.chat(messages)
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return f"查询失败: {e}"

    def _extract_tech_area(self, question: str) -> str:
        """从问题中提取技术领域"""
        tech_keywords = [
            'speculative decoding', 'kv cache', 'flash attention',
            'quantization', 'moe', 'multi-agent', 'agent',
            'inference optimization', 'runtime'
        ]

        question_lower = question.lower()
        for tech in tech_keywords:
            if tech in question_lower:
                return tech

        return 'inference optimization'

    def get_stats(self) -> Dict:
        """获取完整统计"""
        store_stats = self.store.get_stats()
        pipeline_stats = self.stats

        return {
            'pipeline': pipeline_stats,
            'storage': store_stats,
            'uptime': logger.get_metrics().get('uptime', 0)
        }

    def backup(self, filepath: str = None) -> str:
        """备份数据"""
        if not filepath:
            filepath = os.path.join(
                os.path.dirname(self.store.db_path),
                f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            )

        try:
            backup_path = self.store.backup_to_json(filepath)
            logger.info(f"Backup saved: {backup_path}")
            return backup_path
        except Exception as e:
            logger.error(f"Backup failed: {e}")
            return ""

def main():
    parser = argparse.ArgumentParser(description='AI Intelligence OS')
    parser.add_argument('--mode', choices=[
        'daily', 'weekly', 'query', 'stats', 'backup',
        'papers', 'diagram', 'research'
    ], default='daily')
    parser.add_argument('--question', help='查询模式的问题')
    parser.add_argument('--api-key', help='MiniMax API Key')
    parser.add_argument('--force', action='store_true', help='强制执行（跳过检查）')
    parser.add_argument('--venue', help='顶会名称 (iclr, neurips, icml, cvpr等)')
    parser.add_argument('--year', type=int, help='年份 (2024, 2025等)')
    parser.add_argument('--keyword', help='论文搜索关键词')
    parser.add_argument('--topic', help='研究主题')
    parser.add_argument('--depth', choices=['shallow', 'medium', 'deep'], default='deep', help='研究深度')
    args = parser.parse_args()

    try:
        os_version = IntelligenceOS(api_key=args.api_key)

        if args.mode == 'daily':
            lock = PipelineLock(wait_timeout=0)
            with lock as acquired:
                if acquired is None:
                    print("Pipeline already running, skip")
                    return
            result = os_version.run_daily_pipeline(force=args.force)
            print(f"\n流水线执行完成: {result['status']}")

        elif args.mode == 'weekly':
            lock = PipelineLock(wait_timeout=0)
            with lock as acquired:
                if acquired is None:
                    print("Pipeline already running, skip")
                    return
            result = os_version.run_weekly_pipeline()
            print(f"\n周报生成完成: {result['status']}")

        elif args.mode == 'query':
            if not args.question:
                print("请提供 --question 参数")
                return
            answer = os_version.query(args.question)
            print(answer)

        elif args.mode == 'stats':
            stats = os_version.get_stats()
            print(f"\n系统统计:\n{stats}")

        elif args.mode == 'backup':
            path = os_version.backup()
            print(f"\n备份已保存: {path}")

        elif args.mode == 'papers':
            if not args.venue or not args.year:
                print("请提供 --venue 和 --year 参数")
                return
            papers = os_version.conference_store.search_papers(
                venue=args.venue, year=args.year, keyword=args.keyword, limit=20
            )
            print(f"\n{args.venue.upper()} {args.year} 论文列表:")
            for p in papers:
                print(f"  [{p.citation_count} citations] {p.title[:70]}")

        elif args.mode == 'diagram':
            description = args.question or "transformer architecture"
            output = os_version.drawio.generate_architecture_diagram(description)
            print(f"\n图表已生成: {output}")

        elif args.mode == 'research':
            if not args.topic:
                print("请提供 --topic 参数")
                return
            depth = getattr(args, 'depth', None) or 'deep'
            from layers.research.deep_research_agent import DeepResearchAgent
            from layers.topics.topics_registry import load_registry

            # 加载课题注册表，获取课题关键词
            registry = load_registry()
            match_result = registry.match_topic(args.topic)
            if match_result:
                logger.info(f"课题 {args.topic} 匹配到注册靶点: {match_result}")
                topic_keywords = []
                for t in match_result:
                    t_obj = registry._find_topic(t)
                    if t_obj:
                        topic_keywords.extend(t_obj.get('keywords', []))
            else:
                topic_keywords = [args.topic]

            # 用课题关键词初始化 DeepResearchAgent
            agent = DeepResearchAgent(topic_keywords=topic_keywords)
            report = agent.run(topic=args.topic, depth=depth)
            print("\n" + "=" * 60)
            print(f"研究课题: {args.topic}")
            print(f"置信度: {report.confidence}")
            print(f"参考文献: {len(report.references)} 条")
            print("=" * 60)
            print(report.markdown)
            # 保存到 Obsidian
            saved_path = agent.save_report_to_obsidian(report)
            print(f"\n报告已保存: {saved_path}")

    except ValueError as e:
        print(f"初始化失败: {e}")
        print("\n请设置环境变量 MINIMAX_API_KEY 或提供 --api-key 参数")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()