---
type: tech-event
event_type: runtime_feature
entity: MachineLearning
entity_type: project
tech_categories: inference_optimization, runtime_feature
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-27T16:44:14
created: 2026-06-29T04:19:42.531201
tags: [AI-Intelligence, Event, MachineLearning]
---

# Built an LLM training framework that actually runs on older GPUs without crashing [P]

## 基本信息

- **实体**: MachineLearning
- **类型**: runtime_feature
- **技术分类**: inference_optimization, runtime_feature
- **重要性**: P1
- **阶段**: emerging

## 摘要

Hey guys, I was playing around with Nanotron recently and got super frustrated by how many heavy, hardware-specific dependencies it imports at the module level ( flash-attn , triton, functorch , etc.). If you try to run it on older or budget GPUs like a T4 or V100, it just crashes on import. So I wrote Picotron ( https://github.com/Syntropy-AI-Labs/picotron ) to solve this. It's a clean-room rewrite that gets rid of all mandatory GPU-specific dependencies. It runs on pretty much any GPU that supports PyTorch (defaults to FP16 on older cards under compute capability 8.0, and BF16 on newer ones). It falls back to standard PyTorch SDPA by default, but still hooks into FlashAttention-2 at runtime if it detects you have it installed. I used an AI assistant to write a lot of the boilerplate/code modules, but I've got it working locally and just trained a tiny 2M model on FineWeb-Edu. Also added configs for: • GQA / MLA (Multi-head Latent Attention) • QK-Norm & logit soft-capping (Gemma 2 sty

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://www.reddit.com/r/MachineLearning/comments/1uh7ib3/built_an_llm_training_framework_that_actually/

## 来源

Reddit r/MachineLearning

---
**Event ID**: 1239643a4c492add
**Heat Score**: 0.0
**Novelty Score**: 0.0
