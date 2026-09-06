---
type: literature-corpus-entry
citekey: cho2026sparsecache
title: "SparseCache: Extreme Sparse Coding for KV Cache Compression"
authors:
  - "Doohyun Cho"
  - "Myounghoon Cho"
  - "Donghoon Han"
  - "Sohyeon Kim"
  - "Ji-Hoon Kim"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=43zTdoRqY4"
pdf_url: ""
object: KV
method: 低秩
cell: "KV×低秩"
all_objects: []
all_methods: []
abstract: |
  The growing memory footprint of the Key-Value (KV) cache is a critical bottleneck in Large Language Models (LLMs), significantly hindering inference efficiency. While emerging "precomputed RAG" paradigms promise to reduce latency by precomputing KV caches for entire corpora, their prohibitive storage requirements render them impractical. This paper introduces SparseCache, a novel KV Cache compression framework that addresses this bottleneck. SparseCache employs an end-to-end learning framework, inspired by the K-SVD algorithm's alternating optimization, to create separate globally shared dicti
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
  - cho26
---

# SparseCache: Extreme Sparse Coding for KV Cache Compression

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `cho2026sparsecache` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×低秩 |
| **来源** | openreview |
| **作者** | Doohyun Cho, Myounghoon Cho, Donghoon Han |

## 摘要

The growing memory footprint of the Key-Value (KV) cache is a critical bottleneck in Large Language Models (LLMs), significantly hindering inference efficiency. While emerging "precomputed RAG" paradigms promise to reduce latency by precomputing KV caches for entire corpora, their prohibitive storage requirements render them impractical. This paper introduces SparseCache, a novel KV Cache compression framework that addresses this bottleneck. SparseCache employs an end-to-end learning framework, inspired by the K-SVD algorithm's alternating optimization, to create separate globally shared dicti

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