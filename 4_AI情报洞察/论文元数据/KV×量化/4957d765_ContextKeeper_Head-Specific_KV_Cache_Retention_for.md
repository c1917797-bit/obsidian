---
type: literature-corpus-entry
citekey: xu2026contextkeeper
title: "ContextKeeper: Head-Specific KV Cache Retention for Long-Context LLM Inference"
authors:
  - "Tong XU"
  - "Qiong Luo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=7zQy4iHoZ8"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Large Language Model (LLM) inference commonly requires caching all Key-Value (KV) states. This KV cache leads to substantial memory usage and increasing latency in long-context settings. Existing KV cache compression methods reduce cache size by keeping only tokens relevant to the current query, but discarding middle context tokens needed by queries in later turns - harming multi-turn fidelity. We observe head specialization: a minority of attention heads are Context-Anchored (CA), preferring middle context tokens, while most are locality heads, focusing on sink tokens and recent tokens. This
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
  - xu26
---

# ContextKeeper: Head-Specific KV Cache Retention for Long-Context LLM Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xu2026contextkeeper` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Tong XU, Qiong Luo |

## 摘要

Large Language Model (LLM) inference commonly requires caching all Key-Value (KV) states. This KV cache leads to substantial memory usage and increasing latency in long-context settings. Existing KV cache compression methods reduce cache size by keeping only tokens relevant to the current query, but discarding middle context tokens needed by queries in later turns - harming multi-turn fidelity. We observe head specialization: a minority of attention heads are Context-Anchored (CA), preferring middle context tokens, while most are locality heads, focusing on sink tokens and recent tokens. This 

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