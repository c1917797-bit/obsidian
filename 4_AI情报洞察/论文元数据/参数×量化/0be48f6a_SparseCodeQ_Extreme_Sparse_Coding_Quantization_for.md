---
type: literature-corpus-entry
citekey: wang2026sparsecodeq
title: "SparseCodeQ: Extreme Sparse Coding Quantization for Large Vision-Language Models"
authors:
  - "Changyuan Wang"
  - "Runhao Li"
  - "Ziwei Wang"
  - "Yinan Liang"
  - "Yansong Tang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=IdPerHPpW3"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  In this paper, we propose an extreme sparse coding quantization framework of 2-bit large vision-language models (LVLMs) for efficient multimodal reasoning. Conventional codebook-based quantization methods assign the same codeword number to all weights ignoring the significant variance of weight salience, which leads to substantial discretization errors. On the contrary, we flexibly assign optimal codeword combination for each weight based on weight salience to mitigate the performance degradation with negligible complexity overhead. Specifically, we first select the number of codewords for all
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
  - wang26
---

# SparseCodeQ: Extreme Sparse Coding Quantization for Large Vision-Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026sparsecodeq` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Changyuan Wang, Runhao Li, Ziwei Wang |

## 摘要

In this paper, we propose an extreme sparse coding quantization framework of 2-bit large vision-language models (LVLMs) for efficient multimodal reasoning. Conventional codebook-based quantization methods assign the same codeword number to all weights ignoring the significant variance of weight salience, which leads to substantial discretization errors. On the contrary, we flexibly assign optimal codeword combination for each weight based on weight salience to mitigate the performance degradation with negligible complexity overhead. Specifically, we first select the number of codewords for all

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