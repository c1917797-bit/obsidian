---
type: literature-corpus-entry
citekey: anonndpost
title: "Post-Training Sparse Attention with Double Sparsity"
authors: []
year: ""
venue: iclr2025
venue_type: conference
arxiv_id: ""
doi: ""
url: ""
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Long-context inference of Large Language Models (LLMs) is known to be challenging due to the excessive Key-Value(KV) cache accesses. This paper introduces ``Double Sparsity,'' a novel post-training sparse attention technique designed to alleviate this bottleneck by reducing KV cache access. Double Sparsity combines token sparsity, which focuses on using only the important tokens for computing self-attention, with channel sparsity, an approach that uses important feature channels for identifying
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
  - KV
  - 剪枝/稀疏
---

# Post-Training Sparse Attention with Double Sparsity

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `anonndpost` |
| **年份** | N/A |
| **会议/期刊** | iclr2025 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | arXiv |
| **作者** | N/A |

## 摘要

Long-context inference of Large Language Models (LLMs) is known to be challenging due to the excessive Key-Value(KV) cache accesses. This paper introduces ``Double Sparsity,'' a novel post-training sparse attention technique designed to alleviate this bottleneck by reducing KV cache access. Double Sparsity combines token sparsity, which focuses on using only the important tokens for computing self-attention, with channel sparsity, an approach that uses important feature channels for identifying 

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