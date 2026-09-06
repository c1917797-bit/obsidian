---
type: literature-corpus-entry
citekey: chen2026shared
title: "Shared Embedding Optimization: A Two-Stage Approach for Efficient and Effective Feature Embedding"
authors:
  - "Lin Chen"
  - "Kaiyuan Wang"
  - "Matthew Fahrbach"
  - "Xing Gao"
  - "Kyriakos Axiotis"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=i0IrYZNq9z"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Large-scale recommendation systems and other industrial machine learning models depend heavily on embeddings for representing categorical and sparse features. The resulting embedding tables often constitute the majority of a model's parameters, creating a significant bottleneck for training and serving. We propose Shared Embedding Optimization (SEO), a novel two-stage approach to learn compact but effective embeddings.
  In the first stage, a search model utilizing shared embedding tables and a sequential attention mechanism identifies the most salient embedding subspaces (chunks) from a large p
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
  - chen26
---

# Shared Embedding Optimization: A Two-Stage Approach for Efficient and Effective Feature Embedding

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026shared` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Lin Chen, Kaiyuan Wang, Matthew Fahrbach |

## 摘要

Large-scale recommendation systems and other industrial machine learning models depend heavily on embeddings for representing categorical and sparse features. The resulting embedding tables often constitute the majority of a model's parameters, creating a significant bottleneck for training and serving. We propose Shared Embedding Optimization (SEO), a novel two-stage approach to learn compact but effective embeddings.
In the first stage, a search model utilizing shared embedding tables and a sequential attention mechanism identifies the most salient embedding subspaces (chunks) from a large p

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