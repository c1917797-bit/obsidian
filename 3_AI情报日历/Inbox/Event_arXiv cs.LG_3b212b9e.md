---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.LG
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-02T17:16:33
created: 2026-06-03T15:53:35.738618
tags: [AI-Intelligence, Event, arXiv cs.LG]
---

# Value-Aware Stochastic KV Cache Eviction for Reasoning Models

## 基本信息

- **实体**: arXiv cs.LG
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Reasoning models improve accuracy through extended chains of thought, but their long outputs create a memory and compute bottleneck. KV cache eviction methods reduce this cost by evicting unimportant key-value pairs from the cache, yet they often yield worse accuracy than selection-based sparse attention alternatives, which keep the full KV cache. We identify key factors crucial to KV cache eviction accuracy. First, a small fraction of value states have abnormally large magnitudes, and evicting them causes catastrophic failure where models enter repetitive reasoning loops. Second, introducing stochasticity during eviction improves accuracy by increasing cache diversity. Based on these findings, we propose Value-aware Stochastic KV Cache Eviction (VaSE), a training-free recipe that protects large-magnitude value states and promotes diverse eviction decisions. Across six reasoning tasks, Qwen3 models using VaSE with 4x KV cache compression yield higher average accuracies than SOTA select

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.03928v1

## 来源

arXiv cs.LG

---
**Event ID**: 3b212b9e59a2635f
**Heat Score**: 0.0
**Novelty Score**: 0.0
