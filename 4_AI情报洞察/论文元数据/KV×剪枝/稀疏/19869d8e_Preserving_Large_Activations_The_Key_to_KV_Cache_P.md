---
type: literature-corpus-entry
citekey: anonndpreserving
title: "Preserving Large Activations: The Key to KV Cache Pruning"
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
  As context lenghts grows, the increasing size of Key and Value (KV) cache poses a significant challenge to efficiently serving Large Language Models (LLMs). KV cache pruning, by preserving only a small subset of important KV cache for sparse inference, is a recognized effective solution. Our research revealed that large activations are the key to identifying these important KV cache. However, existing methods have not been successful in effectively identifying these important KV cache due to neg
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

# Preserving Large Activations: The Key to KV Cache Pruning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `anonndpreserving` |
| **年份** | N/A |
| **会议/期刊** | iclr2025 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | arXiv |
| **作者** | N/A |

## 摘要

As context lenghts grows, the increasing size of Key and Value (KV) cache poses a significant challenge to efficiently serving Large Language Models (LLMs). KV cache pruning, by preserving only a small subset of important KV cache for sparse inference, is a recognized effective solution. Our research revealed that large activations are the key to identifying these important KV cache. However, existing methods have not been successful in effectively identifying these important KV cache due to neg

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