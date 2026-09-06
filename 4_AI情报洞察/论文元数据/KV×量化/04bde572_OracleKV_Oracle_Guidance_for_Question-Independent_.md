---
type: literature-corpus-entry
citekey: zhu2026oraclekv
title: "OracleKV: Oracle Guidance for Question-Independent KV Cache Eviction"
authors:
  - "Yuanbing Zhu"
  - "Zhenheng Tang"
  - "Xiang Liu"
  - "Xiaojiang Du"
  - "Bo Li"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=k3IAjIsfyw"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Key-Value (KV) caching is a widely adopted technique in large language models (LLMs) to accelerate long-context inference. While recent studies predominantly focus on question-dependent KV cache eviction where cache entries are evicted based on known queries. In this paper, however, we observe these approaches often fail in question-independent scenarios, such as multi-turn dialogues and chunk pre-caching in retrieval-augmented generation (RAG), where future queries remain unknown. Our empirical analysis reveals that most existing KV cache eviction methods underperform in this setting due to t
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
  - 量化
  - zhu26
---

# OracleKV: Oracle Guidance for Question-Independent KV Cache Eviction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhu2026oraclekv` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Yuanbing Zhu, Zhenheng Tang, Xiang Liu |

## 摘要

Key-Value (KV) caching is a widely adopted technique in large language models (LLMs) to accelerate long-context inference. While recent studies predominantly focus on question-dependent KV cache eviction where cache entries are evicted based on known queries. In this paper, however, we observe these approaches often fail in question-independent scenarios, such as multi-turn dialogues and chunk pre-caching in retrieval-augmented generation (RAG), where future queries remain unknown. Our empirical analysis reveals that most existing KV cache eviction methods underperform in this setting due to t

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