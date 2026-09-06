import re

with open('layers/paper_analysis/paper_insights.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new function
new_func = '''    def generate_card(self, paper: PaperMatch) -> PaperCard:
        """生成单篇论文卡片"""
        abstract_text = paper.abstract[:800] if paper.abstract and len(paper.abstract) > 50 else "无摘要信息"

        prompt = f"""请根据以下论文信息，生成30秒速读卡片。

论文标题: {paper.title}
会议/年份: {paper.venue or 'Unknown'} {paper.year or 2024}
摘要: {abstract_text}
领域: {paper.primary_area or 'Unknown'}
引用数: {paper.citation_count or 0}
匹配问题: {', '.join(paper.matched_problems) if paper.matched_problems else 'Unknown'}
匹配技术: {', '.join(paper.matched_techs) if paper.matched_techs else 'Unknown'}

请用JSON格式输出:
{{
    "one_sentence_summary": "一句话总结论文核心贡献（不超过50字）",
    "key_contributions": ["贡献1", "贡献2", "贡献3"],
    "why_important": "为什么这项研究重要？（不超过100字）"
}}

只输出JSON，不要其他内容。
"""

        try:
            response = self.client.chat([{"role": "user", "content": prompt}], temperature=0.3, max_tokens=800)
            data = json.loads(response)

            return PaperCard(
                title=paper.title,
                venue=paper.venue or "Unknown",
                year=paper.year or 2024,
                one_sentence_summary=data.get("one_sentence_summary", ""),
                key_contributions=data.get("key_contributions", []),
                why_important=data.get("why_important", ""),
                matched_problems=paper.matched_problems,
                matched_techs=paper.matched_techs,
                read_time_minutes=paper.read_time_minutes or 30,
                url=paper.url,
                pdf_url=paper.pdf_url,
                citation_count=paper.citation_count or 0,
                relevance_score=paper.relevance_score
            )
        except json.JSONDecodeError as e:
            logger.warning(f"JSON decode error for {paper.title[:50]}: {e}")
            return PaperCard(
                title=paper.title,
                venue=paper.venue or "Unknown",
                year=paper.year or 2024,
                one_sentence_summary=f"论文涉及{'/'.join(paper.matched_problems[:2]) if paper.matched_problems else '相关技术问题'}",
                key_contributions=[f"涉及{tech}" for tech in (paper.matched_techs[:3] if paper.matched_techs else ["需阅读原文"])],
                why_important="生成失败，请阅读原文",
                matched_problems=paper.matched_problems,
                matched_techs=paper.matched_techs,
                read_time_minutes=paper.read_time_minutes or 30,
                url=paper.url,
                pdf_url=paper.pdf_url,
                citation_count=paper.citation_count or 0,
                relevance_score=paper.relevance_score
            )
        except Exception as e:
            logger.warning(f"Failed to generate card for {paper.title[:50]}: {e}")
            return PaperCard(
                title=paper.title,
                venue=paper.venue or "Unknown",
                year=paper.year or 2024,
                one_sentence_summary=abstract_text[:80] + "..." if len(abstract_text) > 80 else abstract_text,
                key_contributions=["见原文摘要"],
                why_important="生成失败，请阅读原文",
                matched_problems=paper.matched_problems,
                matched_techs=paper.matched_techs,
                read_time_minutes=paper.read_time_minutes or 30,
                url=paper.url,
                pdf_url=paper.pdf_url,
                citation_count=paper.citation_count or 0,
                relevance_score=paper.relevance_score
            )
'''

# Find and replace the function using regex
pattern = r'    def generate_card\(self, paper: PaperMatch\) -> PaperCard:.*?(?=\n    def |\nclass |$)'
new_content = re.sub(pattern, new_func, content, count=1, flags=re.DOTALL)

with open('layers/paper_analysis/paper_insights.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully updated generate_card function')
