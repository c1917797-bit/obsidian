---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: cost_optimization, moe
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-12T04:09:54.879880
created: 2026-06-12T04:10:17.654055
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Redesign Mixture-of-Experts Routers with Manifold Power Iteration

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: cost_optimization, moe
- **重要性**: P1
- **阶段**: emerging

## 摘要

Router is the cornerstone component to the Mixture-of-Experts models. Serving as expert proxies, the rows of the router matrix compute their similarity to the MoE inputs to determine which subset of experts is activated. Ideally, each router row is designed to encode the expert matrix into this representative vector, such that its dot-product with token can better reflect token-expert affinity. However, there exists no design principles to enforce this condensation. In this paper, we propose to align each router row with the principal singular direction of the associated expert, as this direction provides the most expressive mathematical description of a matrix. Based on this principle, we propose a router redesign with Manifold Power Iteration (MPI). Specifically, it introduces a "Power-then-Retract" paradigm, where a power iteration step is performed on the router weights, followed by a retraction to impose a norm constraint to ensure both efficiency and stability. Theoretically, we 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.12397

## 来源

HuggingFace Papers

---
**Event ID**: 67da8e5a6fbe044f
**Heat Score**: 0.0
**Novelty Score**: 0.0
