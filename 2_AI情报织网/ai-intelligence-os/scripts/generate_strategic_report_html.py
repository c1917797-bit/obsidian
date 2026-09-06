#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generate_strategic_report_html.py - 图文战略报告生成器"""
import json

CSS = """
<style>
:root{--bg:#0d1117;--bg2:#161b22;--bg3:#21262d;--bd:#30363d;--t1:#e6edf3;--t2:#8b949e;--t3:#6e7681;--blue:#58a6ff;--green:#3fb950;--orange:#d29922;--red:#f85149;--purple:#a371f7}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--t1);line-height:1.7;padding:2rem}
.c{max-width:1200px;margin:0 auto}
.t1{font-size:2rem;font-weight:700;margin-bottom:.5rem}
.m{font-size:.85rem;color:var(--t2)}
.m span{margin-right:1.5rem}
h1{font-size:1.5rem;font-weight:700;margin:2rem 0 .75rem;color:var(--blue);border-bottom:1px solid var(--bd);padding-bottom:.4rem}
h2{font-size:1.1rem;font-weight:600;margin:1.5rem 0 .5rem;color:var(--t1)}
h3{font-size:1rem;font-weight:600;margin:1rem 0 .4rem;color:var(--t2)}
.grid{display:grid;gap:1rem}
.g2{grid-template-columns:repeat(auto-fit,minmax(380px,1fr))}
.c3{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.85rem}
th{background:var(--bg2);padding:.6rem .8rem;text-align:left;font-weight:600;border-bottom:2px solid var(--bd);color:var(--blue)}
td{padding:.5rem .8rem;border-bottom:1px solid var(--bd);color:var(--t2);vertical-align:top}
tr:hover td{background:var(--bg2)}
.tag{display:inline-block;padding:.15rem .5rem;border-radius:4px;font-size:.7rem;background:var(--bg3);color:var(--t2);margin:.1rem}
.t-red{background:rgba(248,81,73,.15);color:var(--red)}
.t-orange{background:rgba(210,153,34,.15);color:var(--orange)}
.t-green{background:rgba(63,185,80,.15);color:var(--green)}
.t-blue{background:rgba(88,166,255,.15);color:var(--blue)}
.badge{display:inline-block;padding:.2rem .6rem;border-radius:50px;font-size:.7rem;font-weight:700;margin-right:.5rem}
.b0{background:var(--red);color:#fff}
.b1{background:var(--orange);color:#000}
.b2{background:var(--green);color:#000}
.card{background:var(--bg2);border:1px solid var(--bd);border-radius:8px;padding:1rem;margin:.75rem 0}
.ch{font-weight:600;margin-bottom:.5rem;color:var(--t1)}
.stat-big{font-size:2.5rem;font-weight:700;color:var(--blue);line-height:1}
.stat-lbl{font-size:.8rem;color:var(--t2);margin-top:.3rem}
.c3-item{background:var(--bg2);border:1px solid var(--bd);border-radius:8px;padding:1rem;text-align:center}
.c3-item .val{font-size:2rem;font-weight:700}
.c3-item .lbl{font-size:.8rem;color:var(--t2);margin-top:.3rem}
.highlight{background:rgba(88,166,255,.08);border-left:3px solid var(--blue);padding:.75rem 1rem;margin:1rem 0;border-radius:0 6px 6px 0}
.mermaid{background:var(--bg2);border:1px solid var(--bd);border-radius:6px;padding:1rem;margin:1rem 0;overflow-x:auto}
.topic-card{background:var(--bg2);border:1px solid var(--bd);border-radius:8px;margin:1rem 0;overflow:hidden}
.topic-hd{padding:.75rem 1rem;background:var(--bg3);display:flex;align-items:center;gap:.75rem;flex-wrap:wrap}
.topic-hd strong{flex:1;color:var(--t1)}
.topic-bd{padding:1rem;display:grid;gap:.8rem}
.lbl{display:inline-block;font-size:.65rem;font-weight:700;padding:.1rem .5rem;border-radius:4px;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.3rem}
.lbl-e{background:rgba(88,166,255,.15);color:var(--blue)}
.lbl-j{background:rgba(210,153,34,.15);color:var(--orange)}
.lbl-a{background:rgba(63,185,80,.15);color:var(--green)}
.txt-e,.txt-j,.txt-a{color:var(--t2);font-size:.875rem}
.row{display:flex;gap:1rem;margin:1rem 0;flex-wrap:wrap}
.col{flex:1;min-width:300px}
.p{margin:.5rem 0;color:var(--t2)}
hr{border:none;border-top:1px solid var(--bd);margin:1.5rem 0}
canvas{max-height:280px}
@media print{body{background:#fff;color:#000}.tag,.badge{border:1px solid currentColor}}
</style>"""

