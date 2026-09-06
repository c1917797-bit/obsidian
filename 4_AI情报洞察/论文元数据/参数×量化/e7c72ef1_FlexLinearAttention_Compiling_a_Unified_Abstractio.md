---
type: literature-corpus-entry
citekey: duanmu2026flexlinearattention
title: "FlexLinearAttention: Compiling a Unified Abstraction into Scalable Kernels for Linear Attention"
authors:
  - "Haojie Duanmu"
  - "Size Zheng"
  - "Ningxin Zheng"
  - "Jianqiao Lu"
  - "Xuegui Zheng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=N4jJQvQSiN"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  The quadratic complexity of softmax attention poses a major bottleneck for long-context modeling, motivating a surge of linear attention variants with linear complexity. Unlike softmax attention, which benefits from optimized kernels, linear attention lacks general-purpose, hardware-efficient support and scalable distributed implementations. We introduce **Flex**ible **L**inear **A**ttention (FlexLA), a domain-specific compiler that automates the generation of high-performance, scalable kernels for a wide range of linear attention models directly from high-level PyTorch code. At its core, Flex
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
  - duanmu26
---

# FlexLinearAttention: Compiling a Unified Abstraction into Scalable Kernels for Linear Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `duanmu2026flexlinearattention` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Haojie Duanmu, Size Zheng, Ningxin Zheng |

## 摘要

The quadratic complexity of softmax attention poses a major bottleneck for long-context modeling, motivating a surge of linear attention variants with linear complexity. Unlike softmax attention, which benefits from optimized kernels, linear attention lacks general-purpose, hardware-efficient support and scalable distributed implementations. We introduce **Flex**ible **L**inear **A**ttention (FlexLA), a domain-specific compiler that automates the generation of high-performance, scalable kernels for a wide range of linear attention models directly from high-level PyTorch code. At its core, Flex

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