---
created: 2026-09-05
type: insight-report
status: active
tags: [codex, gdn, 推理优化, 免训练, 线性注意力, 论文解读]
---

# GDN 模型免训练推理加速 · 论文系统解读报告

> 范围：全库 36,237 篇论文（`inference_optimization_full_tagged.json` 等全部 JSON 源，`last_updated=2026-09-03`）
> 目标：找出对 **Gated DeltaNet（GDN，门控增量网络）** 推理优化有用、**免训练**、且能**提升推理速度**的论文
> 结论：第一梯队 7 篇（GDN 原生）、可迁移 12 篇、转换类 6 篇、需训练对照若干

---

## 一、背景：GDN 为什么"难加速"

GDN 是线性注意力（linear attention）的代表性算子，用**固定大小的循环状态（recurrent state）**取代随序列长度增长的 KV cache，因此：

- 优点：长上下文解码内存 O(1)、无 KV cache 增长（Qwen3-Next≈75% GDN 层、Kimi K3/Solar Open 2 均为 GDN/KDA 混合架构）。
- 痛点：解码阶段是 **memory-bound**——每 token 都要把完整循环状态在 HBM 之间往返一次，算术强度 < 1 FLOP/B；且状态多存于 FP32，更新受内存带宽限制，成为延迟主因。
- 推论：GDN 的加速空间不在"算力"，而在**状态的内存流（量化、物化时机、缓存、投机回滚、内核求逆）**——这正是本期精选论文的主线。

> 术语界定：库中 `AGDN / GDNet(type=深度图超分) / GDNSQ` 与 Gated DeltaNet 无关，已排除。

---

## 二、第一梯队：GDN 原生 · 免训练加速（7 篇）

