---
type: literature-corpus-entry
citekey: papais2026store
title: "SToRe3D: Sparse Token Relevance in ViTs for Efficient Multi-View 3D Object Detection"
authors:
  - "Sandro Papais"
  - "Lezhou Feng"
  - "Charles Cossette"
  - "Lingting Ge"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=GfT31twtCw"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Vision Transformers (ViTs) enable strong multi-view 3D detection but are limited by high inference latency from dense token and query processing across multiple views and large 3D regions. Prior sparsity methods, designed mainly for 2D vision, prune or merge image tokens but do not extend to full-model sparsity or address 3D object queries. We introduce SToRe3D, a relevance-aligned sparsity framework that jointly selects 2D image tokens and 3D object queries while storing filtered features for selective reuse. Mutual 2D-3D relevance heads allocate compute to driving-critical content and preser
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
  - papais26
---

# SToRe3D: Sparse Token Relevance in ViTs for Efficient Multi-View 3D Object Detection

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `papais2026store` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Sandro Papais, Lezhou Feng, Charles Cossette |

## 摘要

Vision Transformers (ViTs) enable strong multi-view 3D detection but are limited by high inference latency from dense token and query processing across multiple views and large 3D regions. Prior sparsity methods, designed mainly for 2D vision, prune or merge image tokens but do not extend to full-model sparsity or address 3D object queries. We introduce SToRe3D, a relevance-aligned sparsity framework that jointly selects 2D image tokens and 3D object queries while storing filtered features for selective reuse. Mutual 2D-3D relevance heads allocate compute to driving-critical content and preser

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