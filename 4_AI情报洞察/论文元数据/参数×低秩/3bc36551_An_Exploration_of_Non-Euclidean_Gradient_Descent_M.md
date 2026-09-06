---
type: literature-corpus-entry
citekey: crawshaw2026an
title: "An Exploration of Non-Euclidean Gradient Descent: Muon and its Many Variants"
authors:
  - "Michael Crawshaw"
  - "Chirag Modi"
  - "Mingrui Liu"
  - "Robert M. Gower"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=un9AWl7llG"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  To define a steepest descent method over a neural network, we need to choose a norm for each layer, a way to aggregate these norms across layers, and whether to use normalization.
  We systematically explore different alternatives for aggregating norms across layers, both formalizing existing combinations of Adam and the recently proposed Muon as a type of non-Euclidean gradient descent, and deriving new variants of the Muon optimizer.
  Through a comprehensive experimental evaluation of the optimizers within our framework, we find that Muon is sensitive to the choice of learning rate, whereas a n
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
  - crawshaw26
---

# An Exploration of Non-Euclidean Gradient Descent: Muon and its Many Variants

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `crawshaw2026an` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Michael Crawshaw, Chirag Modi, Mingrui Liu |

## 摘要

To define a steepest descent method over a neural network, we need to choose a norm for each layer, a way to aggregate these norms across layers, and whether to use normalization.
We systematically explore different alternatives for aggregating norms across layers, both formalizing existing combinations of Adam and the recently proposed Muon as a type of non-Euclidean gradient descent, and deriving new variants of the Muon optimizer.
Through a comprehensive experimental evaluation of the optimizers within our framework, we find that Muon is sensitive to the choice of learning rate, whereas a n

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