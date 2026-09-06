---
type: tech-event
event_type: research_paper
entity: HuggingFace Papers
entity_type: project
tech_categories: research, architecture
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-26T04:13:09.681223
created: 2026-06-26T04:14:14.650188
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# One Model, Many Latencies: Universal Speech Enhancement for Diverse Real-Time Applications

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: research_paper
- **技术分类**: research, architecture
- **重要性**: P1
- **阶段**: emerging

## 摘要

Different real-time speech applications impose distinct latency budgets, often requiring separately trained enhancement models for each scenario. In this paper, we propose a one-for-all, real-time universal speech enhancement model that provides explicit control over both algorithmic and computational latency. Algorithmic latency is flexibly adjusted via configurable look-ahead frames. To avoid learning inefficiency caused by varying padding configurations, we introduce parallel convolutional layers corresponding to different look-ahead settings. Computational latency is controlled through an early-exit mechanism, enabling inference at different network depths. To narrow the performance gap between specialized and flexible models, we propose a two-stage training strategy with a shared-to-multiple decoder transition. Overall, the proposed framework enables a single model to be deployed across diverse latency budgets without retraining separate models.

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.25621

## 来源

HuggingFace Papers

---
**Event ID**: 62b2e7516b1dd0b0
**Heat Score**: 0.0
**Novelty Score**: 0.0
