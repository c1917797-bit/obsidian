---
type: literature-corpus-entry
citekey: jiang2026purekv
title: "PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models"
authors:
  - "Zhonghua Jiang"
  - "Kunxi Li"
  - "Yiyun Zhou"
  - "Sihao Liu"
  - "Zhaode Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=XtpVQ21bcY"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Vision-Language Large Models (VLLMs) faces significant efficiency challenges when processing high-resolution inputs. The quadratic complexity in attention and autoregressive generation, as well as the constantly growing key value (KV) cache size, severely hinder the prefilling and decoding stages. Recent efforts have attempted to compress KV cache by identifying and pruning KV cache of less important tokens, but these methods typically rely on attention scores to estimate token importance, making them incompatible with efficient attention mechanisms such as FlashAttention and Sparse Attention,
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
  - 剪枝/稀疏
  - jiang26
---

# PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `jiang2026purekv` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Zhonghua Jiang, Kunxi Li, Yiyun Zhou |

## 摘要

Vision-Language Large Models (VLLMs) faces significant efficiency challenges when processing high-resolution inputs. The quadratic complexity in attention and autoregressive generation, as well as the constantly growing key value (KV) cache size, severely hinder the prefilling and decoding stages. Recent efforts have attempted to compress KV cache by identifying and pruning KV cache of less important tokens, but these methods typically rely on attention scores to estimate token importance, making them incompatible with efficient attention mechanisms such as FlashAttention and Sparse Attention,

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