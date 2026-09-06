---
type: literature-corpus-entry
citekey: zhang2026falcon
title: "Falcon: Fast Proximal Linearization of Normalized Cuts for Unsupervised Image Segmentation"
authors:
  - "Xiao Zhang"
  - "Xiangyu Han"
  - "Xiwen Lai"
  - "Yao Sun"
  - "Pei Zhang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=PvWHzAf9qp"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Current zero-shot unsupervised segmentation methods based on normalized cuts (NCut) face three key limitations. First, they rely on recursive bipartitions with repeated eigen-decompositions, making them prohibitively expensive at scale. Second, each split requires spectral relaxation followed by rounding, introducing layers of approximation where the final partition may diverge from the true NCut objective. Third, recursive bipartitioning offers no principled assurance of producing a stable $K$-way segmentation, and existing heuristics lack convergence guarantees. We propose \textbf{Falcon}, a
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
  - 低秩
  - zhang26
---

# Falcon: Fast Proximal Linearization of Normalized Cuts for Unsupervised Image Segmentation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026falcon` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Xiao Zhang, Xiangyu Han, Xiwen Lai |

## 摘要

Current zero-shot unsupervised segmentation methods based on normalized cuts (NCut) face three key limitations. First, they rely on recursive bipartitions with repeated eigen-decompositions, making them prohibitively expensive at scale. Second, each split requires spectral relaxation followed by rounding, introducing layers of approximation where the final partition may diverge from the true NCut objective. Third, recursive bipartitioning offers no principled assurance of producing a stable $K$-way segmentation, and existing heuristics lack convergence guarantees. We propose \textbf{Falcon}, a

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