---
type: literature-corpus-entry
citekey: mark2026blob
title: "BLOB-Q: Boosting Low Bit ViT Quantization via Global Optimization on Model Distortion"
authors:
  - "Wang Zhe Mark"
  - "Kaixin Xu"
  - "Xue Geng"
  - "Fen Fang"
  - "Mohamed M. Sabry Aly"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=xjWxWFYxzA"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  In this paper, we present a novel Mixed-Precision Post Training Quantization (PTQ) approach for Vision Transformers (ViTs). Our approach aims to minimize the output distortion caused by quantization, and thus can maximally maintain the accuracy of ViT models even quantized to low bit widths. Different with prior works which typically optimize the output error of current layer (layer distortion), when performing quantization, our approach directly minimizes the output error of the last layer of the model (model distortion). As model distortion is highly related to accuracy, our approach can max
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
  - mark26
---

# BLOB-Q: Boosting Low Bit ViT Quantization via Global Optimization on Model Distortion

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `mark2026blob` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Wang Zhe Mark, Kaixin Xu, Xue Geng |

## 摘要

In this paper, we present a novel Mixed-Precision Post Training Quantization (PTQ) approach for Vision Transformers (ViTs). Our approach aims to minimize the output distortion caused by quantization, and thus can maximally maintain the accuracy of ViT models even quantized to low bit widths. Different with prior works which typically optimize the output error of current layer (layer distortion), when performing quantization, our approach directly minimizes the output error of the last layer of the model (model distortion). As model distortion is highly related to accuracy, our approach can max

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