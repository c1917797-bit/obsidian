---
type: literature-corpus-entry
citekey: gao2026accurate
title: "Accurate and Efficient Singular Value Decomposition For LLMs via Decay-aware Rank Allocation and Feature-Preserved Weight Update"
authors:
  - "Xiangxiang Gao"
  - "Weisheng Xie"
  - "Zhuo Chen"
  - "Chen Hang"
  - "Yuhan Lin"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=TuzsCiHocG"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Singular Value Decomposition (SVD) provides a hardware-agnostic and effective paradigm for compressing and accelerating Large Language Models (LLMs) by decomposing and truncating weight matrices, followed by weight updates to restore accuracy. However, SVD-based compression faces two major challenges:**(1) Rank Selection Problem:** Optimizing truncation and update ranks constitutes a high-dimensional combinatorial problem. Existing solutions rely on computationally expensive search, leading to both suboptimal performance and diminished efficiency. **(2) Limited Accuracy Restoration:** The sequ
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
  - gao26
---

# Accurate and Efficient Singular Value Decomposition For LLMs via Decay-aware Rank Allocation and Feature-Preserved Weight Update

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `gao2026accurate` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Xiangxiang Gao, Weisheng Xie, Zhuo Chen |

## 摘要

Singular Value Decomposition (SVD) provides a hardware-agnostic and effective paradigm for compressing and accelerating Large Language Models (LLMs) by decomposing and truncating weight matrices, followed by weight updates to restore accuracy. However, SVD-based compression faces two major challenges:**(1) Rank Selection Problem:** Optimizing truncation and update ranks constitutes a high-dimensional combinatorial problem. Existing solutions rely on computationally expensive search, leading to both suboptimal performance and diminished efficiency. **(2) Limited Accuracy Restoration:** The sequ

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