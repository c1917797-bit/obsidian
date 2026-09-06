---
type: literature-corpus-entry
citekey: chickering2026gqa
title: "GQA-$\mu$P: The Maximal Parameterization Update for Grouped Query Attention and Fully Sharded Data Parallel"
authors:
  - "Kyle R. Chickering"
  - "Huijuan Wang"
  - "Mengxi Wu"
  - "Alexander Moreno"
  - "Muhao Chen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=UJB2uOS9MR"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Hyperparameter transfer across model architectures dramatically reduces the amount of compute necessary for tuning large language models (LLMs). The maximal update parameterization (μP) ensures transfer through principled mathematical analysis but can be challenging to derive for new model architectures. Building on the spectral feature-learning view of Yang et al. (2023a), we make
  two advances. First, we promote spectral norm conditions on the weights from a heuristic to the definition of feature learning, and as a consequence arrive at the Complete-P depth and weight-decay scalings without r
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
  - chickering26
---

# GQA-$\mu$P: The Maximal Parameterization Update for Grouped Query Attention and Fully Sharded Data Parallel

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chickering2026gqa` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Kyle R. Chickering, Huijuan Wang, Mengxi Wu |

## 摘要

Hyperparameter transfer across model architectures dramatically reduces the amount of compute necessary for tuning large language models (LLMs). The maximal update parameterization (μP) ensures transfer through principled mathematical analysis but can be challenging to derive for new model architectures. Building on the spectral feature-learning view of Yang et al. (2023a), we make
two advances. First, we promote spectral norm conditions on the weights from a heuristic to the definition of feature learning, and as a consequence arrive at the Complete-P depth and weight-decay scalings without r

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