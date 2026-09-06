---
type: literature-corpus-entry
citekey: huang2026oar
title: "OAR: Training Quantization-Friendly Object Detectors via Outlier-Aware Restriction"
authors:
  - "Long Huang"
  - "Yifan Cui"
  - "Zhiwei Dong"
  - "Xu-Cheng Yin"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=TtALfYr3Hp"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Model quantization is widely employed to reduce computational resource usage during inference, often in conjunction with specialized hardware system for acceleration. While modern object detectors perform well at compact bit-widths (e.g., 8-bit), further quantization to ultra-low bit-widths (e.g., 4 or 3 bits) remains challenging. We identify the presence of outliers in the statistical distribution of activations in pre-trained detectors as a key obstacle, as such outliers expand the dynamic range and increase quantization error. Moreover, we observe significant numerical discrepancies in acti
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
  - huang26
---

# OAR: Training Quantization-Friendly Object Detectors via Outlier-Aware Restriction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `huang2026oar` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Long Huang, Yifan Cui, Zhiwei Dong |

## 摘要

Model quantization is widely employed to reduce computational resource usage during inference, often in conjunction with specialized hardware system for acceleration. While modern object detectors perform well at compact bit-widths (e.g., 8-bit), further quantization to ultra-low bit-widths (e.g., 4 or 3 bits) remains challenging. We identify the presence of outliers in the statistical distribution of activations in pre-trained detectors as a key obstacle, as such outliers expand the dynamic range and increase quantization error. Moreover, we observe significant numerical discrepancies in acti

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