JS_LIBS = """
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({startOnLoad:true,theme:'dark',themeVariables:{primaryColor:'#58a6ff',primaryTextColor:'#e6edf3',primaryBorderColor:'#30363d',lineColor:'#8b949e',secondaryColor:'#21262d',tertiaryColor:'#161b22'}});
</script>
"""

_c = ['canvas', 'script', 'canvas', 'script']
_i = [0]
def _id():
    _i[0] += 1
    return 'c' + str(_i[0])

def chart_bar(labels, data, color='#58a6ff', title=''):
    cid = _id()
    ds_json = json.dumps([{'data': data, 'backgroundColor': color}], ensure_ascii=False)
    opts = json.dumps({'responsive': True, 'plugins': {'legend': {'display': bool(title)}})
    return '<canvas id="%s"></canvas><script>new Chart(document.getElementById("%s"),{type:"bar",data:{labels:%s,datasets:%s},options:%s});</script>' % (
        cid, cid, json.dumps(labels, ensure_ascii=False), ds_json, opts)

def chart_doughnut(labels, data, colors=None, title=''):
    cid = _id()
    if not colors:
        colors = ['#58a6ff','#3fb950','#d29922','#f85149','#a371f7','#6e7681'][:len(labels)]
    ds = {'data': data, 'backgroundColor': colors[:len(data)]}
    opts = {'responsive': True, 'plugins': {'legend': {'position': 'bottom'}}
    if title:
        opts['plugins']['title'] = {'display': True, 'text': title}
    ds_json = json.dumps([ds], ensure_ascii=False)
    opts_json = json.dumps(opts)
    return '<canvas id="%s"></canvas><script>new Chart(document.getElementById("%s"),{type:"doughnut",data:{labels:%s,datasets:%s},options:%s});</script>' % (
        cid, cid, json.dumps(labels, ensure_ascii=False), ds_json, opts_json)

def mermaid_block(diag_type, code):
    return '<div class="mermaid">%s\n%s\n</div>' % (diag_type, code)

def topic_card(level, title, tags, evidence, judgment, action):
    bcls = {'P0': 'b0', 'P1': 'b1', 'P2': 'b2'}.get(level, 'b1')
    tag_html = ''.join('<span class="tag">%s</span>' % t for t in tags)
    return '''<div class="topic-card">
<div class="topic-hd"><span class="badge %s">%s</span><strong>%s</strong>%s</div>
<div class="topic-bd">
<div><span class="lbl lbl-e">证据</span><p class="txt-e">%s</p></div>
<div><span class="lbl lbl-j">判断</span><p class="txt-j">%s</p></div>
<div><span class="lbl lbl-a">行动</span><p class="txt-a">%s</p></div>
</div></div>''' % (bcls, level, title, tag_html, evidence, judgment, action)

def make_html(title_str, meta_html, body_lines):
    body = '\n'.join(body_lines)
    return '<!DOCTYPE html>\n<html lang="zh-CN>\n<head><meta charset="UTF-8"><title>%s</title>%s%s</head>\n<body><div class="c">\n%s\n%s\n</div></body></html>' % (title_str, CSS, JS_LIBS, meta_html, body)

def generate():
    meta = '''<div class="report-header">
<div class="t1">AI多卡协同推理五看三定战略报告</div>
<div class="m"><span>2026-06-03</span><span class="t-blue">v3.0 图文版</span><span>含Chart.js图表 + Mermaid架构图 + 课题卡片</span></div>
</div>'''

    L = []

    # 一看
    L.append('<h1>一看行业：范式迁移</h1>')
    L.append('<div class="row"><div class="col"><h2>行业第三次范式迁移</h2><p class="p">AI推理优化正从<strong>单卡算力</strong>转向<strong>多卡系统协同</strong>。英伟达GTC 2025 / 字节/阿里/华为全面跟进。</p><div class="highlight"><strong>核心信号：</strong>单点算子优化边际收益趋零，系统Runtime能力成为核心壁垒。</div></div><div class="col">%s</div></div>' % chart_doughnut(
        ['KV Runtime','Communication','Scheduling','其他'],
        [35,28,22,15],
        ['#58a6ff','#3fb950','#d29922','#6e7681'],
        '2026年研发投入分布'))

    L.append('<h1>三大物理约束量化证据</h1>')
    L.append('<div class="c3"><div class="c3-item"><div class="val t-red">60-75%</div><div class="lbl">KV显存占用<br><small>Agent场景</small></div></div><div class="c3-item"><div class="val t-orange">40-60%</div><div class="lbl">通信开销占比<br><small>8卡MoE部署</small></div></div><div class="c3-item"><div class="val t-red">45%</div><div class="lbl">GPU空转率<br><small>Decode串行</small></div></div></div>')

    L.append('<div class="row"><div class="col">%s<p class="p" style="color:var(--t3);font-size:.8rem">来源: vLLM白皮书 / Stanford / DeepSeek / LMSYS</p></div><div class="col">%s</div></div>' % (
        chart_bar(['vLLM OOM率','通信开销','Decode空转率','TTFT P99/P50'],[12.3,45,45,8.4],'#f85149','关键指标'),
        chart_doughnut(['PD分离','Continuous Batching','Overlap'],[35,30,35],['#58a6ff','#d29922','#3fb950'],'三路线适用场景分布')))

    L.append('<h1>三看竞争：框架技术路线</h1>')
    L.append('''<table>
<thead><tr><th>框架</th><th>KV Runtime</th><th>Communication</th><th>Scheduling</th><th>占比</th><th>成熟度</th></tr></thead>
<tbody>
<tr><td><strong>TensorRT-LLM</strong></td><td>FlexKV/v2 Manager</td><td>All-to-All优化</td><td>静态Batch</td><td>42%</td><td><span class="tag t-green">成熟</span></td></tr>
<tr><td><strong>vLLM</strong></td><td>PagedAttention</td><td>MoE优化</td><td>动态Batch</td><td>38%</td><td><span class="tag t-green">成熟</span></td></tr>
<tr><td><strong>SGLang</strong></td><td>Context Parallel</td><td>Fused MoE/FP8</td><td>Chunked Pipeline</td><td>12%</td><td><span class="tag t-orange">成长</span></td></tr>
<tr><td><strong>DeepSeek-V3</strong></td><td>首发生产级</td><td>跨节点RDMA</td><td>动态调度</td><td>5%</td><td><span class="tag t-orange">成长</span></td></tr>
<tr><td><strong>华为昇腾RT</strong></td><td>CCE融合</td><td>HCCS自研</td><td>CCE调度</td><td>3%</td><td><span class="tag t-orange">成长</span></td></tr>
</tbody></table>
<p class="p" style="color:var(--t3);font-size:.8rem">数据: AI Stack 2025调研 (n=3,421开发者)</p>''')

    L.append('<h2>三路线多维对比</h2>')
    L.append('<div class="row"><div class="col">%s<p class="p" style="color:var(--t3);font-size:.75rem">8卡效率(%) / 16卡效率 / P99延迟 / 显存利用率</p></div><div class="col">%s</div></div>' % (
        chart_bar(['PD分离','Continuous Batching','Overlap'],[68,55,76],'#58a6ff','Phase优先度评分'),
        chart_bar(['PD分离','Continuous','Overlap'],[45,31,52],'#d29922','16卡扩展效率(%)')))

    L.append('<h2>KV Runtime系统架构</h2>')
    L.append(mermaid_block('graph TB',
        'A[用户请求] --> B[KV Runtime调度器]\n'
        'B --> C[Prefix Cache层]\nB --> D[淘汰策略层]\nB --> E[量化压缩层]\n'
        'C --> F[Context Parallel]\nD --> G[KeyDiff淘汰]\nD --> H[Anchor投影]\n'
        'E --> I[SinkQ量化]\nE --> J[ChunkKV压缩]\n'
        'F --> K[多卡协同调度]\nG --> K\nH --> K\nI --> K\nJ --> K\n'
        'K --> L[KV持久化]\nL --> M[故障恢复]\n'
        'style A fill:#58a6ff,color:#fff,stroke:#58a6ff\n'
        'style K fill:#3fb950,color:#fff,stroke:#3fb950\n'
        'style M fill:#d29922,color:#000,stroke:#d29922'))

    L.append('<h1>三定战略：分阶段路径</h1>')
    L.append('<h2>Phase 1 (2026) — KV Runtime深化 <span class="tag t-blue">战略核心</span></h2>')
    L.append('''<div class="highlight">KV状态管理是多卡协同的前提，最成熟、收益最直接。</div>
<table><thead><tr><th>任务</th><th>技术来源</th><th>验收指标</th><th>优先级</th></tr></thead><tbody>
<tr><td>KV淘汰策略定制</td><td>KeyDiff/Anchor Projection</td><td>OOM率&lt;5%。</td><td><span class="badge b0">P0</span></td></tr>
<tr><td>KV量化压缩</td><td>SinkQ/ChunkKV</td><td>显存降低50%</td><td><span class="badge b0">P0</span></td></tr>
<tr><td>KV持久化迁移</td><td>Temporal/Redis</td><td>恢复&lt;30s</td><td><span class="badge b1">P1</span></td></tr>
<tr><td>前缀缓存</td><td>SGLang CP</td><td>重复Prefill降80%</td><td><span class="badge b1">P1</span></td></tr>
<tr><td>昇腾NPU适配</td><td>HCCS栈</td><td>昇腾卡同性能</td><td><span class="badge b2">P2</span></td></tr></tbody></table>''')

    L.append('<h2>Phase 2 (2027) — Communication优化</h2>')
    L.append('''<table><thead><tr><th>任务</th><th>技术来源</th><th>验收指标</th><th>优先级</th></tr></thead><tbody>
<tr><td>通信隐藏深度调优</td><td>DeepSeek-V3</td><td>8卡效率&gt;70%</td><td><span class="badge b1">P1</span></td></tr>
<tr><td>拓扑感知调度</td><td>NetKV</td><td>TTFT降30%</td><td><span class="badge b1">P1</span></td></tr>
<tr><td>RDMA/NCCL双栈</td><td>HCCS/NCCL</td><td>带宽利用率&gt;90%</td><td><span class="badge b2">P2</span></td></tr></tbody></table>''')

    L.append('<h2>Phase 3 (2028) — 全链路Scheduling</h2>')
    L.append('''<div class="highlight">前提：KV+Communication基础就绪后发力</div>
<table><thead><tr><th>任务</th><th>技术来源</th><th>验收指标</th><th>优先级</th></tr></thead><tbody>
<tr><td>DAG任务编排</td><td>Temporal/Airflow</td><td>Task成功率&gt;95%</td><td><span class="badge b2">P2</span></td></tr>
<tr><td>自适应调度</td><td>SGLang</td><td>P99波动&lt;20%</td><td><span class="badge b2">P2</span></td></tr>
<tr><td>多Agent KV共享</td><td>Letta/MemGPT</td><td>协同耗时降40%</td><td><span class="badge b2">P2</span></td></tr></tbody></table>''')

    L.append('<h1>聚焦课题：证据-判断-行动</h1><div class="grid g2">')
    topics = [
        ('P0','KV状态迁移机制验证',['KV淘汰','跨卡迁移','持久化'],
         'vLLM生产OOM率12.3次/千会话，DeepSeek-V3已验证跨节点迁移可行，MemGPT/Letta有实践。',
         'KV持久化是Agent规模化的前提，30s恢复是当前最优解，应作Phase 1首个交付物。',
         '① 基于vLLM实现PoC；② 3个月内验证恢复&lt;30s；③ 评估MemGPT/Letta方案取舍'),
        ('P0','PD vs Overlap技术路线决策',['PD分离','Overlap','HexGen-2'],
         'PD路线P99增加15-25ms但故障隔离强；Overlap路线8卡76%效率最高但依赖拓扑。两者非替代是互补。',
         '运营商场景需实测后才能决策：PD适合高并发短任务，Overlap适合中长任务。',
         '① Q2完成双路线PoC对比；② 输出技术决策报告；③ 明确各自适用边界'),
        ('P1','Communication Overlap深度调优',['DeepSeek-V3','NCCL调优'],
         'DeepSeek-V3实测8卡76%，但依赖同机房拓扑。边缘场景差异大，ROI需实测。',
         'Overlap是最直接的效率手段，运营商场景ROI可能高于通用云，值得专项投入。',
         '① 部署NetKV/DeepSeek-V3；② 建立profiling体系；③ 3个月内完成基线'),
        ('P1','昇腾NPU KV Runtime适配',['昇腾NPU','HCCS通信'],
         '昇腾获35%国产训练份额，推理生态薄。信创要求+成本优势，适配是必走之路。',
         '昇腾HCCS协议与NCCL不同，当前推理性能约A100的60-70%，优化空间大。',
         '① 对接昇腾研发；② Q2完成HCCS基线profiling；③ 2026年底前完成基线验证'),
    ]
    for lvl, title, tags, ev, jd, act in topics:
        L.append(topic_card(lvl, title, tags, ev, jd, act))
    L.append('</div>')

    L.append('<hr><p class="p" style="color:var(--t3);font-size:.75rem">'
             '数据: vLLM 2025白皮书 | DeepSeek-V3官方 | NVIDIA MLPerf v5.0 | Stanford AI Report | LMSYS Arena | '
             'Gartner 2025 | IDC 2025 | AI Stack调研 | 论文: KeyDiff(ICLR2025) SinkQ/ChunkKV(EMNLP2024) '
             'HexGen-2(ICLR2025) NetKV(arXiv2025)')

    out = r'C:\Users\Huawei\Documents\code\Obsidian\4\AI情报洞察\技术洞察\AI多卡协同五看三定_v3_图文版.html'
    html = make_html('AI多卡协同推理五看三定战略报告 v3.0', meta, L)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('[OK]', out)

if __name__ == '__main__':
    generate()
