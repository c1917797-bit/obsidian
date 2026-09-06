# KVCache 压缩技术洞察报告

> **报告日期**: 2026-06-28
> **层级定位**: 基础全景层（KV 压缩技术地图）—— 是 [`关系推理压缩技术洞察报告.md`](关系推理压缩技术洞察报告.md) 与 [`多卡推理压缩技术规划报告.md`](多卡推理压缩技术规划报告.md) 的父层
> **数据来源**: 知识库 `inference_compression_strict.json`（2757篇）+ 外部 arXiv 实时检索（2024-2026，2026-06-28 核实 MLA / R-KV / ThinKV / ShotKV 等）
> **目标读者**: 架构委员会 / 技术委员会
> **核心命题**: KV Cache 已成为推理优化的第一战场；KV 压缩正从"压存储"的单一目标，演进为"**压缩存储 × 减少计算 × 提升复用**"的全生命周期工程，压缩粒度从"全局一刀切"走向"head/layer/task/thought 维度的结构化自适应"。

---

## P0 封面

**标题**：KVCache 压缩技术洞察报告
**副标题**：推理优化的第一战场：从"压存储"到"全生命周期 × 结构化自适应"
**汇报对象**：架构委员会 / 技术委员会
**日期**：2026年6月

---

## P1 执行摘要：结论先行

### 核心观点

KV Cache 是现代 LLM 推理的**核心瓶颈**——它同时挤占显存（HBM）、带宽、并限制吞吐、并发与长上下文能力。在推理模型（reasoning model，生成 8-14× 更长）、长上下文（>128K）、高并发、Agent 多轮四大浪潮叠加下，KV 已从"辅助缓存"变为"主导显存的变量成本"。

围绕这一变化，KV 压缩的主战场已经从"**压存储**"转向两条更高维的路线：
- **全生命周期**：Prefill 源头减量 → Decode 动态压缩 → 跨请求复用，三段闭环
- **结构化自适应**：按 head / layer / task / thought 维度差异化压缩，突破"全局一刀切"上限

### 两大战略控制点

- **控制点一：全生命周期 KV 管理（Lifecycle KV Management）**
  - 解决问题：单段压缩收益递减；跨请求复用打破压缩上限
  - 技术抓手：Prefill 选择性计算、Decode 动态压缩、跨请求前缀/语义复用
- **控制点二：结构化自适应压缩（Structured Adaptive Compression）**
  - 解决问题：全局统一 bit/比例的帕累托上限
  - 技术抓手：head-level/layer-level 预算分配、task/thought 感知、混合精度

### 两项核心课题

- **N：Head-Layer 自适应 KV 混合精度压缩**（量化的结构化自适应）
- **N+1：全生命周期 KV 管理 Runtime**（Prefill→Decode→Reuse 闭环）

### 一句话结论

> **KV 压缩竞争的本质：不是谁压得更狠，而是谁能在"全生命周期"与"结构化自适应"两个维度上把压缩、计算、复用协同到帕累托前沿。**

### 推导逻辑

```
五看洞察（趋势/业界/竞争/技术/机会）
        ↓
两大战略控制点（全生命周期 + 结构化自适应）
        ↓
N / N+1 课题落地
        ↓
核心指标：显存占用 ↓、吞吐 ↑、并发 ↑、长上下文能力 ↑、精度损失 ≤1%
```

### 执行结论（数字佐证）

| 证据 | 现象 | 含义 |
|------|------|------|
| **MLA（DeepSeek-V2，arXiv:2405.04434）**：架构级压缩 KV **减少 93.3%**、吞吐 5.76× | 把 KV 压进隐向量 | 架构级压缩是天花板最高的路线 |
| **R-KV（2505.24133）**：reasoning model 上 10% KV 保 100%、6.6× 吞吐 | 统计压缩失效，关系/冗余信号压倒统计 | reasoning 浪潮倒逼压缩信号升级 |
| **ThinKV（2510.01290，ICLR Oral）**：<5% KV 近无损、5.8× 吞吐 | thought 维度差异化压缩 | 结构化自适应已工业级可行 |
| **Retrieval Head（2404.15574）**：<5% head 贡献主要信息 | 绝大多数 head 可压 | head-level 差异化是物理基础 |
| **vLLM PagedAttention**：预留 90% HBM 给 KV 管理 | 产业已为 KV 重构内存 | KV 是系统设计的中心 |

---

## P2 看趋势：KV 已成推理核心瓶颈，压缩目标从"存储"走向"全生命周期"

### 核心观点

在**推理模型、长上下文（>128K）、高并发、Agent 多轮**四大浪潮叠加下，KV Cache 已成为推理系统的核心约束。压缩目标正从单一的"压存储"，演进为"压缩存储 × 减少计算 × 提升复用"的全生命周期工程。

---

### 前置定义：KV Cache 为何是瓶颈？

KV Cache 是 Transformer 自回归解码时，为避免重复计算而缓存的每层 Key/Value。其大小（字节数）：

```
Size_KV = 2 × L × n_h × d_h × T × B × Precision
          层数  头数  头维  序列长  批大小  精度
```

- **模型权重**：固定成本（不随 T、B 变化）
- **KV Cache**：**可变成本**（随 T×B 线性增长）

> **关键推论**：上下文越长、并发越高、生成越长（reasoning），KV 必然超过权重并先占满 HBM。**解码阶段是内存带宽受限的**——KV 既占显存又占带宽，双重约束。

---

### 论据链：理论 → 实测 → 共识（三层硬证据）

#### 第一层：理论——KV 线性扩张，权重固定（公式推导）

**KV Cache 大小公式推导**：

```
Size_KV = 2 × L × n_kv × d_h × T × B × P
          ↑   ↑    ↑     ↑    ↑   ↑   ↑
         K&V 层数 KV头数 头维 序列 批大小 精度字节
```
- `2`：Key 与 Value 各一份
- `L × n_kv × d_h`：每层每 KV head 的维度（GQA 模型用 n_kv 而非全部 head）
- `T × B`：随序列长度与并发**线性增长**（可变成本）
- `P`：精度（FP16=2，INT8=1，INT4=0.5 字节）

**数值验证（Llama-3-70B，INT8）**：L=80 层，n_kv=8（GQA），d_h=128，P=1 字节
```
每 Token KV = 2 × 80 × 8 × 128 × 1 = 163,840 B ≈ 160 KB  ✓（与上表一致）
128K 单会话: 160KB × 128K = 20.5 GB
32K × 32 并发: 160KB × 32K × 32 = 167 GB > 单卡 H100(80GB)
```
> **机理结论**：权重是 `L × n_total × d` 的固定成本；KV 是 `T×B` 的可变成本。**只要 T×B 足够大，KV 必然超过权重**——这是数学必然，非经验现象。

