---
type: literature-corpus-entry
citekey: teterwak2026op
title: "OP-LoRA: The Blessing of Dimensionality with Overparameterized Low-Rank Adaptation"
authors:
  - "Piotr Teterwak"
  - "Kate Saenko"
  - "Bryan A. Plummer"
  - "Ser-Nam Lim"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=ZBaPU5FL0Z"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-rank adapters (LoRA) enable  finetuning of large models with only a small number of parameters,  reducing storage costs and minimizing the risk of catastrophic forgetting. However, they often suffer from an ill-conditioned loss landscape, leading to difficult optimization.   Prior work addresses these challenges by aligning adapter updates with full finetuning gradients via custom optimizers, but these methods lack the flexibility to accommodate new adapter architectures and are computationally expensive. We instead introduce OP-LoRA, a novel method which replaces each LoRA adapter with we
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
  - teterwak26
---

# OP-LoRA: The Blessing of Dimensionality with Overparameterized Low-Rank Adaptation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `teterwak2026op` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Piotr Teterwak, Kate Saenko, Bryan A. Plummer |

## 摘要

Low-rank adapters (LoRA) enable  finetuning of large models with only a small number of parameters,  reducing storage costs and minimizing the risk of catastrophic forgetting. However, they often suffer from an ill-conditioned loss landscape, leading to difficult optimization.   Prior work addresses these challenges by aligning adapter updates with full finetuning gradients via custom optimizers, but these methods lack the flexibility to accommodate new adapter architectures and are computationally expensive. We instead introduce OP-LoRA, a novel method which replaces each LoRA adapter with we

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