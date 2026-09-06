---
type: tech-event
event_type: research_paper
entity: HuggingFace Papers
entity_type: project
tech_categories: research, architecture
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-11T04:32:00.719499
created: 2026-06-11T04:32:29.181216
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Next Forcing: Causal World Modeling with Multi-Chunk Prediction

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: research_paper
- **技术分类**: research, architecture
- **重要性**: P1
- **阶段**: emerging

## 摘要

Autoregressive video generation has emerged as a powerful paradigm for World Action Models (WAMs). However, existing approaches suffer from slow training convergence and limited converged accuracy, particularly at high frame rates, as the training supervision is confined to the current chunk without explicit signals about future dynamics; they also suffer from slow inference due to iterative video denoising. In this paper, we present Next Forcing, a multi-chunk prediction (MCP) framework for causal world modeling that enables faster training, higher accuracy, and accelerated inference. Inspired by multi-token prediction in large language models, Next Forcing introduces an MCP training objective that augments the main model with lightweight auxiliary MCP modules to simultaneously denoise video chunks at multiple future temporal horizons (next^1, next^2, next^3 chunks). These MCP modules form a causal chain across prediction depths, where intermediate features fused from multiple layers 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.11187

## 来源

HuggingFace Papers

---
**Event ID**: f46d6da905d5527e
**Heat Score**: 0.0
**Novelty Score**: 0.0
