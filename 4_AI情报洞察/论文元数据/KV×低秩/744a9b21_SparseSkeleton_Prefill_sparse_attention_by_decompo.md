---
type: literature-corpus-entry
citekey: sauleau2026sparseskeleton
title: "SparseSkeleton: Prefill sparse attention by decomposition"
authors:
  - "Luc Sauleau"
  - "Wijnand Suijlen"
  - "Harenome Razanajato"
  - "Denis Barthou"
  - "Zhen Zhang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Y5kgP4x20k"
pdf_url: ""
object: KV
method: 低秩
cell: "KV×低秩"
all_objects: []
all_methods: []
abstract: |
  Multi-head attention (MHA) and grouped query head attention (GQA) consti-
  tute essential architectural components of modern large language models (LLMs).
  Even though attention computations remain relatively inexpensive for small-scale
  inputs, the computational cost increases quadratically as the input size expands.
  In long-context scenarios, including tasks such as book-level summarization or
  code repos analysis, time-to-first-token (TTFT) performance can deteriorate sig-
  nificantly. Although various studies have improved prefill stage performance by
  exploiting sparsity structure, sparsity can
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
  - KV
  - 低秩
  - sauleau26
---

# SparseSkeleton: Prefill sparse attention by decomposition

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `sauleau2026sparseskeleton` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×低秩 |
| **来源** | openreview |
| **作者** | Luc Sauleau, Wijnand Suijlen, Harenome Razanajato |

## 摘要

Multi-head attention (MHA) and grouped query head attention (GQA) consti-
tute essential architectural components of modern large language models (LLMs).
Even though attention computations remain relatively inexpensive for small-scale
inputs, the computational cost increases quadratically as the input size expands.
In long-context scenarios, including tasks such as book-level summarization or
code repos analysis, time-to-first-token (TTFT) performance can deteriorate sig-
nificantly. Although various studies have improved prefill stage performance by
exploiting sparsity structure, sparsity can

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