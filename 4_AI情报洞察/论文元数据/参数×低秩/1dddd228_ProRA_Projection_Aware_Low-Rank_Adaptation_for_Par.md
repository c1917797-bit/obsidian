---
type: literature-corpus-entry
citekey: mishra2026prora
title: "ProRA: Projection Aware Low-Rank Adaptation for Parameter Efficient Fine-Tuning"
authors:
  - "Ritik Mishra"
  - "M. Tanveer"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=xuT6MSjLS1"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Despite the remarkable success of large language models (LLMs) across diverse tasks, the computational cost of fine-tuning them remains high. Low-Rank Adaptation (LoRA) addresses this by updating through the product of two low rank matrices. LoRA initializes low-rank matrices using random Gaussian noise and zeros, while keeping the pretrained weights frozen. However, such random and zero initialization leads to slow convergence and limits expressiveness. To overcome these limitations, we propose Projection Aware Low-Rank Adaptation (ProRA). ProRA initializes adapter matrices by projecting the
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
  - mishra26
---

# ProRA: Projection Aware Low-Rank Adaptation for Parameter Efficient Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `mishra2026prora` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Ritik Mishra, M. Tanveer |

## 摘要

Despite the remarkable success of large language models (LLMs) across diverse tasks, the computational cost of fine-tuning them remains high. Low-Rank Adaptation (LoRA) addresses this by updating through the product of two low rank matrices. LoRA initializes low-rank matrices using random Gaussian noise and zeros, while keeping the pretrained weights frozen. However, such random and zero initialization leads to slow convergence and limits expressiveness. To overcome these limitations, we propose Projection Aware Low-Rank Adaptation (ProRA). ProRA initializes adapter matrices by projecting the 

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