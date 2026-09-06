---
type: literature-corpus-entry
citekey: li2026winiq
title: "WiniQ: Accelerating Quantization-Aware Training of LLMs around Saddle Points"
authors:
  - "Dongyue Li"
  - "Zechun Liu"
  - "Kai Yi"
  - "Changsheng Zhao"
  - "Raghuraman Krishnamoorthi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=IEGwgxe13Y"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Quantization-aware training is a widely used approach for language model quantization in sub-4-bit precision. This approach works by training full-precision weights to minimize the loss with gradients on the quantized model. Despite its superior performance, the main bottleneck for this quantized training is its slow convergence, which gets worse in lower bit-widths. While this problem has been observed in prior work, its precise cause has not been carefully studied. In this paper, we analyze the convergence by computing the Hessian spectrum of the model loss throughout quantization-aware trai
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
  - li26
---

# WiniQ: Accelerating Quantization-Aware Training of LLMs around Saddle Points

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026winiq` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Dongyue Li, Zechun Liu, Kai Yi |

## 摘要

Quantization-aware training is a widely used approach for language model quantization in sub-4-bit precision. This approach works by training full-precision weights to minimize the loss with gradients on the quantized model. Despite its superior performance, the main bottleneck for this quantized training is its slow convergence, which gets worse in lower bit-widths. While this problem has been observed in prior work, its precise cause has not been carefully studied. In this paper, we analyze the convergence by computing the Hessian spectrum of the model loss throughout quantization-aware trai

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