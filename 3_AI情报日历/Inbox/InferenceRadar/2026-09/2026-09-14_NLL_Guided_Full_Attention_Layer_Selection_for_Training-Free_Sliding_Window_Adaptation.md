---
type: inference-signal
date: 2026-09-14
discovered: 2026-09-14T09:18:00
source_published: 2026-06-30
source_type: arxiv
primary_source: "https://arxiv.org/abs/2606.27791"
topic: inference-compression
status: candidate
evidence_score: 3
relevance_score: 4
impact_score: 3
novelty_score: 3
urgency_score: 2
reproducibility_score: 3
overall_score: 3.1
confidence: medium
decision: verify
tags: [AI推理, radar, hybrid-attention, qwen3.5, no-training]
---

# NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation

## 一手证据
- 标题：NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation
- 链接：`https://arxiv.org/abs/2606.27791`
- 当前可复用信息：论文核心为“训练后层级选择策略 + 推理阶段全注意力层保留策略”。

## 关键字段对齐（与 `paper_decision_card` / `paper-experiment-contract`）
- paper_decision_card
  - 痛点：全注意力层与长上下文滑窗注意力在精度与推理吞吐间难平衡。
  - Idea：用 NLL 指标驱动的训练后层筛选，决定每层保留 full-attention 的比例。
  - 目标：减少 decode + prefill 代价，保留精度。
  - 适用性：目标模型为已含混合注意力/多机制注意力结构时可优先尝试。
- paper-experiment-contract
  - 验证问题：在固定硬件 + 固定 Qwen3.5 27B 配置下，是否可稳定拿到 >=10% 的 TPOT 或 TTFT 下降。
  - 对照组：完整 attention 路径 vs 层选择路径。
  - 成功判据：质量指标下降不超过既定阈值（需你给定，如 PPL/任务精度/长文本指标），同时 TTFT/TPOT 同时改善且可重复。

## 执行摘要（建议）
该方法是当前“无需训练”优先路径中与 Qwen3.5 更接近的一类。先级建议：高。  
优先做小规模开关实验（A/B）确认可落地性，再决定是否纳入周报。

## 下一步实验（10 条约束）
1. 固定 hardware = 昇腾机型、固定 CANN/CANN2 版本
2. 固定模型 = Qwen3.5-27B（GDN）与同款 dense baseline
3. 固定任务组 = 长上下文/长尾、编码+生成混合样本
4. 指标 = TTFT、TPOT、吞吐、显存、质量（Top-k perplexity 或端到端任务集）
5. 输出 = 层保留策略、误差曲线、速度收益率和精度退化率

