---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: agent_runtime, memory
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-10T04:09:18.541025
created: 2026-06-10T04:10:32.684609
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# Latent Spatial Memory for Video World Models

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: agent_runtime, memory
- **重要性**: P1
- **阶段**: emerging

## 摘要

Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space. This design is both computationally expensive, requiring repeated rendering and VAE encoding, and inherently lossy, as the round trip through pixel space discards rich features of the learned latent representation. In this paper, we introduce latent spatial memory for video world models, a persistent 3D cache that stores scene information directly in the diffusion latent space, avoiding pixel-space reconstruction. Building on this, we propose Mirage, a latent-space spatial memory framework that constructs the memory by lifting latent tokens into 3D via depth-guided back-projection and queries it by synthesizing novel views through direct latent-space warping. This unified formulation eliminates both the information loss of pixel-space reconstruction and the computational burden of repeated encoding and rendering. Experiments show that l

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2606.09828

## 来源

HuggingFace Papers

---
**Event ID**: 1bda646510355770
**Heat Score**: 0.0
**Novelty Score**: 0.0
