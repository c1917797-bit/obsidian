import sys
sys.stdout.reconfigure(encoding='utf-8')

from layers.paper_analysis.paper_search_engine import PaperSearchEngine

engine = PaperSearchEngine(use_index=True)

# Get 10 papers and check their abstracts
results = engine.fast_search(problems=['Agent-Capability', 'Latency'], limit=10)

for i, p in enumerate(results):
    print(f'{i+1}. {p.title[:50]}...')
    print(f'   Abstract length: {len(p.abstract)}')
    print(f'   Abstract preview: {p.abstract[:80]}...')
    print()
