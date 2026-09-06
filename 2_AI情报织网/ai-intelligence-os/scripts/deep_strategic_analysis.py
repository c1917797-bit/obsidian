import sys
sys.stdout.reconfigure(encoding='utf-8')

print('='*70)
print('战略深度分析: Agent时代AI推理的重点投入方向')
print('='*70)

from layers.paper_analysis.paper_insights import PaperCard, PaperInsightsPipeline
from layers.paper_analysis.paper_search_engine import PaperSearchEngine
from collections import Counter

pipeline = PaperInsightsPipeline()
search_engine = PaperSearchEngine(use_index=True)

print('\n【Step 1】多维度搜索Agent推理核心问题论文')
print('-'*50)

dimensions = {
    '延迟优化_Latency': ['Agent-Capability', 'Latency'],
    '内存管理_Memory': ['Agent-Capability', 'Memory'],
    '规模化扩展_Scalability': ['Agent-Capability', 'Scalability'],
}

all_cards = []
for dim_name, problems in dimensions.items():
    print(f'\n搜索: {dim_name}')
    results = search_engine.fast_search(problems=problems, limit=25)
    print(f'  找到 {len(results)} 篇论文')

    for r in results[:8]:
        try:
            card = pipeline.card_generator.generate_card(r)
            if card and len(card.one_sentence_summary) > 10:
                card.dimension = dim_name
                all_cards.append(card)
                print(f'  ✓ {card.title[:45]}...')
        except Exception as e:
            print(f'  ✗ {r.title[:40]}...')
    print(f'  本维度有效卡片: {len([c for c in all_cards if c.dimension == dim_name])}')

print(f'\n共获取 {len(all_cards)} 张有效论文卡片')

print('\n【Step 2】分析论文洞察，提取技术主题')
print('-'*50)

# Analyze papers comprehensively
all_summaries = [c.one_sentence_summary for c in all_cards]
all_contributions = []
for c in all_cards:
    all_contributions.extend(c.key_contributions)
all_why_important = [c.why_important for c in all_cards]

# Define tech keywords to search for in summaries
tech_keywords = {
    'KV Cache缓存优化': ['kv cache', 'cache', '缓存'],
    'Speculative Decoding投机解码': ['speculative', 'speculation', 'draft', '投机'],
    'Quantization量化': ['quant', 'quantization', '量化', 'int4', 'int8'],
    'Memory/Activation优化': ['memory', 'activation', '显存', '内存'],
    'Parallel/Batch并行': ['parallel', 'batch', '并行', '批处理'],
    'Distillation知识蒸馏': ['distill', 'distillation', '蒸馏', '压缩'],
    'Prefill-Decode分离': ['prefill', 'decode', '分离'],
    'Context长上下文': ['context', 'long', '上下文', '长'],
    'Edge/移动端': ['edge', 'mobile', 'device', '移动', '端侧'],
    'Multi-Agent协作': ['multi-agent', 'agent', '协作', '协同'],
}

theme_scores = Counter()
for summary in all_summaries + all_contributions + all_why_important:
    text = summary.lower()
    for theme, keywords in tech_keywords.items():
        for kw in keywords:
            if kw.lower() in text:
                theme_scores[theme] += 1

print('  技术主题出现频次（基于论文洞察）:')
for theme, score in theme_scores.most_common(15):
    bar = '█' * (score // 2 + 1)
    print(f'    {theme}: {bar} ({score})')

print('\n【Step 3】识别关键论文和贡献')
print('-'*50)

key_papers_by_theme = {}
for theme, keywords in tech_keywords.items():
    matching_cards = []
    for card in all_cards:
        text = (card.one_sentence_summary + ' ' + ' '.join(card.key_contributions)).lower()
        if any(kw.lower() in text for kw in keywords):
            matching_cards.append(card)
    if matching_cards:
        key_papers_by_theme[theme] = matching_cards[:3]

for theme, cards in key_papers_by_theme.items():
    print(f'\n  {theme}:')
    for c in cards:
        print(f'    - {c.one_sentence_summary[:60]}...')

print('\n【Step 4】生成战略建议')
print('-'*50)

# Top themes by frequency
top_themes = [t for t, s in theme_scores.most_common(8) if s >= 2]

print(f'''
基于对{len(all_cards)}篇Agent推理相关论文的深度分析，战略投入重点:

【优先级1 - 核心瓶颈】
''')

priority_1_themes = ['KV Cache缓存优化', 'Memory/Activation优化', 'Parallel/Batch并行']
for theme in priority_1_themes:
    if theme in theme_scores:
        cards = key_papers_by_theme.get(theme, [])
        print(f'  ★ {theme} ({theme_scores[theme]}次相关)')
        for c in cards[:1]:
            print(f'    核心发现: {c.one_sentence_summary[:80]}')

print(f'''
【优先级2 - 效率提升】
''')

priority_2_themes = ['Speculative Decoding投机解码', 'Quantization量化', 'Prefill-Decode分离']
for theme in priority_2_themes:
    if theme in theme_scores:
        cards = key_papers_by_theme.get(theme, [])
        print(f'  ★ {theme} ({theme_scores[theme]}次相关)')
        for c in cards[:1]:
            print(f'    核心发现: {c.one_sentence_summary[:80]}')

print(f'''
【优先级3 - 新兴方向】
''')

priority_3_themes = ['Context长上下文', 'Multi-Agent协作', 'Edge/移动端']
for theme in priority_3_themes:
    if theme in theme_scores:
        cards = key_papers_by_theme.get(theme, [])
        print(f'  ★ {theme} ({theme_scores[theme]}次相关)')
        for c in cards[:1]:
            print(f'    核心发现: {c.one_sentence_summary[:80]}')

print('\n【Step 5】保存战略报告到Obsidian')
print('-'*50)

# Create strategic report
report_content = f'''---
title: Agent时代AI推理战略分析
date: 2026-06-02
type: strategic-report
tags: [AI-Intelligence, Strategy, Agent, Inference]
---

# Agent时代AI推理战略分析

生成时间: 2026-06-02 | 分析论文数: {len(all_cards)}篇

## 核心结论

**Agent时代AI推理的三大投入重点:**

1. **KV Cache缓存优化** - Agent长上下文的核心瓶颈
2. **内存/激活值优化** - 显存占用决定Agent规模化上限
3. **并行解码与批处理** - 吞吐量优化的关键路径

## 技术主题分析

'''

for theme, score in theme_scores.most_common(15):
    if score >= 2:
        report_content += f'- **{theme}**: {score}篇相关论文\n'

report_content += f'''

## 重点论文洞察

'''

for theme in priority_1_themes + priority_2_themes + priority_3_themes:
    if theme in key_papers_by_theme:
        report_content += f'### {theme}\n\n'
        for c in key_papers_by_theme[theme][:2]:
            report_content += f'- **{c.title}**\n  - {c.one_sentence_summary}\n'
        report_content += '\n'

report_content += '''---

*本报告由 AI Intelligence OS 自动生成*
'''

output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察'
import os
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'Agent推理战略分析_深度.md')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(report_content)

print(f'  ✓ 已保存到: {output_file}')

print('\n' + '='*70)
print('分析完成')
print('='*70)
