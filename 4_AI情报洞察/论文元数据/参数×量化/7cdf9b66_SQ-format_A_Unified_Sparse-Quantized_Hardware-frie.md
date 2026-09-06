---
type: literature-corpus-entry
citekey: huang2026sq
title: "SQ-format: A Unified Sparse-Quantized Hardware-friendly Data Format for Large Language Models"
authors:
  - "Ruixuan Huang"
  - "Hao Zeng"
  - "Hantao Huang"
  - "Jinyuan Shi"
  - "Minghui Yu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=MPybJCVrgc"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Post-training quantization (PTQ) plays a crucial role in the democratization of large language models (LLMs). However, existing low-bit quantizaiton and sparsification techniques are difficult to balance accuracy and efficiency due to the limited hardware support. For example, W4A8 can only achieve the same peak TOPS as W8A8 whereas the GPU-supported sparse data format (2:4 semi-structure sparse) is seldomly adopted due to the loss of accuracy. To bridge this gap, in this paper, we propose the Sparse-Quantized Format (SQ-format), which is a unified data format for quantization and sparsificati
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
  - huang26
---

# SQ-format: A Unified Sparse-Quantized Hardware-friendly Data Format for Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `huang2026sq` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Ruixuan Huang, Hao Zeng, Hantao Huang |

## 摘要

Post-training quantization (PTQ) plays a crucial role in the democratization of large language models (LLMs). However, existing low-bit quantizaiton and sparsification techniques are difficult to balance accuracy and efficiency due to the limited hardware support. For example, W4A8 can only achieve the same peak TOPS as W8A8 whereas the GPU-supported sparse data format (2:4 semi-structure sparse) is seldomly adopted due to the loss of accuracy. To bridge this gap, in this paper, we propose the Sparse-Quantized Format (SQ-format), which is a unified data format for quantization and sparsificati

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