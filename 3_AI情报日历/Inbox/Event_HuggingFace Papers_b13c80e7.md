---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: inference_optimization, quantization
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-20T10:57:25.408092
created: 2026-06-20T11:09:35.129419
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: inference_optimization, quantization
- **重要性**: P1
- **阶段**: emerging

## 摘要

FP4 training promises substantial reductions in memory and computation cost for LLM pretraining, yet current FP4 hardware paths and recipes, including NVIDIA Blackwell/Rubin-class systems and AMD MI350-series GPUs, remain centered on E2M1 data elements. In this study, we identify a fundamental limitation of that choice: non-uniform formats such as E2M1 inherently suffer from Shrinkage Bias, a systematic negative rounding error caused by the geometric asymmetry of their representable bins. We show that this bias accumulates multiplicatively across layers and is amplified by the Random Hadamard Transform (RHT), providing a unified explanation for the training instability observed in existing E2M1-based FP4 recipes. In contrast, uniform grids (E1M2/INT4) bypass this grid-geometry error and better convert the improved bucket utilization from RHT into higher quantization quality. Based on this finding, we propose UFP4, a uniform 4-bit training recipe that applies RHT to all three training G

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.20381

## 来源

HuggingFace Papers

---
**Event ID**: b13c80e7d1591688
**Heat Score**: 0.0
**Novelty Score**: 0.0
