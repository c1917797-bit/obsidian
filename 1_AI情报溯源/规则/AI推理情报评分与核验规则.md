---
created: 2026-09-06
updated: 2026-09-06
type: verification-rules
status: active
tags: [AI推理, evidence, scoring]
---
# AI 推理情报评分与核验规则

## 证据分

0 无来源；1 二手/营销/仅摘要；2 官方公告但无可审计数据；3 论文或官方报告且实验条件完整；4 另有代码和可复现实验；5 有独立复现或标准 benchmark。

缺少一手 URL、实验条件或精确指标时，不得写“突破”“领先”“显著提升”，只能标为线索。

## 价值分

relevance、impact、novelty、urgency、reproducibility 均为 0–5。  
overall = evidence×0.30 + impact×0.25 + novelty×0.20 + relevance×0.15 + urgency×0.10。

- P0：overall ≥ 4.0 且 evidence ≥ 3，立即深读或复现。
- P1：overall ≥ 3.2 且 evidence ≥ 2，本周核验。
- P2：overall ≥ 2.4，观察。
- Noise：低于 2.4 或偏离推理主线。
- Blocked：缺一手来源、实验条件或存在矛盾。

## 性能 claim 最小字段

model、precision、hardware/count、batch/concurrency、input/output tokens、framework version/commit、TTFT、TPOT、throughput、peak memory、cost/energy、baseline、quality delta。

## 准确性红线

标题摘要只用于初筛；厂商自测只证明披露条件下成立；高影响结论需要一手原文加代码、独立复现或第二份一手材料；论文身份和录用状态单独核验；0 条证据禁止生成完整报告；矛盾证据设为 blocked。