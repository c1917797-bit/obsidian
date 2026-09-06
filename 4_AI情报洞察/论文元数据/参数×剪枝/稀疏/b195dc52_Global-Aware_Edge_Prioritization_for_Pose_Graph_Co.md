---
type: literature-corpus-entry
citekey: wei2026global
title: "Global-Aware Edge Prioritization for Pose Graph Construction in SfM"
authors:
  - "Tong Wei"
  - "Giorgos Tolias"
  - "Jiri Matas"
  - "Daniel Barath"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=tDwJ2gX0Mf"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  The pose graph is an essential component of Structure-from-Motion (SfM) pipelines, where images form the nodes and edges encode relative poses between them. These graphs are typically sparse to reduce the cost of geometric verification required for each candidate edge. In this paper, we focus on robust pose graph initialization, performed at the very beginning of the SfM pipeline. Traditionally, this step relies on image retrieval methods applied independently to each image, connecting it to the $k$ most similar ones according to, e.g., embedding similarity. While effective in practice, this g
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
  - wei26
---

# Global-Aware Edge Prioritization for Pose Graph Construction in SfM

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wei2026global` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Tong Wei, Giorgos Tolias, Jiri Matas |

## 摘要

The pose graph is an essential component of Structure-from-Motion (SfM) pipelines, where images form the nodes and edges encode relative poses between them. These graphs are typically sparse to reduce the cost of geometric verification required for each candidate edge. In this paper, we focus on robust pose graph initialization, performed at the very beginning of the SfM pipeline. Traditionally, this step relies on image retrieval methods applied independently to each image, connecting it to the $k$ most similar ones according to, e.g., embedding similarity. While effective in practice, this g

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