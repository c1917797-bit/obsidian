---
created: 2026-09-25
updated: 2026-09-25
type: paper-deepdive
status: active
tags: [昇腾, 推理优化, prefill-decode, serving, crossflow, agentic]
---
# Crossflow: Prefill-Decode Elasticity for Agentic LLM Serving（深读）

> 来源: arXiv 2609.27085 | 作者: Yi Xu 等 10 人 | 发布: 2026-09-22
> 关联: [[昇腾推理优化候选池]] · [[GDN无损推理加速_全库筛选结论]]（EPD-Serve）

## 一手证据（来自摘要，未核验正文实验细节）

- **动机**：P/D 解聚的收益依赖**静态分区**，但阶段需求不是静态的
  - 大型 LLM fleet：uncached input/output token 比例 peak-to-mean **4.7x**（分钟级）
  - 公共 agentic trace：hourly 比例中位数 **24.5x**/天；replica 重新分配需**数十分钟**
  - 按 P95 配池 → 最多浪费 **17%** 集群容量；低于 P95 → 排队 + 未实现吞吐
- **方法**：边界弹性化，**不改节点角色**。每个 decode 节点发布**短期可撤销 lease**，限定：本地 prefill 计算、KV 容量、传输工作、预估输出
- **结果**（相对静态 P/D）：
  - token 吞吐提升 **16.2–17.4%**（几何均值），高负载最高 **43.4%**
  - 所有评估点平均 TTFT **下降**

## 定量结果

| 指标 | 新方法 | 基线 | 场景 |
|---|---|---:|---|
| Token 吞吐 | +16.2~17.4% (geomean) | 静态 P/D | 公共+内部 traces |
| Token 吞吐（高负载） | 最高 +43.4% | 静态 P/D | 高负载 |
| 集群容量浪费 | ≤17%→回收 | P95 配池 | fleet 级 |
| TTFT | 全点下降 | 静态 P/D | 评估点全覆盖 |
| 需求波动 | peak-to-mean 4.7x / hourly 24.5x | — | agentic |

## 与昇腾的关系

- **先例**：华为昇腾已有 P/D 解聚系统 EPD-Serve（GDN 清单 #6，2601.11590），证明昇腾栈 P/D 解聚可行
- **差异**：EPD-Serve 是静态/固定解聚；Crossflow 是**控制面弹性**（decode 节点可撤销 lease）
- **昇腾等价性**：昇腾栈无 Crossflow 式弹性 lease 的成熟实现 → 符合候选池"昇腾无等价成熟实现"准入

## 昇腾落地路径（分阶段，按候选池 Gate 0-4）

1. **阶段 0 · Profile 需求波动（先行）**
   - 在真实 Qwen3.5-27B serving 上记录 uncached input/output token 比例（分钟级 peak-to-mean）
   - 确认是否 >2x；若需求平稳，此论文优先级下调
2. **阶段 1 · 静态 P/D 基线**
   - 复用/对齐 EPD-Serve 或手动 P/D 拆分，建立同分母基线（Gate 0：冻结模型/镜像/vllm-ascend 版本/dtype/TP/seed）
3. **阶段 2 · Lease 控制面原型**
   - 在 vllm-ascend 调度器加"decode 节点可撤销 lease"语义（本地 prefill 计算/KV 容量/传输/预估输出四维约束）
   - 最小正确性验证（Gate 1 smoke + Gate 1b warm steady-state）
4. **阶段 3 · 完整验证**
   - Gate 2 全数据集 sentinel（p50/p95/p99 TTFT/TPOT/E2E、吞吐、空输出率）
   - Gate 3 参考质量（LongBench-v2/GSM8K）+ Gate 4 full Go（1/5/8/16 ×3）
   - 独立 raw-artifact 审计 + 激活证据（lease 确实进入 hot path）

## 关键挑战

- **工程面**：需改调度控制面，非单一算子；与 vllm-ascend scheduler 深度耦合
- **可撤销 lease 的正确性**：lease 撤销时的 in-flight 请求处理（避免违反"生产基线隔离"原则）
- **激活证据要求**（LESSONS_LEARNED §7.2）：配置开启 ≠ 进入 hot path，需要 planner/scheduler 级证明

## 下一步

- [x] 深读摘要（正文未核验）
- [ ] 阶段 0 profile：真实 workload 需求波动测量
- [ ] 对照 EPD-Serve 实现，确认昇腾 P/D 控制面接口
- [ ] 决定：进入阶段 1（若波动 >2x）

*生成于 2026-09-25 · 关联：[[昇腾推理优化候选池]] · [[AI推理简报_2026-09-25]]*
