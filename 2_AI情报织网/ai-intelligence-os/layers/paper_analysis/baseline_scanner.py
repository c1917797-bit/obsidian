"""
Baseline Scanner - 基线建立 + 增量扫描
用法:
    python baseline_scanner.py --venues iclr2025 --min-score 20
    python baseline_scanner.py --venues iclr2025 --min-score 20 --full
    python baseline_scanner.py --stats
"""
import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

OBSIDIAN_ROOT = Path("C:/Users/Huawei/Documents/code/Obsidian")
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"
WATERMARK_FILE = Path(__file__).parent / "baseline_watermark.json"

PROBLEM_KEYWORDS = {
    'KV Cache': ['kv cache', 'paged attention', 'memory management'],
    'Distributed Inference': ['tensor parallel', 'pipeline parallel', 'distributed', 'multi-gpu'],
    'Agent': ['agent', 'multi-agent', 'planning', 'reasoning'],
    'Latency': ['latency', 'inference speed', 'response time', 'delay'],
    'Throughput': ['throughput', 'tokens per second', 'serving'],
    'Scalability': ['scalability', 'scale', 'multi-node'],
    'Speculative Decoding': ['speculative', 'draft model', 'specdec'],
    'MoE': ['mixture of experts', 'moe'],
    'Quantization': ['quantize', 'quantization', 'int8', 'int4', 'fp8'],
}

TECH_KEYWORDS = {
    'KV Cache': ['kv cache', 'paged attention', 'pagedattention'],
    'Speculative Decoding': ['speculative', 'draft model', 'medusa', 'eagle'],
    'MoE': ['mixture of experts', 'moe'],
    'Quantization': ['quantize', 'quantization', 'int8', 'int4', 'fp8', 'awq', 'gptq'],
    'PD Separation': ['prefill', 'decode', 'disaggregation'],
    'Continuous Batching': ['continuous batching'],
    'vLLM': ['vllm'],
    'SGLang': ['sglang'],
}


def score_paper(title: str, abstract: str, keywords: List[str]) -> Tuple[float, List[str], List[str]]:
    text = (title + " " + abstract + " " + " ".join(keywords)).lower()
    score = 0.0
    matched_problems = []
    matched_techs = []

    for problem, kws in PROBLEM_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                score += 5.0
                if kw in title.lower():
                    score += 10.0
                if problem not in matched_problems:
                    matched_problems.append(problem)

    for tech, kws in TECH_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                score += 8.0
                if tech not in matched_techs:
                    matched_techs.append(tech)

    return score, matched_problems, matched_techs


def generate_citekey(title: str, year: int) -> str:
    words = re.findall(r'[a-zA-Z]+', title.lower())
    stopwords = {'the', 'with', 'from', 'that', 'this', 'based', 'using',
                 'learning', 'network', 'model', 'approach', 'system', 'efficient'}
    meaningful = [w for w in words if len(w) > 4 and w not in stopwords]
    prefix = ''.join(w[0] for w in meaningful[:4])[:6]
    return f"{prefix}{year}"


