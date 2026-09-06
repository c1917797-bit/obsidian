---
type: literature-corpus-entry
citekey: willette2026measure
title: "Measure Once, Mask Once: Delta Refined Block Sparse Attention"
authors:
  - "Jeffrey Willette"
  - "Heejun Lee"
  - "Geon Park"
  - "Sung Ju Hwang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=5HzrYMUlRd"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Long context inference poses a problem for large language models (LLMs) due to the high cost of quadratic attention with long input lengths. Efficient long context inference is a necessity in order to provide low-cost, low-latency LLM serving endpoints. Sparse attention is one way to mitigate the high cost of long context prefills. Many recent state-of-the-art sparse attention methods can be applied on top of pretrained quadratic transformers without any specific finetuning regimen, however, the main obstacle to overcome when designing sparse attention method lies in deciding which parts to co
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
  - willette26
---

# Measure Once, Mask Once: Delta Refined Block Sparse Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `willette2026measure` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Jeffrey Willette, Heejun Lee, Geon Park |

## 摘要

Long context inference poses a problem for large language models (LLMs) due to the high cost of quadratic attention with long input lengths. Efficient long context inference is a necessity in order to provide low-cost, low-latency LLM serving endpoints. Sparse attention is one way to mitigate the high cost of long context prefills. Many recent state-of-the-art sparse attention methods can be applied on top of pretrained quadratic transformers without any specific finetuning regimen, however, the main obstacle to overcome when designing sparse attention method lies in deciding which parts to co

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