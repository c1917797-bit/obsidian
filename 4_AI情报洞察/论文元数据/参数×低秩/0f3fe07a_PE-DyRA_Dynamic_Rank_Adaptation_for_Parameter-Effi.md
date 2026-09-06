---
type: literature-corpus-entry
citekey: zhao2026pe
title: "PE-DyRA: Dynamic Rank Adaptation for Parameter-Efficient  Fine-Tuning via Importance-Aware Pruning and Expansion"
authors:
  - "Xing Zhao"
  - "Liu Yang"
  - "Xi-Le Zhao"
  - "Yu Wang"
  - "Qinghua Hu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Lla4eFlDJu"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  As large language models grow in scale, full-parameter fine-tuning for downstream tasks incurs substantial computational and storage costs. Low-Rank Adaptation (LoRA) provides a parameter-efficient paradigm for model adaptation, but its fixed-rank allocation cannot adapt to the heterogeneous importance of different layers or the evolving requirements across training stages, resulting in either redundancy or insufficient capacity. In this paper, we introduce Dynamic Rank Adaptation via Importance-Aware Pruning and Expansion (PE-DyRA), a novel framework that dynamically allocates ranks through i
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
  - zhao26
---

# PE-DyRA: Dynamic Rank Adaptation for Parameter-Efficient  Fine-Tuning via Importance-Aware Pruning and Expansion

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhao2026pe` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Xing Zhao, Liu Yang, Xi-Le Zhao |

## 摘要

As large language models grow in scale, full-parameter fine-tuning for downstream tasks incurs substantial computational and storage costs. Low-Rank Adaptation (LoRA) provides a parameter-efficient paradigm for model adaptation, but its fixed-rank allocation cannot adapt to the heterogeneous importance of different layers or the evolving requirements across training stages, resulting in either redundancy or insufficient capacity. In this paper, we introduce Dynamic Rank Adaptation via Importance-Aware Pruning and Expansion (PE-DyRA), a novel framework that dynamically allocates ranks through i

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