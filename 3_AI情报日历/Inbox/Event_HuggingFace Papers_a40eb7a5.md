---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-09T11:00:04.530064
created: 2026-06-09T11:01:17.912851
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Visual Para-Thinker++: A Single-Policy Multi-Agent Framework for Visual Reasoning

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Visual reasoning requires integrating evidence distributed across regions, attributes, and relations, making single-chain reasoning prone to early perceptual commitment and hallucination. We propose Visual Para-Thinker++, a single-policy multi-agent framework in which one shared MLLM policy is instantiated as role-conditioned Main, Worker, and Summary Agents. The Main Agent decomposes the task with fixed allocation patterns; Worker Agents reason in parallel under context isolation; and the Summary Agent reconciles full Worker reasoning traces rather than majority-voting on final labels. The shared policy is trained by Multi-Agent Capability Injection and Role-Decoupled Multi-Agent Optimization, which assign role-specific rewards and advantages to corresponding token segments to reduce gradient conflict among collaborative roles. A native inference engine enables efficient multi-agent rollout through shared visual prefix and KV cache reuse. Across V*, CountBench, the RefCOCO family, and

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.09290

## 来源

HuggingFace Papers

---
**Event ID**: a40eb7a5c3794672
**Heat Score**: 0.0
**Novelty Score**: 0.0
