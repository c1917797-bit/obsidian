"""
DeepResearchAgent - 多轮深度研究Agent
实现真正的课题驱动的多轮研究流程
"""
import os
from typing import List, Dict, Optional
from datetime import datetime

from core.logger import get_logger
from core.minimax_client import get_client
from layers.research import ResearchReport, Evidence, ResearchTopic, ResearchGap, MethodComparison
from layers.research.research_topic_analyzer import ResearchTopicAnalyzer
from layers.research.evidence_collector import EvidenceCollector
from layers.research.gap_analyzer import GapAnalyzer

logger = get_logger("DeepResearchAgent")


class DeepResearchAgent:
    """
    深度研究Agent - 多轮研究流程

    流程：
    1. 课题分析（ResearchTopicAnalyzer）
    2. 第一轮搜索 → 初步证据收集
    3. Gap分析 → 识别研究空白
    4. 第二轮搜索（针对空白补充）
    5. 综合生成报告（ResearchReportSynthesizer）
    """

    def __init__(self, topic_keywords: List[str] = None):
        self.analyzer = ResearchTopicAnalyzer()
        self.collector = EvidenceCollector()
        self.gap_analyzer = GapAnalyzer()
        self.client = None  # 延迟初始化
        self.topic_keywords = topic_keywords or []  # 课题关键词用于优先查历史

    def run(self, topic: str, depth: str = "deep") -> ResearchReport:
        """
        主入口：执行多轮研究

        Args:
            topic: 研究课题
            depth: 研究深度 shallow / medium / deep

        Returns:
            ResearchReport: 结构化研究报告
        """
        logger.info(f"开始深度研究: {topic} (depth={depth})")
        start_time = datetime.now()

        try:
            self.client = get_client()
        except Exception:
            logger.warning("MiniMax client unavailable, using basic mode")
            self.client = None

        # ===== Phase 1: 课题分析 =====
        logger.info("[Phase 1] 课题分析...")
        research_topic = self.analyzer.analyze(topic)
        logger.info(f"分解为 {len(research_topic.decomposed_questions)} 个研究问题")

        # ===== Phase 1.5: 从历史数据库优先收集 =====
        if self.topic_keywords:
            logger.info(f"[Phase 1.5] 从历史数据库查找课题积累...")
            historical = self._collect_from_history()
            if historical:
                logger.info(f"找到 {len(historical)} 条历史积累，优先加入证据池")
                initial_evidence = historical + initial_evidence

        # ===== Phase 2: 第一轮证据收集 =====
        logger.info("[Phase 2] 第一轮证据收集...")
        initial_evidence = self.collector.collect(research_topic)
        logger.info(f"收集到 {len(initial_evidence)} 条初始证据")

        # ===== Phase 3: Gap 分析 =====
        logger.info("[Phase 3] 研究空白分析...")
        gaps = self.gap_analyzer.identify_gaps(initial_evidence, topic)
        logger.info(f"识别出 {len(gaps)} 个研究空白")

        # ===== Phase 4: 第二轮（针对 Gap 补充）=====
        if depth == "deep" and gaps:
            logger.info("[Phase 4] 第二轮补充搜索...")
            # 生成针对 gap 的补充 query
            gap_queries = self._generate_gap_queries(gaps, topic)
            research_topic.search_queries.extend(gap_queries)
            supplementary_evidence = self.collector.collect(research_topic)
            initial_evidence.extend(supplementary_evidence)
            logger.info(f"补充后共 {len(initial_evidence)} 条证据")

        # ===== Phase 5: 生成报告 =====
        logger.info("[Phase 5] 报告生成...")
        report = self._synthesize_report(topic, research_topic, initial_evidence, gaps)

        elapsed = (datetime.now() - start_time).total_seconds()
        logger.info(f"研究完成，耗时 {elapsed:.1f}s，报告包含 {len(report.references)} 条参考文献")

        return report

    def _generate_gap_queries(self, gaps: List[ResearchGap], topic: str) -> List[str]:
        """基于研究空白生成补充搜索 query"""
        queries = []
        for gap in gaps:
            if gap.description:
                # 从 gap 描述提取关键词
                keywords = gap.description.split()[:5]
                if keywords:
                    queries.append(' '.join(keywords))
        # 添加原始课题的变体查询
        queries.append(f"{topic} future directions")
        queries.append(f"{topic} open problems")
        return queries[:5]

    def _collect_from_history(self) -> List[Evidence]:
        """从历史数据库（SQLite）中查找课题相关的已积累证据"""
        if not self.topic_keywords or not self.collector.store:
            return []

        evidence_list = []
        try:
            from core.storage import UnifiedStore
            store = self.collector.store or UnifiedStore()

            for kw in self.topic_keywords:
                events = store.get_events_by_tech(kw, days=180, limit=30)
                for event in events:
                    ev = Evidence(
                        source=event.source or 'history',
                        source_type='signal',
                        title=event.title or '',
                        content=event.summary or '',
                        url=event.url or '',
                        relevance=0.7,  # 历史数据相关性折扣
                        quality='medium',
                        claim=self._extract_claim(event),
                        evidence_type='neutral',
                        citation_count=0,
                        venue='',
                        authors=[]
                    )
                    evidence_list.append(ev)

            # 去重
            seen = set()
            unique = []
            for ev in evidence_list:
                key = ev.title[:50].lower()
                if key not in seen:
                    seen.add(key)
                    unique.append(ev)

            return unique
        except Exception as e:
            logger.warning(f"历史数据收集失败: {e}")
            return []

    def _synthesize_report(
        self,
        topic: str,
        research_topic: ResearchTopic,
        evidence: List[Evidence],
        gaps: List[ResearchGap]
    ) -> ResearchReport:
        """
        综合所有发现，生成结构化报告
        """
        from layers.research import MethodComparison, ResearchReport as ResearchReportClass

        # 提取研究问题列表
        questions = [q.question for q in research_topic.decomposed_questions]

        # 分类证据
        supporting = [e for e in evidence if e.evidence_type == 'supporting']
        contradicting = [e for e in evidence if e.evidence_type == 'contradicting']

        # 生成方法对比（从高引用论文中提取）
        method_comparisons = self._build_method_comparisons(evidence)

        # 关键发现
        key_findings = self._extract_key_findings(evidence, supporting)

        # 未来方向
        future_directions = self._generate_future_directions(gaps, evidence)

        # 置信度判断
        confidence = self._assess_confidence(evidence, gaps)

        # 如果有 MiniMax client，使用 LLM 生成更好的综合
        if self.client and len(evidence) > 0:
            try:
                abstract = self._generate_abstract_llm(topic, evidence)
            except Exception as e:
                logger.warning(f"LLM abstract generation failed: {e}")
                abstract = self._generate_abstract_basic(topic, evidence)
        else:
            abstract = self._generate_abstract_basic(topic, evidence)

        report = ResearchReportClass(
            title=f"技术研究报告：{topic}",
            topic=topic,
            abstract=abstract,
            research_questions=questions,
            methodology_comparisons=method_comparisons,
            key_findings=key_findings,
            research_gaps=gaps,
            future_directions=future_directions,
            references=evidence[:30],  # 最多30条参考文献
            confidence=confidence
        )

        return report

    def _build_method_comparisons(self, evidence: List[Evidence]) -> List[MethodComparison]:
        """从证据中构建方法对比"""
        from layers.research import MethodComparison

        comparisons = []
        seen_methods = set()

        for ev in evidence:
            if ev.quality != 'high':
                continue

            # 简单方法名提取：从标题中提取
            method_name = self._extract_method_from_title(ev.title)
            if method_name and method_name not in seen_methods:
                seen_methods.add(method_name)
                comparisons.append(MethodComparison(
                    method_name=method_name,
                    strengths=['需要进一步分析'],
                    limitations=['需要进一步分析'],
                    applicable_scenarios=['待确定'],
                    key_papers=[ev.title],
                    performance_notes=f"来源: {ev.source} ({ev.citation_count} citations)"
                ))

            if len(comparisons) >= 5:  # 最多5个方法对比
                break

        return comparisons

    def _extract_method_from_title(self, title: str) -> str:
        """从论文标题中提取方法名"""
        if not title:
            return ''
        # 简单策略：取标题中前几个重要单词
        words = title.split()
        if len(words) >= 3:
            return ' '.join(words[:3])
        return title[:50]

    def _extract_key_findings(self, evidence: List[Evidence], supporting: List[Evidence]) -> List[str]:
        """提取关键发现"""
        findings = []

        # 按 citation_count 排序，取最高的
        sorted_evidence = sorted(evidence, key=lambda x: x.citation_count, reverse=True)

        for ev in sorted_evidence[:5]:
            if ev.title:
                finding = f"{ev.title}"
                if ev.citation_count > 0:
                    finding += f" (引用: {ev.citation_count})"
                findings.append(finding)

        # 添加支持证据最多的发现
        if supporting:
            top_supporting = supporting[0]
            findings.append(f"核心支持证据：{top_supporting.title}")

        return findings[:7]

    def _generate_future_directions(self, gaps: List[ResearchGap], evidence: List[Evidence]) -> List[str]:
        """生成未来研究方向"""
        directions = []

        for gap in gaps[:3]:
            if gap.gap_type == 'unsolved':
                directions.append(f"解决 {gap.description[:50]}...")
            elif gap.gap_type == 'underexplored':
                directions.append(f"深入研究 {gap.description[:50]}...")
            elif gap.gap_type == 'transfer':
                directions.append(f"迁移 {gap.description[:50]}...")

        # 从证据中提取未来工作建议
        for ev in evidence:
            content_lower = ev.content.lower()
            if 'future work' in content_lower or 'next step' in content_lower:
                for sent in ev.content.split('.'):
                    if 'future' in sent.lower() or 'next' in sent.lower():
                        directions.append(f"未来方向: {sent[:100]}")
                        break

        return directions[:5]

    def _assess_confidence(self, evidence: List[Evidence], gaps: List[ResearchGap]) -> str:
        """评估报告置信度"""
        high_quality = sum(1 for e in evidence if e.quality == 'high')
        total = len(evidence)

        if total == 0:
            return 'low'
        elif high_quality / total > 0.5 and len(gaps) <= 3:
            return 'high'
        elif high_quality / total > 0.3:
            return 'medium'
        return 'low'

    def _generate_abstract_llm(self, topic: str, evidence: List[Evidence]) -> str:
        """使用 LLM 生成摘要"""
        evidence_summary = "\n".join([
            f"- {e.title} ({e.citation_count} citations): {e.content[:100]}..."
            for e in evidence[:10]
        ])

        prompt = f"""基于以下研究证据，为课题「{topic}」生成一个200字的研究摘要。

证据：
{evidence_summary}

要求：
1. 说明该课题的重要性
2. 总结主要研究发现
3. 指出主要研究空白
4. 给出未来方向

格式：摘要应该简洁、专业、可读。"""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat(messages)
            return response[:500] if response else self._generate_abstract_basic(topic, evidence)
        except Exception as e:
            logger.warning(f"LLM abstract generation failed: {e}")
            return self._generate_abstract_basic(topic, evidence)

    def _generate_abstract_basic(self, topic: str, evidence: List[Evidence]) -> str:
        """基础摘要生成"""
        count = len(evidence)
        citation_sum = sum(e.citation_count for e in evidence)
        high_quality = sum(1 for e in evidence if e.quality == 'high')

        abstract = f"""本报告围绕「{topic}」课题，系统收集了 {count} 条研究证据（其中高质量论文 {high_quality} 篇，总引用超过 {citation_sum} 次）。

"""
        if evidence:
            top_ev = max(evidence, key=lambda x: x.citation_count)
            abstract += f"""核心发现：{top_ev.title}，该工作发表在 {top_ev.venue}，引用数 {top_ev.citation_count}。

"""
        if high_quality > 3:
            abstract += f"研究趋势：{high_quality} 篇高引用论文表明该方向已形成一定研究规模，方法路线趋于清晰。"

        return abstract

    def save_report_to_obsidian(self, report: ResearchReport, vault_path: str = None) -> str:
        """
        保存报告到 Obsidian vault
        """
        if not vault_path:
            vault_path = os.environ.get(
                'OBSIDIAN_VAULT_PATH',
                r"C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察"
            )

        date_str = datetime.now().strftime('%Y-%m-%d')
        safe_topic = report.topic[:30].replace('/', '_').replace('\\', '_')
        filename = f"{date_str}_{safe_topic}.md"
        filepath = os.path.join(vault_path, filename)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report.markdown)

        logger.info(f"报告已保存: {filepath}")
        return filepath