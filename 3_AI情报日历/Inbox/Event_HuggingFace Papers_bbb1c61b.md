---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: inference_optimization, speculative_decoding
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-26T04:13:09.681223
created: 2026-06-26T04:14:14.655494
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: inference_optimization, speculative_decoding
- **重要性**: P1
- **阶段**: emerging

## 摘要

Tool Calling and Structured Output are two core capabilities of modern Agent systems, yet their interaction under joint deployment conditions remains insufficiently understood. This paper reports a reproducible phenomenon observed in a production Agent system: when Tool Calling and JSON Schema constraints are simultaneously enabled, multiple open-weight models cease invoking tools despite maintaining high schema compliance. We refer to this behavior as Tool Suppression. Through controlled experiments across multiple model families and deployment settings, we consistently reproduce Tool Suppression under joint constraints, while tool execution and schema compliance remain functional when evaluated independently. Further analysis reveals that JSON Schema constraints are compiled into grammar-based token masks, causing tool-call tokens to become unreachable during decoding. This provides an implementation-level explanation for the observed behavior. To interpret the phenomenon, we formula

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.25605

## 来源

HuggingFace Papers

---
**Event ID**: bbb1c61b3a009253
**Heat Score**: 0.0
**Novelty Score**: 0.0
