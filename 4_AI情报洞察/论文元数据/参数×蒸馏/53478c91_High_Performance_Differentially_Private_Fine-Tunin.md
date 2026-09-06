---
type: literature-corpus-entry
citekey: loo2026high
title: "High Performance Differentially Private Fine-Tuning using Dataset Distillation"
authors:
  - "Noel Loo"
  - "Hanshen Xiao"
  - "Alexander Amini"
  - "Mathias Lechner"
  - "Ramin Hasani"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=VgVeQpagf7"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Differentially Private Stochastic Gradient Descent (DP-SGD),  which iteratively perturbs clipped per-sample gradients and tracks the cumulative privacy risk using composition accounting, has become a cornerstone in private deep learning. Despite its versatility, DP-SGD in practice faces several limitations. It is constrained by the number of gradient iterations permissible under a limited privacy budget, and is restricted by incompatibilities with common deep learning techniques like ensembling and BatchNorm, and typically produces only a single trained model. In this work, we propose an algor
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
  - 蒸馏
  - loo26
---

# High Performance Differentially Private Fine-Tuning using Dataset Distillation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `loo2026high` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Noel Loo, Hanshen Xiao, Alexander Amini |

## 摘要

Differentially Private Stochastic Gradient Descent (DP-SGD),  which iteratively perturbs clipped per-sample gradients and tracks the cumulative privacy risk using composition accounting, has become a cornerstone in private deep learning. Despite its versatility, DP-SGD in practice faces several limitations. It is constrained by the number of gradient iterations permissible under a limited privacy budget, and is restricted by incompatibilities with common deep learning techniques like ensembling and BatchNorm, and typically produces only a single trained model. In this work, we propose an algor

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