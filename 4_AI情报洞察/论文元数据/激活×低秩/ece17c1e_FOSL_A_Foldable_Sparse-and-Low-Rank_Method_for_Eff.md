---
type: literature-corpus-entry
citekey: wang2026fosl
title: "FOSL: A Foldable Sparse-and-Low-Rank Method for Efficient LLM Pre-training"
authors:
  - "Dong Wang"
  - "Francesco Corti"
  - "Yun Cheng"
  - "Olga Saukh"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=O1ClDXOMul"
pdf_url: ""
object: 激活
method: 低秩
cell: "激活×低秩"
all_objects: []
all_methods: []
abstract: |
  We propose FOSL, a foldable, sparse-and-low-rank reparameterization for efficient pre-training that decouples compute from width. Each linear/FFN/attention projection is rewritten as two cooperating paths: a low-rank path that injects expressive features via a compact adapter, and a folded sparse path that computes only a subset of output channels and synthesizes the remainder as virtual channels by reusing computed ones. A lightweight, variance-preserving rescaling keeps activations stable when channels are reused multiple times. This design delivers the benefits of a narrower network interna
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
  - 激活
  - 低秩
  - wang26
---

# FOSL: A Foldable Sparse-and-Low-Rank Method for Efficient LLM Pre-training

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026fosl` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×低秩 |
| **来源** | openreview |
| **作者** | Dong Wang, Francesco Corti, Yun Cheng |

## 摘要

We propose FOSL, a foldable, sparse-and-low-rank reparameterization for efficient pre-training that decouples compute from width. Each linear/FFN/attention projection is rewritten as two cooperating paths: a low-rank path that injects expressive features via a compact adapter, and a folded sparse path that computes only a subset of output channels and synthesizes the remainder as virtual channels by reusing computed ones. A lightweight, variance-preserving rescaling keeps activations stable when channels are reused multiple times. This design delivers the benefits of a narrower network interna

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