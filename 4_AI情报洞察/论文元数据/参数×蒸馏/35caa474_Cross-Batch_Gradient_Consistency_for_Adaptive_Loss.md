---
type: literature-corpus-entry
citekey: xue2026cross
title: "Cross-Batch Gradient Consistency for Adaptive Loss Balancing in Knowledge Distillation"
authors:
  - "Yuhao Xue"
  - "Guosheng Hu"
  - "Wei-Hong Li"
  - "Zhifei Zhang"
  - "Cairong Zhao"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Z0sFCSLw6s"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Knowledge distillation (KD) is a widely used approach for compressing large neural networks into compact student models by combining supervised learning with teacher-guided alignment. While recent studies have attempted to improve KD through adaptive weighting between the supervised and distillation objectives, most existing methods determine weights solely from gradients computed on a single mini-batch. This batch-local perspective neglects the crucial requirement that student updates should generalize across unseen data, often resulting in gradient conflicts, unstable training dynamics, and
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
  - 蒸馏
  - xue26
---

# Cross-Batch Gradient Consistency for Adaptive Loss Balancing in Knowledge Distillation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xue2026cross` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Yuhao Xue, Guosheng Hu, Wei-Hong Li |

## 摘要

Knowledge distillation (KD) is a widely used approach for compressing large neural networks into compact student models by combining supervised learning with teacher-guided alignment. While recent studies have attempted to improve KD through adaptive weighting between the supervised and distillation objectives, most existing methods determine weights solely from gradients computed on a single mini-batch. This batch-local perspective neglects the crucial requirement that student updates should generalize across unseen data, often resulting in gradient conflicts, unstable training dynamics, and 

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