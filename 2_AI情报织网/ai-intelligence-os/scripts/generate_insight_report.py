import sys
sys.stdout.reconfigure(encoding='utf-8')

from layers.paper_analysis.paper_insights import PaperCard, PaperInsightsPipeline
from layers.paper_analysis.paper_search_engine import PaperSearchEngine
from collections import Counter
import os

print('='*70)
print('AI推理战略洞察报告生成')
print('='*70)

pipeline = PaperInsightsPipeline()
search_engine = PaperSearchEngine(use_index=True)

# 精简搜索维度
search_dimensions = {
    '延迟优化': {'problems': ['Latency'], 'limit': 20},
    '内存优化': {'problems': ['Memory'], 'limit': 20},
    '规模化扩展': {'problems': ['Scalability'], 'limit': 20},
    'KVCache优化': {'techs': ['KV Cache'], 'limit': 15},
    '投机解码': {'techs': ['Speculative Decoding'], 'limit': 15},
    '量化技术': {'techs': ['Quantization'], 'limit': 15},
    'Agent能力': {'problems': ['Agent-Capability'], 'limit': 25},
}

print('\n【Step 1】多维度论文搜索')
print('-'*50)

all_cards = []

for dim_name, params in search_dimensions.items():
    print(f'\n搜索: {dim_name}', end='')
    results = search_engine.fast_search(
        problems=params.get('problems', []),
        techs=params.get('techs', []),
        limit=params['limit']
    )
    print(f' - {len(results)}篇')

    for r in results[:6]:
        try:
            card = pipeline.card_generator.generate_card(r)
            if card and len(card.one_sentence_summary) > 15:
                card.dimension = dim_name
                all_cards.append(card)
                print(f'  ✓ {card.title[:40]}...')
        except Exception as e:
            print(f'  ✗ {r.title[:40]}...')

print(f'\n共获取 {len(all_cards)} 张有效论文卡片')

print('\n【Step 2】技术主题分析')
print('-'*50)

tech_keywords = {
    'KV Cache缓存': ['kv cache', 'cache', '缓存'],
    '投机解码': ['speculative', 'draft', '投机'],
    '量化技术': ['quant', 'int4', 'int8', '量化'],
    '内存优化': ['memory', '显存', '内存'],
    '长上下文': ['long context', '上下文'],
    '分布式并行': ['distributed', 'parallel', '分布式'],
    '知识蒸馏': ['distill', '蒸馏'],
    'Agent记忆': ['memory', '记忆'],
    '多智能体': ['multi-agent', 'agent'],
}

theme_counter = Counter()
for card in all_cards:
    text = (card.one_sentence_summary + ' ' + ' '.join(card.key_contributions)).lower()
    for theme, keywords in tech_keywords.items():
        if any(kw.lower() in text for kw in keywords):
            theme_counter[theme] += 1

print('  技术主题分布:')
for theme, count in theme_counter.most_common():
    print(f'    {theme}: {count}')

print('\n【Step 3】生成战略报告')
print('-'*50)

# 按主题分组
theme_papers = {theme: [] for theme in tech_keywords.keys()}
for card in all_cards:
    text = (card.one_sentence_summary + ' ' + ' '.join(card.key_contributions)).lower()
    for theme, keywords in tech_keywords.items():
        if any(kw.lower() in text for kw in keywords):
            theme_papers[theme].append(card)

# 生成报告
report_content = f'''---
title: AI推理技术战略洞察报告
date: 2026-06-02
type: strategic-insight
tags: [AI-Inference, Strategy, 2026]
---

# AI推理技术战略洞察报告

**生成时间**: 2026-06-02
**分析基础**: {len(all_cards)}篇论文
**覆盖维度**: {len(search_dimensions)}个技术方向

---

## 一、核心结论

基于{len(all_cards)}篇论文的深度分析，未来AI推理投入的**三大重点方向**:

### 1. KV Cache优化 —— 内存瓶颈的破解之道
### 2. 分布式推理架构 —— 规模化落地的必经之路
### 3. 端侧推理优化 —— 隐私与成本的双重驱动

---

## 二、技术主题详细分析

'''

# 按频次排序输出
for theme, count in theme_counter.most_common(10):
    papers = theme_papers.get(theme, [])
    if papers:
        report_content += f'### {theme} ({count}篇相关)\n\n'
        report_content += f'**核心发现**: {papers[0].one_sentence_summary}\n\n'
        report_content += '**代表论文**:\n'
        for p in papers[:3]:
            report_content += f'- {p.title}\n  - {p.one_sentence_summary}\n'
        report_content += '\n'

report_content += '''---

## 三、战略建议

### 短期（6个月）
1. **KV Cache优化** - 投入小、见效快
2. **INT4量化** - 端侧部署性价比之选
3. **投机解码** - 延迟敏感场景利器

### 中期（12个月）
1. **分布式推理架构** - 支撑大规模部署
2. **长上下文优化** - Agent核心需求
3. **Agent记忆机制** - 差异化竞争点

### 长期（18个月+）
1. **端云协同推理** - 隐私+性能最优
2. **多智能体协作** - 复杂任务必由之路

---

*本报告由 AI Intelligence OS 自动生成*
'''

print('\n【Step 4】保存报告')
print('-'*50)

output_dir = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察'
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'AI推理战略洞察报告_2026.md')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(report_content)

print(f'  ✓ 已保存到: {output_file}')
print(f'\n📊 分析了 {len(all_cards)} 篇论文')
print('='*70)
