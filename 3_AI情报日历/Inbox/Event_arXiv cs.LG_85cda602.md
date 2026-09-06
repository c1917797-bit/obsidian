---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.LG
entity_type: project
tech_categories: inference_optimization, runtime_feature
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-02T17:27:48
created: 2026-06-03T15:53:35.732039
tags: [AI-Intelligence, Event, arXiv cs.LG]
---

# q0: Primitives for Hyper-Epoch Pretraining

## 基本信息

- **实体**: arXiv cs.LG
- **类型**: runtime_feature
- **技术分类**: inference_optimization, runtime_feature
- **重要性**: P1
- **阶段**: emerging

## 摘要

Multi-epoch training is becoming the standard now that compute is growing faster than the supply of high-quality text. But pretraining a single model saturates within a few passes, long before the compute budget is exhausted. We argue this calls for a conceptual shift from training a single model toward exploring a population of models and aggregating their predictions. We introduce hyper-epoch pretraining (q0), which turns a multi-epoch budget into a population of diverse models whose combined predictions reach a lower validation loss than a single refined model. q0 reduces to three core primitives. A cyclic schedule with anti-correlated learning rate and weight decay collects diverse models from a few parallel trajectories. Chain distillation trains each model against its predecessor so that model quality compounds across the population. A learned prior, fit on a held out set, selects and weights members for any inference budget. On a 1.8B-parameter model trained on 100M FineWeb toke

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.03938v1

## 来源

arXiv cs.LG

---
**Event ID**: 85cda602cdb6debd
**Heat Score**: 0.0
**Novelty Score**: 0.0
