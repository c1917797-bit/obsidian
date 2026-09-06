---
type: literature-corpus-entry
citekey: zhang2026baq
title: "BAQ: Efficient Bit Allocation Quantization for Large Language Models"
authors:
  - "Chao Zhang"
  - "Li Wang"
  - "Samson Lasaulce"
  - "Wenya Yu"
  - "Merouane Abdelkader DEBBAH"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=h7g3HflcxE"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Post-training model quantization is a widely adopted technique for reducing the memory and computational costs of large language models (LLMs). However, most existing methods either fix a uniform bitwidth or rely on binary sensitivity groupings (``sensitive'' vs.\ ``non-sensitive'') that treat all weights within a group identically, ignoring how sensitive each weight actually is and leaving the degree of sensitivity under-exploited. To address this, for the first time in the neural network quantization literature, we introduce an explicit loss--bitwidth relation that links layer-output distort
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
  - zhang26
---

# BAQ: Efficient Bit Allocation Quantization for Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026baq` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Chao Zhang, Li Wang, Samson Lasaulce |

## 摘要

Post-training model quantization is a widely adopted technique for reducing the memory and computational costs of large language models (LLMs). However, most existing methods either fix a uniform bitwidth or rely on binary sensitivity groupings (``sensitive'' vs.\ ``non-sensitive'') that treat all weights within a group identically, ignoring how sensitive each weight actually is and leaving the degree of sensitivity under-exploited. To address this, for the first time in the neural network quantization literature, we introduce an explicit loss--bitwidth relation that links layer-output distort

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