---
type: literature-corpus-entry
citekey: kong2026clapping
title: "Clapping: Removing Per-sample Storage for Pipeline Parallel Distributed Optimization with Communication Compression"
authors:
  - "Boao Kong"
  - "Xu Huang"
  - "Yuqi Xu"
  - "Yixuan Liang"
  - "Bin Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=yOkek71cG5"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Pipeline-parallel distributed optimization is essential for large-scale machine learning but is challenged by significant communication overhead from transmitting high-dimensional activations and gradients between workers. Existing approaches often depend on impractical unbiased gradient assumptions or incur sample-size memory overhead. This paper introduces **Clapping**, a **C**ommunication compression algorithm with **LA**zy sam**P**ling for **P**ipeline-parallel learn**ING**. Clapping adopts a lazy sampling strategy that reuses data samples across steps, breaking sample-wise memory barrier
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
  - 量化
  - kong26
---

# Clapping: Removing Per-sample Storage for Pipeline Parallel Distributed Optimization with Communication Compression

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `kong2026clapping` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Boao Kong, Xu Huang, Yuqi Xu |

## 摘要

Pipeline-parallel distributed optimization is essential for large-scale machine learning but is challenged by significant communication overhead from transmitting high-dimensional activations and gradients between workers. Existing approaches often depend on impractical unbiased gradient assumptions or incur sample-size memory overhead. This paper introduces **Clapping**, a **C**ommunication compression algorithm with **LA**zy sam**P**ling for **P**ipeline-parallel learn**ING**. Clapping adopts a lazy sampling strategy that reuses data samples across steps, breaking sample-wise memory barrier 

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