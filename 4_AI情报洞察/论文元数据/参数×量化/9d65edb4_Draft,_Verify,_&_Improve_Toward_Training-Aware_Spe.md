---
type: literature-corpus-entry
citekey: bhansali2026draft
title: "Draft, Verify, \& Improve: Toward Training-Aware Speculative Decoding"
authors:
  - "Shrenik Bhansali"
  - "Larry Heck"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=CwvY6TXLxr"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Autoregressive (AR) decoding is a major latency bottleneck for large language models. Speculative decoding (SD) accelerates AR by letting a drafter propose multi-token blocks that a verifier accepts or rejects. However, many SD systems require heavy offline training or extra components. These choices raise data/compute cost and can yield brittle drafters under distribution drift.
  We introduce \emph{Draft, Verify, \& Improve (DVI)}, a training-aware self-speculative framework that combines inference with continual online learning. We partition an LLM into a drafter and a verifier, and during ge
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
  - bhansali26
---

# Draft, Verify, \& Improve: Toward Training-Aware Speculative Decoding

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `bhansali2026draft` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Shrenik Bhansali, Larry Heck |

## 摘要

Autoregressive (AR) decoding is a major latency bottleneck for large language models. Speculative decoding (SD) accelerates AR by letting a drafter propose multi-token blocks that a verifier accepts or rejects. However, many SD systems require heavy offline training or extra components. These choices raise data/compute cost and can yield brittle drafters under distribution drift.
We introduce \emph{Draft, Verify, \& Improve (DVI)}, a training-aware self-speculative framework that combines inference with continual online learning. We partition an LLM into a drafter and a verifier, and during ge

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