---
type: literature-corpus-entry
citekey: liu2026from
title: "From Sparse to Structured: A New Paradigm for Gradient-Based Parameter-Efficient Fine-Tuning"
authors:
  - "Xuanbo Liu"
  - "Liu Liu"
  - "Fuxiang Wu"
  - "Fusheng Hao"
  - "Xianglong Liu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=9nOpFdYJez"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Large pre-trained models have demonstrated extensive applications across various fields. However, fine-tuning these models for specific downstream tasks demands significant computational resources and storage. One fine-tuning method, gradient-based parameter selection (GPS), focuses on fine-tuning only the parameters with high gradients in each neuron, thereby reducing the number of training parameters. Nevertheless, this approach increases computational resource requirements and storage demands. In this paper, we propose an efficient gradient-based and regularized fine-tuning method (GRFT) th
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
  - liu26
---

# From Sparse to Structured: A New Paradigm for Gradient-Based Parameter-Efficient Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026from` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Xuanbo Liu, Liu Liu, Fuxiang Wu |

## 摘要

Large pre-trained models have demonstrated extensive applications across various fields. However, fine-tuning these models for specific downstream tasks demands significant computational resources and storage. One fine-tuning method, gradient-based parameter selection (GPS), focuses on fine-tuning only the parameters with high gradients in each neuron, thereby reducing the number of training parameters. Nevertheless, this approach increases computational resource requirements and storage demands. In this paper, we propose an efficient gradient-based and regularized fine-tuning method (GRFT) th

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