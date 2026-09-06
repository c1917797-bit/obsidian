---
type: literature-corpus-entry
citekey: zhao2026parallel
title: "Parallel Prompting: Fast LLM Inference for Shared-Context, Short-to-Moderate Output"
authors:
  - "Zekun Zhao"
  - "Jeffrey Flanigan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=T5KBO4IeM2"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  We introduce $\emph{Parallel Prompting}$, a method for high-throughput, quality-preserving decoding of multiple large language model (LLM) queries that share a common prefix. Such shared-context structure arises naturally in applications including document question answering, few-shot learning, multi-user chat, and evaluation pipelines. Prior approaches either degrade generation quality by merging queries into a single prompt that the model cannot reliably disentangle or impose rigid batching and preallocated memory that limit practical deployment. Parallel Prompting is a free lunch for batch
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
  - zhao26
---

# Parallel Prompting: Fast LLM Inference for Shared-Context, Short-to-Moderate Output

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhao2026parallel` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Zekun Zhao, Jeffrey Flanigan |

## 摘要

We introduce $\emph{Parallel Prompting}$, a method for high-throughput, quality-preserving decoding of multiple large language model (LLM) queries that share a common prefix. Such shared-context structure arises naturally in applications including document question answering, few-shot learning, multi-user chat, and evaluation pipelines. Prior approaches either degrade generation quality by merging queries into a single prompt that the model cannot reliably disentangle or impose rigid batching and preallocated memory that limit practical deployment. Parallel Prompting is a free lunch for batch 

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