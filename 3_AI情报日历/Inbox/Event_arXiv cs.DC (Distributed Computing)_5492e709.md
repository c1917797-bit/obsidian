---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: agent_runtime, memory
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-08T15:38:16
created: 2026-06-10T04:10:32.741150
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# FMplex: Model Virtualization for Serving Extensible Foundation Models

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: runtime_feature
- **技术分类**: agent_runtime, memory
- **重要性**: P1
- **阶段**: emerging

## 摘要

Foundation models (FMs) are increasingly used as backbones for downstream tasks across language, vision, time-series, and multimodal applications. Yet existing model-serving systems deploy each customized task as an independent model instance, thereby replicating heavyweight backbones, wasting accelerator memory, and losing opportunities to amortize batching and loading costs. This paper presents FMplex, a serving system that treats FM backbones as a virtualization substrate for deployment sharing. FMplex presents each task with a virtual foundation model (vFM), a logically private FM instance backed by a shared physical FM. This abstraction lets independently customized tasks share a backbone while preserving task-specific extensions, independent lifecycles, and task-level isolation. In addition, we propose a batch-aware fair-queueing scheduler that combines weighted task-level sharing with inter- and intra-task batching across colocated tasks. We implement a FMplex-based serving stac

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.09643v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: 5492e709fbc4371d
**Heat Score**: 0.0
**Novelty Score**: 0.0
