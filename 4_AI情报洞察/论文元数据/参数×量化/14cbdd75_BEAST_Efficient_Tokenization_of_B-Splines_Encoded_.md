---
type: literature-corpus-entry
citekey: zhou2025beast
title: "BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning"
authors:
  - "Hongyi Zhou"
  - "Weiran Liao"
  - "Xi Huang"
  - "Yucheng Tang"
  - "Fabian Otto"
year: 2025
venue: NeurIPS 2025
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=rQCl1sf62w"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  We present the B-spline Encoded Action Sequence Tokenizer
  (BEAST), a novel action tokenizer that encodes action sequences into compact discrete or continuous tokens using B-splines. In contrast to existing action tokenizers based on vector quantization or byte pair encoding,  BEAST requires no separate tokenizer training and consistently produces tokens of uniform length, enabling fast action sequence generation via parallel decoding. Leveraging our B-spline formulation, BEAST inherently ensures generating smooth trajectories without discontinuities between adjacent segments. We extensively ev
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
  - zhou25
---

# BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhou2025beast` |
| **年份** | 2025 |
| **会议/期刊** | NeurIPS 2025 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Hongyi Zhou, Weiran Liao, Xi Huang |

## 摘要

We present the B-spline Encoded Action Sequence Tokenizer
(BEAST), a novel action tokenizer that encodes action sequences into compact discrete or continuous tokens using B-splines. In contrast to existing action tokenizers based on vector quantization or byte pair encoding,  BEAST requires no separate tokenizer training and consistently produces tokens of uniform length, enabling fast action sequence generation via parallel decoding. Leveraging our B-spline formulation, BEAST inherently ensures generating smooth trajectories without discontinuities between adjacent segments. We extensively ev

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