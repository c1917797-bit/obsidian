---
type: literature-corpus-entry
citekey: wang2026bmattn
title: "BMAttn: Block-Aligned Mixed-Precision  Attention Quantization for LLM Inference"
authors:
  - "Zining Wang"
  - "Haojie Duanmu"
  - "Fanliu Kong"
  - "Zhihang Yuan"
  - "Jinyang Guo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=isBH8kP5AX"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  The proliferation of Large Language Models (LLMs) with extended context windows is severely hampered by the quadratic complexity of the self-attention mechanism. Existing acceleration methods, such as sparse attention and quantization, often employ uniform compression strategies that are misaligned with the non-uniform distribution of information importance within attention maps. This leads to a suboptimal trade-off between computational efficiency and model accuracy. To address this, we introduce Block-based Mixed-precision Attention (BMAttn), a novel framework that enables fine-grained, impo
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

# BMAttn: Block-Aligned Mixed-Precision  Attention Quantization for LLM Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026bmattn` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Zining Wang, Haojie Duanmu, Fanliu Kong |

## 摘要

The proliferation of Large Language Models (LLMs) with extended context windows is severely hampered by the quadratic complexity of the self-attention mechanism. Existing acceleration methods, such as sparse attention and quantization, often employ uniform compression strategies that are misaligned with the non-uniform distribution of information importance within attention maps. This leads to a suboptimal trade-off between computational efficiency and model accuracy. To address this, we introduce Block-based Mixed-precision Attention (BMAttn), a novel framework that enables fine-grained, impo

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