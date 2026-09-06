import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('C:/Users/Huawei/Documents/code/Obsidian/2_AI情报织网/ai-intelligence-os/config/sources_comprehensive.json', encoding='utf-8'))
enabled = [s for s in d['rss_feeds'] if s.get('enabled', False)]
disabled = [s for s in d['rss_feeds'] if not s.get('enabled', False)]
print(f"启用: {len(enabled)} / 总计: {len(d['rss_feeds'])}")
print()

cats = {}
for s in enabled:
    cat = s.get('category','unknown')
    if cat not in cats: cats[cat] = []
    cats[cat].append(s)

for cat, srcs in sorted(cats.items()):
    print(f"=== {cat} ({len(srcs)}) ===")
    for s in sorted(srcs, key=lambda x: (x.get('priority','P9'), x['id'])):
        print(f"  [{s.get('priority','P?')}] {s.get('name','?')}")
    print()
