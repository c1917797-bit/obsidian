---
type: literature-corpus-entry
citekey: haller2026empirical
title: "Empirical Evaluation of Knowledge Distillation from Transformers to Subquadratic Language Models"
authors:
  - "Patrick Haller"
  - "Jonas Golde"
  - "Alan Akbik"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=MnBYX84F6j"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Knowledge distillation is a widely used technique for compressing large language models (LLMs), in which a smaller student model is trained to mimic a larger teacher model. Typically, both the teacher and student models are Transformer-based architectures, leveraging softmax attention for sequence modeling. However, the quadratic complexity of self-attention during inference remains a significant bottleneck, motivating the exploration of subquadratic alternatives such as structured state-space models (SSMs), linear attention, and recurrent architectures.
  In this work, we systematically evaluat
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
  - haller26
---

# Empirical Evaluation of Knowledge Distillation from Transformers to Subquadratic Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `haller2026empirical` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Patrick Haller, Jonas Golde, Alan Akbik |

## 摘要

Knowledge distillation is a widely used technique for compressing large language models (LLMs), in which a smaller student model is trained to mimic a larger teacher model. Typically, both the teacher and student models are Transformer-based architectures, leveraging softmax attention for sequence modeling. However, the quadratic complexity of self-attention during inference remains a significant bottleneck, motivating the exploration of subquadratic alternatives such as structured state-space models (SSMs), linear attention, and recurrent architectures.
In this work, we systematically evaluat

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