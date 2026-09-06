---
type: tech-event
event_type: runtime_feature
entity: arXiv Top Conf Recent (Inference Compression)
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-07-01T10:44:57
created: 2026-07-05T13:44:32.200187
tags: [AI-Intelligence, Event, arXiv Top Conf Recent (Inference Compression)]
---

# MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression

## 基本信息

- **实体**: arXiv Top Conf Recent (Inference Compression)
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Long-context LLM services now sustain prompts with hundreds of thousands to millions of tokens, making the key-value (KV) cache a first-order serving cost. Because the cache grows linearly with context length, it can exhaust GPU memory, force smaller batches, and reduce serving throughput. Prior KV cache compression techniques typically target only the sequence dimension or only the channel dimension, which leaves limited headroom as context windows scale. Compressing both dimensions promises higher memory reduction, but applying the two forms of compression directly leads to significant accuracy loss.
  This paper introduces MosaicKV, a dynamic two-D (dimensional) KV cache compression system for extremely long-context serving. MosaicKV uses dynamic two-D compression to address the accuracy challenge, exploiting the non-uniform importance distribution of elements within the KV cache. Instead of applying one compression pattern globally, MosaicKV identifies important elements for each K

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2607.00760v1

## 来源

arXiv Top Conf Recent (Inference Compression)

---
**Event ID**: bfa2db096d46222b
**Heat Score**: 0.0
**Novelty Score**: 0.0
