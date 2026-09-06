# -*- coding: utf-8 -*-
"""
fix_version_refs.py
- 修复版本号引用不一致
- 目标.md v1.1/v2.0 -> v2.1
- 推理压缩.md v2.0 -> v3.0
"""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察'

REPLACEMENTS = [
    (r'推理压缩\.md\s*v2\.0', '推理压缩.md v3.0'),
    (r'推理压缩\.md\s*v2 ', '推理压缩.md v3.0 '),
    (r'目标\.md\s*v1\.1', '目标.md v2.1'),
    (r'目标\.md\s*v2\.0', '目标.md v2.1'),
    (r'目标\.md（v2\.0）', '目标.md（v2.1）'),
    (r'目标\.md（v1\.1）', '目标.md（v2.1）'),
]

def fix_content(content):
    changes = []
    new_content = content
    for pattern, replacement in REPLACEMENTS:
        matches = re.findall(pattern, new_content)
        if matches:
            count = len(matches)
            new_content = re.sub(pattern, replacement, new_content)
            changes.append((pattern, replacement, count))
    return new_content, changes

def main():
    base_path = Path(BASE_DIR)
    md_files = list(base_path.rglob('*.md'))
    print(f"扫描 {len(md_files)} 个 .md 文件\n")

    total_fixes = 0
    files_changed = []

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            new_content, changes = fix_content(content)

            if changes:
                rel_path = md_file.relative_to(base_path)
                print(f"[{rel_path}]")
                for pattern, replacement, count in changes:
                    print(f"  {pattern} -> {replacement} ({count}处)")
                    total_fixes += count

                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_changed.append(rel_path)
        except Exception as e:
            print(f"处理失败 {md_file}: {e}")

    print(f"\n=== 总计 ===")
    print(f"修复: {total_fixes} 处")
    print(f"修改文件: {len(files_changed)} 个")

if __name__ == '__main__':
    main()
