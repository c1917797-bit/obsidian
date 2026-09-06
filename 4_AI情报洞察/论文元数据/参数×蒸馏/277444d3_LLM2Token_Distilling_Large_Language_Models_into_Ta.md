---
type: literature-corpus-entry
citekey: zou2026llm
title: "LLM2Token: Distilling Large Language Models into Task-Specific Tokenizer"
authors:
  - "Ziyi Zou"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=gCUW1T9scF"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  We present LLM to Tokenizer, a new distrilling method that preserves the prior knowledge from LLMs in the form of tokenizer, diverging from neural network based methods. This simple, intuitive method allows strong performance even only using one-hot encoding and a simgle-layer logistic regression. Based on the generated tokenizer, without any pre-training, surpressing GPT-2 with just 0.01\% parameters. On event recognition tasks, the L2T method achieves an F1 score of 0.408 while using only 0.1\% of the parameters compared to previous models. We also observed that stronger foundation models le
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
  - zou26
---

# LLM2Token: Distilling Large Language Models into Task-Specific Tokenizer

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zou2026llm` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Ziyi Zou |

## 摘要

We present LLM to Tokenizer, a new distrilling method that preserves the prior knowledge from LLMs in the form of tokenizer, diverging from neural network based methods. This simple, intuitive method allows strong performance even only using one-hot encoding and a simgle-layer logistic regression. Based on the generated tokenizer, without any pre-training, surpressing GPT-2 with just 0.01\% parameters. On event recognition tasks, the L2T method achieves an F1 score of 0.408 while using only 0.1\% of the parameters compared to previous models. We also observed that stronger foundation models le

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