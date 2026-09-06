---
type: literature-corpus-entry
citekey: hou2026continual
title: "Continual Parameter-Efficient Adaptation for Rehearsal-Free Graph Class-Incremental Learning"
authors:
  - "Yue Hou"
  - "Ruomei Liu"
  - "Yiman Zhong"
  - "Yingke Su"
  - "Junran Wu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=e6N1ZFY2X1"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Graph Class-Incremental Learning (GCIL) seeks to learn novel classes sequentially while preserving knowledge acquired from previously seen classes. However, to tackle the pervasive challenge of catastrophic forgetting, recent GCIL methods often train separate classifiers from scratch for each task, which is redundant in design and computationally expensive. Moreover, isolating streaming data in different tasks hampers knowledge transfer across tasks. To address these dilemmas, we first propose Graph2Hyper, a parameter-efficient framework that utilizes a hypernetwork to generate task-specific c
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
  - 量化
  - hou26
---

# Continual Parameter-Efficient Adaptation for Rehearsal-Free Graph Class-Incremental Learning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hou2026continual` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yue Hou, Ruomei Liu, Yiman Zhong |

## 摘要

Graph Class-Incremental Learning (GCIL) seeks to learn novel classes sequentially while preserving knowledge acquired from previously seen classes. However, to tackle the pervasive challenge of catastrophic forgetting, recent GCIL methods often train separate classifiers from scratch for each task, which is redundant in design and computationally expensive. Moreover, isolating streaming data in different tasks hampers knowledge transfer across tasks. To address these dilemmas, we first propose Graph2Hyper, a parameter-efficient framework that utilizes a hypernetwork to generate task-specific c

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