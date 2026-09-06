---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.MA (Multiagent Systems)
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-11T13:47:33
created: 2026-06-12T04:06:17.324817
tags: [AI-Intelligence, Event, arXiv cs.MA (Multiagent Systems)]
---

# Can I Buy Your KV Cache?

## 基本信息

- **实体**: arXiv cs.MA (Multiagent Systems)
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Right now, across the world, AI agents are repeating the same absurd act: to read one document, they each recompute it from scratch. Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built. The same answer, computed a million times. We make a proposal that is almost offensively simple: compute it once. Let a publisher precompute a document's KV cache, and let every other agent buy the right to load it and skip prefill. It works, and it is token-exact: loading a precomputed KV and continuing matches prefilling from scratch (24/24 greedy tokens, and at the logits level), with no accuracy cost. On Qwen3-4B, reuse is 9-50x cheaper in compute than prefill, and the gap widens with length (prefill's attention scales with L^2), so a single reuse already pays it back. Then the part that matters: where the KV lives. Shipping it fails, because KV is nearly inco

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.13361v1

## 来源

arXiv cs.MA (Multiagent Systems)

---
**Event ID**: d4cee9d3f76f0393
**Heat Score**: 0.0
**Novelty Score**: 0.0