- 推理模型（R1 类）生成 **8-14×** 更长的输出（R-KV §2.1 实测），T 急剧膨胀
- 长上下文 128K-1M 使 T 上限数倍提升
- 高并发 B 使 KV 同比放大
- 三者相乘 → KV 在生产负载下远超权重（详见多卡报告 P2 的 DeepSeek-V3 实测：128K/64 并发下 KV 是权重的 4 倍）

**为何解码阶段是"带宽受限"（算术强度论证）**：
```
解码每步：读全部 KV → 算 1 个 token 的 attention
算术强度 = FLOPs / 字节 ≈ (2×d) / (2×T×d) = 1/T
T=128K 时，算术强度 ≈ 8e-6 → 远低于 GPU 平凡点(~100)
→ 解码是内存带宽受限，KV 既占显存又吃带宽，双重瓶颈
```

**Llama-3-70B（Dense，INT8，每 Token KV ≈ 160KB）规模演算**：

| 场景 | 上下文(T) | 并发(B) | KV Cache | 对比权重(140GB) | 结论 |
|------|-----------|---------|----------|----------------|------|
| 单会话，128K | 128K | 1 | 20.5 GB | 14.6% | 可控 |
| 8K，Batch=32 | 8K | 32 | 41.9 GB | 30% | 占 H100 一半 |
| 32K，Batch=32 | 32K | 32 | 167 GB | 119% | **超单卡 H100** |
| reasoning，长生成 | 128K×8× | 16 | ≫权重 | — | KV 主导 |

> **推论**：即便无 reasoning，32K/32 并发已超单卡。叠加 reasoning 的 8-14× 长生成，KV 在解码阶段必然主导显存——这是"解码阶段内存带宽受限"的量化根因。

#### 第二层：工业实测——压缩路线的天花板与突破

| 路线 | 代表 | 压缩效果 | 性质 |
|------|------|---------|------|
| **架构级压缩** | MLA（DeepSeek-V2）| **KV −93.3%**、吞吐 5.76× | 训练时确定，天花板最高 |
| **量化** | KIVI / MixKVQ / PM-KVQ | 2-4 bit，3-8× 内存↓ | 存储侧，精度受限 |
| **稀疏/驱逐** | H2O / SnapKV / R-KV / ThinKV | 保留 5-20% KV | 计算侧，需好信号 |
| **缓存复用** | RadixAttention / LMCache | 跨请求命中省全量计算 | 打破压缩上限（复用=0 成本）|

**MLA 压缩原理（为何能 −93.3%）**：MLA 不存完整 (K,V)，而是存一个**低维隐向量 c**，K/V 在 attention 时即时上投影还原：
```
传统:  存 K ∈ R^(d), V ∈ R^(d)      → 每 token 2d
MLA:   存 c = W_DKV · h ∈ R^(d_c), d_c ≪ d
       K = W_UKV · c,  V = W_UV · c   (用时还原)
→ 每 token 存 d_c ≪ 2d   ⇒  DeepSeek-V2 实测 KV −93.3%
```
> **机理**：MLA 本质是 **KV 的低秩分解**——把高维 KV 压到低秩隐空间。代价：需训练时学习 W_DKV/W_UKV，**无法事后套用到任意模型**。这是它"天花板最高但不可叠加"的根本原因。

> **关键洞察**：单条路线收益递减。MLA 已把架构红利吃掉 93%，但 reasoning 浪潮又把它"吃回来"——R-KV 显示 reasoning 下通用压缩 baseline 仅保 60%。**突破上限靠"全生命周期 × 结构化自适应"的协同**，而非单点压更狠。

#### 第三层：学术界与产业界共识

- **vLLM**：默认预留 90% HBM 给 KV；PagedAttention 围绕 KV 分页管理
- **NVIDIA Dynamo**：四级 KV 分层（HBM → DRAM → SSD → Network），前提是"KV 超出 GPU 显存时 offloading 最有效"
- **LMCache / Tutti**：SSD-backed KV，"KV footprint 远超 GPU HBM 与 CPU DRAM"
- **SGLang**：RadixAttention 按前缀树复用 KV，跨请求共享
- **综述共识**（LLMOrbit, arXiv:2601.14053）：明确把"MLA 8× KV 压缩"列为突破 scaling wall 的关键范式之一

---

### 本页最终推导

```
推理模型(长生成) + 长上下文 + 高并发 + Agent 多轮
        ↓
KV 线性扩张（公式必然）→ 主导显存与带宽
        ↓
架构压缩(MLA −93%) 红利被 reasoning 浪潮吃回（R-KV: baseline 仅 60%）
        ↓
单点压缩收益递减
        ↓
突破口：全生命周期(复用打破上限) × 结构化自适应(差异化突破帕累托)
        ↓
范式转移：从"压存储"到"全生命周期 × 结构化自适应"
```

### 前提限定

> ⚠️ 本结论适用于 **长上下文（>32K）、高并发（>16）、推理模型、Agent 多轮**负载。短问答、低并发场景 KV 占比低，简单量化即足够。

### So What

KV 是推理系统的设计中心。谁掌握"全生命周期 + 结构化自适应"的 KV 压缩栈，谁就掌握吞吐、并发、长上下文与成本效率的制高点。

---

## P3 看业界：工业框架已围绕 KV 重构

### 核心观点

主流推理框架（vLLM / SGLang / TensorRT-LLM / Dynamo / LMCache）的能力已收敛到 KV 管理的三个维度：**分页管理、分层卸载、跨请求复用**。产业实践证明 KV 是系统重构的中心。

### 框架能力对照

| 框架 | KV 管理核心能力 | 定位 |
|------|---------------|------|
| **vLLM** | PagedAttention（分页）、Prefix Cache、社区集成 SnapKV/KIVI | 事实标准，KV 内存管理 |
| **SGLang** | RadixAttention（前缀树复用）、长上下文调度 | 复用 + 调度 |
| **TensorRT-LLM** | INT8/FP8 KV、极致吞吐 | NVIDIA 生产级 |
| **NVIDIA Dynamo** | 四级 KV 分层（HBM→DRAM→SSD→Network） | KV offloading |
| **LMCache / Tutti** | SSD-backed KV、分布式 KV 共享 | 跨节点/跨请求 KV 池 |
| **DiffKV（SOSP 2025）** | key/value/token/head 三级差异化内存管理 | 系统级差异化 |

### 业界已形成的三大共识

**① 分页管理是地基**：PagedAttention 把 KV 按 block 管理，消除碎片，是所有动态压缩（驱逐/复用）的前提。

