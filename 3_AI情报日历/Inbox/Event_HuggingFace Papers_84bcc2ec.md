---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: agent_runtime, memory
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-12T04:09:54.879880
created: 2026-06-12T04:10:17.654055
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: agent_runtime, memory
- **重要性**: P1
- **阶段**: emerging

## 摘要

Vision-language models (VLMs) project images into hundreds to thousands of visual tokens, making decoder inference expensive in both attention computation and KV-cache memory. Existing visual-token reduction methods largely follow a rank-and-remove paradigm: they score visual tokens, keep a compact subset, and permanently discard the rest. We show that this irreversible action is fragile because visual-token importance changes across decoder depth; tokens ranked low at one stage may become relevant in later layers, especially for grounding-sensitive queries. We propose Reroute, a training-free plug-in that replaces removal with recoverable routing. At each routing stage, selected vision tokens pass through decoder blocks, while deferred tokens bypass the stage and re-enter the candidate pool at the next routing decision. Reroute reuses existing attention-score ranking rules and stage-wise schedules, preserving the theoretical TFLOPs and KV-cache budget class of the pruning method it au

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.12412

## 来源

HuggingFace Papers

---
**Event ID**: 84bcc2ec88e298bb
**Heat Score**: 0.0
**Novelty Score**: 0.0
