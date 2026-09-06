---
type: literature-corpus-entry
citekey: park2026orcas
title: "ORCaS: Unsupervised Depth Completion via Occluded Region Completion as Supervision"
authors:
  - "Hyoungseob Park"
  - "Runjian Chen"
  - "Patrick Rim"
  - "Dong Lao"
  - "Alex Wong"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=v2skNLbrfF"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  We propose a method for inferring an egocentric dense depth map from an RGB image and a sparse point cloud.
  The crux of our method lies in modeling the 3D scene implicitly within the latent space and learning an inductive bias in an unsupervised manner through principles of Structure-from-Motion. To force the learning of this inductive bias, we propose to optimize for an ill-posed objective during training: predicting latent features that are not observed in the input view, but exist in the 3D scene. This is facilitated by means of rigid warping of latent features from the input view to a nea
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
  - 参数
  - 剪枝/稀疏
  - park26
---

# ORCaS: Unsupervised Depth Completion via Occluded Region Completion as Supervision

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `park2026orcas` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Hyoungseob Park, Runjian Chen, Patrick Rim |

## 摘要

We propose a method for inferring an egocentric dense depth map from an RGB image and a sparse point cloud. 
The crux of our method lies in modeling the 3D scene implicitly within the latent space and learning an inductive bias in an unsupervised manner through principles of Structure-from-Motion. To force the learning of this inductive bias, we propose to optimize for an ill-posed objective during training: predicting latent features that are not observed in the input view, but exist in the 3D scene. This is facilitated by means of rigid warping of latent features from the input view to a nea

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