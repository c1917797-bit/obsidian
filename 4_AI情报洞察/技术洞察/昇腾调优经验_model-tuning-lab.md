---
created: 2026-09-25
updated: 2026-09-25
type: experience-card
status: active
tags: [昇腾, 调优经验, model-tuning-lab, 方法论]
source: "C:\Users\Huawei\Downloads\model-tuning-lab-main\model-tuning-lab-main\docs"
---
# 昇腾调优经验（model-tuning-lab 沉淀）

> 来源：Model Tuning Lab（Ascend 910B4 / Qwen 推理 / vLLM-Ascend）实测沉淀。
> 用途：论文筛选、实验设计、验收的常驻规则。关联 [[昇腾推理优化候选池]]。

## 论文筛选（Paper-to-Ascend）

1. **架构适用性是选论文前的 gate**（§6.3）：先证明已装模型含所需机制 + 方法命中已观察瓶颈，再花 NPU 时间；dense 优先 exact speculative/MTP、attention/KV/decode 改进、无需重训练的 inference-time 技术
2. **端到端测量**（§6.1）：理论计算削减 ≠ 端到端赢。实测：Dynamic MoE 的 GMM 快 8.85%，但路由开销 6.36x 慢，整体延迟退化 82-96%
3. **scope 分离**（§6.2）：implementation / operator-block / full-model 三个决策范围不得越级推广；负结果只覆盖其真实证据范围

## 实验设计

4. **分母命名**（§7.1）：A/B 必须 same-denominator；不同机制分开记账（HYPIC-only vs no-cache、PDC-only 等）
5. **hot-path 激活证据**（§7.2）：配置开关/import 日志 ≠ 进入 hot path；需 planner/scheduler/worker 级激活证明
6. **容量算术**（§7.3）：admission budget 必须覆盖全物理需求（private suffix、seam/sink、block 对齐、workspace、保留 token）
7. **设备映射是实验身份**（§7.4）：host/container NPU ID 分开记录，TP 度证明后再测量
8. **性能与质量是独立契约**（§7.5）：`ignore_eos`/thinking/缓存/采样式状态分阶段；性能采样与确定性质量采样分开，阶段间重启同臂

## 测量与指标

9. **p95 为主指标**，p50 典型，p99/max 尾部；单独报告 TTFT/TPOT/输出 tok/s/E2E/完成 token 分布
10. **更短输出 ≠ 更快引擎**：提前终止/少 token 是模型行为，不是推理加速
11. **冷启动/编译污染**：先 warm 同并发，等 bisheng/hivmc/clang 编译安静后再测量
12. **生产基线隔离**：服务漂移（ablation runner 改动）即拒绝作 baseline，重新隔离
13. **环境定向先行**：性能证据始于精确硬件/软件/模型/命令/topology/目标设备证明；检查 HugeTLB、容器内 profiling 工具（torch_npu.profiler/msprof/asys），上游 CANN 源码须匹配已装 CANN release

## 验收与审计

14. **分阶段 admission**（Gate 0-4）：身份冻结 → 生产代表 smoke → warm steady-state → 全数据集 sentinel → 早期参考质量 → full Go（1/5/8/16 ×3 + 完整质量重复 + 运维稳定性）
15. **完成 = 独立 raw-artifact 审计**（§7.7）：不因渲染报告/文件存在就接受；operational failure ≠ algorithm failure（§7.8）
16. **长运行按验证单元续跑**：JSONL 稳定索引 + ok 状态 + 哈希，绝不平均部分行
17. **质量证据必须带 reference**：空 answer 数据集只测延迟/终止行为，不得声称准确率

## 禁止清单

- 修改 raw 输出以通过验证
- SHA/协议漂移后重跑
- 无 reference 数据声称质量
- 单指标/单 cell 推荐生产切换
- lab Go 后自动改生产配置（需 canary/A-B）
- 凭 HBM 算术单判模型可行性（是系统容量问题，非 HBM-only 数学）

## 与候选池的关系

候选池"筛选标准"一节即本卡浓缩版；本卡保留完整规则与出处。

*生成于 2026-09-25 · 关联：[[昇腾推理优化候选池]] · [[GDN无损推理加速_全库筛选结论]]*
