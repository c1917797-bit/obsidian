---
type: literature-corpus-entry
citekey: anonndstealing
title: "Stealing User Prompts from Mixture-of-Experts Models"
authors: []
year: ""
venue: iclr2025
venue_type: conference
arxiv_id: ""
doi: ""
url: ""
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Mixture of Expert (MoE) models improve the efficiency and scalability of dense language models by \emph{routing} each token to a small number of experts in each layer of the model. In this paper, we show how an adversary that can arrange for their queries to appear in the same batch of examples as a victim's queries can exploit expert-choice routing to the full disclosure of a victim's prompt. We successfully demonstrate the effectiveness of this attack on a two-layered Mixtral model. Our result
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "arxiv"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - 参数
  - 量化
---

# Stealing User Prompts from Mixture-of-Experts Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `anonndstealing` |
| **年份** | N/A |
| **会议/期刊** | iclr2025 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | arXiv |
| **作者** | N/A |

## 摘要

Mixture of Expert (MoE) models improve the efficiency and scalability of dense language models by \emph{routing} each token to a small number of experts in each layer of the model. In this paper, we show how an adversary that can arrange for their queries to appear in the same batch of examples as a victim's queries can exploit expert-choice routing to the full disclosure of a victim's prompt. We successfully demonstrate the effectiveness of this attack on a two-layered Mixtral model. Our result

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
*生成日期: 2026-07-06 | 来源: arXiv*