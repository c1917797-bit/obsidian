---
type: literature-corpus-entry
citekey: rahman2026hoba
title: "HOBA: Higher-Order Block-Diagonal Attention Unrolling for Transformer"
authors:
  - "Mafizur Rahman"
  - "Lijun Qian"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=2tNlroZztK"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Transformers with 2D self-attention are powerful but computationally intensive, specifically for long sequences due to their quadratic complexity. Therefore, sparse attention methods attempt to alleviate this cost by limiting attention patterns. However, they often compromise explainability and fail to generalize well to global dependencies. Therefore, we propose Higher-Order Block-Diagonal Attention (HOBA), a novel transformer variant that models triplet interactions utilizing 3D attention tensors and block-diagonal unrolling. HOBA can capture richer patterns within and across blocks while ef
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
  - rahman26
---

# HOBA: Higher-Order Block-Diagonal Attention Unrolling for Transformer

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `rahman2026hoba` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Mafizur Rahman, Lijun Qian |

## 摘要

Transformers with 2D self-attention are powerful but computationally intensive, specifically for long sequences due to their quadratic complexity. Therefore, sparse attention methods attempt to alleviate this cost by limiting attention patterns. However, they often compromise explainability and fail to generalize well to global dependencies. Therefore, we propose Higher-Order Block-Diagonal Attention (HOBA), a novel transformer variant that models triplet interactions utilizing 3D attention tensors and block-diagonal unrolling. HOBA can capture richer patterns within and across blocks while ef

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