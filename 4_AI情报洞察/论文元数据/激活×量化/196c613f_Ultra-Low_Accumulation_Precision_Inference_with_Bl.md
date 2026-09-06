---
type: literature-corpus-entry
citekey: anonndultra
title: "Ultra-Low Accumulation Precision Inference with Block Floating Point Arithmetic"
authors: []
year: ""
venue: iclr2025
venue_type: conference
arxiv_id: ""
doi: ""
url: ""
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Block Floating Point (BFP) quantization offers a hardware-efficient numerical range trade-off. Previous studies have quantized weights and activations to an extremely low precision using the BFP arithmetic. However, as the precision of weights and activations is reduced, we have identified that accumulation becomes a hardware bottleneck in the BFP MAC. Nevertheless, existing attempts to decrease the precision of accumulation in matrix multiplication have generally preserved model performance thr
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "arxiv"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - 激活
  - 量化
---

# Ultra-Low Accumulation Precision Inference with Block Floating Point Arithmetic

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `anonndultra` |
| **年份** | N/A |
| **会议/期刊** | iclr2025 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | arXiv |
| **作者** | N/A |

## 摘要

Block Floating Point (BFP) quantization offers a hardware-efficient numerical range trade-off. Previous studies have quantized weights and activations to an extremely low precision using the BFP arithmetic. However, as the precision of weights and activations is reduced, we have identified that accumulation becomes a hardware bottleneck in the BFP MAC. Nevertheless, existing attempts to decrease the precision of accumulation in matrix multiplication have generally preserved model performance thr

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
*生成日期: 2026-07-06 | 来源: arXiv*