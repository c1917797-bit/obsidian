---
type: literature-corpus-entry
citekey: xia2026intra
title: "INTRA: Interleaved Non-contiguous Token spaRse Attention"
authors:
  - "Yuxuan Xia"
  - "Wenbo Lu"
  - "Shaoyi Zheng"
  - "Haoming Liu"
  - "Shenji Wan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=hqqhBFhR8k"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Transformer models have revolutionized generation tasks, but the quadratic complexity of the attention mechanism limits scalability to long input sequences.
  Prior work introduces sparse attention to mitigate this cost, but relies on contiguous memory access patterns that result in wasted computation for their proposed sparsity layouts, limiting practical efficiency.
  In this paper, we propose $\textbf{I}$nterleaved $\textbf{N}$on-contiguous $\textbf{T}$oken spa$\textbf{R}$se $\textbf{A}$ttention (INTRA), a token-wise sparse attention framework that supports flexible sparsity by redesigning me
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
  - xia26
---

# INTRA: Interleaved Non-contiguous Token spaRse Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xia2026intra` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Yuxuan Xia, Wenbo Lu, Shaoyi Zheng |

## 摘要

Transformer models have revolutionized generation tasks, but the quadratic complexity of the attention mechanism limits scalability to long input sequences. 
Prior work introduces sparse attention to mitigate this cost, but relies on contiguous memory access patterns that result in wasted computation for their proposed sparsity layouts, limiting practical efficiency. 
In this paper, we propose $\textbf{I}$nterleaved $\textbf{N}$on-contiguous $\textbf{T}$oken spa$\textbf{R}$se $\textbf{A}$ttention (INTRA), a token-wise sparse attention framework that supports flexible sparsity by redesigning me

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