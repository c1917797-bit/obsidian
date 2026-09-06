---
type: literature-corpus-entry
citekey: chang2026proda
title: "ProDA: Profile-Decomposed Adaptation for Capturing the Structured Residual in Low-Rank Updates"
authors:
  - "Yupeng Chang"
  - "Yuan Wu"
  - "Yi Chang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=e3uQFSdJP0"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-Rank Adaptation (LoRA), a cornerstone of parameter-efficient fine-tuning (PEFT), relies on the core assumption that weight updates are inherently low-rank. We challenge this premise, revealing that this low-rank approximation systematically neglects a significant and highly structured residual, which we term the **missing profile**. To harness this insight, we introduce Profile-Decomposed Adaptation (ProDA), a novel method that captures this residual using highly efficient, axis-aligned vectors. Critically, instead of treating this component as a static error to be corrected, ProDA integra
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
  - chang26
---

# ProDA: Profile-Decomposed Adaptation for Capturing the Structured Residual in Low-Rank Updates

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chang2026proda` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Yupeng Chang, Yuan Wu, Yi Chang |

## 摘要

Low-Rank Adaptation (LoRA), a cornerstone of parameter-efficient fine-tuning (PEFT), relies on the core assumption that weight updates are inherently low-rank. We challenge this premise, revealing that this low-rank approximation systematically neglects a significant and highly structured residual, which we term the **missing profile**. To harness this insight, we introduce Profile-Decomposed Adaptation (ProDA), a novel method that captures this residual using highly efficient, axis-aligned vectors. Critically, instead of treating this component as a static error to be corrected, ProDA integra

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