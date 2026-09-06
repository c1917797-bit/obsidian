---
type: literature-corpus-entry
citekey: lai2026rs
title: "RS-MoE: Collaborative Compression for Mixture-of-Experts LLMs based on Low-Rank and Sparse Approximation"
authors:
  - "Jiajun Lai"
  - "Shijie Li"
  - "Huaiguang Jiang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=5SQbPbCU6P"
pdf_url: ""
object: 激活
method: 低秩
cell: "激活×低秩"
all_objects: []
all_methods: []
abstract: |
  Mixture-of-Experts (MoE) based Large Language Models (LLMs), despite their computational efficiency, face significant storage and memory challenges, which hinder their deployment on edge devices.
  However, existing methods primarily focus on compressing at the expert level, resulting in the loss of specialized knowledge.
  To address these challenges, we propose a novel framework termed RS-MoE, which compresses MoE models by collaboratively decomposing the weights of each expert into low-rank and sparse components.
  Through a preliminary investigation of the relationship between activations and
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
  - 低秩
  - lai26
---

# RS-MoE: Collaborative Compression for Mixture-of-Experts LLMs based on Low-Rank and Sparse Approximation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lai2026rs` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×低秩 |
| **来源** | openreview |
| **作者** | Jiajun Lai, Shijie Li, Huaiguang Jiang |

## 摘要

Mixture-of-Experts (MoE) based Large Language Models (LLMs), despite their computational efficiency, face significant storage and memory challenges, which hinder their deployment on edge devices. 
However, existing methods primarily focus on compressing at the expert level, resulting in the loss of specialized knowledge. 
To address these challenges, we propose a novel framework termed RS-MoE, which compresses MoE models by collaboratively decomposing the weights of each expert into low-rank and sparse components. 
Through a preliminary investigation of the relationship between activations and

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