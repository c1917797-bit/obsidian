---
type: literature-corpus-entry
citekey: gao2026taming
title: "Taming Massive Activations and Preconditioning Weights: GSR-Guided Quantization for W4A4"
authors:
  - "Hongji Gao"
  - "Xingyu Liao"
  - "Jinhui Yuan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=mUB2N8L0vD"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Large language model inference is constrained by memory and latency. Uniform low‑bit quantization would help, but recent evidence shows massive activations—rare, extremely large, and largely input‑invariant per‑token scalars—rather than generic channel‑wise outliers. Methods that “smooth” activation outliers by migrating scale into weights are therefore less effective under this phenomenon. We address this by explicitly rotating activations and preconditioning weights so that both become easy to quantize.
  
  We first identify that the \textbf{grid-to-standard-deviation ratio (GSR)},
  $
  \rho^X_\t
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
  - 量化
  - gao26
---

# Taming Massive Activations and Preconditioning Weights: GSR-Guided Quantization for W4A4

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `gao2026taming` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Hongji Gao, Xingyu Liao, Jinhui Yuan |

## 摘要

Large language model inference is constrained by memory and latency. Uniform low‑bit quantization would help, but recent evidence shows massive activations—rare, extremely large, and largely input‑invariant per‑token scalars—rather than generic channel‑wise outliers. Methods that “smooth” activation outliers by migrating scale into weights are therefore less effective under this phenomenon. We address this by explicitly rotating activations and preconditioning weights so that both become easy to quantize.

We first identify that the \textbf{grid-to-standard-deviation ratio (GSR)}, 
$
\rho^X_\t

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