# -*- coding: utf-8 -*-
"""
fix_broken_links.py
- 扫描 4_AI情报洞察/ 目录下所有 .md 文件
- 修复因文件移动导致的 broken links
"""
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察'

LINK_MAPPINGS = {
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

NAME_MAPPINGS = {
    '课题规划_5场景_2026Q3': '课题规划_5场景',
    '课题规划_P1重点_v2.0_2026Q3': '课题规划_P1重点',
    '课题规划_P2观察_v2.0_2026Q3': '课题规划_P2观察',
    '课题规划_v2.0机制_2026Q3': '课题规划_v2.0机制',
    '课题规划_推理压缩_5场景_2026Q3': '推理压缩_5场景',
    '课题规划_推理压缩_v2.0_2026Q3': '推理压缩_v2.0',
    '一致性测试_评分表_模板': '测评/一致性测试_评分表_模板',
    '一致性测试_结果分析': '测评/一致性测试_结果分析',
    '方法论_v2.0_升级总结': '方法论自更新日志',
}

WIKILINK_PATTERN = re.compile(r'\[\[([^\]]+)\]\]')
MDLINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')

def extract_old_refs(content):
    """提取所有可能的旧引用"""
    refs = []

    for match in WIKILINK_PATTERN.finditer(content):
        target = match.group(1)
        if '|' in target:
            link, _ = target.split('|', 1)
        else:
            link = target
        refs.append(('wiki', match.start(), target, link.strip()))

    for match in MDLINK_PATTERN.finditer(content):
        url = match.group(2)
        if not url.startswith(('http://', 'https://', '#', 'mailto:')):
            refs.append(('md', match.start(), match.group(2), url.strip()))

    return refs

def find_matching_link(text, mappings, name_mappings):
    """查找匹配的映射"""
    for old, new in mappings.items():
        old_name = Path(old).stem
        if text == old or text == old_name or text.endswith(old):
            return new, 'full_path'

        if text == old_name or old_name in text:
            new_name = Path(new).stem
            return new, 'name_partial'

    for old_name, new_name in name_mappings.items():
        if text == old_name:
            return new_name, 'name_full'
        if old_name in text:
            return new_name, 'name_partial'

    return None, None

def fix_content(content, file_path):
    """修复内容中的 broken links"""
    fixed_content = content
    changes = []

    def replace_wikilink(match):
        target = match.group(1)
        if '|' in target:
            link_part, alias = target.split('|', 1)
        else:
            link_part = target
            alias = None

        link_clean = link_part.strip()

        new_ref, match_type = find_matching_link(link_clean, LINK_MAPPINGS, NAME_MAPPINGS)
        if new_ref:
            new_target = new_ref
            if alias:
                new_target = f"{new_ref}|{alias}"
            else:
                new_target = new_ref
            changes.append(('wiki', link_clean, new_ref))
            return f"[[{new_target}]]"
        return match.group(0)

    def replace_mdlink(match):
        url = match.group(2)
        if url.startswith(('http://', 'https://', '#', 'mailto:')):
            return match.group(0)

        new_ref, match_type = find_matching_link(url, LINK_MAPPINGS, NAME_MAPPINGS)
        if new_ref:
            changes.append(('md', url, new_ref))
            return f"[{match.group(1)}]({new_ref})"
        return match.group(0)

    new_content = WIKILINK_PATTERN.sub(replace_wikilink, fixed_content)
    new_content = MDLINK_PATTERN.sub(replace_mdlink, new_content)

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

            new_content, changes = fix_content(content, md_file)

            if changes:
                rel_path = md_file.relative_to(base_path)
                print(f"\n[{rel_path}] 修复 {len(changes)} 处链接:")
                for link_type, old, new in changes:
                    print(f"  [{link_type}] {old} -> {new}")

                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                total_fixes += len(changes)
                files_with_fixes.append(rel_path)
        except Exception as e:
            print(f"处理失败 {md_file}: {e}")

    print(f"\n=== 总计 ===")
    print(f"修复链接数: {total_fixes}")
    print(f"修改文件数: {len(files_with_fixes)}")

    if files_with_fixes:
        print(f"\n修改的文件:")
        for f in files_with_fixes:
            print(f"  - {f}")

if __name__ == '__main__':
    main()
