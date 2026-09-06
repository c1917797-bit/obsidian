---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.LG
entity_type: project
tech_categories: cost_optimization, moe
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-23T12:34:09
created: 2026-06-24T12:14:40.340485
tags: [AI-Intelligence, Event, arXiv cs.LG]
---

# CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation

## 基本信息

- **实体**: arXiv cs.LG
- **类型**: runtime_feature
- **技术分类**: cost_optimization, moe
- **重要性**: P1
- **阶段**: emerging

## 摘要

Emerging LLM services increasingly host many sparse MoE models, yet most models receive sparse requests and remain cold. This creates a GPU memory problem: model weights are stable and model-determined, while KV-cache is transient and demand-determined. Because cold models rarely reach peak KV-cache demand at the same time, reserving worst-case KV capacity per model wastes memory; a shared KV-cache pool can instead provision aggregate active demand. However, KV-cache sharing is not sufficient when weights and KV-cache remain in a monolithic GPU memory pool. Static weights compete with dynamic KV-cache, and KV-head-limited attention under cold, low-concurrency traffic exposes only a fraction of replicated KV capacity, leading to low GPU memory utilization and weak long-context support. We present CrossPool, a serving engine for cold MoE models that separates FFN weights and KV-cache into two GPU memory pools: a weights pool that consolidates FFN weights across cold models, and a KV-cach

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.24506v1

## 来源

arXiv cs.LG

---
**Event ID**: 8fa474af317baaa6
**Heat Score**: 0.0
**Novelty Score**: 0.0
