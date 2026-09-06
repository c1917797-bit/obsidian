---
type: literature-corpus-entry
citekey: li2026antkv
title: "AnTKV: Anchor Token-Aware Ultra-Low-Bit Vector Quantization for KV Cache in Large Language Models"
authors:
  - "Zeyu Li"
  - "Xiao Chuanfu"
  - "Yang Wang"
  - "Xiang Liu"
  - "Zhenheng Tang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=9gqNsQeW8F"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Quantization has emerged as an effective and lightweight solution to reduce the memory footprint of the KV cache in Large Language Models. Nevertheless, minimizing the accuracy degradation caused by ultra-low-bit KV cache quantization remains a significant challenge. While scalar quantization is constrained by 1-bit bound, vector quantization exploits intra-vector correlations and enables sub-bit regimes, making it more suitable for ultra-low-bit quantization. To further mitigate quantization-induced degradation, we reveal that the degradation is highly uneven across tokens in attention qualit
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
  - KV
  - 量化
  - li26
---

# AnTKV: Anchor Token-Aware Ultra-Low-Bit Vector Quantization for KV Cache in Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026antkv` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Zeyu Li, Xiao Chuanfu, Yang Wang |

## 摘要

Quantization has emerged as an effective and lightweight solution to reduce the memory footprint of the KV cache in Large Language Models. Nevertheless, minimizing the accuracy degradation caused by ultra-low-bit KV cache quantization remains a significant challenge. While scalar quantization is constrained by 1-bit bound, vector quantization exploits intra-vector correlations and enables sub-bit regimes, making it more suitable for ultra-low-bit quantization. To further mitigate quantization-induced degradation, we reveal that the degradation is highly uneven across tokens in attention qualit

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