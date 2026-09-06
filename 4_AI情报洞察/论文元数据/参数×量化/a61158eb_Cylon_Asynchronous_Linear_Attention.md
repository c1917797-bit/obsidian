---
type: literature-corpus-entry
citekey: waitz2026cylon
title: "Cylon: Asynchronous Linear Attention"
authors:
  - "Alexander Waitz"
  - "Benjamin Frederick Spector"
  - "Christopher Re"
  - "Simran Arora"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=va4FWa5TDN"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Sequence models face stark tradeoffs between recall quality and memory efficiency. Recall -- the ability to use information over long sequences -- is critical for sequence modeling tasks ranging from information extraction to reasoning.
  Prior work has shown that in theory, \textit{linear} attention models with sufficient recurrent state sizes can expand the Pareto frontier of the recall-memory tradeoff space beyond alternative architectures such as softmax attention and state space models.
  However, it is difficult to scale the linear attention state size due to hardware bottlenecks. I/O aware
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
  - waitz26
---

# Cylon: Asynchronous Linear Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `waitz2026cylon` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Alexander Waitz, Benjamin Frederick Spector, Christopher Re |

## 摘要

Sequence models face stark tradeoffs between recall quality and memory efficiency. Recall -- the ability to use information over long sequences -- is critical for sequence modeling tasks ranging from information extraction to reasoning. 
Prior work has shown that in theory, \textit{linear} attention models with sufficient recurrent state sizes can expand the Pareto frontier of the recall-memory tradeoff space beyond alternative architectures such as softmax attention and state space models.
However, it is difficult to scale the linear attention state size due to hardware bottlenecks. I/O aware

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