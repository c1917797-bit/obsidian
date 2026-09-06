#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_paper_cards.py - Add ARS-compatible frontmatter to paper-card notes

Adds to all type: paper-card notes:
- citekey: unique citation key generated from title
- authors: "Unknown" (placeholder, can be updated from Zotero)
- year: extracted from date field

Usage:
    python fix_paper_cards.py [--dry-run] [--vault PATH]
"""
import os
import re
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple

def generate_citekey(title: str, year: int) -> str:
    """Generate citekey from title"""
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    clean = re.sub(r'\s+', '', clean)
    clean = clean.lower()[:40]

    words = [w for w in clean if w.isalpha()]
    prefix = ''.join(words[:4]) if len(words) >= 4 else ''.join(words)

    short_hash = hashlib.md5(title.encode()).hexdigest()[:4]

    return f"{prefix}{year}{short_hash}"

def parse_frontmatter(content: str) -> Tuple[dict, str, str]:
    """Parse frontmatter, return (fm_dict, body, full_content)"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content, content

    fm_lines = match.group(1).split('\n')
    fm = {}
    for line in fm_lines:
        if ':' in line:
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")

    return fm, match.group(2), content

def build_frontmatter(fm: dict, citekey: str, authors: str, year: int) -> str:
    """Build new frontmatter"""
    lines = [
        '---',
        f'title: "{fm.get("title", "")}"',
        f'venue: {fm.get("venue", "")}',
        f'authors: "{authors}"',
        f'year: {year}',
        f'citekey: {citekey}',
        f'citations: {fm.get("citations", 0)}',
        f'relevance_score: {fm.get("relevance_score", 0)}',
    ]

    tags = fm.get('tags', '[]')
    if not tags.startswith('['):
        tags = f'[{tags}]'
    lines.append(f'tags: {tags}')

    date_val = fm.get('date', '')
    lines.append(f'date: {date_val}')

    type_val = fm.get('type', 'paper-card')
    lines.append(f'type: {type_val}')

    lines.append('---')
    return '\n'.join(lines)

def process_file(filepath: Path) -> Optional[str]:
    """Process single file, return new content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  [WARN] Read failed {filepath}: {e}")
        return None

    fm, body, _ = parse_frontmatter(content)

    if fm.get('type') != 'paper-card':
        return None

    if 'citekey' in fm:
        return None

    date_str = fm.get('date', '')
    try:
        if date_str:
            year = int(date_str.split('-')[0])
        else:
            year = 2026
    except:
        year = 2026

    title = fm.get('title', filepath.stem)
    ck = generate_citekey(title, year)

    authors = fm.get('authors', 'Unknown')
    new_fm = build_frontmatter(fm, ck, authors, year)

    return new_fm + '\n' + body

def main():
    parser = argparse.ArgumentParser(description='Add ARS frontmatter to paper-card notes')
    parser.add_argument('--vault', default=r'C:\Users\Huawei\Documents\code\Obsidian',
                        help='Obsidian vault path')
    parser.add_argument('--dry-run', action='store_true', help='Display only, no changes')
    parser.add_argument('--force', action='store_true', help='Force update even if citekey exists')
    args = parser.parse_args()

    vault = Path(args.vault)
    count = 0
    updated = 0
    skipped = 0

    print(f"[SCAN] vault: {vault}")
    print(f"[MODE] {'DRY RUN (display only)' if args.dry_run else 'APPLY (actual changes)'}")

    for md_file in vault.rglob('*.md'):
        if '.obsidian' in md_file.parts or '.trash' in md_file.parts:
            continue
        if 'paper-card' not in md_file.read_text(encoding='utf-8', errors='ignore'):
            continue

        count += 1
        result = process_file(md_file)

        if result is None:
            skipped += 1
            continue

        ck_match = re.search(r'citekey:\s*(\S+)', result)
        citekey = ck_match.group(1) if ck_match else 'N/A'

        if args.dry_run:
            print(f"  [FILE] {md_file.relative_to(vault)}")
            print(f"         citekey: {citekey}")
        else:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"  [OK] Updated {md_file.relative_to(vault)}")
                updated += 1
            except Exception as e:
                print(f"  [FAIL] {md_file.relative_to(vault)}: {e}")

    print()
    print(f"[STATS] paper-cards found: {count}")
    print(f"        already have citekey: {skipped}")
    print(f"        need update: {count - skipped}")

    if args.dry_run:
        print()
        print("[TIP] Run without --dry-run to apply changes")

if __name__ == '__main__':
    main()
