---
created: 2026-09-11
updated: 2026-09-11
type: insight-report
status: active
tags: [codex, gdn, 推理优化, 无损加速, 论文筛选, qwen3.5-27b, ascend]
---

# GDN 无损推理加速 · 全库筛选结论与论文清单

> 目标：Qwen3.5-27B（48 层 GDN 混合）· Ascend 910B4 · 物理 0–3 卡 TP4
> 硬约束：不改权重、不重训、不量化、不删层/token、不用 MTP/投机解码、零实质精度回退
> 验收：TTFT P95 降 ≥40%、TPOT P95 降 ≥20%

---

## 一、筛选标准（精简）

1. 硬性准入：适配 Qwen3.5-27B 实际结构 + Ascend 910B4/TP4 + 无损 + 公开源码 + 可改可商用 License + 昇腾栈无等价成熟实现 + 独立插件可回滚 + 正式会议优先。
2. 命中真实瓶颈：明确改善 Prefill / Decode / 通信 / 调度中的哪条，覆盖真实 shape/dtype/layout/TP 分片。
3. 先算收益上限：整体延迟降低 ≈ `f × (1 − 1/s)`；f<5% 直接淘汰。
4. 工程可行性：最小算子入口、不依赖昇腾缺失硬件、保持现有接口、可独立验证。
5. 验证顺序固定：源码适配审查 → 收益准入 → 最小正确性 → 完整算子链 → 服务激活 → c1/c16 筛选 → 全 357 条配对精度。
6. 排序：真实瓶颈匹配 ＞ 可实现的净收益 ＞ 源码完整度/迁移成本 ＞ 正式会议证据 ＞ 发布时间。

---

## 二、全库检索结果

| 步骤 | 数量 |
|---|---|
| 全库去重论文 | 33,760 |
| 排除量化/剪枝/稀疏/蒸馏/低秩/投机/早退（违反无损约束） | − |
| 无损服务加速候选 | 659 |
| 待核验（值得上 Qwen3.5-27B 验证） | 6 |
| 可立项 | **0**（无一篇给出 Ascend/Qwen 真实 profile 证据） |

---

## 三、结论：值得验证的 6 篇（全无损）

| # | 论文 | 来源 | 命中瓶颈 |
|---|---|---|---|
| 1 | KVBuffer: IO-aware Serving for Linear Attention | [arXiv 2605.19049](https://arxiv.org/abs/2605.19049) | GDN decode 状态 IO |
| 2 | DeltaLog: Deferred Materialization of Recurrent States | [arXiv 2608.15533](https://arxiv.org/abs/2608.15533) | GDN decode 状态写回 |
| 3 | Fast and Stable Triangular Inversion for Delta-Rule Linear Transformers | [arXiv 2605.21325](https://arxiv.org/abs/2605.21325) | Prefill 三角求逆 |
| 4 | LASP-2: Sequence Parallelism for Linear Attention and its Hybrid | OpenReview `c6TDOPEQ0e` | TP 通信 / 长上下文 |
| 5 | Scaling State-Space Models on Multiple GPUs with Tensor Parallelism | [arXiv 2602.21144](https://arxiv.org/abs/2602.21144) | TP4 分片 |
| 6 | EPD-Serve: … Disaggregation Serving System On Ascend | [arXiv 2601.11590](https://arxiv.org/abs/2601.11590) | P/D 解聚（TTFT） |

## 四、排除的 GDN 热门论文（违反硬约束）

| 论文 | 来源 | 排除原因 |
|---|---|---|
| DAMP: Recurrent-State Quantization | [2608.27513](https://arxiv.org/abs/2608.27513) | 量化 |
| When Good Enough Is Optimal (Matrix Inversion Approximation) | [2606.06034](https://arxiv.org/abs/2606.06034) | 近似（精度损失） |
| DASC: Decay-Aware State Compression | [2608.30386](https://arxiv.org/abs/2608.30386) | 有损压缩 |
| TreeWY: Speculative Verification for GDN Hybrids | [2608.20961](https://arxiv.org/abs/2608.20961) | 投机解码 |
| A Persistent-State Dataflow Accelerator (FPGA) | [2603.05931](https://arxiv.org/abs/2603.05931) | FPGA 非昇腾 ASIC |
| Ladder Residual / Ladder-Residual | OpenReview `6R4TGPd74N` / `bJnSplWSCL` | 改残差需重训 |

## 五、备选参考（无损，二级优先级）

| 论文 | 来源 |
|---|---|
| KVPR: I/O-Aware KV Cache Partial Recomputation | ACL Findings 2025 `2025.findings-acl.997` |
| Scaling LLM Inference Beyond Amdahl's Limits | [2606.01927](https://arxiv.org/abs/2606.01927) |
| Untied Ulysses: Context Parallelism via Headwise Chunking | [2602.21196](https://arxiv.org/abs/2602.21196) |
| Compiler-First State Space Duality & O(1) Caching | [2603.09555](https://arxiv.org/abs/2603.09555) |
| DUET: Disaggregated Hybrid Mamba-Transformer | [2603.15530](https://arxiv.org/abs/2603.15530) |

---

## 六、下一步（验证顺序）

1. **先 profile** Qwen3.5-27B（Ascend 910B4、TP4），确认三条路径谁占关键路径：
   - ① GDN decode 状态写回（48 层 GDN，<1 FLOP/B，最可能）
   - ② TP4 通信（FFN all-reduce / attention）
   - ③ Prefill chunkwise 三角求逆
   - ④ 服务级 P/D 解聚
2. 若 ① 占大头 → 只验 **KVBuffer + DeltaLog**。
3. 每篇按：源码适配审查（维度/GQA/BF16/CANN 可跑/License）→ 收益准入（f×）→ 最小正确性 → 完整算子链 → 服务激活。

## 待验证问题

- [ ] Qwen3.5-27B 是否真为 GDN 混合、GDN 层数/状态维度/TP 分片方式待确认
- [ ] KVBuffer / DeltaLog 是否纯 PyTorch/CANN 可跑（不依赖 CUDA 专有算子）
- [ ] 各候选的 License 是否允许修改、分发与商业使用
- [ ] 三/四条瓶颈路径的实际占比 f 未测

---

*生成于 2026-09-11 · 关联：[[GDN模型免训练推理加速_论文系统解读报告]] · [[📋_目录导航]]*
