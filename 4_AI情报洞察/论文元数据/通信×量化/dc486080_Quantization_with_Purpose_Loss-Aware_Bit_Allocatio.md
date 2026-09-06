---
type: literature-corpus-entry
citekey: gao2026quantization
title: "Quantization with Purpose: Loss-Aware Bit Allocation for Gradient Compression"
authors:
  - "Fei Gao"
  - "Wang Zhe Mark"
  - "Wenhan Yang"
  - "Long Xu"
  - "LINGYU DUAN"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=0wCTDqkK8I"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Gradient quantization is a critical technique for reducing communication overhead in large-scale distributed training. However, existing methods often employ fixed bit-width quantization or adaptive quantizers optimized with signal-level distortion metrics such as MSE, which poorly correlate with model performance. In this paper, we propose a novel layer-wise bit allocation framework for gradient quantization, formulated under a rate-distortion optimization (RDO) paradigm. Unlike prior approaches, our method introduces a loss-aware distortion metric that directly quantifies the impact of quant
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
  - 通信
  - 量化
  - gao26
---

# Quantization with Purpose: Loss-Aware Bit Allocation for Gradient Compression

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `gao2026quantization` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Fei Gao, Wang Zhe Mark, Wenhan Yang |

## 摘要

Gradient quantization is a critical technique for reducing communication overhead in large-scale distributed training. However, existing methods often employ fixed bit-width quantization or adaptive quantizers optimized with signal-level distortion metrics such as MSE, which poorly correlate with model performance. In this paper, we propose a novel layer-wise bit allocation framework for gradient quantization, formulated under a rate-distortion optimization (RDO) paradigm. Unlike prior approaches, our method introduces a loss-aware distortion metric that directly quantifies the impact of quant

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