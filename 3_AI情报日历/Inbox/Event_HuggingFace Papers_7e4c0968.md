---
type: tech-event
event_type: research_paper
entity: HuggingFace Papers
entity_type: project
tech_categories: research, architecture
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-20T10:57:25.408092
created: 2026-06-20T11:09:35.113333
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: research_paper
- **技术分类**: research, architecture
- **重要性**: P1
- **阶段**: emerging

## 摘要

The Frechet Inception Distance (FID) is the de facto arbiter of image generation, yet most papers report just a single number from a single trained model using a single sampling seed. How reproducible is that number if we retrain the model, or merely resample from it? In this paper, we treat FID as a random variable on a two-axis panel of training and generation seeds, and measure its variance directly on several hundred SiT networks trained on class-conditional ImageNet 256x256. We report surprising findings: (a) Retraining the model using the same recipe with a different seed moves FID 3.2x more (in Inception feature space) than redrawing samples from a fixed network. (b) That gap is driven by three factors: random initialisation, data ordering, and the per-step Gaussian noise of the flow-matching loss. (c) Increasing compute or model size barely tightens the spread, holding the FID coefficient of variation (CoV) inside a 1-2% band. (d) Per-cell classifier-free-guidance tuning halves

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.20536

## 来源

HuggingFace Papers

---
**Event ID**: 7e4c0968dc038935
**Heat Score**: 0.0
**Novelty Score**: 0.0
