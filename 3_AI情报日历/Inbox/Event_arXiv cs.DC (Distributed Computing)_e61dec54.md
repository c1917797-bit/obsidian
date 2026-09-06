---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: agent_runtime, memory
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-18T09:29:28
created: 2026-06-20T11:09:35.174705
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# Online Dynamic Batching with Formal Guarantees for LLM Training

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: runtime_feature
- **技术分类**: agent_runtime, memory
- **重要性**: P1
- **阶段**: emerging

## 摘要

Modern LLM training breaks a core assumption behind offline batch samplers: the true training cost of a sample is only observable after preprocessing, augmentation, templating, tokenization, and multimodal visual-token expansion. Unless one pays for a preprocessing- and augmentation-dependent length cache, batch construction is therefore blind to the quantity that determines padding, memory use, and GPU saturation. We introduce Online Dynamic Batching (ODB), a DataLoader-side drop-in system that moves batch formation to this point of accurate observability while preserving DDP step alignment. We formalize this synchronization requirement as the Distributed Group Alignment Problem and prove deadlock-free bounded termination with default join-mode identity coverage and opt-in non-join sample-quota closure. ODB requires no model, optimizer, or attention-kernel changes and is released as online-dynamic-batching with lightweight trainer adapters. Across public 2B/8B Qwen3-VL runs on UltraCh

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.19989v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: e61dec540149d56b
**Heat Score**: 0.0
**Novelty Score**: 0.0
