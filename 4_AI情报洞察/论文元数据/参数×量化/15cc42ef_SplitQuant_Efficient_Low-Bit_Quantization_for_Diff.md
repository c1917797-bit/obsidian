---
type: literature-corpus-entry
citekey: ma2026splitquant
title: "SplitQuant: Efficient Low-Bit Quantization for Diffusion Transformers via In-Channel Dimension Splitting"
authors:
  - "Yuexiao Ma"
  - "Xinxiong Wu"
  - "Xiwei Xu"
  - "Feng Ling"
  - "Xiawu Zheng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=kBRXrAkqR2"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Diffusion models currently dominate the field of image generation. However, generating high-resolution images requires larger-scale diffusion models that consume substantial computational resources and memory during inference. While post-training quantization offers a promising solution to reduce computational costs and memory usage through low-precision representations, existing approaches face significant challenges when applied to diffusion models. Unlike large language models that are memory-bound, \textbf{Di}ffusion \textbf{T}ransformers (DiT) are compute-intensive during inference. Conse
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
  - ma26
---

# SplitQuant: Efficient Low-Bit Quantization for Diffusion Transformers via In-Channel Dimension Splitting

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `ma2026splitquant` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yuexiao Ma, Xinxiong Wu, Xiwei Xu |

## 摘要

Diffusion models currently dominate the field of image generation. However, generating high-resolution images requires larger-scale diffusion models that consume substantial computational resources and memory during inference. While post-training quantization offers a promising solution to reduce computational costs and memory usage through low-precision representations, existing approaches face significant challenges when applied to diffusion models. Unlike large language models that are memory-bound, \textbf{Di}ffusion \textbf{T}ransformers (DiT) are compute-intensive during inference. Conse

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