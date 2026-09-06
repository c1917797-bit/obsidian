---
type: literature-corpus-entry
citekey: sternal2026addition
title: "Addition Circuit: How LLMs Add in Their Heads using State Vectors"
authors:
  - "Tomasz Sternal"
  - "Torsten Hoefler"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=i6fc97RY1l"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Large Language Models (LLMs) are often treated as black boxes, yet many of their behaviours suggest the presence of internal, algorithm-like structures. We present addition circuit as a concrete, mechanistic example of such a structure: a sparse set of attention heads that perform integer addition. Focusing on two popular open-source models (Llama 3.1 8B and Llama 3.1 70B), we make the following contributions. (i) We extend prior work on two-argument addition to the multi-argument setting, showing that both models employ fixed subsets of attention heads specialized in encoding summands at spec
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
  - 剪枝/稀疏
  - sternal26
---

# Addition Circuit: How LLMs Add in Their Heads using State Vectors

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `sternal2026addition` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Tomasz Sternal, Torsten Hoefler |

## 摘要

Large Language Models (LLMs) are often treated as black boxes, yet many of their behaviours suggest the presence of internal, algorithm-like structures. We present addition circuit as a concrete, mechanistic example of such a structure: a sparse set of attention heads that perform integer addition. Focusing on two popular open-source models (Llama 3.1 8B and Llama 3.1 70B), we make the following contributions. (i) We extend prior work on two-argument addition to the multi-argument setting, showing that both models employ fixed subsets of attention heads specialized in encoding summands at spec

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