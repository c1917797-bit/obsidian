#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
report_charts.py - 生成可视化图表 JS/CSS/HTML 片段
支持: Chart.js 图表 / Mermaid 架构图 / 图片卡片
"""
import json
from typing import Dict, List, Any

CHART_ID_COUNTER = 0

def _next_id(prefix="chart"):
    global CHART_ID_COUNTER
    CHART_ID_COUNTER += 1
    return f"{prefix}_{CHART_ID_COUNTER}"

# ============ Chart.js 图表 ============

CHART_CSS = """
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
"""

def bar_chart(labels: List[str], datasets: List[Dict], title: str = "") -> str:
    """生成柱状图 HTML"""
    cid = _next_id("bar")
    canvas = f'<canvas id="{cid}" style="max-height:300px"></canvas>'
    script = f"""
<script>
(function() {{
    const ctx = document.getElementById('{cid}');
    if (!ctx) return;
    new Chart(ctx, {{
        type: 'bar',
        data: {{
            labels: {json.dumps(labels, ensure_ascii=False)},
            datasets: {json.dumps(datasets, ensure_ascii=False)}
        }},
        options: {{
            responsive: true,
            plugins: {{
                {'title' if title else 'legend': {{'display': {str(bool(title)).lower()}, 'text': {json.dumps(title, ensure_ascii=False)}}}
            }},
            scales: {{ y: {{ beginAtZero: true }} }}
        }}
    }});
}})();
</script>"""
    return canvas + script

def radar_chart(labels: List[str], datasets: List[Dict], title: str = "") -> str:
    """生成雷达图 HTML"""
    cid = _next_id("radar")
    canvas = f'<canvas id="{cid}" style="max-height:320px"></canvas>'
    script = f"""
<script>
(function() {{
    const ctx = document.getElementById('{cid}');
    if (!ctx) return;
    new Chart(ctx, {{
        type: 'radar',
        data: {{
            labels: {json.dumps(labels, ensure_ascii=False)},
            datasets: {json.dumps(datasets, ensure_ascii=False)}
        }},
        options: {{
            responsive: true,
            plugins: {{
                {'title' if title else 'legend': {{'display': {str(bool(title)).lower()}, 'text': {json.dumps(title, ensure_ascii=False)}}}
            }}
        }}
    }});
}})();
</script>"""
    return canvas + script

def horizontal_bar(labels: List[str], values: List[float], color: str = "#58a6ff", title: str = "") -> str:
    """生成横向柱状图"""
    datasets = [{"label": title or "数值", "data": values, "backgroundColor": color}]
    cid = _next_id("hbar")
    canvas = f'<canvas id="{cid}" style="max-height:{max(200, len(labels)*40}px"></canvas>'
    script = f"""
<script>
(function() {{
    const ctx = document.getElementById('{cid}');
    if (!ctx) return;
    new Chart(ctx, {{
        type: 'bar',
        data: {{
            labels: {json.dumps(labels, ensure_ascii=False)},
            datasets: {json.dumps(datasets, ensure_ascii=False)}
        }},
        options: {{
            indexAxis: 'y',
            responsive: true,
            plugins: {{ legend: {{ display: false }} }},
            scales: {{ x: {{ beginAtZero: true }} }}
        }}
    }});
}})();
</script>"""
    return canvas + script

def doughnut_chart(labels: List[str], values: List[float], colors: List[str] = None, title: str = "") -> str:
    """生成环形图"""
    if colors is None:
        import colorsys
        colors = [f"hsl({int(h)}, 70%, 50%)" for h in [i/len(labels)*360 for i in range(len(labels))]]
    datasets = [{"data": values, "backgroundColor": colors[:len(labels)]}]
    cid = _next_id("doughnut")
    canvas = f'<canvas id="{cid}" style="max-height:280px;max-width:280px"></canvas>'
    script = f"""
<script>
(function() {{
    const ctx = document.getElementById('{cid}');
    if (!ctx) return;
    new Chart(ctx, {{
        type: 'doughnut',
        data: {{
            labels: {json.dumps(labels, ensure_ascii=False)},
            datasets: {json.dumps(datasets, ensure_ascii=False)}
        }},
        options: {{
            responsive: true,
            plugins: {{
                legend: {{ position: 'bottom' }},
                {'title' if title else 'title': {{'display': {str(bool(title)).lower()}, 'text': {json.dumps(title, ensure_ascii=False)}}}
            }}
        }}
    }});
}})();
</script>"""
    return canvas + script

# ============ Mermaid 架构图 ============

MERMAED_CSS = """
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{ startOnLoad: true, theme: 'dark', themeVariables: {{ primaryColor: '#58a6ff', primaryTextColor: '#e6edf3', primaryBorderColor: '#30363d', lineColor: '#8b949e', secondaryColor: '#21262d', tertiaryColor: '#161b22' }}});</script>
"""

def mermaid_block(diagram_type: str, code: str) -> str:
    """生成 Mermaid 图表"""
    return f'<div class="mermaid">{diagram_type}\n{code}\n</div>'

def table_md(headers: List[str], rows: List[List[str]]) -> str:
    """生成 Markdown 表格 HTML"""
    thead = '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr></thead>'
    tbody = '<tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows) + '</tbody>'
    return f'<table class="data-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table>'

# ============ 图片卡片 ============

def image_card(url: str, alt: str = "", caption: str = "", width: str = "100%") -> str:
    """生成图片卡片 HTML"""
    return f'''
<div class="image-card" style="margin:1.5rem 0">
    <img src="{url}" alt="{alt}" style="width:{width};border-radius:6px;border:1px solid var(--border);" loading="lazy">
    {f'<p class="image-caption">{caption}</p>' if caption else ''}
</div>'''

def topic_card(topic: str, evidence: str, judgment: str, action: str,
              tags: List[str] = None, level: str = "P1") -> str:
    """生成课题卡片: 证据-判断-行动"""
    tag_html = ''.join(f'<span class="tag">{t}</span>' for t in (tags or []))
    level_color = {"P0": "badge-red", "P1": "badge-orange", "P2": "badge-green"}.get(level, "badge-orange")
    return f'''
<div class="topic-card">
    <div class="topic-header">
        <span class="badge {level_color}">{level}</span>
        <strong>{topic}</strong>
        {tag_html}
    </div>
    <div class="topic-body">
        <div class="topic-evidence">
            <span class="topic-label">证据</span>
            <p>{evidence}</p>
        </div>
        <div class="topic-judgment">
            <span class="topic-label">判断</span>
            <p>{judgment}</p>
        </div>
        <div class="topic-action">
            <span class="topic-label">行动</span>
            <p>{action}</p>
        </div>
    </div>
</div>'''

STYLE_EXTRA = """
.image-card { text-align: center; }
.image-caption { font-size: 0.8rem; color: var(--text-secondary); margin-top: 0.5rem; }
.topic-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin: 1rem 0;
    overflow: hidden;
}
.topic-header {
    padding: 0.75rem 1rem;
    background: var(--bg-tertiary);
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex-wrap: wrap;
}
.topic-header strong { color: var(--text-primary); flex: 1; }
.topic-body { padding: 1rem; display: grid; gap: 1rem; }
.topic-label {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    margin-bottom: 0.4rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.topic-evidence .topic-label { background: rgba(88,166,255,0.15); color: var(--accent-blue); }
.topic-judgment .topic-label { background: rgba(210,153,34,0.15); color: var(--accent-orange); }
.topic-action .topic-label { background: rgba(63,185,80,0.15); color: var(--accent-green); }
.topic-body p { margin: 0; color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5; }
.data-table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.875rem; }
.data-table th { background: var(--bg-secondary); color: var(--accent-blue); padding: 0.6rem; text-align: left; border-bottom: 2px solid var(--border); }
.data-table td { padding: 0.5rem 0.6rem; border-bottom: 1px solid var(--border); color: var(--text-secondary); }
.data-table tr:hover td { background: var(--bg-secondary); }
.mermaid { background: var(--bg-secondary); border-radius: 6px; padding: 1rem; margin: 1rem 0; }
"""
