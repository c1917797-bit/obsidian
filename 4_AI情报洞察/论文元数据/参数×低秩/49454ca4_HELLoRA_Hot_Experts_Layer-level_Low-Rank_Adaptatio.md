---
type: literature-corpus-entry
citekey: wei2026hellora
title: "HELLoRA: Hot Experts Layer-level Low-Rank Adaptation for MOE Model"
authors:
  - "JIA WEI"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=CsHahbRAFZ"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-Rank Adaptation (LoRA) has become the dominant paradigm for Parameter-Efficient Fine-Tuning (PEFT) of large language models. However, most prior work focuses on dense architectures. In contrast, Mixture-of-Experts (MoE) models—now a de facto standard—scale parameter counts while keeping per-token compute nearly constant, creating new challenges for LoRA: how to minimize trainable parameters and maximize fine-tuning throughput without sacrificing quality. We propose Hot-Experts Layer-level Low-Rank Adaptation ($\textbf{HELLoRA}$), a simple yet effective scheme that attaches LoRA modules onl
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
  - wei26
---

# HELLoRA: Hot Experts Layer-level Low-Rank Adaptation for MOE Model

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wei2026hellora` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | JIA WEI |

## 摘要

Low-Rank Adaptation (LoRA) has become the dominant paradigm for Parameter-Efficient Fine-Tuning (PEFT) of large language models. However, most prior work focuses on dense architectures. In contrast, Mixture-of-Experts (MoE) models—now a de facto standard—scale parameter counts while keeping per-token compute nearly constant, creating new challenges for LoRA: how to minimize trainable parameters and maximize fine-tuning throughput without sacrificing quality. We propose Hot-Experts Layer-level Low-Rank Adaptation ($\textbf{HELLoRA}$), a simple yet effective scheme that attaches LoRA modules onl

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