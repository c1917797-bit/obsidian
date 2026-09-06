<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agent时代AI推理优化技术规划</title>
<style>
:root{--bg:#fff;--bg-alt:#f7f9fc;--border:#d0d7de;--text:#1a1a1a;--muted:#57606a;--primary:#003366;--pl:#e8f0fe;--accent:#0550ae;--ok:#1a7f37;--warn:#9a6700}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.65;font-size:15px}
nav{position:fixed;top:0;left:0;width:230px;height:100vh;background:var(--bg-alt);border-right:1px solid var(--border);padding:1rem .75rem;overflow-y:auto;font-size:.8rem}
nav a{display:block;padding:.35rem .5rem;color:var(--muted);text-decoration:none;border-radius:4px}
nav a:hover{background:var(--pl);color:var(--primary)}
nav .ng{font-weight:600;color:var(--primary);margin:.75rem .5rem .25rem;font-size:.72rem;text-transform:uppercase;letter-spacing:.04em}
main{margin-left:230px;max-width:980px;padding:2rem 2.5rem 4rem}
.page{margin-bottom:3.5rem;padding-bottom:2rem;border-bottom:2px solid var(--border)}
.ptitle{font-size:1.75rem;font-weight:700;color:var(--primary);margin-bottom:.75rem}
.meta{color:var(--muted);font-size:.875rem;margin-top:.5rem}
.carry{background:#fff8e6;border-left:4px solid var(--warn);padding:.75rem 1rem;margin:1rem 0;font-size:.9rem}
.page-q{background:var(--pl);border-left:4px solid var(--primary);padding:.85rem 1.1rem;margin:1rem 0;font-weight:600;color:var(--primary)}
.claim{background:var(--bg-alt);border:1px solid var(--border);padding:.75rem 1rem;margin:.75rem 0;font-size:.95rem;font-style:italic;color:var(--muted)}
.scr{border:1px solid var(--border);border-radius:6px;margin:1rem 0;overflow:hidden}
.scr-h{background:var(--primary);color:#fff;padding:.45rem .85rem;font-size:.82rem;font-weight:600}
.scr-b{padding:.85rem 1.1rem}
.scr-b .view{font-weight:600;color:var(--primary);margin-bottom:.35rem}
.scr-b .evi{font-size:.88rem;margin:.5rem 0}
.scr-b .so{margin-top:.5rem;padding-top:.5rem;border-top:1px dashed var(--border);font-size:.92rem}
.concl{background:var(--bg-alt);border:1px solid var(--border);padding:.85rem 1.15rem;margin-top:1.5rem;font-size:.95rem}
.concl strong{color:var(--primary)}
.trans{background:var(--pl);border:1px dashed var(--accent);padding:.75rem 1rem;margin-top:1rem;font-size:.92rem}
h2{font-size:1.2rem;color:var(--primary);margin:1.5rem 0 .65rem;border-bottom:1px solid var(--border);padding-bottom:.3rem}
h3{font-size:1.02rem;margin:1rem 0 .45rem}
table{width:100%;border-collapse:collapse;margin:.85rem 0;font-size:.86rem}
th{background:var(--primary);color:#fff;padding:.55rem .7rem;text-align:left}
td{padding:.55rem .7rem;border-bottom:1px solid var(--border);vertical-align:top}
tr:nth-child(even){background:var(--bg-alt)}
.tag{display:inline-block;padding:.12rem .4rem;background:var(--bg-alt);border:1px solid var(--border);border-radius:3px;font-size:.72rem;margin:.1rem}
.insight{display:inline-block;background:var(--accent);color:#fff;padding:.1rem .45rem;border-radius:3px;font-size:.75rem;font-weight:600}
.topic{display:inline-block;background:var(--primary);color:#fff;padding:.15rem .55rem;border-radius:4px;font-size:.82rem;font-weight:600}
.evidence{font-size:.78rem;color:var(--muted)}
.evidence a{color:var(--accent)}
.fig{margin:1.1rem 0;text-align:center}
.fig svg{max-width:100%;height:auto}
.fig-cap{font-size:.8rem;color:var(--muted);margin-top:.4rem;text-align:left}
.card{border:1px solid var(--border);border-radius:6px;padding:1rem;margin:.85rem 0;background:#fff}
.card-t{font-weight:700;color:var(--primary);margin-bottom:.4rem}
.step{display:flex;gap:.2rem;margin-bottom:.85rem;flex-wrap:wrap}
.step span{padding:.2rem .45rem;font-size:.72rem;border-radius:3px;background:var(--bg-alt);color:var(--muted)}
.step span.on{background:var(--primary);color:#fff}
.step span.done{background:var(--pl);color:var(--primary)}
.footnote{font-size:.78rem;color:var(--muted);margin-top:.5rem}
@media print{nav{display:none}main{margin-left:0;max-width:100%}}
@media(max-width:900px){nav{position:static;width:100%;height:auto}main{margin-left:0;padding:1rem}}
</style>
</head>
<body>
<nav>
<div class="ng">报告</div>
<a href="#cover">封面</a><a href="#p1">P1 执行摘要</a>
<div class="ng">洞察</div>
<a href="#p2">P2 看趋势</a><a href="#p3">P3 看业界</a><a href="#p4">P4 看竞争</a><a href="#p5">P5 看机会</a>
<div class="ng">总结与课题</div>
<a href="#p6">P6 战略总结</a><a href="#p7">P7 课题 N</a><a href="#p8">P8 课题 N+1</a>
<a href="#appendix">附录</a>
</nav>
<main>

<section id="cover" class="page">
<h1 class="ptitle">Agent 时代 AI 推理优化技术规划</h1>
<p class="meta">生成时间：2026-06-10 · 读者：昇腾 NPU 推理加速团队 · 叙事：洞察 → 总结 → 课题</p>
<p class="meta"><span class="tag">State-Centric</span><span class="tag">Qwen3-30B-A3B</span><span class="tag">MindIE 插件</span><span class="tag">MoE EP</span></p>
<p style="margin-top:1rem">本报告以 <strong>Qwen3-30B-A3B</strong> 为统一算例模型，沿 L0→L5 分析层级，从四看洞察推导两大课题，并在 MindIE / 灵衢 / HCCL 之上以 <strong>L2 插件</strong> 交付，不重复造 Runtime 轮子。</p>
</section>

<section id="p1" class="page">
<h1 class="ptitle">P1 执行摘要</h1>
<div class="page-q">B1 本页问题：Agent 时代推理优化的战略主线是什么？竞争力锚点在哪？</div>
<div class="claim">B2 待证命题：本页将证明——四看洞察可闭合推导至两大控制点（压状态 / 压流量），并映射为课题 N 与 N+1。</div>

<div class="scr"><div class="scr-h">SCR 片1 · 叙事主线</div><div class="scr-b">
<div class="view">【观点】推理优化范式正从 Compute-Centric 转向 State-Centric；竞争力锚点为吞吐与时延，而非单纯峰值算力。</div>
<div class="evi">【证据】Gemini 1.5 Pro 支持 <strong>2M token</strong> 上下文；GPT-4o <strong>128K</strong>。<span class="evidence"><a href="https://developers.googleblog.com/en/gemini-15-pro-2m-context/">Google Developers Blog</a></span></div>
<div class="so">【所以】长上下文 + Agent 多轮使 <strong>状态（KV）</strong> 成为与权重并列的 HBM 占用主体。</div>
</div></div>

<div class="scr"><div class="scr-h">SCR 片2 · 算例锚点（Qwen3-30B-A3B）</div><div class="scr-b">
<div class="view">【观点】对 MoE 模型，State-bound 来自 <strong>权重 + B×S·KV 共存</strong>，而非单会话 KV 超过权重。</div>
<div class="evi">【证据】L=48, H=4, D=128, M=2；权重 FP16 ≈ <strong>61 GB</strong>；S=32K 单会话 KV ≈ <strong>3 GB</strong>；B=8 时 KV ≈ 24 GB → 合计 <strong>≈85 GB</strong>（超 80GB 卡）。<span class="evidence"><a href="https://huggingface.co/Qwen/Qwen3-30B-A3B">HF Qwen3-30B-A3B</a></span></div>
<div class="so">【所以】Agent Serving 下须同时关注 <strong>S 增长</strong>（多轮）与 <strong>B 并发</strong>。</div>
</div></div>

<div class="scr"><div class="scr-h">SCR 片3 · 洞察→课题（预告，正式命名见 P6.4）</div><div class="scr-b">
<div class="view">【观点】四看洞察 I1–I4 闭合至两大控制点，对应两个 L2 插件课题。</div>
<table><tr><th>洞察</th><th>控制点</th><th>课题</th></tr>
<tr><td><span class="insight">I1</span> State-bound</td><td>压状态（ΔS + ΔM）</td><td><span class="topic">N</span> 语义感知动态 KV 稀疏化</td></tr>
<tr><td><span class="insight">I2</span> 路径 B Comm</td><td>压流量</td><td><span class="topic">N+1</span> MoE 通信量压缩</td></tr>
<tr><td><span class="insight">I3</span> L2 工程化缺口</td><td>语义策略 + 载荷压缩</td><td>N / N+1</td></tr>
<tr><td><span class="insight">I4</span> L2 叠加 L1</td><td>插件交付</td><td>集成边界</td></tr></table>
<div class="so">【所以】全文严格遵循 <strong>洞察 → 总结 → 课题</strong>，P6.4 首次正式命名 N/N+1。</div>
</div></div>

<div class="fig">
<svg viewBox="0 0 760 140" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="22" font-size="12" font-weight="bold" fill="#003366">洞察 → 课题 → 竞争力</text>
<rect x="20" y="35" width="70" height="36" fill="#0550ae"/><text x="55" y="58" text-anchor="middle" font-size="9" fill="#fff">I1 P2</text>
<rect x="100" y="35" width="70" height="36" fill="#0550ae"/><text x="135" y="58" text-anchor="middle" font-size="9" fill="#fff">I2 P3</text>
<rect x="180" y="35" width="70" height="36" fill="#0550ae"/><text x="215" y="58" text-anchor="middle" font-size="9" fill="#fff">I3 P4</text>
<rect x="260" y="35" width="70" height="36" fill="#0550ae"/><text x="295" y="58" text-anchor="middle" font-size="9" fill="#fff">I4 P5</text>
<text x="340" y="58" font-size="14" fill="#003366">→</text>
<rect x="360" y="35" width="90" height="36" fill="#e8f0fe" stroke="#003366"/><text x="405" y="58" text-anchor="middle" font-size="9">压状态</text>
<rect x="460" y="35" width="90" height="36" fill="#e8f0fe" stroke="#003366"/><text x="505" y="58" text-anchor="middle" font-size="9">压流量</text>
<text x="560" y="58" font-size="14" fill="#003366">→</text>
<rect x="580" y="30" width="80" height="46" fill="#003366"/><text x="620" y="50" text-anchor="middle" font-size="9" fill="#fff">N</text><text x="620" y="65" text-anchor="middle" font-size="9" fill="#fff">N+1</text>
<text x="680" y="58" font-size="14" fill="#003366">→</text>
<rect x="700" y="35" width="50" height="36" fill="#f7f9fc" stroke="#d0d7de"/><text x="725" y="58" text-anchor="middle" font-size="8">TPS</text>
<rect x="20" y="90" width="720" height="40" fill="#f7f9fc" stroke="#d0d7de"/>
<text x="380" y="108" text-anchor="middle" font-size="10">根技术延伸：量化 · 稀疏 · 蒸馏 → 参数时代能力复用到 State / Comm</text>
<text x="380" y="122" text-anchor="middle" font-size="9" fill="#57606a">交付形态：MindIE / CANN / HCCL 插件 — 不造 Runtime</text>
</svg>
<p class="fig-cap">图 P1-1：全文推导链总览</p>
</div>

<div class="concl"><strong>B4 本页已证：</strong>Agent 时代推理竞争力取决于状态与通信管理；Qwen3-30B-A3B 算例证出 B×S·KV 与权重共存触顶 HBM。</div>
<div class="trans"><strong>B5 过渡：</strong>首要绑定约束是否仍为算力？→ <strong>P2</strong></div>
</section>

<section id="p2" class="page">
<div class="step"><span class="on">P2</span><span>P3</span><span>P4</span><span>P5</span><span>P6</span></div>
<h1 class="ptitle">P2 看趋势：State-bound 成为 Serving 首要约束 <span class="insight">→ I1</span></h1>
<div class="page-q">B1 承接 P1：Agent + 长上下文下，首要绑定约束是否仍为算力？</div>
<div class="claim">B2 待证命题：本页将证明——有状态 Agent Serving 下，HBM 容量（State）先于 FLOPs 触顶，系统进入 State-bound 范式。</div>

<div class="scr"><div class="scr-h">Step1 · 工作负载：有状态多轮 Agent</div><div class="scr-b">
<div class="view">【观点】工作负载从无状态单次问答变为有状态多轮 Agent；每轮 tool 调用与上下文注入使 <strong>unique KV 随轮次累积</strong>。</div>
<div class="evi">【证据】Stateful Inference 显示多轮会话 KV 增长可达单轮的 <strong>2.1×–4.2×</strong>；IntentKV 针对 cross-turn 意图稀疏。<span class="evidence"><a href="https://arxiv.org/html/2606.09916">IntentKV</a></span></div>
<div class="so">【所以】公式中 <strong>S</strong> 随 Agent 轨迹增长，且多会话叠加 <strong>B</strong>。</div>
</div></div>

<div class="scr"><div class="scr-h">Step2 · KV footprint 公式与 Qwen3-30B-A3B 算例</div><div class="scr-b">
<div class="view">【观点】KV 占用可审计：KVCache = 2 × L × H × D × S × B × M（字节）。</div>
<table><tr><th>符号</th><th>Qwen3-30B-A3B</th><th>说明</th></tr>
<tr><td>L / H / D / M</td><td>48 / 4 / 128 / 2</td><td>GQA 32Q/4KV；MoE 128 experts top-8</td></tr>
<tr><td>系数</td><td>98,304 B/token</td><td>≈96 KB/token</td></tr>
<tr><td>S=8K, B=1</td><td>≈0.8 GB</td><td>与公开测算 ~805MB 一致</td></tr>
<tr><td>S=32K, B=1</td><td>≈3.0 GB</td><td>KV ≪ 权重 61GB</td></tr>
<tr><td>S=32K, B=8</td><td>≈24 GB</td><td>权重+KV ≈85GB → OOM</td></tr>
<tr><td>S=32K, B=16</td><td>≈48 GB</td><td>仅 KV 已接近单卡容量</td></tr></table>
<div class="so">【所以】对该 MoE，State-bound 主因是 <strong>61GB 权重 + B×S·KV</strong>，非「32K 后 KV>weights」（交叉点 S≈620K，超原生 32K）。</div>
</div></div>

<div class="scr"><div class="scr-h">Step3 · 算力未消失，但 Serving 容量非算力绑定</div><div class="scr-b">
<div class="view">【观点】Decode 阶段 memory-bandwidth bound；Continuous Batching 提高利用率但 <strong>不减 KV 总量</strong>。</div>
<div class="evi">【证据】vLLM 生产部署中 GPU 显存利用率可达 <strong>90–92%</strong>，KV 为 OOM 主因。<span class="evidence"><a href="https://arxiv.org/abs/2309.06180">PagedAttention (vLLM)</a></span></div>
<div class="so">【所以】<strong>专家限定</strong>：本页论 Serving 并发容量；单请求 Prefill 峰值可 compute-bound，不与本页矛盾。</div>
</div></div>

<div class="scr"><div class="scr-h">Step4–5 · State-bound 判定与 State-Centric 命名</div><div class="scr-b">
<div class="view">【观点】当 HBM 被权重+KV 占满，系统主矛盾从「装不下（参数）」变为「存不下（状态）」→ <strong>State-Centric</strong> 范式。</div>
<div class="evi">【证据】NVIDIA Dynamo 将 KV 作为一等公民：HBM→CPU→SSD→网络分层管理。<span class="evidence"><a href="https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/">NVIDIA Dynamo</a></span></div>
<div class="so">【所以】产出洞察 <span class="insight">I1</span>：Agent Serving 下 unique KV 增长 → State-bound → 控制点 <strong>压状态</strong>。</div>
</div></div>

<div class="fig">
<svg viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="12" font-weight="bold" fill="#003366">Qwen3-30B-A3B：KV 随 S 增长 vs 权重线（B=1）</text>
<line x1="60" y1="180" x2="640" y2="180" stroke="#333"/>
<line x1="60" y1="30" x2="60" y2="180" stroke="#333"/>
<text x="350" y="210" text-anchor="middle" font-size="10">序列长度 S (K tokens)</text>
<text x="25" y="105" font-size="10" transform="rotate(-90 25 105)">显存 GB</text>
<polyline points="60,170 160,165 260,155 360,140 460,115 560,80 640,50" fill="none" stroke="#0550ae" stroke-width="2"/>
<line x1="60" y1="55" x2="640" y2="55" stroke="#c00" stroke-dasharray="6"/>
<text x="645" y="58" font-size="9" fill="#c00">权重≈61GB</text>
<text x="200" y="150" font-size="9" fill="#0550ae">KV(B=1)</text>
<text x="400" y="100" font-size="9" fill="#57606a">S=32K: KV≈3GB</text>
<rect x="480" y="95" width="140" height="55" fill="#e8f0fe" stroke="#003366"/>
<text x="550" y="115" text-anchor="middle" font-size="9">B=8, S=32K</text>
<text x="550" y="130" text-anchor="middle" font-size="9">KV≈24GB</text>
<text x="550" y="145" text-anchor="middle" font-size="9">+权≈61GB=85GB</text>
</svg>
<p class="fig-cap">图 P2-1：KV = 2LHDSBM；MoE 场景 State-bound 来自权重+并发 KV 共存</p>
</div>
<p class="footnote">* Prefix Cache 仅减少<strong>重复前缀</strong>的复算与存储共享，不减少每会话 unique 轨迹 KV 增长（见 P3 脚注）。</p>

<div class="concl"><strong>B4 本页已证（I1）：</strong>Serving 下 unique KV 随 Agent 轮次增，HBM State-bound；公式 2LHDSBM 可审计。</div>
<div class="trans"><strong>B5 过渡：</strong>State-bound 后产业在系统层如何应对？是否所有场景都叠加通信瓶颈？→ <strong>P3</strong></div>
</section>

<section id="p3" class="page">
<div class="step"><span class="done">P2</span><span class="on">P3</span><span>P4</span><span>P5</span><span>P6</span></div>
<h1 class="ptitle">P3 看业界：拓扑双路径的系统响应 <span class="insight">→ I2</span></h1>
<div class="carry"><strong>承接 P2：</strong>已证 State-bound。遗留：L1 系统如何按部署拓扑响应？</div>
<div class="page-q">B1 瓶颈落在单节点池内，还是必须跨节点？各拓扑下产业怎么做？</div>
<div class="claim">B2 待证命题：本页将证明——产业 L1 按 Scale Up / Scale Out 二分管理 State；Comm 仅在路径 B（MoE EP / 跨节点 KV）出现。</div>

<div class="scr"><div class="scr-h">片0 · 分析框架：拓扑决策</div><div class="scr-b">
<div class="view">【观点】路径 A（Scale Up）= 单节点 HBM/池内 OOM；路径 B（Scale Out）= MoE EP 跨卡 或 KV 超单卡需池化。</div>
<div class="so">【所以】Agent 长上下文 alone 通常先走路径 A；Qwen3-30B-A3B MoE 部署同时触发路径 B。</div>
</div></div>

<div class="scr"><div class="scr-h">片1 · 路径 A — Scale Up</div><div class="scr-b">
<div class="view">【观点】单节点 KV 超 HBM → L1 扩展内存层次（分页、卸载、池内管理）。</div>
<div class="evi">【证据】Dynamo KVBM：HBM→CPU→SSD→网络四层；MindIE KV 分页与 Continuous Batching。<span class="evidence"><a href="https://docs.dynamo.nvidia.com/dynamo/design-docs/overall-architecture">Dynamo Docs</a></span></div>
<div class="so">【所以】L1 解决<strong>存放与调度</strong>，不减少单会话 unique KV 随轮次增长。</div>
</div></div>

<div class="scr"><div class="scr-h">片2 · 路径 B — Scale Out + Comm</div><div class="scr-b">
<div class="view">【观点】MoE EP 跨节点时，计算:通信可接近 <strong>1:1</strong>；路由扇出 ≤4 节点/token 为架构响应。</div>
<div class="evi">【证据】DeepSeek-V3：跨节点 EP 计算通信比 ≈1:1（未重叠）；NVLink 160GB/s vs IB 50GB/s。<span class="evidence"><a href="https://arxiv.org/abs/2412.19437">DeepSeek-V3</a></span> 灵衢 CloudMatrix <strong>384 卡</strong>超节点 KV 池化。<span class="evidence"><a href="https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech">华为 HC 2025</a></span></div>
<div class="so">【所以】路径 B 叠加 <strong>Communication</strong> 瓶颈；路由扇出属拓扑/架构层，非 P4 竞争列。</div>
</div></div>

<div class="scr"><div class="scr-h">片3 · 汇聚：L1 共同边界</div><div class="scr-b">
<div class="view">【观点】无论 A/B，L1 优化重心已从算力扩展迁移至 State Management → Communication Optimization。</div>
<table><tr><th>层级</th><th>路径 A</th><th>路径 B</th></tr>
<tr><td>L1 动作</td><td>分页、卸载、批调度</td><td>KV 池化 + EP 集合通信</td></tr>
<tr><td>代表</td><td>MindIE / Dynamo KVBM</td><td>灵衢 384卡 / HCCL EP</td></tr>
<tr><td>边界</td><td colspan="2"><strong>不减少</strong> unique KV 绝对增长量；不减 dispatch 载荷字节</td></tr></table>
<div class="so">【所以】产出 <span class="insight">I2</span>：L1 按拓扑管 State；路径 B 须 <strong>压流量</strong>。</div>
</div></div>

<div class="fig">
<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="12" font-weight="bold" fill="#003366">P3 拓扑双路径（同维分解）</text>
<rect x="20" y="40" width="300" height="70" fill="#e8f0fe" stroke="#003366"/>
<text x="170" y="62" text-anchor="middle" font-size="11" font-weight="bold">路径 A · Scale Up</text>
<text x="170" y="80" text-anchor="middle" font-size="9">MindIE 分页 · Dynamo KVBM</text>
<text x="170" y="95" text-anchor="middle" font-size="9">单节点 HBM 不够 → 扩展内存层次</text>
<rect x="380" y="40" width="300" height="70" fill="#e8f0fe" stroke="#003366"/>
<text x="530" y="62" text-anchor="middle" font-size="11" font-weight="bold">路径 B · Scale Out</text>
<text x="530" y="80" text-anchor="middle" font-size="9">灵衢 384卡 · MoE EP · HCCL</text>
<text x="530" y="95" text-anchor="middle" font-size="9">跨节点 KV + dispatch → Comm 1:1</text>
<rect x="120" y="130" width="460" height="55" fill="#f7f9fc" stroke="#d0d7de"/>
<text x="350" y="152" text-anchor="middle" font-size="10">L1 共同边界：管理资源，不减 unique 状态绝对量</text>
<text x="350" y="170" text-anchor="middle" font-size="9" fill="#57606a">在 L1 之上仍有 L2 减量空间 → P4</text>
</svg>
<p class="fig-cap">图 P3-1：Scale Up / Scale Out 汇聚；Comm 仅路径 B</p>
</div>

<div class="concl"><strong>B4 本页已证（I2）：</strong>产业 L1 按拓扑管理 State/Comm；L1 不减 unique KV 与 dispatch 绝对量。</div>
<div class="trans"><strong>B5 过渡：</strong>L2 算法层在各减量作用点上谁领先、工程化空白在哪？→ <strong>P4</strong></div>
</section>

<section id="p4" class="page">
<div class="step"><span class="done">P2</span><span class="done">P3</span><span class="on">P4</span><span>P5</span><span>P6</span></div>
<h1 class="ptitle">P4 看竞争：瓶颈域 × 公式因子 <span class="insight">→ I3</span></h1>
<div class="carry"><strong>承接 P3：</strong>L1 管资源不减量。遗留：L2 竞争格局与工程化缺口？</div>
<div class="page-q">B1 域 × 作用点矩阵如何填？集合层策略演进至哪一代？</div>
<div class="claim">B2 待证命题：本页将证明——State 行按 ΔM/ΔS_keep/ΔS_gen 三因子竞争；Comm 行（路径 B 前提）仅链路效率与载荷压缩两列；昇腾栈存在工程化缺口。</div>

<div class="scr"><div class="scr-h">片1 · State 行：KV 公式因子</div><div class="scr-b">
<table><tr><th>列（因子）</th><th>减符号</th><th>代表</th><th>关键数据</th><th>竞争强度</th></tr>
<tr><td><strong>ΔM</strong></td><td>M↓</td><td>KIVI, TurboQuant, FP8 KV</td><td>TurboQuant 6×+ 压缩</td><td>红海</td></tr>
<tr><td><strong>ΔS_keep</strong></td><td>S↓留存</td><td>H2O→SnapKV, PyramidKV</td><td>SnapKV <strong>3.6×</strong>加速、<strong>8.2×</strong>内存</td><td>红海</td></tr>
<tr><td><strong>ΔS_gen</strong></td><td>S↓生成</td><td>LazyLLM</td><td>Prefill <strong>2.34×</strong></td><td>成熟</td></tr></table>
<p class="evidence">SnapKV: <a href="https://arxiv.org/abs/2404.14469">arXiv:2404.14469</a> · LazyLLM: <a href="https://arxiv.org/abs/2407.14057">arXiv:2407.14057</a> · TurboQuant: <a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">Google Research</a></p>
<div class="so">【所以】统计/窗口策略（SnapKV）已红海；<strong>工作流/语义策略</strong>（IntentKV peak ↓77.8%）为 N 切口。</div>
</div></div>

<div class="scr"><div class="scr-h">片2 · ΔS_keep 附条：语义策略演进</div><div class="scr-b">
<table><tr><th>代际</th><th>决定什么</th><th>代表</th><th>昇腾栈状态</th></tr>
<tr><td>统计/窗口</td><td>注意力重要性</td><td>SnapKV, H2O</td><td>论文多、L1 未统一集成</td></tr>
<tr><td><strong>工作流/语义</strong></td><td>Agent 阶段/tool 边界</td><td>IntentKV, KVFlow 2.19×</td><td><strong>工程化缺口（N）</strong></td></tr></table>
<div class="so">【所以】非「学术空白」，而是 <strong>栈内/工程化不足</strong>。</div>
</div></div>

<div class="scr"><div class="scr-h">片3 · Comm 行（前提：P3 路径 B）— 仅 2 列</div><div class="scr-b">
<table><tr><th>列</th><th>减什么</th><th>代表</th><th>数据</th></tr>
<tr><td><strong>链路效率</strong></td><td>相同字节传更快</td><td>DeepEP, DualPipe</td><td>DeepEP FP8 ~50% 带宽</td></tr>
<tr><td><strong>载荷压缩</strong></td><td>dispatch 字节更少</td><td>MegaScale-MoE</td><td>FP8 all-to-all 压缩</td></tr></table>
<p class="evidence">DeepEP: <a href="https://github.com/deepseek-ai/DeepEP">GitHub</a> · MegaScale-MoE: <a href="https://arxiv.org/abs/2505.11432">arXiv:2505.11432</a></p>
<div class="so">【所以】DeepEP（传更快）与 N+1（传更少）<strong>正交互补</strong>；载荷压缩在 HCCL 路径 <strong>工程化不足</strong>。</div>
</div></div>

<div class="fig">
<svg viewBox="0 0 720 260" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="12" font-weight="bold" fill="#003366">P4 竞争矩阵 · KV = 2LHDSBM</text>
<text x="30" y="50" font-size="10" fill="#57606a">行/列</text>
<text x="150" y="50" text-anchor="middle" font-size="10" font-weight="bold">ΔM</text>
<text x="280" y="50" text-anchor="middle" font-size="10" font-weight="bold">ΔS_keep</text>
<text x="420" y="50" text-anchor="middle" font-size="10" font-weight="bold">ΔS_gen</text>
<text x="560" y="50" text-anchor="middle" font-size="10" font-weight="bold">Comm·效率</text>
<text x="680" y="50" text-anchor="middle" font-size="10" font-weight="bold">Comm·载荷</text>
<rect x="30" y="60" width="80" height="50" fill="#003366"/><text x="70" y="90" text-anchor="middle" font-size="9" fill="#fff">State</text>
<rect x="120" y="60" width="100" height="50" fill="#f7f9fc" stroke="#d0d7de"/><text x="170" y="88" text-anchor="middle" font-size="8">KIVI/TQ</text>
<rect x="230" y="60" width="120" height="50" fill="#e8f0fe" stroke="#003366"/><text x="290" y="82" text-anchor="middle" font-size="8">SnapKV</text><text x="290" y="96" text-anchor="middle" font-size="8" fill="#c00">+语义 N</text>
<rect x="360" y="60" width="120" height="50" fill="#f7f9fc" stroke="#d0d7de"/><text x="420" y="88" text-anchor="middle" font-size="8">LazyLLM</text>
<rect x="490" y="60" width="100" height="50" fill="#f0f0f0" stroke="#ccc"/><text x="540" y="88" text-anchor="middle" font-size="8" fill="#999">N/A</text>
<rect x="600" y="60" width="100" height="50" fill="#f0f0f0" stroke="#ccc"/><text x="650" y="88" text-anchor="middle" font-size="8" fill="#999">N/A</text>
<rect x="30" y="120" width="80" height="50" fill="#003366"/><text x="70" y="142" text-anchor="middle" font-size="8" fill="#fff">Comm</text><text x="70" y="155" text-anchor="middle" font-size="7" fill="#ddf4ff">路径B</text>
<rect x="120" y="120" width="360" height="50" fill="#f0f0f0" stroke="#ccc"/><text x="300" y="150" text-anchor="middle" font-size="8" fill="#999">State 因子不适用</text>
<rect x="490" y="120" width="100" height="50" fill="#f7f9fc" stroke="#d0d7de"/><text x="540" y="148" text-anchor="middle" font-size="8">DeepEP</text>
<rect x="600" y="120" width="100" height="50" fill="#e8f0fe" stroke="#003366"/><text x="650" y="142" text-anchor="middle" font-size="8">MegaScale</text><text x="650" y="156" text-anchor="middle" font-size="8" fill="#c00">N+1</text>
<rect x="120" y="185" width="480" height="60" fill="#fff8e6" stroke="#9a6700"/>
<text x="360" y="205" text-anchor="middle" font-size="9">ΔS_keep 语义策略附条：统计策略(红海) → 工作流语义(工程化缺口)</text>
<text x="360" y="225" text-anchor="middle" font-size="9">IntentKV / KVFlow 为 SOTA 参照，非终点</text>
</svg>
<p class="fig-cap">图 P4-1：State 三因子 + Comm 两列（路由扇出已在 P3 路径 B）</p>
</div>

<div class="concl"><strong>B4 本页已证（I3）：</strong>L2 在 ΔM/ΔS_keep/ΔS_gen 有竞品；语义策略与 Comm 载荷压缩在昇腾栈工程化不足。</div>
<div class="trans"><strong>B5 过渡：</strong>MindIE/灵衢 已做 L1，团队应加码 L1 还是 L2？→ <strong>P5</strong></div>
</section>

<section id="p5" class="page">
<div class="step"><span class="done">P2</span><span class="done">P3</span><span class="done">P4</span><span class="on">P5</span><span>P6</span></div>
<h1 class="ptitle">P5 看机会：L2 减量叠加 L1 <span class="insight">→ I4</span></h1>
<div class="carry"><strong>承接 P4：</strong>工程化缺口已识别。遗留：投资 L1 调优还是 L2 减量？</div>
<div class="page-q">B1 调优天花板 vs 减量价值？为何仍要做 L2？</div>
<div class="claim">B2 待证命题：本页将证明——L2 插件式减量与 MindIE/灵衢/HCCL 正交叠加；根技术（量化/稀疏/蒸馏）可从参数时代延伸到 State/Comm。</div>

<div class="scr"><div class="scr-h">片1 · L1 调优天花板</div><div class="scr-b">
<div class="view">【观点】PagedAttention 将碎片从 60–80% 降至 &lt;4%，但上下文仍随 S 线性增长；DeepEP 传更快但不减字节。</div>
<div class="so">【所以】调优有顶；须从源头减 <strong>S</strong> 与 <strong>M</strong>、减 dispatch 载荷。</div>
</div></div>

<div class="scr"><div class="scr-h">片2 · L2 与 L1 正交叠加</div><div class="scr-b">
<div class="view">【观点】算法团队做 L2 插件；MindIE/灵衢 做 L1 平台——<strong>集成而非替代</strong>。</div>
<table><tr><th>层级</th><th>职责</th><th>本团队</th></tr>
<tr><td>L1</td><td>分页、调度、EP、池化</td><td><strong>复用</strong></td></tr>
<tr><td>L2</td><td>语义稀疏、dispatch 压缩、CANN kernel</td><td><strong>建设</strong></td></tr>
<tr><td>L3</td><td>自研 Runtime、替代 HCCL</td><td><strong>不做</strong></td></tr></table>
<div class="so">【所以】产出 <span class="insight">I4</span>：课题形态 = L2 插件挂载。</div>
</div></div>

<div class="fig">
<svg viewBox="0 0 640 180" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="12" font-weight="bold" fill="#003366">L1 底座 + L2 插件叠加</text>
<rect x="40" y="40" width="560" height="50" fill="#e8f0fe" stroke="#003366"/>
<text x="320" y="62" text-anchor="middle" font-size="11">L1：MindIE · 灵衢 · HCCL · vLLM-Ascend</text>
<text x="320" y="78" text-anchor="middle" font-size="9">分页 · 调度 · KV 池化 · EP 集合通信</text>
<rect x="80" y="105" width="200" height="55" fill="#003366"/><text x="180" y="128" text-anchor="middle" font-size="10" fill="#fff">N · 语义 KV 插件</text><text x="180" y="145" text-anchor="middle" font-size="8" fill="#ddf4ff">ΔS_keep + ΔM</text>
<rect x="360" y="105" width="200" height="55" fill="#003366"/><text x="460" y="128" text-anchor="middle" font-size="10" fill="#fff">N+1 · dispatch 压缩</text><text x="460" y="145" text-anchor="middle" font-size="8" fill="#ddf4ff">HCCL 前载荷压缩</text>
</svg>
<p class="fig-cap">图 P5-1：叠加不造轮子</p>
</div>

<div class="concl"><strong>B4 本页已证（I4）：</strong>L2 减量与 L1 正交；应在已有栈上插件交付。根技术矩阵详见 P6.2。</div>
<div class="trans"><strong>B5 过渡：</strong>如何从四看归纳 N/N+1 及昇腾集成边界？→ <strong>P6</strong></div>
</section>

<section id="p6" class="page">
<div class="step"><span class="done">洞察</span><span class="on">P6 总结</span><span>课题</span></div>
<h1 class="ptitle">P6 战略总结：洞察 → 课题</h1>

<h2>6.1 洞察小结（I1–I4，无课题名）</h2>
<table><tr><th>编号</th><th>洞察</th><th>So What</th></tr>
<tr><td><span class="insight">I1</span></td><td>Agent Serving unique KV 增长 → State-bound</td><td>压状态（ΔS + ΔM）</td></tr>
<tr><td><span class="insight">I2</span></td><td>L1 拓扑响应；路径 B 叠加 Comm</td><td>压流量</td></tr>
<tr><td><span class="insight">I3</span></td><td>ΔS_keep 语义策略、Comm 载荷工程化不足</td><td>N / N+1 切口</td></tr>
<tr><td><span class="insight">I4</span></td><td>L2 叠加 L1，插件交付</td><td>集成边界</td></tr></table>

<h2>6.2 根技术地图</h2>
<table><tr><th>根技术</th><th>参数（已成熟）</th><th>状态 · 压状态</th><th>通信 · 压流量</th></tr>
<tr><td>低比特量化</td><td>GPTQ / AWQ</td><td>KIVI / TurboQuant → <strong>N·ΔM</strong></td><td>FP8 dispatch → <strong>N+1</strong></td></tr>
<tr><td>稀疏/剪枝</td><td>结构剪枝</td><td>SnapKV → <strong>N·ΔS_keep</strong></td><td>路由稀疏</td></tr>
<tr><td>蒸馏</td><td>Logits 蒸馏</td><td>KV 蒸馏（Phase 2）</td><td>Router 蒸馏（Phase 2）</td></tr></table>

<h2>6.3 规划策略</h2>
<table><tr><th>时间</th><th>对象</th><th>瓶颈</th><th>控制点</th></tr>
<tr><td>过去</td><td>压参数</td><td>装不下</td><td>参数量化（已成熟）</td></tr>
<tr><td><strong>现在</strong></td><td><strong>压状态</strong></td><td>存不下</td><td>N：语义稀疏 + KV 量化</td></tr>
<tr><td><strong>未来</strong></td><td><strong>压流量</strong></td><td>传不快</td><td>N+1：dispatch 压缩</td></tr></table>

<h2>6.4 课题确定（首次正式命名 N / N+1）</h2>
<p><strong>因为</strong> I1 证出 State-bound，I3 证出语义策略未入昇腾 L1，I4 证出应叠加 L2 而非重造 Runtime，<strong>所以</strong> 优先立项 <span class="topic">N</span>。<strong>因为</strong> I2 证出 MoE 路径 B 下 Comm 与计算同级，I3 证出载荷压缩工程化不足，<strong>所以</strong> 跟进 <span class="topic">N+1</span>（复用团队 MoE 经验）。</p>

<table><tr><th>课题</th><th>优先级</th><th>洞察</th><th>控制点</th><th>根技术</th><th>交付</th></tr>
<tr><td><strong>N</strong> 语义感知动态 KV 稀疏化</td><td><strong>N</strong></td><td>I1+I3+I4</td><td>压状态 ΔS+ΔM</td><td>稀疏+量化</td><td>MindIE KV 插件</td></tr>
<tr><td><strong>N+1</strong> MoE 通信量压缩</td><td>N+1</td><td>I2+I3+I4</td><td>压流量</td><td>量化+稀疏路由</td><td>HCCL 前压缩</td></tr></table>

<h3>不造轮子清单</h3>
<table><tr><th>能力</th><th>已有提供者</th><th>我们做法</th></tr>
<tr><td>KV 分页</td><td>MindIE / vLLM</td><td>挂载稀疏于 KV 写入路径</td></tr>
<tr><td>KV 跨卡池化</td><td>灵衢 / Dynamo</td><td>减量后降低池化压力</td></tr>
<tr><td>MoE EP</td><td>HCCL / DeepEP</td><td>HCCL 前压缩；不自研 EP 栈</td></tr>
<tr><td>Attention 稀疏</td><td>SnapKV 等</td><td>增量=Agent 语义 + 昇腾算子</td></tr></table>

<h3>昇腾集成边界</h3>
<table><tr><th>栈层</th><th>复用</th><th>建设（L2）</th><th>挂载点</th></tr>
<tr><td>MindIE</td><td>分页·调度</td><td>Agent 语义稀疏</td><td>KV 写入 / attention 回调</td></tr>
<tr><td>CANN</td><td>基础算子</td><td>稀疏 attention + 量化 KV</td><td>算子库插件</td></tr>
<tr><td>HCCL</td><td>EP 集合通信</td><td>dispatch 载荷压缩</td><td>AllToAll 前编码</td></tr>
<tr><td>灵衢</td><td>384 卡 KV 池化</td><td>更小 KV 降带宽</td><td>与 N 效果叠加</td></tr></table>

<div class="fig">
<svg viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="11" font-weight="bold" fill="#003366">L0→L5 层级</text>
<rect x="20" y="35" width="100" height="30" fill="#e8f0fe" stroke="#003366"/><text x="70" y="54" text-anchor="middle" font-size="8">L0 P2</text>
<rect x="130" y="35" width="100" height="30" fill="#e8f0fe" stroke="#003366"/><text x="180" y="54" text-anchor="middle" font-size="8">L1 P3</text>
<rect x="240" y="35" width="100" height="30" fill="#e8f0fe" stroke="#003366"/><text x="290" y="54" text-anchor="middle" font-size="8">L2 P4</text>
<rect x="350" y="35" width="100" height="30" fill="#e8f0fe" stroke="#003366"/><text x="400" y="54" text-anchor="middle" font-size="8">L3 P5</text>
<rect x="460" y="35" width="100" height="30" fill="#003366"/><text x="510" y="54" text-anchor="middle" font-size="8" fill="#fff">L4 P6</text>
<rect x="570" y="35" width="110" height="30" fill="#003366"/><text x="625" y="54" text-anchor="middle" font-size="8" fill="#fff">L5 P7/8</text>
</svg>
<p class="fig-cap">图 P6-1：分析层级闭合</p>
</div>

<div class="concl"><strong>本页已证：</strong>I1–I4 → N/N+1；N 优先（Agent 普适）；N+1 复用 MoE 经验。</div>
<div class="trans">→ <strong>P7</strong>（N 技术闭环）/ <strong>P8</strong>（N+1 技术闭环）</div>
</section>

<section id="p7" class="page">
<div class="step"><span class="done">洞察</span><span class="done">总结</span><span class="on">课题 N</span></div>
<h1 class="ptitle">P7 课题 N：语义感知动态 KV 稀疏化</h1>
<div class="carry"><strong>洞察回溯：</strong>本课题由 <span class="insight">I1</span> + <span class="insight">I3</span> + <span class="insight">I4</span> 推导 → 控制点：<strong>压状态</strong>（ΔS_keep → ΔM）</div>

<div class="scr"><div class="scr-h">挑战</div><div class="scr-b">
<ul><li><strong>跨 turn 累积 KV</strong>：Agent 多轮 tool 调用使 S 持续增长，长会话 OOM</li>
<li><strong>统计稀疏不够</strong>：SnapKV 在任务切换时可能误删关键状态</li>
<li><strong>框架缺口</strong>：MindIE 无工作流语义稀疏策略模块</li>
<li><strong>质量约束</strong>：须 Agent 轨迹级评测，非单榜 MMLU</li></ul>
</div></div>

<div class="scr"><div class="scr-h">技术流水线（公式因子顺序）</div><div class="scr-b">
<p><strong>语义策略(定 S 子集) → ΔS_keep 稀疏 → ΔM 量化 → MindIE KV 写入插件</strong></p>
<table><tr><th>阶段</th><th>公式因子</th><th>参照 SOTA</th></tr>
<tr><td>语义输入</td><td>决定有效 S 子集</td><td>IntentKV peak ↓77.8%</td></tr>
<tr><td>集合稀疏</td><td>ΔS_keep</td><td>SnapKV 3.6×/8.2×</td></tr>
<tr><td>表示量化</td><td>ΔM</td><td>LazyLLM 2.34×（ΔS_gen 可选）</td></tr></table>
<p class="evidence">目标：<strong>对齐论文公开 SOTA</strong>为参照；增量在 Agent 轨迹评测 + 昇腾 CANN 集成。不承诺无出处 TTFT/并发百分比。</p>
</div></div>

<div class="fig">
<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="12" font-weight="bold" fill="#003366">P7 插件挂载 · MindIE / CANN</text>
<rect x="20" y="45" width="110" height="44" fill="#f7f9fc" stroke="#d0d7de"/><text x="75" y="72" text-anchor="middle" font-size="9">Agent 调度器</text>
<rect x="150" y="40" width="120" height="54" fill="#e8f0fe" stroke="#003366"/><text x="210" y="62" text-anchor="middle" font-size="9" font-weight="bold">语义策略模块</text><text x="210" y="78" text-anchor="middle" font-size="8">tool/阶段边界</text>
<rect x="290" y="45" width="100" height="44" fill="#fff" stroke="#0550ae"/><text x="340" y="72" text-anchor="middle" font-size="9">ΔS_keep</text>
<rect x="410" y="45" width="100" height="44" fill="#fff" stroke="#0550ae"/><text x="460" y="72" text-anchor="middle" font-size="9">ΔM 量化</text>
<rect x="530" y="35" width="170" height="64" fill="#003366"/><text x="615" y="58" text-anchor="middle" font-size="9" fill="#fff">MindIE KV 插件</text><text x="615" y="74" text-anchor="middle" font-size="8" fill="#ddf4ff">写入/attention 回调</text>
<rect x="150" y="110" width="200" height="40" fill="#f7f9fc" stroke="#d0d7de"/><text x="250" y="135" text-anchor="middle" font-size="9">CANN：稀疏 attention kernel</text>
<rect x="370" y="110" width="200" height="40" fill="#f7f9fc" stroke="#d0d7de"/><text x="470" y="135" text-anchor="middle" font-size="9">任务成功率反馈闭环</text>
</svg>
<p class="fig-cap">图 P7-1：N 课题技术闭环与挂载点</p>
</div>

<div class="concl"><strong>本页结论：</strong>N 以稀疏+量化在 MindIE 上插件交付，解决 Agent「存不下」，对齐 SnapKV/IntentKV SOTA 并做昇腾工程化。</div>
</section>

<section id="p8" class="page">
<div class="step"><span class="done">洞察</span><span class="done">总结</span><span class="on">课题 N+1</span></div>
<h1 class="ptitle">P8 课题 N+1：MoE 通信量压缩</h1>
<div class="carry"><strong>洞察回溯：</strong>本课题由 <span class="insight">I2</span> + <span class="insight">I3</span> + <span class="insight">I4</span> 推导 → 控制点：<strong>压流量</strong></div>

<div class="scr"><div class="scr-h">挑战</div><div class="scr-b">
<ul><li><strong>通信墙</strong>：DeepSeek-V3 EP 计算:通信 ≈1:1</li>
<li><strong>DeepEP 不减量</strong>：优化链路效率，dispatch 字节仍随 expert 数增长</li>
<li><strong>路由稳定性</strong>：top-k 对 FP8/INT4 压缩误差敏感（团队 MoE 经验）</li>
<li><strong>集成约束</strong>：压缩在 HCCL 发起前，<strong>不替代 HCCL</strong></li></ul>
</div></div>

<div class="scr"><div class="scr-h">技术路径</div><div class="scr-b">
<table><tr><th>技术</th><th>机制</th><th>根技术</th><th>参照</th></tr>
<tr><td>FP8/INT4 dispatch</td><td>载荷减半+</td><td>量化</td><td>DeepEP ~50% 带宽；MegaScale-MoE</td></tr>
<tr><td>冗余 token 合并</td><td>减重复 dispatch</td><td>稀疏</td><td>MegaScale-MoE</td></tr>
<tr><td>路由稳定补偿</td><td>EPHandle 缓存、误差监控</td><td>量化+蒸馏</td><td>团队 MoE 路由经验</td></tr></table>
<p><strong>与 DeepEP 关系：</strong>传更快（DeepEP）+ 传更少（N+1）正交，可叠加。</p>
</div></div>

<div class="fig">
<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="12" font-weight="bold" fill="#003366">P8 HCCL 前压缩挂载</text>
<rect x="20" y="50" width="90" height="40" fill="#f7f9fc" stroke="#d0d7de"/><text x="65" y="75" text-anchor="middle" font-size="9">MoE Router</text>
<rect x="130" y="42" width="130" height="56" fill="#e8f0fe" stroke="#003366"/><text x="195" y="65" text-anchor="middle" font-size="9" font-weight="bold">载荷压缩模块</text><text x="195" y="82" text-anchor="middle" font-size="8">FP8 · 冗余削减</text>
<rect x="280" y="50" width="100" height="40" fill="#003366"/><text x="330" y="75" text-anchor="middle" font-size="9" fill="#fff">HCCL AllToAll</text>
<rect x="400" y="50" width="100" height="40" fill="#f7f9fc" stroke="#d0d7de"/><text x="450" y="75" text-anchor="middle" font-size="9">Expert 计算</text>
<rect x="520" y="50" width="100" height="40" fill="#003366"/><text x="570" y="75" text-anchor="middle" font-size="9" fill="#fff">HCCL Combine</text>
<rect x="130" y="115" width="200" height="45" fill="#fff8e6" stroke="#9a6700"/><text x="230" y="135" text-anchor="middle" font-size="9">DeepEP：链路效率（互补）</text>
<rect x="350" y="115" width="270" height="45" fill="#e8f0fe" stroke="#003366"/><text x="485" y="135" text-anchor="middle" font-size="9" font-weight="bold">N+1：字节数削减（本课题）</text>
</svg>
<p class="fig-cap">图 P8-1：HCCL 前压缩，不替代 EP 栈</p>
</div>

<div class="concl"><strong>本页结论：</strong>N+1 在 HCCL 前做 dispatch 压缩，复用团队 MoE 经验，与 DeepEP 互补。</div>
</section>

<section id="appendix" class="page">
<h1 class="ptitle">附录</h1>
<h2>A. 论断-来源索引</h2>
<table><tr><th>论断</th><th>数据</th><th>来源</th></tr>
<tr><td>Qwen3-30B-A3B 结构</td><td>L=48,H=4,D=128,61GB</td><td><a href="https://huggingface.co/Qwen/Qwen3-30B-A3B">HF</a></td></tr>
<tr><td>KV 公式系数</td><td>98304 B/token</td><td>2×48×4×128×2</td></tr>
<tr><td>SnapKV</td><td>3.6×/8.2×</td><td><a href="https://arxiv.org/abs/2404.14469">arXiv:2404.14469</a></td></tr>
<tr><td>LazyLLM</td><td>2.34×</td><td><a href="https://arxiv.org/abs/2407.14057">arXiv:2407.14057</a></td></tr>
<tr><td>IntentKV</td><td>peak ↓77.8%</td><td><a href="https://arxiv.org/html/2606.09916">arXiv</a></td></tr>
<tr><td>DeepSeek EP</td><td>计算:通信≈1:1</td><td><a href="https://arxiv.org/abs/2412.19437">arXiv:2412.19437</a></td></tr>
<tr><td>DeepEP</td><td>FP8 ~50% 带宽</td><td><a href="https://github.com/deepseek-ai/DeepEP">GitHub</a></td></tr>
<tr><td>灵衢</td><td>384 卡超节点</td><td><a href="https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech">华为 HC 2025</a></td></tr>
<tr><td>vLLM 显存</td><td>90–92%</td><td><a href="https://arxiv.org/abs/2309.06180">PagedAttention</a></td></tr>
<tr><td>Gemini 上下文</td><td>2M token</td><td><a href="https://developers.googleblog.com/en/gemini-15-pro-2m-context/">Google Blog</a></td></tr>
</table>

<h2>B. 页间推导索引</h2>
<table><tr><th>从</th><th>已证</th><th>遗留问题</th><th>到</th></tr>
<tr><td>P1</td><td>主线与算例锚点</td><td>首要约束是否仍为算力？</td><td>P2</td></tr>
<tr><td>P2</td><td>I1 State-bound</td><td>L1 如何响应？</td><td>P3</td></tr>
<tr><td>P3</td><td>I2 拓扑+Comm</td><td>L2 竞争与缺口？</td><td>P4</td></tr>
<tr><td>P4</td><td>I3 工程化缺口</td><td>投资 L1 还是 L2？</td><td>P5</td></tr>
<tr><td>P5</td><td>I4 插件叠加</td><td>定课题与边界</td><td>P6</td></tr>
<tr><td>P6</td><td>N/N+1</td><td>技术闭环</td><td>P7/P8</td></tr></table>

<h2>C. 核心参考文献</h2>
<ul style="font-size:.88rem">
<li>SnapKV — <a href="https://arxiv.org/abs/2404.14469">arXiv:2404.14469</a></li>
<li>LazyLLM — <a href="https://arxiv.org/abs/2407.14057">arXiv:2407.14057</a></li>
<li>IntentKV — <a href="https://arxiv.org/html/2606.09916">arXiv:2606.09916</a></li>
<li>KVFlow — <a href="https://arxiv.org/abs/2507.07400">arXiv:2507.07400</a></li>
<li>DeepSeek-V3 — <a href="https://arxiv.org/abs/2412.19437">arXiv:2412.19437</a></li>
<li>DeepEP — <a href="https://github.com/deepseek-ai/DeepEP">GitHub</a></li>
<li>MegaScale-MoE — <a href="https://arxiv.org/abs/2505.11432">arXiv:2505.11432</a></li>
<li>NVIDIA Dynamo — <a href="https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/">Blog</a></li>
<li>KV Cache Survey — <a href="https://arxiv.org/abs/2412.19442">arXiv:2412.19442</a></li>
</ul>
</section>

</main>
</body>
</html>
