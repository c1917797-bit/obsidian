---
type: literature-corpus-entry
citekey: chatzoudis2026visual
title: "Visual Sparse Steering (VS2): Unsupervised Adaptation for Image Classification via Sparsity-Guided Steering Vectors"
authors:
  - "Gerasimos Chatzoudis"
  - "Zhuowei Li"
  - "Gemma Elyse Moran"
  - "Hao Wang"
  - "Dimitris N. Metaxas"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=8HZzPtMcZo"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Steering vision foundation models at test time, without retraining or access to large labeled datasets, is a desirable yet challenging goal, particularly in dynamic or resource-constrained settings. We present Visual Sparse Steering (VS2), a lightweight, label-free test-time method that constructs a steering vector from sparse features extracted by a Sparse Autoencoder (SAE) trained on the model’s internal activations. On CIFAR-100, CUB-200, and Tiny-ImageNet, VS2 improves the top-1 accuracy of the CLIP zero-shot baseline by 4.12\%, 1.08\%, and 1.84\%, respectively. Since not all features lear
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
  - 激活
  - 剪枝/稀疏
  - chatzoudis26
---

# Visual Sparse Steering (VS2): Unsupervised Adaptation for Image Classification via Sparsity-Guided Steering Vectors

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chatzoudis2026visual` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Gerasimos Chatzoudis, Zhuowei Li, Gemma Elyse Moran |

## 摘要

Steering vision foundation models at test time, without retraining or access to large labeled datasets, is a desirable yet challenging goal, particularly in dynamic or resource-constrained settings. We present Visual Sparse Steering (VS2), a lightweight, label-free test-time method that constructs a steering vector from sparse features extracted by a Sparse Autoencoder (SAE) trained on the model’s internal activations. On CIFAR-100, CUB-200, and Tiny-ImageNet, VS2 improves the top-1 accuracy of the CLIP zero-shot baseline by 4.12\%, 1.08\%, and 1.84\%, respectively. Since not all features lear

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