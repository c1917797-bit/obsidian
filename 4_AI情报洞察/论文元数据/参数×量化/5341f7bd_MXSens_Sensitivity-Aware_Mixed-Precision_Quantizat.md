---
type: literature-corpus-entry
citekey: harma2026mxsens
title: "MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference"
authors:
  - "Simla Burcu Harma"
  - "Danila Mishin"
  - "Zhengyuan Su"
  - "Ayan Chakraborty"
  - "Dongho Ha"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=883lVZEH6m"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  4-bit quantization enables efficient LLM inference, but suffers from significant accuracy degradation due to outliers. Prior work addresses this problem via data rotation or mixed-precision integer quantization, but often relies on software-managed scaling and frequent dequantization, incurring substantial overhead. Microscaling formats, such as MXINT, eliminate these inefficiencies by encoding scales in hardware, yet remain incompatible with rotation-based methods. Our analysis reveals that outliers vary in severity, from rare extremes to frequent mild deviations, and that quantization sensit
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
  - harma26
---

# MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `harma2026mxsens` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Simla Burcu Harma, Danila Mishin, Zhengyuan Su |

## 摘要

4-bit quantization enables efficient LLM inference, but suffers from significant accuracy degradation due to outliers. Prior work addresses this problem via data rotation or mixed-precision integer quantization, but often relies on software-managed scaling and frequent dequantization, incurring substantial overhead. Microscaling formats, such as MXINT, eliminate these inefficiencies by encoding scales in hardware, yet remain incompatible with rotation-based methods. Our analysis reveals that outliers vary in severity, from rare extremes to frequent mild deviations, and that quantization sensit

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