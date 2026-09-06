"""
GapAnalyzer - 研究空白分析器
从证据中识别研究空白、矛盾点和未解决方向
"""
from typing import List, Dict, Set
from collections import defaultdict

from core.logger import get_logger
from layers.research import Evidence, ResearchGap, ResearchTopic

logger = get_logger("GapAnalyzer")


class GapAnalyzer:
    """
    研究空白分析器
    通过分析已收集的证据，识别：
    1. 无人研究的方向
    2. 方法局限性
    3. 矛盾的观点
    4. 从其他领域迁移的机会
    """

    def __init__(self):
        # 已解决的问题关键词
        self.SOLVED_INDICATORS = [
            'achieve state-of-the-art', 'significantly improved', 'outperforms',
            'solved', 'effective method', 'best results', 'novel approach'
        ]
        # 未解决/开放问题关键词
        self.UNSOLVED_INDICATORS = [
            'open problem', 'future work', 'remains unsolved', 'challenging',
            'limitation', 'cannot handle', 'fails to', 'still needs',
            'insufficient', 'limited by'
        ]
        # 矛盾声明关键词
        self.CONTRADICTION_INDICATORS = [
            'however', 'but', 'in contrast', 'unlike', 'while',
            'debate', 'controversy', 'contradict', 'disagree'
        ]

    def identify_gaps(self, evidence: List[Evidence], topic: str) -> List[ResearchGap]:
        """
        识别研究空白

        Args:
            evidence: 已收集的证据列表
            topic: 原始课题

        Returns:
            List[ResearchGap]: 研究空白列表
        """
        gaps = []

        # 分析每个证据的方法和局限性
        method_tracker = defaultdict(list)  # track what methods claim to solve what
        limitations_by_method = defaultdict(list)  # track method limitations

        for ev in evidence:
            content_lower = ev.content.lower()

            # 记录方法 → 解决的问题
            for sent in self._split_sentences(ev.content):
                sent_lower = sent.lower()

                # 检查是否是方法声明
                method_name = self._extract_method_name(sent)
                if method_name:
                    if any(ind in sent_lower for ind in self.SOLVED_INDICATORS):
                        method_tracker[method_name].append({
                            'solved': True,
                            'evidence_id': ev.title[:30],
                            'claim': sent[:100]
                        })
                    if any(ind in sent_lower for ind in self.UNSOLVED_INDICATORS):
                        limitations_by_method[method_name].append(sent[:100])

        # 识别未解决问题
        topic_keywords = topic.lower().split()
        for ev in evidence:
            content_lower = ev.content.lower()

            # 如果证据提到"未解决"但与课题相关
            if any(ind in content_lower for ind in self.UNSOLVED_INDICATORS):
                if self._is_topic_relevant(content_lower, topic_keywords):
                    gap = ResearchGap(
                        gap_type='unsolved',
                        description=self._summarize_gap(ev.content),
                        evidence_refs=[ev.title[:30]],
                        urgency='medium',
                        potential_impact='high'
                    )
                    if not self._gap_exists(gaps, gap):
                        gaps.append(gap)

        # 识别未被充分探索的方向
        if len(evidence) < 5:
            gap = ResearchGap(
                gap_type='underexplored',
                description='该方向仅有 ' + str(len(evidence)) + ' 条相关证据，可能缺乏系统性研究',
                evidence_refs=[],
                urgency='high',
                potential_impact='medium'
            )
            gaps.append(gap)

        # 识别方法局限性导致的空白
        for method, limitations in limitations_by_method.items():
            if len(limitations) >= 2:
                lim_str = "; ".join(limitations[:2])
                gap = ResearchGap(
                    gap_type='contradiction',
                    description=method + ' 方法存在多重局限：' + lim_str,
                    evidence_refs=[method],
                    urgency='medium',
                    potential_impact='medium'
                )
                if not self._gap_exists(gaps, gap):
                    gaps.append(gap)

        # 识别迁移机会（如果某方法在多个证据中被提及但在课题方向没被使用）
        method_mentions = {m: len(v) for m, v in method_tracker.items()}
        for method, count in method_mentions.items():
            if count >= 3 and method.lower() not in topic.lower():
                # 这个方法被多次提及但不在课题关键词中，可能是迁移机会
                gap = ResearchGap(
                    gap_type='transfer',
                    description=method + ' 在类似任务中表现良好（出现 ' + str(count) + ' 次），可能适合迁移到本课题',
                    evidence_refs=[method],
                    urgency='low',
                    potential_impact='high'
                )
                if not self._gap_exists(gaps, gap):
                    gaps.append(gap)

        logger.info("识别出 " + str(len(gaps)) + " 个研究空白")
        return gaps

    def analyze_method_limitations(self, evidence: List[Evidence]) -> List[str]:
        """
        分析现有方法的局限性

        Returns:
            List[str]: 方法局限性描述列表
        """
        limitations = []

        for ev in evidence:
            content = ev.content
            content_lower = content.lower()

            # 查找提到局限性的句子
            if any(kw in content_lower for kw in self.UNSOLVED_INDICATORS):
                for sent in self._split_sentences(content):
                    sent_lower = sent.lower()
                    if any(kw in sent_lower for kw in self.UNSOLVED_INDICATORS):
                        if len(sent) > 20 and len(sent) < 200:
                            limitations.append(sent.strip())

        return limitations[:10]  # 最多10条

    def _is_topic_relevant(self, content: str, keywords: List[str]) -> bool:
        """判断内容是否与课题相关"""
        content_lower = content.lower()
        matches = sum(1 for kw in keywords if kw in content_lower)
        return matches >= 1

    def _extract_method_name(self, sentence: str) -> str:
        """从句子中提取方法名（简单实现）"""
        # 常见的"我们提出/开发/引入X方法"模式
        import re
        patterns = [
            r'we propose (\w+)',
            r'we introduce (\w+)',
            r'we develop (\w+)',
            r'present (\w+) method',
            r'(\w+) approach',
            r'(\w+) framework'
        ]
        for pattern in patterns:
            match = re.search(pattern, sentence, re.IGNORECASE)
            if match:
                return match.group(1)[:30]
        return ''

    def _split_sentences(self, text: str) -> List[str]:
        """简单分句"""
        import re
        sentences = re.split(r'[.!?\n]', text)
        return [s.strip() for s in sentences if s.strip()]

    def _summarize_gap(self, content: str) -> str:
        """总结研究空白"""
        sentences = self._split_sentences(content)
        # 找到提到 open problem / future work 的句子
        for sent in sentences:
            sent_lower = sent.lower()
            if any(kw in sent_lower for kw in self.UNSOLVED_INDICATORS):
                return sent[:150]
        # 回退：取第一句
        return content[:150] if content else "未明确描述"

    def _gap_exists(self, gaps: List[ResearchGap], new_gap: ResearchGap) -> bool:
        """检查是否已存在类似的研究空白"""
        for g in gaps:
            if g.gap_type == new_gap.gap_type and g.description[:50] == new_gap.description[:50]:
                return True
        return False