---
type: literature-corpus-entry
citekey: lee2026compensate
title: "Compensate, Don't Reconstruct: Parameter- and Data-Efficient 2-bit LLM Quantization"
authors:
  - "Geonho Lee"
  - "Janghwan Lee"
  - "Jungwook Choi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=zcK14OnlcK"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  The substantial memory footprint of large language models (LLMs) remains a key barrier to their on-device deployment. 2-bit quantization is a promising solution; however, current methods impose a difficult trade-off between the high accuracy of training-intensive Quantization-Aware Training (QAT) and the efficiency of lower-performing Quantization Error Compensation (QEC). Our analysis of QEC reveals a critical insight: its effectiveness is more dependent on minimizing activation discrepancy than weight discrepancy alone. Building on this, we introduce LG-QEC, a framework that significantly en
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
  - 激活
  - 量化
  - lee26
---

# Compensate, Don't Reconstruct: Parameter- and Data-Efficient 2-bit LLM Quantization

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lee2026compensate` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Geonho Lee, Janghwan Lee, Jungwook Choi |

## 摘要

The substantial memory footprint of large language models (LLMs) remains a key barrier to their on-device deployment. 2-bit quantization is a promising solution; however, current methods impose a difficult trade-off between the high accuracy of training-intensive Quantization-Aware Training (QAT) and the efficiency of lower-performing Quantization Error Compensation (QEC). Our analysis of QEC reveals a critical insight: its effectiveness is more dependent on minimizing activation discrepancy than weight discrepancy alone. Building on this, we introduce LG-QEC, a framework that significantly en

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