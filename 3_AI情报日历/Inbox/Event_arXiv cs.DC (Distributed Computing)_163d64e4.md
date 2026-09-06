---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: inference_optimization, quantization
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-08T16:02:03
created: 2026-06-10T04:10:32.735891
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: runtime_feature
- **技术分类**: inference_optimization, quantization
- **重要性**: P1
- **阶段**: emerging

## 摘要

AutoMegaKernel (AMK) compiles a HuggingFace Llama-family model into a single persistent cooperative CUDA kernel that runs the whole forward pass in one launch, with no per-model hand-written CUDA. The contribution is the system, not raw speed.
  A frozen schedule-IR validator statically certifies deadlock-freedom and race-freedom via static graph checks (not a mechanized proof), so an unsafe agent-proposed schedule is rejected before launch: across 7,160 adversarial schedules (6,091 unsafe) it had zero false-accepts and accepted all 360 real lowerings. The same source retargets sm_80/sm_90/sm_120 from one codebase, auto-generates correct megakernels for 10 of 10 supported models, and on a real SmolLM2-135M checkpoint reproduces HuggingFace greedy decode token-for-token (perplexity match 2.5e-7). An unattended, agent-drivable autoresearch loop self-improves the megakernel over its own baseline (1.25-1.72x).
  A search-found int8 (W8A16) megakernel beats CUDA-graphed cuBLAS bf16 at batch

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.09682v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: 163d64e4249d2a43
**Heat Score**: 0.0
**Novelty Score**: 0.0
