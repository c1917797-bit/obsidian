---
type: literature-corpus-entry
citekey: li2026optimized
title: "Optimized Early-Exit Based Speculative Decoding via Pipeline Parallelism"
authors:
  - "Ruanjun Li"
  - "Ziheng Liu"
  - "Yuanming Shi"
  - "Jiawei Shao"
  - "Chi Zhang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=6ezbdRe90k"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Large language models (LLMs) deliver impressive generation quality, but incur very high inference cost for the auto-regressive decoding manner.
  Early-exit based speculative decoding (EESD) has emerged to reduce decoding latency.
  However, in practice, many approaches struggle to achieve an expected acceleration in the draft-then-verify paradigm even with a well-aligned early-exit head and selected exit position.
  Our analysis reveals that EESD only pays off when the vast majority of draft tokens are accepted by the LLM.
  Otherwise, the draft cost may overcome the acceleration gain and lead to a n
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
  - 通信
  - 量化
  - li26
---

# Optimized Early-Exit Based Speculative Decoding via Pipeline Parallelism

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026optimized` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Ruanjun Li, Ziheng Liu, Yuanming Shi |

## 摘要

Large language models (LLMs) deliver impressive generation quality, but incur very high inference cost for the auto-regressive decoding manner.
Early-exit based speculative decoding (EESD) has emerged to reduce decoding latency.
However, in practice, many approaches struggle to achieve an expected acceleration in the draft-then-verify paradigm even with a well-aligned early-exit head and selected exit position.
Our analysis reveals that EESD only pays off when the vast majority of draft tokens are accepted by the LLM.
Otherwise, the draft cost may overcome the acceleration gain and lead to a n

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