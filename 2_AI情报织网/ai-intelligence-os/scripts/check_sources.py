import sys
sys.stdout.reconfigure(encoding='utf-8')
from core.storage import UnifiedStore
from collections import Counter, defaultdict

print('='*70)
print('战略分析: Agent时代下AI推理 - 信息源验证')
print('='*70)

store = UnifiedStore()

import sqlite3
conn = sqlite3.connect(store.db_path)
cursor = conn.cursor()

# 1. Check signals by source type (last 7 days)
cursor.execute('''
    SELECT source_type, category, COUNT(*) as cnt
    FROM signals
    WHERE created_at > datetime('now', '-7 days')
    GROUP BY source_type, category
    ORDER BY cnt DESC
    LIMIT 20
''')
print('\n【一、近7天信号来源分布】')
for row in cursor.fetchall():
    print(f'  {row[0]} [{row[1]}]: {row[2]} 条')

# 2. Check Twitter signals
cursor.execute('''
    SELECT title, source, created_at
    FROM signals
    WHERE source_type = 'twitter_rss'
    AND created_at > datetime('now', '-7 days')
    ORDER BY created_at DESC
    LIMIT 10
''')
print('\n【二、近7天Twitter信号 (AI相关)】')
twitter_texts = []
for row in cursor.fetchall():
    twitter_texts.append(row[0])
    if any(kw in row[0].lower() for kw in ['agent', 'llm', 'inference', 'ai', 'model', 'openai', 'nvidia', 'google']):
        print(f'  [{row[2][:10]}] {row[0][:60]}...')

# 3. Check news signals
cursor.execute('''
    SELECT title, source, created_at
    FROM signals
    WHERE category IN ('news_cn', 'news')
    AND created_at > datetime('now', '-7 days')
    ORDER BY created_at DESC
    LIMIT 10
''')
print('\n【三、近7天中文新闻信号】')
for row in cursor.fetchall():
    print(f'  [{row[2][:10]}] {row[0][:60]}...')

# 4. Check GitHub releases (important for tech trends)
cursor.execute('''
    SELECT title, source, created_at
    FROM signals
    WHERE source LIKE '%github%'
    AND created_at > datetime('now', '-7 days')
    ORDER BY created_at DESC
    LIMIT 15
''')
print('\n【四、近7天GitHub发布信号】')
for row in cursor.fetchall():
    print(f'  [{row[2][:10]}] {row[0][:60]}...')

# 5. Summary
cursor.execute('''
    SELECT COUNT(*) FROM signals
    WHERE created_at > datetime('now', '-7 days')
''')
total = cursor.fetchone()[0]

cursor.execute('''
    SELECT COUNT(*) FROM signals
    WHERE created_at > datetime('now', '-7 days')
    AND category IN ('news_cn', 'news', 'social')
''')
news_count = cursor.fetchone()[0]

cursor.execute('''
    SELECT COUNT(*) FROM signals
    WHERE created_at > datetime('now', '-7 days')
    AND (source_type = 'atom' OR source_type = 'hf_api')
''')
tech_count = cursor.fetchone()[0]

print('\n【五、信息源7天汇总】')
print(f'  总信号: {total} 条')
print(f'  新闻/社交: {news_count} 条 ({100*news_count//total}%)')
print(f'  技术发布: {tech_count} 条 ({100*tech_count//total}%)')

conn.close()

print('\n' + '='*70)
print('结论')
print('='*70)
