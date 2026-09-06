---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: inference_optimization, runtime_feature
importance: P1
confidence: 0.6
stage: emerging
date: 2026-07-05T13:40:19.957719
created: 2026-07-05T13:44:32.144344
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# From SRA to Self-Flow: Data Augmentation or Self-Supervision?

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: inference_optimization, runtime_feature
- **重要性**: P1
- **阶段**: emerging

## 摘要

Representation alignment has become an effective way to accelerate diffusion transformer training and improve generation quality. Recent self-alignment methods, such as SRA and Self-Flow, further remove the dependency on external pretrained encoders by constructing alignment within the diffusion model itself. However, the mechanism behind the improvement from SRA to Self-Flow, dual-time scheduling, remains under-examined: Self-Flow attributes its gain to interactions between tokens at different noise levels, where cleaner tokens help infer noisier ones. In this work, we revisit this explanation and ask whether the gain instead comes from data augmentation along the noise dimension. To disentangle these factors, we introduce Attention Separation, which preserves the same dual-timestep input as Self-Flow while blocking attention between tokens assigned to different noise levels. Surprisingly, removing such interaction does not degrade performance and can even improve it, suggesting that 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2607.02508

## 来源

HuggingFace Papers

---
**Event ID**: 139c748c79531c5e
**Heat Score**: 0.0
**Novelty Score**: 0.0
