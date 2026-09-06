---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: inference_optimization, speculative_decoding
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-18T03:21:32
created: 2026-06-20T11:09:35.179923
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: runtime_feature
- **技术分类**: inference_optimization, speculative_decoding
- **重要性**: P1
- **阶段**: emerging

## 摘要

The scaling of LLMs toward long-context inference has shifted the primary serving system bottleneck from computation to memory capacity. Traditional solutions for dense attention models rely on RDMA-based disaggregated memory pools, which perform coarse-grained fetching of the entire prefix KV cache from remote storage to local memory before decoding. However, this approach is fundamentally inefficient for emerging sparse attention models. While only a small fraction of KV entries are active during decoding, these systems still fetch the full KV cache locally, leading to severe transmission bottlenecks and local memory wastage. To address this, we propose SAC, the first efficient disaggregated KV cache system optimized for sparse attention models. By leveraging the low-latency, cache-line granularity load/store semantics of Compute Express Link (CXL), SAC fetches only the required top-k KV entries on demand during inference. Evaluations on DeepSeek-V3.2 using SGLang show that SAC achie

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.19746v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: 28354e27ac86b7d7
**Heat Score**: 0.0
**Novelty Score**: 0.0