### 1. DAMP — 循环状态量化（PTQ）
- **arXiv** [2608.27513](https://arxiv.org/abs/2608.27513)
- **问题**：GDN/KDA 循环状态存 FP32，占显存大、更新带宽受限，拖慢解码。
- **方法**：首个研究 GDN/KDA **循环状态的后训练量化（PTQ）**，利用"衰减感知（decay-aware）"做混合精度——按各头/通道的衰减强度分配位宽。
- **价值**：免训练，直接砍状态带宽与显存，是 GDN 解码提速的第一性手段。

### 2. TreeWY — 免快照的投机解码验证
- **arXiv** [2608.20961](https://arxiv.org/abs/2608.20961)
- **问题**：GDN 混合模型做投机解码时，为回滚被拒 token 需在**每个草稿位置**快照完整循环状态，且快照无法跨草稿树分支共享 → 宽树高接受率在内存上不可行。
- **方法**：**去除快照**，用树结构 WY（Woodbury/WY 分解）表示进行投机验证。
- **价值**：恢复 GDN 混合模型的投机解码收益，免训练，直接提升解码吞吐。

### 3. DASC — 衰减感知的状态压缩（前缀缓存）
- **arXiv** [2608.30386](https://arxiv.org/abs/2608.30386)
- **问题**：前缀复用需为 GDN 层保存"状态检查点（state checkpoint）"，全量存储加剧内存压力，导致更多驱逐与重复 prefill。
- **方法**：分析 GDN/KDA 的衰减结构，发现不同头/通道对前缀信息的保留能力不同，据此**有损压缩状态检查点**。
- **价值**：面向 serving 的免训练系统优化，降低长上下文多租户场景内存换 prefilling 成本。

### 4. DeltaLog — 循环状态延迟物化
- **arXiv** [2608.15533](https://arxiv.org/abs/2608.15533)
- **问题**：现有解码实现每个 token 后都**物化并写回完整循环状态**，状态维护成为内存流量重灾区（大状态 + 多头时尤甚）。
- **方法**：**延迟物化（deferred materialization）**，压缩状态表示、避免逐 token 全量写回，**不改变模型语义**。
- **价值**：免训练、零精度损失的纯系统层提速。

### 5. When Good Enough Is Optimal — 仅 MatMul 的矩阵求逆
- **arXiv** [2606.06034](https://arxiv.org/abs/2606.06034) · [[2606.06034_When_Good_Enough_Is_Optimal_Multiplication-Only_Ma]]
- **问题**：chunk-wise 并行线性注意力的**下三角矩阵求逆**是长上下文瓶颈，前向代换在 NPU 上并行度低、硬件利用率差。
- **方法**：针对逆矩阵"对角线集中"特性，用**截断 Neumann 展开 + 结构掩码 + 并行残差校正**，将求逆转化为纯 MatMul。
- **价值**：**最贴合昇腾/NPU 场景**——把串行求逆变成可高并行的矩阵乘，免训练算子级加速。

### 6. Fast and Stable Triangular Inversion — 三角求逆稳定化
- **arXiv** [2605.21325](https://arxiv.org/abs/2605.21325) · [[2605.21325_Fast_and_Stable_Triangular_Inversion_for_Delta-Rul]]
- **问题**：delta-rule（GDN 同族）的三角矩阵求逆既是瓶颈又对数值误差高度敏感，实现不当会显著恶化端到端精度。
- **方法**：系统分析 + 提出**快速且数值稳定的求逆算法**。
- **价值**：通用（Qwen3.5/3.6、Kimi Linear、RWKV-7 均适用），是"求逆加速"与"数值稳定性"的统一解，与 #5 互补。

### 7. Persistent-State Dataflow Accelerator — FPGA 持久化状态流
- **arXiv** [2603.05931](https://arxiv.org/abs/2603.05931) · [[2603.05931_A_Persistent-State_Dataflow_Accelerator_for_Memory]]
- **问题**：证明 GDN batch-1 解码 memory-bound 是**架构性**而非算法性（所有次二次序列模型解码算术强度 < 1 FLOP/B）。
- **方法**：FPGA 上**持久化状态数据流加速器**，让循环状态常驻片上，避免每 token 往返 HBM。
- **价值**：给出 GDN 加速的硬件范式，适合与 #1（量化）叠加做定制化推理卡。

---

## 三、第二梯队：可迁移的免训练加速（12 篇）

### 量化（PTQ）
- **Quamba2**（ICML 2025 Poster）/ **Quamba / Quamba-SE** — 选择性 SSM 的 PTQ 框架，状态量化思路可直接迁移到 GDN。
- **Q-Mamba**（OpenReview Reject）— 思路参考，质量定位低，勿作为依据。

### 投机解码
- **SpecMamba**（[2509.19873](https://arxiv.org/abs/2509.19873)）— FPGA 上 Mamba 投机解码，生态可迁移。

### 缓存 / 系统
- **AVMP（Asymmetric Virtual Memory Paging）**（[2605.22416](https://arxiv.org/abs/2605.22416)）— KV（线性增长）与 SSM 状态（固定）分池 + 统一虚拟地址，避免统一池对齐造成的 7.3× 容量浪费。
- **DUET**（[2603.15530](https://arxiv.org/abs/2603.15530)）— 混合模型的 prefill/decode 解聚打包。
- **Pimba** — 处理内内存（PIM）加速 post-Transformer 服务。

### 免训练剪枝
- **SparseSSM**（ICLR 2026）— 将 OBS 框架扩展到 SSM，**one-shot 免训练剪枝**状态转移矩阵。

### 硬件协同
- HEMERA / ViM-Q / Mamba-X / eMamba — 边缘 FPGA 软硬协同，工程落地参考。

---

## 四、第三梯队：Transformer → GDN 转换（免训练/低训练）

- **Taylor-Calibrate**（[2606.16429](https://arxiv.org/abs/2606.16429)）— 核心：用 Taylor 展开为 GDN 学生的 decay/write/output-gating 动态做**有原理的初始化**，解决"直接拷贝 teacher 投影导致转换崩坏"。**最值得关注**的转换路线。
- **LoLCATs**（ICLR 2025）— low-rank 线性化，免大规模预训练成本。
- **STILL** — token 级选择做 intra-layer hybrid，线性化。
- **Untangling Component Imbalance** — 修正转换方法的组件失衡。
- **Hybrid Linear Attention Done Right** — 蒸馏 + 极长上下文架构配方。
- **Super Apriel**（[2604.19877](https://arxiv.org/abs/2604.19877)）— 单 checkpoint 多速度档（FA/SWA/KDA/GDN 每层四选一），serving 时免重载切换（需一次性预训练 supernet）。

---

## 五、对照：需重新训练（本任务排除，仅存档）

FG²-GDN、CARVE、QED、Preconditioned DeltaNet、MDN、OSDN、Sparse Delta Memory、DeltaProduct、HOLA、GPN、Kimi Linear(KDA 架构本身)、WriteSAE 等——均属架构/训练创新，不满足"免训练"。

## 六、背景 / 奠基

- **Gated Delta Networks: Improving Mamba2 with Delta Rule**（ICLR 2025）— GDN 起源论文。
- Kimi K3 / Qwen3.8-Next / Solar Open 2 — GDN hybrid 工业落地模型报告。
- 综述：Linear Attention Architectures、On Subquadratic Architectures、A Systematic Analysis of Hybrid Linear Attention。

---

## 七、综合建议（技术路线）

| 优化维度 | 首选论文 | 组合方式 |
|---|---|---|
| 状态带宽/显存 | DAMP(量化) | 与 DeltaLog 叠加：量化降位宽 + 延迟物化降写回 |
| 解码吞吐 | TreeWY(投机) | 与 DASC 组合：投机 + 前缀状态缓存 |
| 算子内核（NPU） | When Good Enough / Triangular Inversion | 求逆 → 纯 MatMul，直接上昇腾 |
| serving 内存 | DASC / AVMP / DUET | 状态检查点压缩 + 分池分页 |
| 硬件 | Persistent-State Accelerator | 状态常驻片上，与 PTQ 叠加 |
| 模型获取 | Taylor-Calibrate | 免训练转为 GDN，再走上面提速 |

---

## 八、开放问题（待精读）

- [ ] DAMP / TreeWY / DASC / DeltaLog / Tail-Replay 五篇为 2026-08 新入库，**性能数字未录入**元数据卡，需精读补全（加速比/精度损耗）。
- [ ] `Super Apriel` 摘要字段在库中缺失，需从 arXiv 原文补。
- [ ] 三角求逆两篇（#5/#6）与昇腾 CANN 现网算子的差距待实测。
- [ ] 状态量化对**召回/长程依赖**的精度下限尚缺公开基准。

---

*生成于 2026-09-05 · 数据源 `inference_optimization_full_tagged.json` / `inference_compression_v8.json` · 命中 GDN 37 + 线性家族 217（去重后）*