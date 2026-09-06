---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: inference_optimization, runtime_feature
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-29T04:16:36.144002
created: 2026-06-29T04:19:42.485640
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: inference_optimization, runtime_feature
- **重要性**: P1
- **阶段**: emerging

## 摘要

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding. The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final. It improves a vision-language-action (VLA) policy with a reinforcement-learning loop. The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live failure detection, and candidate selection. The work mostly recombines existing RL ideas with engineering and optimization contributions that can be used together as one recipe or individually: AWR + RECAP combined for flow-matching VLA; an asynchronous distributed training / rollout pipeline through HuggingFace Hub; inference-time hyperparameters optimization via Thompson sampling; a sim-to-real recipe with camera-alignment tooling, heavy augmentation and DAgger-like HIL data collection.

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.27163

## 来源

HuggingFace Papers

---
**Event ID**: 4a04f3273554c1da
**Heat Score**: 0.0
**Novelty Score**: 0.0
