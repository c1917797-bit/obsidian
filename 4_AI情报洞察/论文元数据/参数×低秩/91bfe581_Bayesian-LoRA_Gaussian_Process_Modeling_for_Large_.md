---
type: literature-corpus-entry
citekey: lin2026bayesian
title: "Bayesian-LoRA: Gaussian Process Modeling for Large Language Models"
authors:
  - "Moule Lin"
  - "Shuhao Guan"
  - "Andrea Patane"
  - "David Gregg"
  - "Goetz Botterweck"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=MalCcTWn7j"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Pre-trained LLMs are often reasonably calibrated on pre-training like distributions, but fine-tuning them for specific domains often causes a substantial deterioration in calibration, especially on small datasets, leading to overconfident predictions. Although existing Bayesian approaches alleviate this degradation, their computational cost is prohibitive at LLM scale. In this work, we introduce Bayesian-LoRA, which applies a Sparse Gaussian Process (SGP) to the Low-Rank Adaptation (LoRA) fine-tuning approach and integrates a normalizing flow to stabilize the training process, thereby substant
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
  - 低秩
  - lin26
---

# Bayesian-LoRA: Gaussian Process Modeling for Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lin2026bayesian` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Moule Lin, Shuhao Guan, Andrea Patane |

## 摘要

Pre-trained LLMs are often reasonably calibrated on pre-training like distributions, but fine-tuning them for specific domains often causes a substantial deterioration in calibration, especially on small datasets, leading to overconfident predictions. Although existing Bayesian approaches alleviate this degradation, their computational cost is prohibitive at LLM scale. In this work, we introduce Bayesian-LoRA, which applies a Sparse Gaussian Process (SGP) to the Low-Rank Adaptation (LoRA) fine-tuning approach and integrates a normalizing flow to stabilize the training process, thereby substant

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