**② 分层卸载扩展容量**：KV 超出 HBM 时，Dynamo/LMCache 用 DRAM/SSD 扩展——KV 成为"可分层的存储对象"，而非单纯 GPU 显存。

**③ 跨请求复用打破上限**：RadixAttention/LMCache 让相同前缀/语义的 KV 跨请求共享——**复用的 KV 成本为 0，是唯一能"突破压缩上限"的路线**。

### MoE + 推理模型的叠加挑战

- MoE 架构（DeepSeek-V3/Kimi K2）使 KV 与专家通信双重膨胀（详见多卡报告）
- 推理模型长生成使 KV 在**解码阶段**爆炸（R-KV/ThinKV 聚焦点）
- 两者叠加：KV 既要多卡分布（通信），又要动态压缩（信号）

### 本页推论

```
分页管理(地基) + 分层卸载(扩容) + 跨请求复用(打破上限)
        ↓
KV 已是"可管理、可分层、可复用"的系统对象
        ↓
工业框架围绕 KV 重构完成 → 下一步是压缩算法与系统的深度协同
```

### So What

基础设施已就位。竞争的下一程在"压缩算法 × 系统协同"——谁的压缩能无缝挂载到 PagedAttention/分层/复用栈上，谁就赢。

---

## P4 看竞争：KV 压缩已分化为六大技术族

### 核心观点

KV 压缩已从早期单一的"token 选择"，分化为**六大技术族**，分别从"存更少 bit / 留更少 token / 压缩结构 / 只保关键 head / 复用 / 系统重构"六个角度进攻同一瓶颈。

### 失效案例集（"为何单点压缩不够"的实证）

下列案例证明：每种单点方法都有其**明确失效边界**，正是这些失效定义了六大族的能力天花板，也论证了"协同"的必要性。

**案例 1：SnapKV 在 reasoning 上"反向保留"（R-KV Figure 3 实证）**
```
现象: SnapKV 按 attention 分数保留 top token
机理: reasoning model 的重复自反思片段彼此产生高 attention
结果: SnapKV 把重复的"我再来验证一下…"当"重要"过度保留
      而真正关键但分散的推理步骤被丢弃
量化: 同样压到 10% KV，SnapKV 类 baseline 仅保 60% 性能
结论: 统计信号在 reasoning 负载下系统性误判
```

**案例 2：Sliding Window 在 NIAH 崩塌（强关系依赖任务）**
```
任务: 大海捞针(NIAH)——需精确定位并串联"针"
方法对照(32K NIAH):
  Full KV        → 100%
  CONF-KV(置信度) → 91.4%
  H2O(heavy hit) → 80.6%
  Sliding Window → 53.8%  ← 崩塌
机理: 滑窗只保近期 token，把早期"针"的关系信息删掉
结论: 强关系依赖任务对"丢历史"零容忍
```

**案例 3：全局 INT4 在算术推理上崩（KVFundaBench O1，ICML 2026）**
```
任务: 算术推理(GSM8K)
现象: 压缩比 <20% 时，精度从 0.75 跌到 <0.5
对照: 检索任务(NIAH)同压缩比仍稳
机理: 算术的非-sink attention 更弥散(依赖更广上下文)
      一刀切量化破坏 dispersed 的推理线索 → disrupted CoT links
结论: "通用任务可接受的损失"在推理任务上被非线性放大
```

**案例 4：删除关键 head / 异常 value 的灾难性失效**
```
Retrieval Head: 剪除 <5% 的检索 head → 检索失败 + 幻觉
              （剪随机非检索 head 无影响 → 因果性证明）
VaSE: 驱逐少量异常大 value 态 → 模型进入"重复推理循环"
ThinKV: 移除 T(回溯)思维 → 模型无限循环
结论: 少数关键结构(head/value/thought)是"不可压"的，全局策略会误伤
```

> **失效案例的战略含义**：案例 1-3 证明"全局统计压缩"在 reasoning/关系任务失效；案例 4 证明"少数关键结构不可压"。两者共同指向——**必须用结构化自适应(保护关键 head/thought) + 全生命周期(复用避免重压)**，这正是两大控制点的实证来源。

### 六大技术族全景

| 技术族 | 核心思想 | 代表 | 成熟度 | 压的是 |
|--------|---------|------|--------|--------|
| **① 量化** | 存更少 bit | KIVI(2bit)、MixKVQ、PM-KVQ、KVQuant | TRL 6-8，vLLM 已集成 | 精度/字节 |
| **② 稀疏/驱逐** | 留更少 token | H2O、SnapKV、R-KV、ThinKV、LazyEviction | TRL 4-7 | token 数 |
| **③ 低秩/结构化** | 压缩表示结构 | **MLA(−93.3%)**、低秩近似、CLA/YOCO/MiniCache(跨层) | MLA 已量产 | 结构 |
| **④ 检索头/head 级** | 只关键 head 重要 | Retrieval Head(<5%)、HeadKV | TRL 3-5 | head 数 |
| **⑤ 缓存复用** | 跨请求共享 | RadixAttention、LMCache、CacheBlend | TRL 7-8 | 计算量(0 成本) |
| **⑥ 架构/系统** | 系统级重构 | PagedAttention、FlashAttention、Dynamo、DiffKV | TRL 8-9 | 显存/带宽 |

### 技术族之间的正交与叠加关系

```
                 压缩对象维度
    ┌─────────────────────────────────────────┐
    │  存储(bit)    token数    结构    head    计算(复用)
    │   量化         稀疏      低秩   检索头    复用
    │   KIVI        SnapKV    MLA   HeadKV   RadixAttn
    └─────────────────────────────────────────┘
                      ×（正交可叠加）
    ┌─────────────────────────────────────────┐
    │              全生命周期时序                │
    │   Prefill减量  →  Decode压缩  →  跨请求复用 │
    └─────────────────────────────────────────┘
```

> **关键**：六大族彼此**正交**——量化压字节、稀疏压 token 数、低秩压结构、检索头压 head、复用省计算、系统管显存。**任意叠加都乘性放大收益**。这也是为何"协同"是竞争核心。

### 竞争焦点：哪里已饱和、哪里是窗口

| 方向 | 状态 | 判断 |
|------|------|------|
| 全局 KV 量化（INT4/2-bit） | 接近饱和 | 红海，差异化难 |
| 通用 token 驱逐（H2O/SnapKV） | 成熟 | 红海，reasoning 下失效 |
| 架构级（MLA） | DeepSeek 量产 | 已被头部占据，模仿价值低 |
| **head/layer 自适应** | 新兴 | ThinKV/ReasonAlloc/DiffKV 验证有效，**未达工业标准** |
| **跨请求语义复用** | 新兴 | RadixAttention 仅前缀，**语义级复用空白** |
| **全生命周期协同** | 空白 | Prefill/Decode/Reuse 从未统一闭环 |

