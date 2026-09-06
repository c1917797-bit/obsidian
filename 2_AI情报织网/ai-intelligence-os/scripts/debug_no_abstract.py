import sys
sys.stdout.reconfigure(encoding='utf-8')

from layers.paper_analysis.paper_search_engine import PaperSearchEngine
from core.minimax_client import get_client
import json

engine = PaperSearchEngine(use_index=True)
client = get_client()

results = engine.fast_search(problems=['Agent-Capability', 'Memory'], limit=1)
p = results[0]

print(f'Paper: {p.title[:50]}...')
abstract_val = p.abstract[:100] if p.abstract else "EMPTY"
print(f'Abstract: {repr(abstract_val)}')

abstract_text = '无摘要信息'

prompt = f"""请根据以下论文信息，生成30秒速读卡片。

论文标题: {p.title}
会议/年份: {p.venue or 'Unknown'} {p.year or 2024}
摘要: {abstract_text}
领域: {p.primary_area or 'Unknown'}
引用数: {p.citation_count or 0}
匹配问题: {', '.join(p.matched_problems) if p.matched_problems else 'Unknown'}
匹配技术: {', '.join(p.matched_techs) if p.matched_techs else 'Unknown'}

请用JSON格式输出:
{{
    "one_sentence_summary": "一句话总结论文核心贡献（不超过50字）",
    "key_contributions": ["贡献1", "贡献2", "贡献3"],
    "why_important": "为什么这项研究重要？（不超过100字）"
}}

只输出JSON，不要其他内容。
"""

response = client.chat([{"role": "user", "content": prompt}], temperature=0.3, max_tokens=800)
print(f'\nResponse ({len(response)} chars):')
print(response[:300])
print('...')

try:
    data = json.loads(response)
    print('\nJSON parsed successfully!')
    print(data)
except json.JSONDecodeError as e:
    print(f'\nJSON decode error: {e}')
    print(f'Response starts with: {repr(response[:100])}')
