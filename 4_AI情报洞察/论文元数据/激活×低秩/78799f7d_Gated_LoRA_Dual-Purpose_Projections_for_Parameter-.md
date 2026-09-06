---
type: literature-corpus-entry
citekey: eom2026gated
title: "Gated LoRA: Dual-Purpose Projections for Parameter-Efficient Mini-Expert Fine-Tuning"
authors:
  - "SooHwan Eom"
  - "Hee Suk Yoon"
  - "Eunseop Yoon"
  - "Mark A. Hasegawa-Johnson"
  - "Chang D. Yoo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=ZiBDVotA7g"
pdf_url: ""
object: 激活
method: 低秩
cell: "激活×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-Rank Adaptation (LoRA) is widely used for parameter-efficient fine-tuning (PEFT) of large language models (LLMs). Yet, its uniform activation of all rank components can lead to task interference and hinder generalization when fine-tuning a model to multiple tasks and datasets. We introduce Gated LoRA, which employs input-dependent gating to selectively activate only the most relevant rank-1 directions. The key design is a dual‑purpose projection: the same matrices that compute LoRA features also drive rank selection, adding no extra trainable parameters. Across nine language understanding
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
  - 低秩
  - eom26
---

# Gated LoRA: Dual-Purpose Projections for Parameter-Efficient Mini-Expert Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `eom2026gated` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×低秩 |
| **来源** | openreview |
| **作者** | SooHwan Eom, Hee Suk Yoon, Eunseop Yoon |

## 摘要

Low-Rank Adaptation (LoRA) is widely used for parameter-efficient fine-tuning (PEFT) of large language models (LLMs). Yet, its uniform activation of all rank components can lead to task interference and hinder generalization when fine-tuning a model to multiple tasks and datasets. We introduce Gated LoRA, which employs input-dependent gating to selectively activate only the most relevant rank-1 directions. The key design is a dual‑purpose projection: the same matrices that compute LoRA features also drive rank selection, adding no extra trainable parameters. Across nine language understanding 

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