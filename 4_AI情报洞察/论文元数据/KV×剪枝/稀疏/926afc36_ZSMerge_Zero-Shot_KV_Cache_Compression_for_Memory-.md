---
type: literature-corpus-entry
citekey: liu2026zsmerge
title: "ZSMerge: Zero-Shot KV Cache Compression for Memory-Efficient Long-Context LLMs"
authors:
  - "Xin LIU"
  - "Xudong Wang"
  - "Pei Liu"
  - "Guoming Tang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=WJ5BIKfc5A"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  The linear growth of key-value (KV) cache memory and quadratic computational complexity in attention mechanisms pose significant bottlenecks for large language models (LLMs) in long-context processing. While existing KV cache optimization methods address these challenges through token pruning or feature merging, they often incur irreversible information loss or require costly retraining. To this end, we propose ZSMerge, a dynamic KV cache compression framework designed for efficient cache management, featuring three key operations: (1) fine-grained memory allocation guided by multi-dimensional
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
  - KV
  - 剪枝/稀疏
  - liu26
---

# ZSMerge: Zero-Shot KV Cache Compression for Memory-Efficient Long-Context LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026zsmerge` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Xin LIU, Xudong Wang, Pei Liu |

## 摘要

The linear growth of key-value (KV) cache memory and quadratic computational complexity in attention mechanisms pose significant bottlenecks for large language models (LLMs) in long-context processing. While existing KV cache optimization methods address these challenges through token pruning or feature merging, they often incur irreversible information loss or require costly retraining. To this end, we propose ZSMerge, a dynamic KV cache compression framework designed for efficient cache management, featuring three key operations: (1) fine-grained memory allocation guided by multi-dimensional

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