### 本页推论

```
单点饱和：全局量化、通用驱逐、架构模仿 → 红海
窗口犹在：head/layer 自适应、语义复用、全生命周期协同 → 蓝海
        ↓
竞争本质：从"压更狠"转向"压更准(自适应) + 压更久(复用) + 压更协同(全生命周期)"
```

### So What

六大族已把单点空间填满。**真正的差异化在"自适应 × 复用 × 协同"三者的结合**——这是控制点一、二的竞争内核。

---

## P5 看技术：压缩方法全景矩阵与信号演进

### 核心观点

KV 压缩的**方法（量化/稀疏/低秩/复用）是稳定的根技术**，但**驱动它们的信号正持续升级**：magnitude → semantic → redundancy → reasoning-aware → relation-graph。信号升级是长期竞争力。

### 压缩信号演进（主线）

| 年份 | 信号时代 | 代表 | 信号本质 |
|------|---------|------|---------|
| 2023 | magnitude/统计 | H2O、早期量化 | 按 attention 分数 / weight 幅度 |
| 2024 | semantic | SnapKV（聚类锚点）、CONF-KV（置信度） | 按语义聚类 |
| 2025 | redundancy/reasoning | **R-KV**（冗余，λ=0.1）、ThinKV（thought） | 按冗余/思维类型 |
| 2026+ | relation-graph | （见关系推理压缩报告） | 按实体-关系图连通性 |

> **演化主线**：信号越来越接近"信息的真实价值结构"。每一次信号升级都突破前一时代的帕累托上限。

### 压缩对象 × 压缩方法 全景矩阵

| 对象 ↓ / 方法 → | 量化 | 稀疏/驱逐 | 低秩/结构 | 复用 |
|----------------|------|----------|----------|------|
| **Prefill（长输入）** | — | SnapKV、LazyLLM、FTP | MLA（架构） | 前缀缓存 |
| **Decode（长生成）** | KIVI、MixKVQ、PM-KVQ | H2O、R-KV、ThinKV、LazyEviction | CLA/YOCO（跨层） | RadixAttention |
| **跨请求** | — | — | — | LMCache、CacheBlend |
| **head/layer 维度** | HeadKV、ThinKV(TBQ) | ReasonAlloc（层预算） | — | — |

### 六大族代表方法速览（含真实数据）

**① 量化族**
- **KIVI**：2-bit，key per-channel / value per-token，无需微调
- **MixKVQ（2512.19206）**：query 感知混合精度，识别需高精度的关键 key channel
- **PM-KVQ（2505.18610）**：渐进式混合精度 + RoPE 感知，长 CoT 提升 8%
- **ThinKV-TBQ**：按 thought 类型分配 8/4/2-bit（R/E/T）

**② 稀疏/驱逐族**
- **H2O**：heavy hitter 保留（经典，reasoning 下失效）
- **SnapKV**：聚类锚点 + observation window
- **R-KV（2505.24133）**：冗余感知，λ=0.1（90% 关系信号），10%→100%、6.6× 吞吐
- **ThinKV（2510.01290，ICLR Oral）**：thought 自适应，<5% KV、5.8× 吞吐、1.68× 低 TPOT
- **LazyEviction（2506.15969）**：Token Importance Recurrence，延迟驱逐保留周期性关键 token
- **VaSE（2606.03928）**：保护异常大 value 态，避免重复推理循环

**③ 低秩/结构化族**
- **MLA（DeepSeek-V2，2405.04434）**：KV 压进隐向量，**−93.3%**、吞吐 5.76×——天花板最高
- **CLA / YOCO / MiniCache**：跨层共享 KV，层维度压缩
- 低秩近似：KV 矩阵低秩分解

**④ 检索头/head 级族**
- **Retrieval Head（2404.15574）**：<5% head 是检索载体，剪除→幻觉；CoT 强依赖
- **HeadKV**：head 级预算分配

**⑤ 缓存复用族**
- **RadixAttention（SGLang）**：前缀树复用
- **LMCache / Tutti**：分布式/SSD-backed KV 共享
- **CacheBlend**：RAG 知识融合复用

**⑥ 架构/系统族**
- **PagedAttention（vLLM）**：分页管理地基
- **FlashAttention**：IO 感知注意力
- **Dynamo**：四级分层
- **DiffKV（SOSP 2025）**：三级差异化内存管理
- **ThinKV-CT kernel**：扩展 PagedAttention 原地复用被驱逐槽，避免 gather compaction（实测 R-KV gather 在大 batch 下 TPOT 慢化 37×）

### 机理工作示例（关键方法走查）

**示例 1：ThinKV 的 thought 自适应压缩走查（ICLR 2026 Oral）**

设 CoT 生成如下（τ=128 token 一段）：
```
[R 段] "设 x 为苹果数，则方程为 x+3=10..."   ← reasoning，中等稀疏
[E 段] "计算: 10-3=7"                        ← execution，低稀疏(强依赖上下文)
[T 段] "等一下，我需要验证..."               ← transition，高稀疏(回溯)
[R 段] "重新设 y 为总数..."                  ← reasoning
```
ThinKV 处理：
```
① thought 分类(attention 稀疏三模态):
   R 段稀疏度≈中 → R;  E 段≈低 → E;  T 段≈高 → T

② TBQ 按思维类型分配精度:
   R token → 4-bit(NVFP4);  E token → 4-bit;  T token → 2-bit(ternary)

③ TBE 在 T 段(轨迹改变点)触发渐进驱逐:
   出现 T 段 → 前置 R 段保留率 64→32→16→8→4 逐级降
   (用 K-means 聚类 post-RoPE key 选保留代表)

结果: KV <5%，近无损，吞吐 5.8×
机理: T 段是"推理换轨点"，其后旧思路影响力递减 → 可大胆压
```
> **机理要点**：ThinKV 把"何时压、压多狠"锚定在**思维类型**上，而非全局比例。这是"结构化自适应"的典型实例。

**示例 2：Retrieval Head 的因果性验证（为何 head 级差异化有物理基础）**
```
实验(2404.15574):
  Llama-2 7B 中有 12 个 retrieval head "总是" attend 到所需信息
  对照:
    剪除这 <5% retrieval head → 检索失败 + 幻觉
    剪除等量随机非检索 head → 检索能力不受影响
  → 因果性证明: 信息检索由少数 head 承载
推论: 关键 head 必须高精度保留，其余 head 高度可压
      → head 级差异化不是启发式，是有机制支撑的物理事实
```

