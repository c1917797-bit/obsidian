---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.LG (Inference Compression Keywords)
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-25T06:56:43
created: 2026-06-26T04:14:14.765021
tags: [AI-Intelligence, Event, arXiv cs.LG (Inference Compression Keywords)]
---

# PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs

## 基本信息

- **实体**: arXiv cs.LG (Inference Compression Keywords)
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Autoregressive large language model (LLM) serving is increasingly limited by key-value (KV) cache movement rather than dense matrix multiplication. Modern paged-attention systems reduce KV-cache fragmentation and mature kernels such as FlashInfer provide highly optimized native-paged decode attention. However, the best single-kernel implementation is not always the best serving schedule: low-active long-context decode can under-utilize commodity GPUs, while mixed sequence lengths introduce a tension between many exact-length launches and coarse padded batches. We present PersistentKV, a native block-table decode attention engine and page-aware scheduling study for grouped-query attention (GQA). PersistentKV maps work by KV-head group, is designed to reuse K,V tiles across grouped query heads, supports native page tables, and adds a compact workqueue schedule that executes only non-empty row-KV-head-sequence-split tasks. On an RTX 3060 with FP16, page size 16, Hq=32, Hkv=8, d=128, and i

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.26666v1

## 来源

arXiv cs.LG (Inference Compression Keywords)

---
**Event ID**: bb185d3df3ef4661
**Heat Score**: 0.0
**Novelty Score**: 0.0
