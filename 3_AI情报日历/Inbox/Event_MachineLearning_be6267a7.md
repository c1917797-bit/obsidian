---
type: tech-event
event_type: runtime_feature
entity: MachineLearning
entity_type: project
tech_categories: cost_optimization, moe
importance: P1
confidence: 0.6
stage: emerging
date: 2026-07-03T21:18:10
created: 2026-07-05T13:44:32.240699
tags: [AI-Intelligence, Event, MachineLearning]
---

# H64LM: A 249M-parameter Mixture-of-Experts Transformer built from scratch in PyTorch [P]

## 基本信息

- **实体**: MachineLearning
- **类型**: runtime_feature
- **技术分类**: cost_optimization, moe
- **重要性**: P1
- **阶段**: emerging

## 摘要

Hi everyone, I built H64LM, a research project to better understand modern LLMs by implementing one from scratch in PyTorch. Instead of relying on high-level training frameworks, I implemented the core components myself attention, MoE routing, normalization, and the training loop. Features 249M-parameter Transformer Grouped Query Attention (GQA) Sparse Mixture-of-Experts (8 experts, Top-2 routing) with 3 auxiliary routing losses SwiGLU, RoPE, RMSNorm Sliding-window attention Mixed-precision training, gradient accumulation Custom training loop (no Trainer abstractions) Checkpointing and resume support The included checkpoint was trained on a subset of WikiText-103 to validate the pipeline end-to-end, not to be a strong model it's visibly overfit past epoch 10 (best val PPL ~40.5). Known limitations are documented in the README, including batch-size-1-only generation and no true DDP (falls back to DataParallel). GitHub: https://github.com/Haiderkhan64/H64LM Feedback on the implementation

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://www.reddit.com/r/MachineLearning/comments/1umqfd2/h64lm_a_249mparameter_mixtureofexperts/

## 来源

Reddit r/MachineLearning

---
**Event ID**: be6267a7748845fd
**Heat Score**: 0.0
**Novelty Score**: 0.0
