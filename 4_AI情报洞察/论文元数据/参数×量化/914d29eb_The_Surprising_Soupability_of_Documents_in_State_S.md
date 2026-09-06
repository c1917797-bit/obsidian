---
type: literature-corpus-entry
citekey: jafari2026the
title: "The Surprising Soupability of Documents in State Space Models"
authors:
  - "Yasaman Jafari"
  - "Zixian Wang"
  - "Leon Bergen"
  - "Taylor Berg-Kirkpatrick"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Mw6TUZer5l"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  We investigate whether hidden states from Structured State Space Models (SSMs) can be merged post hoc to support downstream reasoning. Inspired by model souping, we propose a strategy where documents are encoded independently and their representations are pooled, via simple operations like averaging, into a single context state. This approach, which we call document souping, enables modular encoding and reuse without reprocessing the full input for each query. We demonstrate that finetuned Mamba2 models with souped representations achieve competitive or superior performance across multi-hop QA
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
  - jafari26
---

# The Surprising Soupability of Documents in State Space Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `jafari2026the` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yasaman Jafari, Zixian Wang, Leon Bergen |

## 摘要

We investigate whether hidden states from Structured State Space Models (SSMs) can be merged post hoc to support downstream reasoning. Inspired by model souping, we propose a strategy where documents are encoded independently and their representations are pooled, via simple operations like averaging, into a single context state. This approach, which we call document souping, enables modular encoding and reuse without reprocessing the full input for each query. We demonstrate that finetuned Mamba2 models with souped representations achieve competitive or superior performance across multi-hop QA

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