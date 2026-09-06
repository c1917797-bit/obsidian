---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.LG
entity_type: project
tech_categories: inference_optimization, runtime_feature
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-02T17:00:15
created: 2026-06-03T15:53:35.751289
tags: [AI-Intelligence, Event, arXiv cs.LG]
---

# MAdam: Metric-Aware Multi-Objective Adam

## 基本信息

- **实体**: arXiv cs.LG
- **类型**: runtime_feature
- **技术分类**: inference_optimization, runtime_feature
- **重要性**: P1
- **阶段**: emerging

## 摘要

Multi-objective optimization (MOO) underlies many machine learning problems, yet MOO solvers across the loss-balancing, gradient-balancing, and Pareto-based families almost universally hand their reconciled directions to Adam~\cite{kingma2015adam}. We show this coupling introduces two systematic gaps between the solver's intent and the optimizer's execution. The first is a \emph{weighting mismatch}: Adam's second-moment denominator entangles the time-varying preference vector with gradient statistics, marginalizing the preference into a history average and collapsing distinct Pareto trade-offs toward a near-uniform mixture. The second is a \emph{geometric mismatch}: Adam's adaptive metric distorts the Euclidean geometry MOO solvers assume, turning aligned objectives into apparent conflicts. To resolve both jointly, we introduce \textbf{MAdam} (Metric-Aware Multi-Objective Adam), a drop-in wrapper that leaves both solver and optimizer unchanged. MAdam preconditions the reconciled direct

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.03904v1

## 来源

arXiv cs.LG

---
**Event ID**: da7ea8e969d5bdb6
**Heat Score**: 0.0
**Novelty Score**: 0.0
