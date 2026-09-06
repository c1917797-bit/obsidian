---
type: literature-corpus-entry
citekey: namkung2026rapa
title: "RAPA: Recursively Aligned Pathway Adaptation of Large Language Models"
authors:
  - "Sol Namkung"
  - "Sunghyeon Woo"
  - "Inho Jeong"
  - "Dongsuk Jeon"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=QTNkVX15o5"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Parameter-Efficient Fine-Tuning (PEFT) adapts large language models (LLMs) by training only a small fraction of parameters. Adapter-based approaches reduce compute per step but introduce practical overhead from the additional adapter path (e.g., extra kernel launches and activation storage). Adapter-free approaches avoid this structural overhead by directly updating pretrained weights; however, per-layer random index selection can fragment the trainable subspace, attenuating gradient flow and limiting accuracy. We propose **Recursively Aligned Pathway Adaptation (RAPA)**, an adapter-free PEFT
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
  - namkung26
---

# RAPA: Recursively Aligned Pathway Adaptation of Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `namkung2026rapa` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Sol Namkung, Sunghyeon Woo, Inho Jeong |

## 摘要

Parameter-Efficient Fine-Tuning (PEFT) adapts large language models (LLMs) by training only a small fraction of parameters. Adapter-based approaches reduce compute per step but introduce practical overhead from the additional adapter path (e.g., extra kernel launches and activation storage). Adapter-free approaches avoid this structural overhead by directly updating pretrained weights; however, per-layer random index selection can fragment the trainable subspace, attenuating gradient flow and limiting accuracy. We propose **Recursively Aligned Pathway Adaptation (RAPA)**, an adapter-free PEFT 

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