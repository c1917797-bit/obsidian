---
type: literature-corpus-entry
citekey: zheng2026group
title: "Group-Wise Optimization for Self-Extensible Codebooks in Vector Quantized Models"
authors:
  - "Hong-Kai Zheng"
  - "Piji Li"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=SI2WqpqPiC"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Vector Quantized Variational Autoencoders (VQ-VAEs) leverage self-supervised learning through reconstruction tasks to represent continuous vectors using the closest vectors in a codebook. However, issues such as codebook collapse persist in the VQ model. To address these issues, existing approaches employ implicit static codebooks or jointly optimize the entire codebook, but these methods constrain the codebook's learning capability, leading to reduced reconstruction quality. In this paper, we propose Group-VQ, which performs group-wise optimization on the codebook. Each group is optimized ind
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
  - 量化
  - zheng26
---

# Group-Wise Optimization for Self-Extensible Codebooks in Vector Quantized Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zheng2026group` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Hong-Kai Zheng, Piji Li |

## 摘要

Vector Quantized Variational Autoencoders (VQ-VAEs) leverage self-supervised learning through reconstruction tasks to represent continuous vectors using the closest vectors in a codebook. However, issues such as codebook collapse persist in the VQ model. To address these issues, existing approaches employ implicit static codebooks or jointly optimize the entire codebook, but these methods constrain the codebook's learning capability, leading to reduced reconstruction quality. In this paper, we propose Group-VQ, which performs group-wise optimization on the codebook. Each group is optimized ind

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