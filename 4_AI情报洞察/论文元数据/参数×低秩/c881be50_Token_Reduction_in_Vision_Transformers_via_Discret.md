---
type: literature-corpus-entry
citekey: marchetti2026token
title: "Token Reduction in Vision Transformers via Discrete Wavelet Decomposition"
authors:
  - "Michele Marchetti"
  - "Davide Traini"
  - "Domenico Ursino"
  - "Luca Virgili"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=jdu24QufJY"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Vision Transformers (ViTs) have achieved remarkable performance across various computer vision tasks, yet their high computational cost remains a significant limitation in many real-world scenarios. As noted in prior studies, decreasing the number of tokens processed by the attention layers of a ViT directly reduces the required operations. Building on this idea, and drawing inspiration from signal processing, we reinterpret the token embeddings of a ViT layer as a signal, which allows us to apply the Discrete Wavelet Transform (DWT) to separate low- and high-frequency components. Guided by th
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
  - marchetti26
---

# Token Reduction in Vision Transformers via Discrete Wavelet Decomposition

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `marchetti2026token` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Michele Marchetti, Davide Traini, Domenico Ursino |

## 摘要

Vision Transformers (ViTs) have achieved remarkable performance across various computer vision tasks, yet their high computational cost remains a significant limitation in many real-world scenarios. As noted in prior studies, decreasing the number of tokens processed by the attention layers of a ViT directly reduces the required operations. Building on this idea, and drawing inspiration from signal processing, we reinterpret the token embeddings of a ViT layer as a signal, which allows us to apply the Discrete Wavelet Transform (DWT) to separate low- and high-frequency components. Guided by th

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