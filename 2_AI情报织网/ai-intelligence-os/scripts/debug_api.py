import sys
sys.stdout.reconfigure(encoding='utf-8')

from layers.paper_analysis.paper_search_engine import PaperSearchEngine
from core.minimax_client import get_client
import json

engine = PaperSearchEngine(use_index=True)
client = get_client()

results = engine.fast_search(problems=['Agent-Capability', 'Latency'], limit=3)
p = results[1]  # SmartCache

print(f'Paper: {p.title[:50]}...')
print(f'Abstract: {p.abstract[:200]}...')

prompt = f"""请根据以下论文信息，生成30秒速读卡片。

论文标题: {p.title}
会议/年份: {p.venue} {p.year}
摘要: {p.abstract[:800]}
领域: {p.primary_area}
引用数: {p.citation_count}
匹配问题: {', '.join(p.matched_problems)}
匹配技术: {', '.join(p.matched_techs)}

请用JSON格式输出:
{{
    "one_sentence_summary": "一句话总结论文核心贡献（不超过50字）",
    "key_contributions": ["贡献1", "贡献2", "贡献3"],
    "why_important": "为什么这项研究重要？（不超过100字）"
}}

只输出JSON，不要其他内容。
"""

print('\nSending request to MiniMax...')
response = client.chat([{"role": "user", "content": prompt}], temperature=0.3, max_tokens=800)
print(f'\nRaw response ({len(response)} chars):')
print(response[:500])
print('...')

try:
    data = json.loads(response)
    print('\nParsed JSON:')
    print(json.dumps(data, ensure_ascii=False, indent=2))
except json.JSONDecodeError as e:
    print(f'\nJSON parse error: {e}')
    print(f'Response starts with: {repr(response[:100])}')
