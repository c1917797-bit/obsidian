---
type: literature-corpus-entry
citekey: merinov2026layer
title: "Layer-Based 3D Gaussian Splatting for Sparse-View CT Reconstruction"
authors:
  - "Artem Merinov"
  - "Xia Li"
  - "Alessandro Torcinovich"
  - "Oswald Lanz"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Hmnh6UhDp6"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  We introduce a dynamic framework for 3D sparse-view Gaussian Splatting that learns scene representations through layerwise, iterative refinement of the Gaussian primitives. Conventional methods typically rely on dense, one-time initialization, where the placement of Gaussians is guided by 2D projection supervision and density control. However, such strategies can lead to misalignment with the true 3D structure, particularly in regions with insufficient projection information due to sparse-view acquisition. In contrast, we adopt a coarse-to-fine approach beginning with a base representation and
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
  - merinov26
---

# Layer-Based 3D Gaussian Splatting for Sparse-View CT Reconstruction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `merinov2026layer` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Artem Merinov, Xia Li, Alessandro Torcinovich |

## 摘要

We introduce a dynamic framework for 3D sparse-view Gaussian Splatting that learns scene representations through layerwise, iterative refinement of the Gaussian primitives. Conventional methods typically rely on dense, one-time initialization, where the placement of Gaussians is guided by 2D projection supervision and density control. However, such strategies can lead to misalignment with the true 3D structure, particularly in regions with insufficient projection information due to sparse-view acquisition. In contrast, we adopt a coarse-to-fine approach beginning with a base representation and

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