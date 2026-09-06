---
type: literature-corpus-entry
citekey: lee2026is
title: "Is Bidirectionality Necessary in Mamba for Time Series Forecasting?"
authors:
  - "Seunghan Lee"
  - "Juri Hong"
  - "Kibok Lee"
  - "Taeyoung Park"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=N6MIqE11eF"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Mamba is a sequential model that has recently emerged as a promising alternative to Transformers, offering near-linear complexity.
  However, although channels in time series (TS) data generally lack a sequential order, recent studies have adopted Mamba to capture channel dependencies (CD) in TS, introducing a sequential order bias. To address this, prior works have adopted bidirectional Mamba to scan channels in both forward and reverse orders. In this paper, we show that unidirectional Mamba can effectively replace the bidirectional Mamba with simple strategies. To this end, we propose FSMamba
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
  - lee26
---

# Is Bidirectionality Necessary in Mamba for Time Series Forecasting?

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lee2026is` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Seunghan Lee, Juri Hong, Kibok Lee |

## 摘要

Mamba is a sequential model that has recently emerged as a promising alternative to Transformers, offering near-linear complexity.
However, although channels in time series (TS) data generally lack a sequential order, recent studies have adopted Mamba to capture channel dependencies (CD) in TS, introducing a sequential order bias. To address this, prior works have adopted bidirectional Mamba to scan channels in both forward and reverse orders. In this paper, we show that unidirectional Mamba can effectively replace the bidirectional Mamba with simple strategies. To this end, we propose FSMamba

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