**示例 3：PagedAttention + ThinKV-CT（系统层如何避免驱逐的开销）**
```
问题: 驱逐产生非连续"内存洞" → 需 gather compaction 整理
      实测: R-KV 的 gather 在大 batch 下 TPOT 慢化 37×(HBM 带宽争用)

ThinKV-CT 解法(扩展 PagedAttention 块表):
  块表新增字段: thought类型 / 起始索引 / 段掩码 / 驱逐掩码
  被驱逐 token 不立即删除，而是"软标记"在驱逐掩码里
  新 token 到来时 → 查同 thought 类型的可回收槽 → 原地覆写
  (attention 对 KV 顺序置换不变 → 无需重排)

机理: 用"原地复用"替代"gather 整理"，消除 37× 慢化
启示: 关系/自适应压缩的工程实现必须避免 gather(课题一的 Runtime 约束)
```

**示例 4：RadixAttention 跨请求复用（为何复用是"0 成本"）**
```
请求 A: "请总结《三体》第一部"  →  Prefill 算 KV，存前缀树
请求 B: "请总结《三体》第二部"  →  共享前缀"请总结《三体》"
                                  命中部分 → 跳过该部分 Prefill 计算
请求 C: "请总结《三体》"        →  完全命中前缀 → 几乎免 Prefill

机理: 前缀树把"已算过的 KV"跨请求共享
      命中 = 0 计算 0 存储(复用现成) → 突破"压缩"上限
局限: 只认"字符级前缀"；"语义相同表述不同"无法命中
      → 语义指纹复用是下一站(课题二)
```

### 技术成熟度现状

| 技术族 | TRL | 工业集成 | 核心瓶颈 |
|--------|-----|---------|---------|
| 全局量化(INT4/2) | 7-8 | vLLM/TRT-LLM | 2-bit 精度损失 |
| 通用驱逐(H2O/SnapKV) | 6-7 | vLLM/SGLang 社区 | reasoning 下失效 |
| 架构(MLA) | 9 | DeepSeek 量产 | 模仿价值低 |
| head/layer 自适应 | 4-5 | 未集成 | 无统一 Runtime |
| 语义级复用 | 3-4 | 仅前缀复用 | 语义指纹空白 |
| 全生命周期协同 | 2-3 | 无 | 三段未闭环 |

### 本页推论

根技术（量化/稀疏/低秩/复用）稳定且团队已具备；**信号升级（→reasoning-aware）与维度升级（→head/layer/全生命周期）是注入根技术的新价值**。

### So What

掌握"信号升级 + 维度升级"两条注入路径，即可把团队已有的量化/稀疏/复用能力迁移到 KV 压缩的新前沿。

---

## P6 看机会：全生命周期 × 结构化自适应 = 两个突破上限的方向

### 核心观点

单点压缩收益递减。两个方向能**突破帕累托上限**：① 用复用打破压缩上限（全生命周期）；② 用差异化突破一刀切上限（结构化自适应）。

### 机会一：全生命周期 KV 管理（控制点一）

- **传统思路**：只压 Decode 阶段 KV → 单段收益递减
- **下一阶段**：**Prefill 源头减量（少生成）→ Decode 动态压缩（少存）→ 跨请求复用（0 成本）** 三段闭环

**关键机会点**：
```
复用是唯一"0 成本"路线 → 打破压缩上限
但 RadixAttention 只做前缀复用 → 语义级复用空白
语义指纹缓存（相同语义不同表述的 KV 复用）是复用的下一站
```

### 机会二：结构化自适应压缩（控制点二）

- **传统思路**：全局统一 bit、固定驱逐比例 → 帕累托上限低
- **下一阶段**：**按 head / layer / task / thought 维度差异化** → 突破上限

**关键机会点**：
```
Retrieval Head 证明 <5% head 关键 → head 级差异化有物理基础
ThinKV 证明 thought 差异化可行（5.8× 吞吐）
ReasonAlloc 证明 layer 预算（Reasoning Wave）有效
但：head/layer/task 自适应从未统一进工业 Runtime
```

### 机会三：reasoning 浪潮倒逼的信号升级（演进分支）

- reasoning model 长生成使通用压缩失效（R-KV baseline 仅 60%）
- 倒逼压缩信号从统计升级到 redundancy/thought/relation
- **详见 [`关系推理压缩技术洞察报告.md`](关系推理压缩技术洞察报告.md)**（本层的一个演进分支，不再展开）

### 压缩对象 × 时序 × 自适应 三维机会地图

| 时序＼自适应 | 全局 | head/layer | task/thought |
|------------|------|-----------|-------------|
| **Prefill** | SnapKV（成熟） | 层预算（ReasonAlloc） | （空白） |
| **Decode** | H2O（饱和） | ThinKV-TBQ（新兴） | ThinKV-TBE（新兴） |
| **跨请求** | 前缀复用（成熟） | — | 语义复用（空白） |

> **空白点**：Prefill×task、跨请求×语义复用、全生命周期闭环——三处高机会。

### Why Us（团队优势）

| 已有能力 | 迁移方向（KV 压缩） | 复用程度 |
|---------|-------------------|---------|
| 模型量化 | KV 混合精度量化 | 高 |
| 稀疏优化 | KV 驱逐、head 级稀疏 | 高 |
| 推理 Runtime | 全生命周期 KV 管理 Runtime | 中高 |
| 多卡并行 | KV 分层/分布式复用 | 中 |

组织优势：研究与工程闭环，量化/稀疏/Runtime 三件套已具备，KV 压缩是天然延伸。

### 本页推论

两个突破方向（全生命周期 + 结构化自适应）+ 一个演进分支（reasoning 信号升级），构成 KV 压缩的机会版图。

### So What

"全生命周期协同 + 结构化自适应"是 KV 压缩的长期护城河，越早把三段闭环与差异化挂载到 Runtime，越难复制。

---

## P7 战略总结：收敛为两大战略控制点

### 控制点一：全生命周期 KV 管理（Lifecycle KV Management）

- **解决问题**：单段压缩收益递减；KV 在解码阶段爆炸（详见 P2）
- **核心指标**：跨请求 KV 命中率、端到端吞吐、长上下文并发
- **技术抓手**：Prefill 选择性计算（FTP/LazyLLM 思路）、Decode 动态压缩、跨请求前缀/语义复用、分层卸载

### 控制点二：结构化自适应压缩（Structured Adaptive Compression）

- **解决问题**：全局一刀切的帕累托上限；reasoning 下通用压缩失效
- **核心指标**：精度-压缩帕累托前沿、head/layer 预算利用率
- **技术抓手**：head-level/layer-level 预算分配（ReasonAlloc/HeadKV）、task/thought 感知（ThinKV）、混合精度（MixKVQ/TBQ）

