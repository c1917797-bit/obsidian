# -*- coding: utf-8 -*-
"""fix_version_refs_v2.py - 批量更新版本引用到最新"""
import os, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察'

REPLACEMENTS = [
    (r'目标\.md\s*v2\.1', '目标.md v2.2'),
    (r'目标\.md\s*v2\.0(?!\.)', '目标.md v2.2'),
    (r'目标\.md（v2\.1）', '目标.md（v2.2）'),
    (r'目标\.md（v2\.0）', '目标.md（v2.2）'),
    (r'洞察写作指南\.md\s*v1\.0', '洞察写作指南.md v1.4'),
    (r'洞察写作指南\.md\s*v1\.1(?!\.)', '洞察写作指南.md v1.4'),
    (r'洞察写作指南\.md\s*v1\.2(?!\.)', '洞察写作指南.md v1.4'),
    (r'洞察写作指南\.md\s*v1\.3(?!\.)', '洞察写作指南.md v1.4'),
    (r'洞察写作指南 v1\.0', '洞察写作指南 v1.4'),
    (r'洞察写作指南 v1\.1(?!\.)', '洞察写作指南 v1.4'),
    (r'洞察写作指南 v1\.2(?!\.)', '洞察写作指南 v1.4'),
    (r'洞察写作指南 v1\.3(?!\.)', '洞察写作指南 v1.4'),
    (r'主模板.*v1\.0(?!\.)', '主模板 v1.3'),
    (r'主模板.*v1\.1(?!\.)', '主模板 v1.3'),
    (r'主模板.*v1\.2(?!\.)', '主模板 v1.3'),
    (r'推理压缩\.md\s*v2\.0(?!\.)', '推理压缩.md v3.0'),
]

def fix(content):
    changes = []
    new = content
    for pat, rep in REPLACEMENTS:
        matches = re.findall(pat, new)
        if matches:
            cnt = len(matches)
            new = re.sub(pat, rep, new)
            changes.append((pat, rep, cnt))
    return new, changes

total = 0
files_changed = []
for md in Path(BASE).rglob('*.md'):
    try:
        with open(md, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        new, changes = fix(content)
        if changes:
            rel = md.relative_to(BASE)
            cnt = sum(c for _,_,c in changes)
            print(f"[{rel}] {cnt} 处")
            with open(md, 'w', encoding='utf-8') as f:
                f.write(new)
            total += cnt
            files_changed.append(rel)
    except Exception as e:
        print(f"ERROR {md.name}: {e}")

print(f"\n总计: {total} 处, {len(files_changed)} 个文件")
