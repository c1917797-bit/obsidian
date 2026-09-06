---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: inference_optimization, kv_cache
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-07T13:57:05
created: 2026-06-10T04:10:32.752366
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: runtime_feature
- **技术分类**: inference_optimization, kv_cache
- **重要性**: P1
- **阶段**: emerging

## 摘要

Prefill-decode (PD) disaggregation decouples prompt processing from token generation, but it also turns the key-value (KV) cache into a network payload. Existing PD-side KV reduction methods are mostly binary: selected tokens are transmitted at full precision and the rest are not transmitted. This paper argues that binary selection leaves a useful design space unused. SpectrumKV assigns a precision level to each token instead: attention sinks and other high-importance tokens are protected at FP16, medium-importance tokens are sent at INT8, and low-importance tokens are sent at INT4 when the model can tolerate it. The main practical complication is that INT4 tolerance is model-dependent. Qwen2.5-7B catastrophically fails under INT4 KV quantization, while Mistral-7B and Gemma-2-9B remain stable. SpectrumKV therefore runs a lightweight deployment-time probe: three aggressive NIAH trials under a 3-tier policy. Models that pass use FP16+INT8+INT4; models that fail fall back to FP16+INT8. Ac

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.08635v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: b28a017edc626664
**Heat Score**: 0.0
**Novelty Score**: 0.0
