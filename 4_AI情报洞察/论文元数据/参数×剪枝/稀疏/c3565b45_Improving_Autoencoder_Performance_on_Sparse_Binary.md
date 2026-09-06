---
type: literature-corpus-entry
citekey: selani2026improving
title: "Improving  Autoencoder Performance on Sparse Binary Data through Sparsity-Aware Loss Functions"
authors:
  - "Daniyal Selani"
  - "Rachel Knevel"
  - "Erik B van den Akker"
  - "Marcel Reinders"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=aKltXivka4"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Conventional reconstruction losses for autoencoders such as mean squared error (MSE) and binary cross-entropy (BCE) are poorly suited for sparse binary data. These measures can achieve deceptively low loss by trivially predicting the dominant zeros, while failing to capture the rare but informative non-zero entries. Prior work has primarily focused on architectural modifications or training heuristics to address this issue, leaving the design of loss functions largely overlooked. In this work, we shift focus to the reconstruction loss itself, exploring sparsity-aware reconstruction losses by e
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
  - 剪枝/稀疏
  - selani26
---

# Improving  Autoencoder Performance on Sparse Binary Data through Sparsity-Aware Loss Functions

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `selani2026improving` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Daniyal Selani, Rachel Knevel, Erik B van den Akker |

## 摘要

Conventional reconstruction losses for autoencoders such as mean squared error (MSE) and binary cross-entropy (BCE) are poorly suited for sparse binary data. These measures can achieve deceptively low loss by trivially predicting the dominant zeros, while failing to capture the rare but informative non-zero entries. Prior work has primarily focused on architectural modifications or training heuristics to address this issue, leaving the design of loss functions largely overlooked. In this work, we shift focus to the reconstruction loss itself, exploring sparsity-aware reconstruction losses by e

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