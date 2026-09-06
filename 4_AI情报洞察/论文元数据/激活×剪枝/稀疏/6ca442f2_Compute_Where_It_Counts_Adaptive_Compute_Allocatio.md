---
type: literature-corpus-entry
citekey: iyer2026compute
title: "Compute Where It Counts: Adaptive Compute Allocation for Large Language Models via Learned Granular Sparsity"
authors:
  - "Niveditha S. Iyer"
  - "Cyris Kissane"
  - "Adam Klein"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=xNeyfH3qZS"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Sparsity-aware inference can dramatically shrink computation requirements by reducing the number of parameters used in each forward pass. Existing methods tend to be heuristic (zeroing activations below fixed thresholds, retaining top-K activations etc). These methods do not directly optimize individual thresholds using gradient-based methods and experience sharp performance degradation beyond 50% sparsity. This paper describes CWIC (Compute Where it Counts), a method that makes sparsity thresholds learnable and contextual. CWIC encourages conditional computation that allows model to designate
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
  - 激活
  - 剪枝/稀疏
  - iyer26
---

# Compute Where It Counts: Adaptive Compute Allocation for Large Language Models via Learned Granular Sparsity

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `iyer2026compute` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Niveditha S. Iyer, Cyris Kissane, Adam Klein |

## 摘要

Sparsity-aware inference can dramatically shrink computation requirements by reducing the number of parameters used in each forward pass. Existing methods tend to be heuristic (zeroing activations below fixed thresholds, retaining top-K activations etc). These methods do not directly optimize individual thresholds using gradient-based methods and experience sharp performance degradation beyond 50% sparsity. This paper describes CWIC (Compute Where it Counts), a method that makes sparsity thresholds learnable and contextual. CWIC encourages conditional computation that allows model to designate

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