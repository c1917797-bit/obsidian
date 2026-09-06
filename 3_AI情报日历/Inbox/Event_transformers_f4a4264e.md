---
type: tech-event
event_type: runtime_feature
entity: transformers
entity_type: project
tech_categories: inference_optimization, quantization
importance: P1
confidence: 0.6
stage: emerging
date: 2026-07-05T13:40:27.116430
created: 2026-07-05T13:44:32.210584
tags: [AI-Intelligence, Event, transformers]
---

# OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers

## 基本信息

- **实体**: transformers
- **类型**: runtime_feature
- **技术分类**: inference_optimization, quantization
- **重要性**: P1
- **阶段**: emerging

## 摘要

Diffusion transformers (DiTs) achieve state-of-the-art image and video generation, but their multi-step sampling and growing parameter count make inference expensive. Post-training quantization (PTQ) is the natural remedy, yet DiT activations shift across timesteps, prompts, and guidance branches, forcing prior methods to re-fit calibration data for every new checkpoint or modality. We present OrbitQuant, a data-agnostic weight-activation quantizer that bypasses range estimation by quantizing in a normalized, rotated basis. In this basis, a randomized permuted block-Hadamard (RPBH) rotation concentrates each coordinate around one fixed, known marginal regardless of the input, so a single Lloyd-Max codebook serves all timesteps, prompts, and layers of a given input dimension. We extend the same quantizer to weight rows offline, absorbing the rotation into the weights so that it cancels inside each linear layer and only a forward rotation on the activations remains at runtime. The same r

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2607.02461

## 来源

HuggingFace Papers

---
**Event ID**: f4a4264eabf49367
**Heat Score**: 0.0
**Novelty Score**: 0.0
