---
type: tech-event
event_type: research_paper
entity: arXiv cs.DC (Distributed Computing)
entity_type: project
tech_categories: research, architecture
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-22T21:48:53
created: 2026-06-24T12:14:40.392794
tags: [AI-Intelligence, Event, arXiv cs.DC (Distributed Computing)]
---

# The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing

## 基本信息

- **实体**: arXiv cs.DC (Distributed Computing)
- **类型**: research_paper
- **技术分类**: research, architecture
- **重要性**: P1
- **阶段**: emerging

## 摘要

GPU Confidential Computing (GPU-CC) now preserves GPU-local performance: on NVIDIA B300, BF16 matmul runs at 0.998x of non-confidential performance. Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. This paper studies that gap on two Blackwell platforms, RTX Pro 6000 and B300 HGX, and identifies its dominant cause: the confidential VM-GPU bridge, not GPU compute.
  We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. Secure copies do not gain CUDA-stream concurrency within a context, asynchronous transfers block at the runtime boundary, and small crossings pay a fixed toll. This violates the assumptions of modern inference runtimes, where DMA is expected to be cheap, concurrent, and asynchronous. In vLLM dense decode, the gap closes around 44x-slower small alloc-and-copy operations; targeted patches reject alternative explanations. A scheduling flag recovers 57% of the g

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.23969v1

## 来源

arXiv cs.DC (Distributed Computing)

---
**Event ID**: 7d2d819a973a395e
**Heat Score**: 0.0
**Novelty Score**: 0.0
