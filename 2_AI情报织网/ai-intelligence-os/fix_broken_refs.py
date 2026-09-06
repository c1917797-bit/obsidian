# -*- coding: utf-8 -*-
"""
fix_broken_refs.py
- 扫描 4_AI情报洞察/ 目录下所有 .md 文件
- 修复 plain text 形式和 wiki link 形式的旧引用
"""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察'

PATH_MAPPINGS = {
    '方法论/输出/课题规划_5场景_2026Q3.md': '课题规划/2026Q3/课题规划_5场景.md',
    '方法论/输出/课题规划_P1重点_v2.0_2026Q3.md': '课题规划/2026Q3/课题规划_P1重点.md',
    '方法论/输出/课题规划_P2观察_v2.0_2026Q3.md': '课题规划/2026Q3/课题规划_P2观察.md',
    '方法论/输出/课题规划_v2.0机制_2026Q3.md': '课题规划/2026Q3/课题规划_v2.0机制.md',
    '方法论/输出/课题规划_推理压缩_5场景_2026Q3.md': '课题规划/2026Q3/推理压缩_5场景.md',
    '方法论/输出/课题规划_推理压缩_v2.0_2026Q3.md': '课题规划/2026Q3/推理压缩_v2.0.md',
    '方法论/输出/推理压缩技术全景图_v2_数据驱动版.md': '论文洞察/推理压缩技术全景图_v2_数据驱动版.md',
    '方法论/一致性测试_评分表_模板.md': '方法论/测评/一致性测试_评分表_模板.md',
    '方法论/一致性测试_结果分析.md': '方法论/测评/一致性测试_结果分析.md',
    '方法论/方法论_v2.0_升级总结.md': '方法论/方法论自更新日志.md',
}

SORTED_KEYS = sorted(PATH_MAPPINGS.keys(), key=lambda x: -len(x))

def fix_content(content):
    """修复 plain text 形式的旧路径引用"""
    changes = []
    new_content = content

    for old_path in SORTED_KEYS:
        if old_path in new_content:
            new_path = PATH_MAPPINGS[old_path]
            new_content = new_content.replace(old_path, new_path)
            count = content.count(old_path) - new_content.count(old_path)
            for _ in range(count):
                changes.append((old_path, new_path))

    return new_content, changes

def main():
    base_path = Path(BASE_DIR)
    if not base_path.exists():
        print(f"目录不存在: {BASE_DIR}")
        return

    md_files = list(base_path.rglob('*.md'))
    print(f"扫描 {len(md_files)} 个 .md 文件")

    total_fixes = 0
    files_with_fixes = []

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            new_content, changes = fix_content(content)

            if changes:
                rel_path = md_file.relative_to(base_path)
                print(f"\n[{rel_path}] 修复 {len(changes)} 处引用:")
                for old, new in changes:
                    print(f"  {old}")
                    print(f"    -> {new}")

                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                total_fixes += len(changes)
                files_with_fixes.append(rel_path)
        except Exception as e:
            print(f"处理失败 {md_file}: {e}")

    print(f"\n=== 总计 ===")
    print(f"修复引用数: {total_fixes}")
    print(f"修改文件数: {len(files_with_fixes)}")

if __name__ == '__main__':
    main()
