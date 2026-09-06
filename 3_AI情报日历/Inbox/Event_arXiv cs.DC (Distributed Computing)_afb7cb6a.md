---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: cost_optimization, moe
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-25T05:10:20
created: 2026-06-26T04:14:14.744113
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: runtime_feature
- **技术分类**: cost_optimization, moe
- **重要性**: P1
- **阶段**: emerging

## 摘要

Mixture-of-Experts (MoE) architectures scale large language models (LLMs) to hundreds of billions of parameters. Serving a single MoE model requires multiple GPUs operating in parallel, typically through tensor parallelism (TP) or expert parallelism (EP). The optimal choice depends on the number of in-flight requests: TP is faster at low concurrency, whereas EP wins at high concurrency. Production workloads cross this boundary continually: online serving sees bursty arrivals that subside into quiet periods, and reinforcement-learning rollouts begin as a high-concurrency burst that decays into a long tail of stragglers. Pinning either layout therefore forfeits performance when the workload crosses to the other side.
  We present Moebius, a serving system that switches between EP and TP at runtime without restarting the engine or dropping in-flight requests. Our key insight is that EP and TP are two layouts of one model, not two models: they compute the same function over byte-identical 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.26607v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: afb7cb6a84ad1f80
**Heat Score**: 0.0
**Novelty Score**: 0.0
