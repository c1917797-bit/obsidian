---
type: literature-corpus-entry
citekey: anonndturborag
title: "TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text"
authors: []
year: ""
venue: iclr2025
venue_type: conference
arxiv_id: ""
doi: ""
url: ""
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Current Retrieval-Augmented Generation (RAG) systems concatenate and process numerous retrieved document chunks for prefill which requires a large volume of computation, therefore leading to significant latency in time-to-first-token (TTFT). To reduce the computation overhead as well as TTFT, we introduce TurboRAG, a novel RAG system that redesigns the inference paradigm of the current RAG system by first pre-computing and storing the key-value (KV) caches of documents offline, and then directly
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "arxiv"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - KV
  - 量化
---

# TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `anonndturborag` |
| **年份** | N/A |
| **会议/期刊** | iclr2025 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | arXiv |
| **作者** | N/A |

## 摘要

Current Retrieval-Augmented Generation (RAG) systems concatenate and process numerous retrieved document chunks for prefill which requires a large volume of computation, therefore leading to significant latency in time-to-first-token (TTFT). To reduce the computation overhead as well as TTFT, we introduce TurboRAG, a novel RAG system that redesigns the inference paradigm of the current RAG system by first pre-computing and storing the key-value (KV) caches of documents offline, and then directly

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
*生成日期: 2026-07-06 | 来源: arXiv*