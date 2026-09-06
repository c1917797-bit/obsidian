import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os'
comp = json.load(open(os.path.join(BASE, 'config', 'sources_comprehensive.json'), encoding='utf-8'))
feeds = comp.get('rss_feeds', [])
p0 = [f for f in feeds if f.get('priority') == 'P0']
p1 = [f for f in feeds if f.get('priority') == 'P1']
p2 = [f for f in feeds if f.get('priority') == 'P2']
print('Total feeds:', len(feeds))
print('P0:', len(p0), 'P1:', len(p1), 'P2:', len(p2))
print('P0 categories:', set(f.get('category') for f in p0))
print('P0 names:', [f.get('name') for f in p0[:10]])

# Check if the obsidian_sink vault path is correct
sink_path = os.path.join(BASE, 'layers/output/obsidian_sink.py')
sink = open(sink_path, encoding='utf-8').read()
for line in sink.split('\n'):
    if 'vault_path' in line.lower() or '2_AI情报日历' in line:
        print('SINK:', line)