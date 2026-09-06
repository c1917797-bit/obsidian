---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.CL
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-08T15:43:16
created: 2026-06-09T11:01:17.939449
tags: [AI-Intelligence, Event, arXiv cs.CL]
---

# End-to-End Context Compression at Scale

## 基本信息

- **实体**: arXiv cs.CL
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pr

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.09659v1

## 来源

arXiv cs.CL

---
**Event ID**: 5e942ab8ea6e57a4
**Heat Score**: 0.0
**Novelty Score**: 0.0
