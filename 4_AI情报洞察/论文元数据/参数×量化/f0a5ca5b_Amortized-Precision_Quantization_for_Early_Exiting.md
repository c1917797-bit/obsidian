---
type: literature-corpus-entry
citekey: fang2026amortized
title: "Amortized-Precision Quantization for Early Exiting in Vision Transformers"
authors:
  - "Rui Fang"
  - "Hsi-Wen Chen"
  - "Ming-syan Chen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Y8pXEF38EO"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Vision Transformers (ViTs) achieve state-of-the-art results across classification, detection, and segmentation, but their heavy computation hinders deployment on resource-constrained devices. Quantization is a common technique to improve efficiency, yet conventional approaches assume static inference and ignore the input-dependent utility of layers under dynamic strategies such as Early Exiting (EE). This mismatch leads to inefficient bit allocation: shallow layers may be over-provisioned while deeper exits, which dominate late-stage decisions, remain under-optimized. We introduce **Amortized-
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
  - fang26
---

# Amortized-Precision Quantization for Early Exiting in Vision Transformers

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `fang2026amortized` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Rui Fang, Hsi-Wen Chen, Ming-syan Chen |

## 摘要

Vision Transformers (ViTs) achieve state-of-the-art results across classification, detection, and segmentation, but their heavy computation hinders deployment on resource-constrained devices. Quantization is a common technique to improve efficiency, yet conventional approaches assume static inference and ignore the input-dependent utility of layers under dynamic strategies such as Early Exiting (EE). This mismatch leads to inefficient bit allocation: shallow layers may be over-provisioned while deeper exits, which dominate late-stage decisions, remain under-optimized. We introduce **Amortized-

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