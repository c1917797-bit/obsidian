---
type: literature-corpus-entry
citekey: liu2026compressed
title: "Compressed Step Information Memory for End-to-End Agent Foundation Models"
authors:
  - "Xinxin Liu"
  - "Weizhen Li"
  - "Weichen Sun"
  - "Xinlong Yang"
  - "Tianrui Qin"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=vUG2hpVJWR"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Large Language Model (LLM) agents excel in tasks like translation, code generation, and decision-making, but consecutive tool calls in complex scenarios lead to excessively long contexts. Despite SOTA LLMs’ 128K+ token context windows, unstructured data interactions easily exceed limits, harming task focus and increasing resource costs.
  Existing solutions have flaws: forced truncation causes information loss, external memory modules lack end-to-end optimization, and context summarization wastes KV cache and loses data.
  To address this, we propose Compressed Step Information Memory (CSIM), an e
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
  - liu26
---

# Compressed Step Information Memory for End-to-End Agent Foundation Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026compressed` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Xinxin Liu, Weizhen Li, Weichen Sun |

## 摘要

Large Language Model (LLM) agents excel in tasks like translation, code generation, and decision-making, but consecutive tool calls in complex scenarios lead to excessively long contexts. Despite SOTA LLMs’ 128K+ token context windows, unstructured data interactions easily exceed limits, harming task focus and increasing resource costs.
Existing solutions have flaws: forced truncation causes information loss, external memory modules lack end-to-end optimization, and context summarization wastes KV cache and loses data.
To address this, we propose Compressed Step Information Memory (CSIM), an e

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