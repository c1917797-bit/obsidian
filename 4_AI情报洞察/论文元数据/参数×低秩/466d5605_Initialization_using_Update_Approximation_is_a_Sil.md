---
type: literature-corpus-entry
citekey: ponkshe2026initialization
title: "Initialization using Update Approximation is a Silver Bullet for Extremely Efficient Low-Rank Fine-Tuning"
authors:
  - "Kaustubh Ponkshe"
  - "Raghav Singhal"
  - "Eduard Gorbunov"
  - "Alexey Tumanov"
  - "Samuel Horváth"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=KXJa6pPx0o"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-rank adapters have become standard for efficiently fine-tuning large language models, but they often fall short of achieving the performance of full fine-tuning. We propose a method, **LoRA** **S**ilver **B**ullet or **LoRA-SB**, that approximates full fine-tuning within low-rank subspaces using a carefully designed initialization strategy. We theoretically demonstrate that the architecture of LoRA-XS, which inserts a learnable $r \times r$ matrix between $B$ and $A$ while keeping other matrices fixed, provides the precise conditions needed for this approximation. We leverage its constrain
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
  - ponkshe26
---

# Initialization using Update Approximation is a Silver Bullet for Extremely Efficient Low-Rank Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `ponkshe2026initialization` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Kaustubh Ponkshe, Raghav Singhal, Eduard Gorbunov |

## 摘要

Low-rank adapters have become standard for efficiently fine-tuning large language models, but they often fall short of achieving the performance of full fine-tuning. We propose a method, **LoRA** **S**ilver **B**ullet or **LoRA-SB**, that approximates full fine-tuning within low-rank subspaces using a carefully designed initialization strategy. We theoretically demonstrate that the architecture of LoRA-XS, which inserts a learnable $r \times r$ matrix between $B$ and $A$ while keeping other matrices fixed, provides the precise conditions needed for this approximation. We leverage its constrain

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