### 两大控制点的关系

```
控制点一（全生命周期）：横向贯穿 Prefill→Decode→Reuse，用复用打破上限
         ×
控制点二（结构化自适应）：纵向按 head/layer/task/thought 差异化，突破帕累托
         ↓
KV 压缩竞争力 = 全生命周期协同 × 结构化自适应
         ↓
覆盖长上下文 / 高并发 / 推理模型 / Agent 四大负载
```

### Why Now（为什么是现在）

| 机会窗口 | 原因 |
|---------|------|
| head/layer 自适应 | ThinKV(ICLR Oral)/ReasonAlloc/DiffKV 已验证有效，但未达工业标准 Runtime |
| 语义级复用 | RadixAttention 仅前缀，语义指纹复用空白 |
| 全生命周期协同 | Prefill/Decode/Reuse 从未统一闭环，系统侧空白 |
| reasoning 信号升级 | R-KV/ThinKV/ShotKV(ICML) 浪潮刚起，关系图统一是下一站（见关系报告） |

### 三个空白 = 三个护城河

```
空白一：head/layer/task 自适应统一 Runtime（结构化自适应）
空白二：语义级跨请求 KV 复用（全生命周期）
空白三：Prefill-Decode-Reuse 全生命周期闭环（系统协同）
        ↓
三个空白相互独立又彼此支撑，构成 KV 压缩的完整护城河
```

---

## P8 课题规划

> **关联精读**：reasoning 浪潮的对标基线详见 [`02_论文精读\关系推理压缩_论文精读_20260628.md`](./02_论文精读/关系推理压缩_论文精读_20260628.md)。本层课题聚焦"全生命周期 + 结构化自适应"两个控制点，与关系报告课题正交可叠加。

### 课题一：Head-Layer 自适应 KV 混合精度压缩技术

#### 关键挑战

KV 量化的帕累托上限受限于"全局一刀切"：所有 head、所有 layer 用统一 bit。但 Retrieval Head（2404.15574）证明 **<5% head 是检索载体**（剪除→幻觉），其余 head 高度可压；ThinKV-TBQ 证明按 thought 分配 8/4/2-bit 可行；ReasonAlloc 证明 layer 预算（Reasoning Wave）有效。**但 head/layer/task 三个维度的自适应量化从未统一进工业 Runtime**。全局 INT4 在长上下文/推理任务精度损失大，而关键 head 需要高精度——这个矛盾未被系统解决。

#### 技术目标

对长上下文（128K）、推理模型、高并发场景：
- KV 显存占用降低 **60-75%**（等效 2-4 bit 平均精度）
- 长上下文/推理任务精度损失 **≤1%**
- 与现有驱逐/复用正交，可叠加

#### 关键技术

**1 head 敏感度标定（离线）**
基于 Retrieval Head 机制，标定每个 head 的"检索重要性"：用 NIAH/CoT 任务测 head 屏蔽后的精度下降，划分 {关键 head, 普通 head, 可压 head}。
*可信性*：Retrieval Head 证明 head 重要性幂律分布；HeadKV 验证 head 级预算有效。

**2 layer 预算分配（Reasoning Wave 思路）**
按层注意力冗余度分配 KV 预算（Lethe/ReasonAlloc 思路），冗余高的层给更少预算。
*可信性*：ReasonAlloc 验证 layer 预算超越均匀 R-KV/SnapKV；Lethe 验证层稀疏感知有效。

**3 head-layer 联合混合精度**
关键 head × 关键 layer → FP8/FP16；可压 head × 冗余 layer → INT2/ternary；中间 → INT4。联合决策矩阵。
*可信性*：ThinKV-TBQ 验证 thought 维度混合精度可行；本课题是 head×layer 二维扩展。

#### 风险与缓解

| 风险 | 缓解 |
|------|------|
| head 标定跨任务不稳定 | 多任务联合标定 + 软分配（概率权重）|
| 混合精度 kernel 碎片化 | 沿用 ThinKV 的 group quantization + 解量化 fused GEMM |
| 关键 head 误判致幻觉 | Retrieval Head 因果性已证；保守保留 top-5% head 高精度 |

#### 关键假设与验证清单

| # | 假设 | 验证方法 | 预期结论 | 风险 |
|---|------|---------|---------|------|
| H1 | head 重要性呈幂律（少数 head 关键）| 屏蔽 head 测精度下降 | top-5% head 决定主要精度 | 低（Retrieval Head 已证）|
| H2 | head×layer 联合混合精度优于全局 INT4 | 同显存对照 | 精度 +3-5pp | 中（核心假设）|
| H3 | layer 预算（Reasoning Wave）可迁移到通用模型 | 跨模型层冗余度测量 | 冗余模式可泛化 | 中 |
| H4 | 关键 head 高精度 + 可压 head INT2 叠加正交 | 联合消融 | 叠加收益 > 单独之和×0.8 | 低 |

#### 验证里程碑

```
M1（2周）：head 敏感度标定，验证幂律分布
M2（4周）：layer 预算分配原型
M3（6周）：head×layer 联合混合精度 v0
M4（8周）：LongBench/AIME 达标（精度损失≤1%，显存↓60%+）→ 立项
```

---

### 课题二：全生命周期 KV 管理 Runtime

#### 关键挑战

现有 KV 压缩各自为政：Prefill 压缩（SnapKV/LazyLLM）、Decode 压缩（R-KV/ThinKV）、跨请求复用（RadixAttention/LMCache）三段**从未统一闭环**。后果：Prefill 减量的 token 在 Decode 又被重复压缩（浪费）；Decode 压缩的 KV 无法跨请求复用（RadixAttention 只认前缀）；复用命中的 KV 未跳过 Prefill 计算（重复算）。**三段割裂使总收益 < 各段之和**。

#### 技术目标

对 Agent 多轮、长上下文、高并发场景：
- 跨请求 KV 命中率 **≥50%**（前缀 + 语义）
- 端到端吞吐提升 **40-60%**
- Prefill 计算量降低 **30%+**（命中即跳过）

#### 关键技术

**1 三段闭环调度**
统一 Runtime 管理 Prefill→Decode→Reuse：Prefill 选择性计算产出"必要 KV"→ Decode 动态压缩 → 压缩后 KV 建索引供跨请求复用 → 命中时跳过 Prefill 直接复用。
*可信性*：vLLM PagedAttention 是分页地基；SCOPE 已尝试分离 prefill/decode 压缩；本课题是三段全闭环。

