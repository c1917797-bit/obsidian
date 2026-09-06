import sys
sys.stdout.reconfigure(encoding='utf-8')

from layers.paper_analysis.paper_search_engine import PaperSearchEngine
from layers.paper_analysis.paper_insights import PaperCardGenerator
import json

engine = PaperSearchEngine(use_index=True)
gen = PaperCardGenerator()

results = engine.fast_search(problems=['Agent-Capability', 'Latency'], limit=5)
for i, p in enumerate(results[:5]):
    print(f'\n--- Paper {i+1}: {p.title[:50]}... ---')
    print(f'Abstract: {p.abstract[:100]}...')
    try:
        card = gen.generate_card(p)
        print(f'Success!')
        print(f'  Summary: {card.one_sentence_summary[:60] if card.one_sentence_summary else "empty"}...')
        print(f'  Contributions: {card.key_contributions[:2]}')
    except Exception as e:
        print(f'Error: {e}')
