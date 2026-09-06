---
type: literature-corpus-entry
citekey: lee2026unified
title: "Unified Progressive Quantization toward 2-bit Instruction-Tuned LLMs"
authors:
  - "Jung Hyun Lee"
  - "Seungjae Shin"
  - "Vinnam Kim"
  - "Jaeseong You"
  - "An Chen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=7133LhmfQx"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  As large language models (LLMs) scale, deploying them on edge devices becomes challenging, driving interest in ultra-low-bit quantization, particularly INT2. Through quantization error bound derivation, we identify two key factors for effective 2‑bit quantization of instruction-tuned LLMs: (1) progressive quantization is critical, introducing an intermediate 4‑bit stage—quantizing FP16 to INT4 before reducing to INT2; (2) quantization‑aware training (QAT) should minimize the divergence between INT2 and FP16 output distributions, rather than optimizing with next‑token prediction loss, to retain
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
  - lee26
---

# Unified Progressive Quantization toward 2-bit Instruction-Tuned LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lee2026unified` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Jung Hyun Lee, Seungjae Shin, Vinnam Kim |

## 摘要

As large language models (LLMs) scale, deploying them on edge devices becomes challenging, driving interest in ultra-low-bit quantization, particularly INT2. Through quantization error bound derivation, we identify two key factors for effective 2‑bit quantization of instruction-tuned LLMs: (1) progressive quantization is critical, introducing an intermediate 4‑bit stage—quantizing FP16 to INT4 before reducing to INT2; (2) quantization‑aware training (QAT) should minimize the divergence between INT2 and FP16 output distributions, rather than optimizing with next‑token prediction loss, to retain

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