#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
html_sink.py - 将 Markdown 报告转换为 HTML 格式
"""
import re
import os
from pathlib import Path
from datetime import datetime

CSS = """
<style>
:root {
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-tertiary: #21262d;
    --border: #30363d;
    --text-primary: #e6edf3;
    --text-secondary: #8b949e;
    --text-muted: #6e7681;
    --accent-blue: #58a6ff;
    --accent-green: #3fb950;
    --accent-orange: #d29922;
    --accent-red: #f85149;
    --accent-purple: #a371f7;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    padding: 2rem;
}

.container { max-width: 1200px; margin: 0 auto; }

/* Header */
.report-header {
    border-bottom: 1px solid var(--border);
    padding-bottom: 1.5rem;
    margin-bottom: 2rem;
}

.report-title {
    font-size: 2rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.report-meta {
    font-size: 0.875rem;
    color: var(--text-secondary);
}

.report-meta span { margin-right: 1.5rem; }

/* Headings */
h1 { font-size: 1.75rem; font-weight: 600; margin: 2rem 0 1rem; color: var(--text-primary); border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }
h2 { font-size: 1.4rem; font-weight: 600; margin: 1.5rem 0 0.75rem; color: var(--accent-blue); }
h3 { font-size: 1.15rem; font-weight: 600; margin: 1.25rem 0 0.5rem; color: var(--text-primary); }
h4 { font-size: 1rem; font-weight: 600; margin: 1rem 0 0.5rem; color: var(--text-secondary); }

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    font-size: 0.9rem;
}

th {
    background: var(--bg-secondary);
    color: var(--text-primary);
    padding: 0.75rem;
    text-align: left;
    font-weight: 600;
    border-bottom: 2px solid var(--border);
}

td {
    padding: 0.75rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
}

tr:hover { background: var(--bg-secondary); }

/* Tags */
.tag {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    background: var(--bg-tertiary);
    border-radius: 4px;
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin: 0.2rem;
}

.tag-red { background: rgba(248, 81, 73, 0.15); color: var(--accent-red); }
.tag-orange { background: rgba(210, 153, 34, 0.15); color: var(--accent-orange); }
.tag-green { background: rgba(63, 185, 80, 0.15); color: var(--accent-green); }
.tag-blue { background: rgba(88, 166, 255, 0.15); color: var(--accent-blue); }
.tag-purple { background: rgba(163, 113, 247, 0.15); color: var(--accent-purple); }

/* Cards */
.card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1rem;
    margin: 1rem 0;
}

.card-header {
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

/* Lists */
ul, ol { padding-left: 1.5rem; margin: 0.5rem 0; }
li { margin: 0.3rem 0; }

/* Code */
code {
    font-family: 'SF Mono', Consolas, monospace;
    background: var(--bg-tertiary);
    padding: 0.15rem 0.4rem;
    border-radius: 3px;
    font-size: 0.875rem;
}

pre {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1rem;
    overflow-x: auto;
    margin: 1rem 0;
}

/* Blockquote */
blockquote {
    border-left: 3px solid var(--accent-blue);
    padding-left: 1rem;
    margin: 1rem 0;
    color: var(--text-secondary);
    font-style: italic;
}

/* Horizontal rule */
hr {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0;
}

/* Highlight */
.highlight {
    background: rgba(88, 166, 255, 0.1);
    border-left: 3px solid var(--accent-blue);
    padding: 0.75rem 1rem;
    margin: 1rem 0;
}

/* Badges */
.badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: 50px;
    font-size: 0.7rem;
    font-weight: 600;
}

