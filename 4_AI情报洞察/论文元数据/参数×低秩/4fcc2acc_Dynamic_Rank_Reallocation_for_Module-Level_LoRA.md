---
type: literature-corpus-entry
citekey: zhong2026dynamic
title: "Dynamic Rank Reallocation for Module-Level LoRA"
authors:
  - "Xu-Xiang Zhong"
  - "Han-Jia Ye"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=kTUcVs58RH"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-Rank Adaptation (LoRA) and its variants have been widely applied in parameter-efficient fine-tuning of large language models.
  However, most existing approaches assign the same rank to all modules, which limits the representational capacity and adaptation flexibility of the finetuned model.
  Inspired by interference theory in human learning, which posits that forgetting outdated knowledge while allocating more resources to relevant new knowledge facilitates better learning, we propose the Dynamic rank re-Allocation method (DaRA).
  In DaRA, the rank of each module represents a direction in
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
  - zhong26
---

# Dynamic Rank Reallocation for Module-Level LoRA

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhong2026dynamic` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Xu-Xiang Zhong, Han-Jia Ye |

## 摘要

Low-Rank Adaptation (LoRA) and its variants have been widely applied in parameter-efficient fine-tuning of large language models. 
However, most existing approaches assign the same rank to all modules, which limits the representational capacity and adaptation flexibility of the finetuned model. 
Inspired by interference theory in human learning, which posits that forgetting outdated knowledge while allocating more resources to relevant new knowledge facilitates better learning, we propose the Dynamic rank re-Allocation method (DaRA). 
In DaRA, the rank of each module represents a direction in 

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