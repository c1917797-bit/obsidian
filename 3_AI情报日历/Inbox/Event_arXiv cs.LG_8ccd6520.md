---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.LG
entity_type: project
tech_categories: inference_optimization, quantization
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-18T16:54:07
created: 2026-06-20T11:09:35.152158
tags: [AI-Intelligence, Event, arXiv cs.LG]
---

# UltraQuant: 4-bit KV Caching for Context-Heavy Agents

## 基本信息

- **实体**: arXiv cs.LG
- **类型**: runtime_feature
- **技术分类**: inference_optimization, quantization
- **重要性**: P1
- **阶段**: emerging

## 摘要

Context-heavy agents place unusual pressure on the key-value (KV) cache: long prefixes are reused across many short turns, while concurrency determines whether the serving system can keep GPUs utilized. We study 4-bit KV-cache compression for this setting, using TurboQuant-style rotation and codebook quantization as a quality anchor and vLLM FP8 KV caching as the deployment anchor. We report three contributions. First, we frame 4-bit KV caching around multi-round agent workloads where task quality, cache residency, and serving throughput must be measured jointly. Second, we describe the practical design choices needed to make the 4-bit path robust, including asymmetric K/V treatment, Walsh-Hadamard rotation, QJL removal, and block-scale variants. Third, we present serving optimizations on AMD GPUs, including optimized decode-attention kernels and UltraQuant, an FP4 approximation path that uses FP8 queries, FP4 KV tensors, UE8M0 group scales, and native scaled-MFMA support on CDNA4. On 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.20474v1

## 来源

arXiv cs.LG

---
**Event ID**: 8ccd6520953370b2
**Heat Score**: 0.0
**Novelty Score**: 0.0