.badge-green { background: var(--accent-green); color: #000; }
.badge-orange { background: var(--accent-orange); color: #000; }
.badge-red { background: var(--accent-red); color: #fff; }

/* Grid */
.grid { display: grid; gap: 1rem; }
.grid-2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }

/* Print */
@media print {
    body { background: #fff; color: #000; }
    .tag, .badge { border: 1px solid currentColor; }
}
</style>
"""

def md_to_html(text):
    """Convert Markdown to HTML"""
    lines = text.split('\n')
    result = []
    in_table = False
    in_list = False

    for line in lines:
        # Headers
        if line.startswith('#######'):
            line = re.sub(r'^#######\s+', '<h6>', line) + '</h6>'
        elif line.startswith('######'):
            line = re.sub(r'^######\s+', '<h6>', line) + '</h6>'
        elif line.startswith('#####'):
            line = re.sub(r'^#####\s+', '<h5>', line) + '</h5>'
        elif line.startswith('####'):
            line = re.sub(r'^####\s+', '<h4>', line) + '</h4>'
        elif line.startswith('###'):
            line = re.sub(r'^###\s+', '<h3>', line) + '</h3>'
        elif line.startswith('##'):
            line = re.sub(r'^##\s+', '<h2>', line) + '</h2>'
        elif line.startswith('#'):
            line = re.sub(r'^#\s+', '<h1>', line) + '</h1>'

        # Table detection
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                # Check if header row
                if re.search(r'\|[-:\s]+\|', line):
                    continue  # Skip separator
                parts = [p.strip() for p in line.split('|')[1:-1]]
                result.append('<table><thead><tr>')
                for p in parts:
                    result.append(f'<th>{p}</th>')
                result.append('</tr></thead><tbody>')
            else:
                if re.search(r'\|[-:\s]+\|', line):
                    continue
                parts = [p.strip() for p in line.split('|')[1:-1]]
                result.append('<tr>')
                for p in parts:
                    result.append(f'<td>{p}</td>')
                result.append('</tr>')
            continue
        else:
            if in_table:
                result.append('</tbody></table>')
                in_table = False

        # Bold and italic
        line = re.sub(r'\*\*(.+?)\*\*', '<strong>\1</strong>', line)
        line = re.sub(r'\*(.+?)\*', '<em>\1</em>', line)
        line = re.sub(r'`(.+?)`', '<code>\1</code>', line)

        # Blockquote
        if line.startswith('>'):
            line = f'<blockquote>{line[1:].strip()}</blockquote>'

        # HR
        if line.strip() == '---':
            line = '<hr>'

        # List items
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            cleaned = re.sub(r"^[\*\-\s]+", "", line).strip()
            line = f'<li>{cleaned}</li>'
        elif re.match(r'^\d+\.\s+', line):
            line = re.sub(r'^(\d+)\.\s+', r'<li>\1. ', line) + '</li>'

        # Paragraph
        if line.strip() and not line.startswith('<') and not line.strip().startswith('</'):
            line = f'<p>{line.strip()}</p>'

        result.append(line)

    if in_table:
        result.append('</tbody></table>')

    return '\n'.join(result)

def convert_report(md_path, output_path=None):
    """Convert a markdown report to HTML"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        body = fm_match.group(2)
    else:
        fm_text = ''
        body = content

    # Parse frontmatter
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()

    title = fm.get('title', 'Report')
    date = fm.get('date', datetime.now().strftime('%Y-%m-%d'))
    tags = fm.get('tags', '')

    # Convert body
    body_html = md_to_html(body)

    # Build HTML
    tags_html = ''
    if tags:
        tag_list = [t.strip() for t in tags.replace('[', '').replace(']', '').split(',')]
        for tag in tag_list:
            tags_html += f'<span class="tag">{tag}</span>'

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {CSS}
</head>
<body>
    <div class="container">
        <div class="report-header">
            <h1 class="report-title">{title}</h1>
            <div class="report-meta">
                <span>生成时间: {date}</span>
                {tags_html}
            </div>
        </div>
        <div class="report-body">
            {body_html}
        </div>
    </div>
</body>
</html>"""

    if output_path is None:
        output_path = md_path.replace('.md', '.html')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[OK] Generated: {output_path}")
    return output_path

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python html_sink.py <markdown_file> [output_html]")
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_report(md_file, html_file)
