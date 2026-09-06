---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: cost_optimization, moe
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-26T04:13:09.681223
created: 2026-06-26T04:14:14.634709
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Nemotron-TwoTower: Diffusion Language Modeling with Pretrained Autoregressive Context

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: cost_optimization, moe
- **重要性**: P1
- **阶段**: emerging

## 摘要

Diffusion language models offer a promising alternative to autoregressive models due to their potential for parallel and iterative generation. However, existing approaches use a single network for both context representation and iterative denoising, forcing one model to serve both roles and limiting its capacity for either role. We propose TwoTower, a block-wise autoregressive diffusion model that decouples these roles into two towers: a frozen AR context tower that causally processes clean tokens, and a trainable diffusion denoiser tower with bidirectional block attention that refines noisy blocks via cross-attention to the context. Built on Nemotron-3-Nano-30B-A3B, an open-weight 30B hybrid Mamba-Transformer MoE model, and trained on approximately 2.1T tokens, Nemotron-TwoTower retains 98.7% of the autoregressive baseline's quality while offering 2.42X higher wall-clock generation throughput. We release the code and model weights at https://huggingface.co/collections/nvidia/nemotron-

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.26493

## 来源

HuggingFace Papers

---
**Event ID**: cb69bddc0072baec
**Heat Score**: 0.0
**Novelty Score**: 0.0
