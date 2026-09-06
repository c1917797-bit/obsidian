---
type: literature-corpus-entry
citekey: raj2026quic
title: "QuIC: Quantum-Inspired Compound Adapters for Parameter Efficient Fine-Tuning"
authors:
  - "Snehal Raj"
  - "Brian Coyle"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=OJ3tzHSIis"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Scaling full fine-tuning of large foundation models strains GPU memory and training time. Parameter Efficient Fine-Tuning (PEFT) methods address this issue via adapter modules which update only a small subset of model parameters. In this work, we introduce Quantum-Inspired Compound Adapters (QuIC Adapters), a PEFT approach inspired from Hamming-weight preserving quantum circuits that can effectively fine-tune a model using less than $0.02\%$ memory footprint of the base model. QuIC adapters preserve pretrained representations by enforcing orthogonality in weight parameters, and have native dep
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
  - raj26
---

# QuIC: Quantum-Inspired Compound Adapters for Parameter Efficient Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `raj2026quic` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Snehal Raj, Brian Coyle |

## 摘要

Scaling full fine-tuning of large foundation models strains GPU memory and training time. Parameter Efficient Fine-Tuning (PEFT) methods address this issue via adapter modules which update only a small subset of model parameters. In this work, we introduce Quantum-Inspired Compound Adapters (QuIC Adapters), a PEFT approach inspired from Hamming-weight preserving quantum circuits that can effectively fine-tune a model using less than $0.02\%$ memory footprint of the base model. QuIC adapters preserve pretrained representations by enforcing orthogonality in weight parameters, and have native dep

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