**2 语义级跨请求复用**
超越前缀复用：用 KV 的语义指纹（embedding LSH hash）做缓存键，相同语义不同表述的 KV 可复用。
*可信性*：RadixAttention 验证前缀复用有效；Models Take Notes 验证 KV 笔记本 98.5% hit rate；语义指纹是下一站。

**3 复用-压缩协同**
复用命中的 KV 直接以压缩态存储（不还原），Decode 直接在压缩态上计算；未命中的走 Prefill 减量+Decode 压缩。
*可信性*：ThinKV-CT kernel 验证压缩态原地复用可行（避免 gather compaction）。

#### 风险与缓解

| 风险 | 缓解 |
|------|------|
| 语义指纹误命中致错误 | 相似度阈值 + 增量校验（命中后轻量重算关键 head）|
| 三段调度开销 | 沿用 PagedAttention 分页，调度开销 <5% |
| 复用 KV 与新 query 不匹配 | query 感知的部分复用（CacheBlend 思路）|

#### 关键假设与验证清单

| # | 假设 | 验证方法 | 预期结论 | 风险 |
|---|------|---------|---------|------|
| H1 | 语义复用命中率显著高于纯前缀 | 跨请求 trace 统计 | 语义命中率比前缀 +20pp | 中 |
| H2 | 三段闭环总收益 > 各段之和 | 端到端 vs 分段独立 | 协同收益 >10% | 中（核心假设）|
| H3 | 压缩态 KV 可直接复用计算（免还原）| 压缩态 Decode 精度测试 | 精度损失 <1% | 中（ThinKV-CT 支撑）|
| H4 | 复用命中可跳过 Prefill 计算 | 命中请求的 Prefill 耗时测量 | Prefill −30%+ | 低 |

#### 验证里程碑

```
M1（2周）：前缀复用基线测量（RadixAttention 复现）
M2（4周）：语义指纹缓存原型
M3（6周）：三段闭环调度 v0
M4（8周）：AgentBench/LongBench 达标（命中率≥50%，吞吐↑40%+）→ 立项
```

---

### 课题优先级

| 课题 | 优先级 | 依赖 | 理由 |
|------|--------|------|------|
| 课题一：head-layer 自适应量化 | 🥇 P0 | 无 | 物理基础已证（Retrieval Head），空白明确 |
| 课题二：全生命周期 Runtime | 🥈 P0 | 课题一压缩态可复用 | 系统侧空白，复用打破上限 |
| （演进分支：reasoning 信号） | 见关系报告 | — | 关系图统一是下一站 |

```
立即（本月）：课题一/二 两周验证启动，head 标定 + 前缀复用基线
Q3：课题一 head×layer 混合精度达标；课题二三段闭环原型
Q4：两课题立项执行，集成 vLLM/SGLang Runtime
```

---

## P9 风险与前提限定

### KV 压缩 vs 权重压缩：定位对照

| 维度 | 权重压缩 | KV 压缩 |
|------|---------|--------|
| 对象 | 固定成本 | 可变成本（随 T×B 增长）|
| 主导场景 | 端侧/单机 | 长上下文/高并发/推理/Agent |
| 成熟度 | INT4 已产品化 | 量化成熟，自适应/复用新兴 |
| 团队定位 | 已有 | 本层聚焦 |

### 核心前提限定

> ⚠️ 本报告结论受以下前提约束：

1. **负载前提**：结论适用于长上下文（>32K）、高并发（>16）、推理模型、Agent 多轮。短问答/低并发场景 KV 占比低，简单量化即足够，强行上自适应/复用得不偿失。
2. **架构前提**：MLA 等**架构级压缩需训练时确定**，本层课题聚焦**训练无关的推理时压缩**（适配任意模型）。MLA 是天花板参照，非可叠加对象。
3. **数据前提**：所有数字（MLA −93.3%、R-KV 6.6×、ThinKV 5.8×、Retrieval Head <5%）来自公开论文，未外推。工业部署数值需团队自测。
4. **课题未验证前提**：head-layer 自适应量化、全生命周期 Runtime 为前瞻课题，效果待 M1-M4 验证。

### 主要风险与对策

| 风险类别 | 风险 | 对策 |
|---------|------|------|
| 精度风险 | 混合精度/驱逐在极端长上下文精度崩塌 | 失效保险（精度跌破阈值即回补高精度）|
| 工程风险 | 混合精度 kernel 碎片化、gather compaction 慢化 | 沿用 ThinKV-CT 原地复用 + fused GEMM |
| 复用风险 | 语义复用误命中 | 相似度阈值 + 增量校验 |
| 范围风险 | 课题过散 | 严格 P0 优先：head-layer 量化 + 全生命周期 Runtime 先行 |

### 反向论点（Devil's Advocate）

| 反向论点 | 回应 |
|---------|------|
| "MLA 已 −93%，KV 压缩已解决" | MLA 是架构级、需训练、被 DeepSeek 占据；推理时压缩适配任意模型，且 reasoning 浪潮把红利吃回（R-KV baseline 仅 60%）|
| "全局 INT4 够用" | 全局量化在长上下文/推理任务精度损失大（KVFundaBench O1：算术 <20% 压缩比崩）；head 差异化是突破点 |
| "复用只对相同请求有效" | RadixAttention 已证前缀复用跨请求有效；语义复用是其泛化 |
| "全生命周期协同太复杂" | PagedAttention 分页地基已在；三段闭环是调度层工作，非算法重写 |

---

## 附录 A：KV 压缩全景速查

```
KV Cache 压缩技术树
├── 量化（压字节）──── TRL 6-8，已集成
│   ├── 全局: KIVI(2bit), KVQuant
│   ├── 混合精度: MixKVQ, PM-KVQ, ThinKV-TBQ
│   └── head/layer: HeadKV（新兴）
│
├── 稀疏/驱逐（压 token）──── TRL 4-7
│   ├── 统计: H2O(heavy hitter), SnapKV(cluster)
│   ├── 冗余/关系: R-KV(λ=0.1, 10%→100%)
│   ├── thought: ThinKV(<5% KV, 5.8×)
│   ├── 时序: LazyEviction(recurrence)
│   └── value 保护: VaSE(异常 value)
│
├── 低秩/结构化（压结构）──── MLA 量产
│   ├── 架构: MLA(DeepSeek, −93.3%)
│   ├── 跨层: CLA/YOCO/MiniCache
│   └── 低秩近似
│
├── 检索头/head 级（压 head）──── TRL 3-5
│   └── Retrieval Head(<5%), HeadKV
│
├── 缓存复用（省计算）──── TRL 7-8
│   ├── 前缀: RadixAttention(SGLang)
│   ├── 分布式: LMCache, Tutti
│   ├── RAG: CacheBlend
│   └── 语义: ⭐ 空白（机会）
│
└── 架构/系统（管显存）──── TRL 8-9
    ├── 分页: PagedAttention(vLLM)
    ├── IO: FlashAttention
    ├── 分层: Dynamo(四级)
    ├── 差异化: DiffKV(SOSP, 三级)
    └── 原地复用: ThinKV-CT kernel
```

