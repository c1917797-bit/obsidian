# -*- coding: utf-8 -*-
import os
os.environ['PYTHONUTF8'] = '1'

import sys
import os
import json
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from layers.insight.insight_agent import InsightAgent

json_path = 'data/reports/ComprehensiveInsight_20260528_154533.json'
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

signals = data['signals']
print(f"Loaded {len(signals)} signals")

class MockEvent:
    def __init__(self, sig):
        self.id = sig['id']
        self.title = sig['title']
        self.url = sig['url']
        self.source = sig['source']
        self.source_type = sig.get('source_type', '')
        self.summary = sig.get('summary', '')
        self.entity = sig.get('source', '').split()[0] if sig.get('source') else 'Unknown'
        self.company = sig.get('source', '').split()[0] if sig.get('source') else ''
        self.importance = sig.get('priority', 'P1')
        self.event_type = sig.get('category', 'unknown')
        self.tech_categories = []
        self.innovation = ''
        self.problem_solved = ''
        self.metadata = sig.get('metadata', {})
        self.published = sig.get('published', '')
        self.tags = sig.get('tags', [])

events = [MockEvent(sig) for sig in signals]
agent = InsightAgent()

hot_events = []
hot_tech = []
hot_trend = []
standard = []

for e in events:
    cat = agent._categorize_event(e)
    if cat == '热点事件':
        hot_events.append(e)
    elif cat == '热点技术':
        hot_tech.append(e)
    elif cat == '热点方向':
        hot_trend.append(e)
    else:
        standard.append(e)

def sort_events(events_list):
    priority_order = {'P0': 0, 'P1': 1, 'P2': 2}
    return sorted(events_list, key=lambda e: (
        priority_order.get(getattr(e, 'importance', 'P1'), 1),
        -len(getattr(e, 'title', ''))
    ))

hot_events = sort_events(hot_events)
hot_tech = sort_events(hot_tech)
hot_trend = sort_events(hot_trend)
standard = sort_events(standard)

print(f"分类结果: 热点事件={len(hot_events)}, 热点技术={len(hot_tech)}, 热点方向={len(hot_trend)}, 标准={len(standard)}")

def is_valid_insight(entry, category_hint):
    """检查内容是否有效（非空、非提示词残留、非截断）"""
    if not entry or len(entry) < 80:
        return False
    bad_patterns = ['The user', 'You are', 'want a', '请根据以下', '严格按以下格式']
    for pattern in bad_patterns:
        if pattern in entry[:100]:
            return False
    if category_hint == '热点技术' and '[热点技术]' not in entry:
        return False
    if category_hint == '热点事件' and '[热点事件]' not in entry:
        return False
    if category_hint == '热点方向' and '[热点方向]' not in entry:
        return False
    return True

def build_with_retry(event, category_hint, max_attempts=3):
    """使用增强重试逻辑构建条目"""
    entry = None
    for attempt in range(max_attempts):
        try:
            entry = agent._build_brief_entry(event)
            if is_valid_insight(entry, category_hint):
                return entry
            print(f"  Attempt {attempt+1} returned invalid content, retrying...")
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
        if attempt < max_attempts - 1:
            wait_time = (attempt + 1) * 2
            print(f"  Waiting {wait_time}s before retry...")
            time.sleep(wait_time)
    return agent._build_standard_entry(
        agent._categorize_event(event),
        event.title[:100],
        event.summary[:300] if event.summary else '',
        event.url,
        event.entity,
        '中'
    )

date_str = datetime.now().strftime('%Y-%m-%d')

report = f"""📡 前沿科技简报 · {date_str}

"""

# 热点事件 - P0 5条
report += f"""## 🔥 热点事件

"""
count = 0
for e in hot_events[:5]:
    print(f"处理热点事件: {e.title[:50]}...")
    entry = build_with_retry(e, '热点事件')
    report += entry + "\n\n"
    count += 1

if count == 0:
    report += "暂无热点事件。\n\n"

# 热点技术 - P0 6条
report += f"""## 💡 热点技术

"""
count = 0
for e in hot_tech[:6]:
    print(f"处理热点技术: {e.title[:50]}...")
    entry = build_with_retry(e, '热点技术')
    report += entry + "\n\n"
    count += 1

if count == 0:
    report += "暂无热点技术。\n\n"

# 热点方向 - P0 5条
report += f"""## 📊 热点方向

"""
count = 0
for e in hot_trend[:5]:
    print(f"处理热点方向: {e.title[:50]}...")
    entry = build_with_retry(e, '热点方向')
    report += entry + "\n\n"
    count += 1

if count == 0:
    report += "暂无热点方向。\n\n"

# 文末汇总
report += f"""---

📌 文末汇总
- 今日最值得深读: {hot_tech[0].title[:50] if hot_tech else '暂无'} ; {hot_events[0].title[:50] if hot_events else '暂无'}
- 今日可跳过: 无
- 待观察趋势(跨条目): AI Agent持续火热，多厂商发布新版框架和模型

---
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Report ID**: {datetime.now().strftime('%Y%m%d%H%M%S')}
"""

output_path = f'C:\\Users\\Huawei\\Documents\\code\\Obsidian\\3_AI情报日历\\Daily\\DailyReport_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"\n✅ Report saved to: {output_path}")
print(f"📊 Report size: {len(report)} chars, {len(report.splitlines())} lines")