def load_watermark() -> Dict:
    if WATERMARK_FILE.exists():
        try:
            return json.loads(WATERMARK_FILE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {}


def save_watermark(data: Dict):
    WATERMARK_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def load_conference_papers(venue: str, year: int) -> List[Dict]:
    json_path = Path(__file__).parent.parent / "data" / "conference_papers" / f"{venue.lower()}{year}.json"
    if not json_path.exists():
        return []
    try:
        data = json.loads(json_path.read_text(encoding='utf-8'))
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in ['papers', 'results', 'data']:
                if key in data:
                    return data[key]
    except Exception:
        pass
    return []


def scan_baseline(
    venues: List[str],
    years: List[int],
    min_score: float = 20.0,
    full: bool = False,
    dry_run: bool = False
) -> Dict:
    watermark = load_watermark()
    existing_citekeys = set()

    if not full:
        for f in CORPUS_DIR.glob("*.md"):
            existing_citekeys.add(f.stem)
        print(f"[Watermark] Existing: {len(existing_citekeys)} entries")

    print("=" * 60)
    print("Baseline Scanner - 2025论文基线")
    print("=" * 60)
    print(f"Venues: {', '.join(v.upper() for v in venues)}")
    print(f"Years: {', '.join(map(str, years))}")
    print(f"Min score: {min_score}")
    print(f"Mode: {'FULL' if full else 'INCREMENTAL'}")
    print("=" * 60)

    all_papers = []
    stats = {'loaded': 0, 'scored': 0, 'saved': 0, 'skipped': 0, 'new': 0}

    for venue in venues:
        for year in years:
            print(f"\nLoading {venue.upper()}{year}...")
            papers = load_conference_papers(venue, year)
            print(f"  Loaded {len(papers)} papers")
            stats['loaded'] += len(papers)

            for paper in papers:
                title = paper.get('title', '')
                abstract = paper.get('abstract', '')
                keywords = paper.get('keywords', [])
                if isinstance(keywords, str):
                    keywords = [keywords]

                score, problems, techs = score_paper(title, abstract, keywords)

                if score >= min_score:
                    paper['relevance_score'] = score
                    paper['matched_problems'] = problems
                    paper['matched_techs'] = techs
                    paper['venue'] = venue.upper()
                    paper['year'] = year
                    all_papers.append(paper)
                    stats['scored'] += 1

    all_papers.sort(key=lambda x: x['relevance_score'], reverse=True)
    print(f"\nMatched: {stats['scored']} papers (score >= {min_score})")

    if not all_papers:
        return stats

    if not dry_run:
        CORPUS_DIR.mkdir(parents=True, exist_ok=True)

    saved = 0
    for paper in all_papers:
        citekey = generate_citekey(paper['title'], paper.get('year', 2025))
        filename = f"{citekey}.md"
        filepath = CORPUS_DIR / filename

        if not full and filepath.exists():
            stats['skipped'] += 1
            continue

        if not dry_run:
            content = format_corpus_entry(paper, citekey)
            filepath.write_text(content, encoding='utf-8')

        saved += 1
        stats['saved'] += 1
        stats['new'] += 1

        if saved <= 10 or saved % 20 == 0:
            print(f"  + {citekey}: {paper['title'][:45]}... (score={paper['relevance_score']:.0f})")

    if not dry_run and saved > 0:
        watermark['last_scan'] = datetime.now().isoformat()
        watermark['venues'] = venues
        watermark['years'] = years
        watermark['min_score'] = min_score
        watermark['total_saved'] = watermark.get('total_saved', 0) + saved
        save_watermark(watermark)

    print("\n" + "=" * 60)
    print(f"Results: loaded={stats['loaded']}, matched={stats['scored']}, "
          f"new={stats['new']}, skipped={stats['skipped']}")
    print("=" * 60)

    return stats


def format_corpus_entry(paper: Dict, citekey: str) -> str:
    authors = paper.get('authors', [])
    if isinstance(authors, list):
        authors_str = '; '.join(authors[:5])
    else:
        authors_str = str(authors)

    abstract = paper.get('abstract', '') or ''
    title = paper.get('title', '')
    year = paper.get('year', 2025)
    venue = paper.get('venue', 'Conference')
    score = paper.get('relevance_score', 0)
    problems = paper.get('matched_problems', [])
    techs = paper.get('matched_techs', [])
    url = paper.get('url', f"https://arxiv.org/abs/{paper.get('id', '')}")
    citations = paper.get('citation_count', paper.get('citations', 0))

    return f"""---
type: literature-corpus-entry
citekey: {citekey}
title: "{title}"
authors: {authors_str}
year: {year}
venue: {venue}
url: {url}
abstract: |
{abstract[:3000]}
citation_count: {citations}
relevance_score: {score}
matched_problems: [{', '.join(problems)}]
matched_techs: [{', '.join(techs)}]
pre_screened_status: Included
contamination_signals:
  preprint_post_llm_inflection: false
  semantic_scholar_unmatched: null
  openalex_unmatched: null
  crossref_unmatched: null
source: baseline-scan-2025
created: {datetime.now().strftime('%Y-%m-%d')}
---

# {title}

**{venue} {year}** | Citations: {citations} | Score: {score:.0f}

## 作者
{authors_str}

## 摘要
{abstract[:1500]}...

## 匹配问题
{', '.join([f'`{p}`' for p in problems])}

## 匹配技术
{', '.join([f'`{t}`' for t in techs])}

## 链接
[Paper]({url})

---

*Baseline Scanner | {datetime.now().strftime('%Y-%m-%d')}*
"""


def show_stats():
    wm = load_watermark()
    corpus_count = len(list(CORPUS_DIR.glob("*.md"))) if CORPUS_DIR.exists() else 0

    print("=" * 60)
    print("Baseline Scanner - 统计")
    print("=" * 60)
    print(f"Corpus entries: {corpus_count}")
    if wm:
        print(f"Last scan: {wm.get('last_scan', 'never')}")
        print(f"Total saved: {wm.get('total_saved', 0)}")
        print(f"Venues: {wm.get('venues', [])}")
        print(f"Years: {wm.get('years', [])}")
        print(f"Min score: {wm.get('min_score', 'N/A')}")
    print("=" * 60)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Baseline Scanner')
    parser.add_argument('--venues', '-v', default='iclr2025,nips2025',
                        help='Venues (e.g., iclr2025,nips2025)')
    parser.add_argument('--min-score', '-s', type=float, default=20.0,
                        help='Minimum relevance score')
    parser.add_argument('--full', '-f', action='store_true',
                        help='Full scan (ignore watermark)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Dry run')
    parser.add_argument('--stats', action='store_true',
                        help='Show stats only')
    args = parser.parse_args()

    if args.stats:
        show_stats()
        return

    # 解析 venues 和 years
    venues = []
    years = set()
    for v in args.venues.split(','):
        v = v.strip()
        year_match = re.search(r'(\d{4})', v)
        venue_part = re.sub(r'\d{4}', '', v)
        if year_match:
            years.add(int(year_match.group(1)))
        if venue_part:
            venues.append(venue_part.rstrip('_'))

    if not venues:
        venues = ['iclr', 'nips']
    if not years:
        years = {2025}

    scan_baseline(
        venues=venues,
        years=list(years),
        min_score=args.min_score,
        full=args.full,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