### 附录 B：KV 压缩选型决策树

> **给你的导航**：按场景与约束，选择 KV 压缩路线。

```
                    ┌──────────────────────────────┐
                    │   你的首要约束是什么？          │
                    └──────────────┬───────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          ▼                        ▼                        ▼
   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐
   │ 显存不够      │         │ 吞吐/并发不够 │         │ 精度不能掉    │
   └──────┬───────┘         └──────┬───────┘         └──────┬───────┘
          ▼                        ▼                        ▼
   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐
   │ 量化(KIVI 2bit)│        │ 复用(RadixAttn)│        │ head自适应   │
   │ + 稀疏(SnapKV) │        │ + 分层(Dynamo) │        │ (HeadKV/ThinKV)│
   │ + 分层卸载     │        │ 首选复用(0成本)│        │ 保护关键head │
   └──────────────┘         └──────────────┘         └──────────────┘

                    ┌──────────────────────────────┐
                    │   你的负载类型？              │
                    └──────────────┬───────────────┘
                                   │
          ┌──────────────┬─────────┴────────┬──────────────┐
          ▼              ▼                  ▼              ▼
   ┌────────────┐ ┌────────────┐    ┌────────────┐ ┌────────────┐
   │ 长上下文    │ │ 推理模型    │    │ Agent 多轮  │ │ 短问答      │
   │ >128K      │ │ CoT 长生成  │    │ 跨请求      │ │ 低并发      │
   ├────────────┤ ├────────────┤    ├────────────┤ ├────────────┤
   │ SnapKV稀疏  │ │ R-KV/ThinKV│    │ RadixAttn   │ │ 全局INT4    │
   │ +KIVI量化   │ │ (reasoning │    │ +LMCache    │ │ (KIVI)足够  │
   │ +MLA(若可训)│ │  信号压缩)  │    │ 复用         │ │ 不必自适应  │
   └────────────┘ └────────────┘    └────────────┘ └────────────┘
```

### 附录 C：一页速查（Quick Reference）

| 你要做的 | 控制点 | 课题 | 代表方法 |
|---------|--------|------|---------|
| 降 KV 显存且保精度 | 自适应 | 课题一 | head-layer 混合精度（HeadKV+ThinKV-TBQ）|
| 提升并发/吞吐 | 全生命周期 | 课题二 | 三段闭环 + 语义复用 |
| 长上下文推理保精度 | 自适应 | 课题一 | Retrieval Head 保护 + 层预算 |
| Agent 多轮省成本 | 全生命周期 | 课题二 | 跨请求前缀/语义复用 |
| reasoning 模型长生成 | （演进分支）| 见关系报告 | R-KV/ThinKV + 关系图 |

### 附录 D：关键论文索引（论据来源）

> 标注 arXiv ID 的为外部检索核实文献（2024-2026）；其余来自知识库语料。

| 技术族 | 论文 | arXiv / 会议 | 贡献 |
|--------|------|------------|------|
| 架构 | **DeepSeek-V2（MLA）** | **2405.04434** | MLA KV **−93.3%**、吞吐 5.76× |
| 稀疏 | **R-KV** | **2505.24133** | 冗余感知，10%→100%、6.6× 吞吐 |
| 稀疏 | **ThinKV** | **2510.01290 / ICLR 2026 Oral** | thought 自适应，<5% KV、5.8× 吞吐 |
| 稀疏 | **LazyEviction** | **2506.15969** | Token Importance Recurrence |
| 稀疏 | **VaSE** | **2606.03928** | 异常 value 保护，避免循环 |
| 量化 | **MixKVQ** | **2512.19206** | query 感知混合精度 |
| 量化 | **PM-KVQ** | **2505.18610** | 渐进式混合精度，长 CoT +8% |
| 量化 | **KIVI** | 知识库 | 2-bit KV，per-channel/per-token |
| 稀疏 | H2O / SnapKV | 知识库 | heavy hitter / cluster anchor |
| 稀疏 | **Lethe** | **2511.06029 / AAAI 2026** | 层-时双维自适应 |
| 稀疏 | **ReasonAlloc** | **2606.11164** | Reasoning Wave 层预算 |
| head | **Retrieval Head** | **2404.15574** | <5% head 是检索载体 |
| 系统 | **DiffKV** | **2412.03131 / SOSP 2025** | 三级差异化内存管理 |
| 保真 | **ShotKV/KVFundaBench** | **2502.01941 / ICML 2026** | disrupted CoT links 实证 |
| 系统 | PagedAttention(vLLM) | 知识库 | 分页管理地基 |
| 复用 | RadixAttention(SGLang) | 知识库 | 前缀树复用 |
| 复用 | LMCache / Tutti | 知识库 | 分布式/SSD-backed KV |

### 附录 E：关键术语表

| 术语 | 定义 |
|------|------|
| KV Cache | Transformer 自回归解码缓存的每层 Key/Value，避免重复计算 |
| Prefill / Decode | 预填充（处理输入）/ 解码（生成输出）两阶段 |
| MLA（Multi-head Latent Attention）| DeepSeek 把 KV 压进隐向量的架构级压缩 |
| Retrieval Head | 负责检索的少数 attention head（<5%），剪除致幻觉 |
| 全生命周期 KV 管理 | Prefill 减量 → Decode 压缩 → 跨请求复用 的三段闭环 |
| 结构化自适应压缩 | 按 head/layer/task/thought 维度差异化的压缩 |
| Heavy Hitter | H2O 定义的高 attention token，reasoning 下失效 |
| Reasoning Wave | ReasonAlloc 发现的架构驱动层需求模式 |

---

*本报告为 KV 压缩基础全景层，与 [`参数压缩技术洞察报告.md`](参数压缩技术洞察报告.md)（权重=固定成本，互补两半）、[`关系推理压缩技术洞察报告.md`](关系推理压缩技术洞察报告.md)（演进分支：reasoning 信号升级）、[`多卡推理压缩技术规划报告.md`](多卡推理压缩技术规划报告.md)（多卡 KV 分布 + 通信）互补。核心命题"全生命周期 × 结构化自适应"由理论（KV 线性扩张公式）、实测（MLA −93%、R-KV 6.6×、ThinKV 5.8×）、共识（vLLM/Dynamo/LMCache 围绕 KV 重构）三层证据交叉验证。所有量化数据来自公开论文，未做外推。*
