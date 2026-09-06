---
type: literature-corpus-entry
citekey: liu2026conductor
title: "Conductor: Dynamically Orchestrating Pipeline Parallelism with Multi-Granularity Control"
authors:
  - "Ziyuan Liu"
  - "Xingbo Dong"
  - "Le Xue"
  - "Yuezhe Yang"
  - "kevinchenkai"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=mhLh7rXt7g"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Pipeline parallelism is a cornerstone of large-scale model training, yet its efficiency is fundamentally limited by straggler-induced pipeline bubbles. This issue is exacerbated by static scheduling approaches, including handcrafted heuristics and Integer Linear Programming (ILP), that are inherently brittle to real-world execution time variance. In this work, we introduce \textsc{Conductor}, a dynamic, two-tiered scheduling framework that, to our knowledge, is the first to virtually eliminate straggler-induced bubbles under realistic, stochastic conditions. The key insight is to decouple glob
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
  - liu26
---

# Conductor: Dynamically Orchestrating Pipeline Parallelism with Multi-Granularity Control

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026conductor` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Ziyuan Liu, Xingbo Dong, Le Xue |

## 摘要

Pipeline parallelism is a cornerstone of large-scale model training, yet its efficiency is fundamentally limited by straggler-induced pipeline bubbles. This issue is exacerbated by static scheduling approaches, including handcrafted heuristics and Integer Linear Programming (ILP), that are inherently brittle to real-world execution time variance. In this work, we introduce \textsc{Conductor}, a dynamic, two-tiered scheduling framework that, to our knowledge, is the first to virtually eliminate straggler-induced bubbles under realistic, stochastic conditions. The key insight is to decouple glob

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