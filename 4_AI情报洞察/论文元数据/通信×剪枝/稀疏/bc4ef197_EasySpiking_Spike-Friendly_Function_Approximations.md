---
type: literature-corpus-entry
citekey: yuan2026easyspiking
title: "EasySpiking: Spike-Friendly Function Approximations for Spiking LLMs  Without Fine-Tuning"
authors:
  - "Xinzhe Yuan"
  - "Xiang Peng"
  - "Huan Xiong"
  - "Bin Gu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Vz0fxQp79c"
pdf_url: ""
object: 通信
method: 剪枝/稀疏
cell: "通信×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Transformer-scale large language models (LLMs) deliver state-of-the-art accuracy but demand heavy floating-point computation and memory bandwidth, making them impractical for low-power devices. Spiking neural networks (SNNs) promise efficiency through sparse, event-driven communication, yet current ANN-to-SNN conversion pipelines still rely on floating-point softmax, RMSNorm and SwiGLU/SiLU or fall back to ReLU-compatible spiking surrogates, often requiring fine-tuning to recover accuracy. This work introduces a family of spike-friendly approximations that collectively replace softmax, RMSNorm
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "openreview"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - 通信
  - 剪枝/稀疏
  - yuan26
---

# EasySpiking: Spike-Friendly Function Approximations for Spiking LLMs  Without Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yuan2026easyspiking` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Xinzhe Yuan, Xiang Peng, Huan Xiong |

## 摘要

Transformer-scale large language models (LLMs) deliver state-of-the-art accuracy but demand heavy floating-point computation and memory bandwidth, making them impractical for low-power devices. Spiking neural networks (SNNs) promise efficiency through sparse, event-driven communication, yet current ANN-to-SNN conversion pipelines still rely on floating-point softmax, RMSNorm and SwiGLU/SiLU or fall back to ReLU-compatible spiking surrogates, often requiring fine-tuning to recover accuracy. This work introduces a family of spike-friendly approximations that collectively replace softmax, RMSNorm

## 关键创新

*待精读后在此填写 1-3 个方法核心创新点*

> 提示：
> - 这个方法解决什么问题？
> - 相比已有方法的本质区别？
> - 实验中验证了什么关键指标？

## 性能数据

| 模型/场景 | 压缩率 | 精度 | 加速比 | 显存 |
|-----------|--------|------|--------|------|
| 待填 | | | | |

> 精读时把论文表格中的关键数字搬过来

## 代码与资源


- **代码**: （精读时查找GitHub链接）
- **HuggingFace模型**: （如适用）

## 我的笔记

*精读笔记在此写，或链接到 [[专题笔记名]]*

## 相关论文

*精读时用Obsidian双链 `[[arxiv_id]]` 连接相关工作*

---

*基于 ARS v3.6.4 literature_corpus_entry schema*  
*生成日期: 2026-07-06 | 来源: openreview*