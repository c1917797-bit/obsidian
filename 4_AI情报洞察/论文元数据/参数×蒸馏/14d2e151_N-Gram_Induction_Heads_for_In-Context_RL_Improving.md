---
type: literature-corpus-entry
citekey: zisman2026n
title: "N-Gram Induction Heads for In-Context RL: Improving Stability and Reducing Data Needs"
authors:
  - "Ilya Zisman"
  - "Alexander Nikulin"
  - "Viacheslav Sinii"
  - "Denis Tarasov"
  - "Lyubaykin Nikita"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=7gLNA6nT5d"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  In-context learning allows models like transformers to adapt to new tasks from a few examples without updating their weights, a desirable trait for reinforcement learning (RL). However, existing in-context RL methods, such as Algorithm Distillation (AD), demand large, carefully curated datasets and can be unstable and costly to train due to the transient nature of in-context learning abilities. In this work, we integrated the n-gram induction heads into transformers for in-context RL. By incorporating these n-gram attention patterns, we considerably reduced the amount of data required for gene
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
  - zisman26
---

# N-Gram Induction Heads for In-Context RL: Improving Stability and Reducing Data Needs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zisman2026n` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Ilya Zisman, Alexander Nikulin, Viacheslav Sinii |

## 摘要

In-context learning allows models like transformers to adapt to new tasks from a few examples without updating their weights, a desirable trait for reinforcement learning (RL). However, existing in-context RL methods, such as Algorithm Distillation (AD), demand large, carefully curated datasets and can be unstable and costly to train due to the transient nature of in-context learning abilities. In this work, we integrated the n-gram induction heads into transformers for in-context RL. By incorporating these n-gram attention patterns, we considerably reduced the amount of data required for gene

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