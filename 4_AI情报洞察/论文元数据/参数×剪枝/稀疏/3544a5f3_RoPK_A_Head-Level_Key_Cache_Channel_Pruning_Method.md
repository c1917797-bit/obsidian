---
type: literature-corpus-entry
citekey: huang2026ropk
title: "RoPK: A Head-Level Key Cache Channel Pruning Method for Efficient Long-Context LLM Inference"
authors:
  - "Weizhong Huang"
  - "Yuxin Zhang"
  - "Xiawu Zheng"
  - "Fei Chao"
  - "Rongrong Ji"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=SRXVoLJEaq"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  The substantial memory overhead of the Key-Value (KV) cache is a critical bottleneck in Large Language Models (LLMs), limiting context length and inference throughput. While prior compression techniques have targeted various dimensions of the cache, they typically assume a uniform channel allocation for all attention heads, which leads to inaccurate channel pruning and a significant drop in accuracy. This paper introduces a novel head-level key cache channel pruning method that allocates channel budgets based on a new head importance estimation algorithm derived from Rotary Position Embedding
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
  - huang26
---

# RoPK: A Head-Level Key Cache Channel Pruning Method for Efficient Long-Context LLM Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `huang2026ropk` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Weizhong Huang, Yuxin Zhang, Xiawu Zheng |

## 摘要

The substantial memory overhead of the Key-Value (KV) cache is a critical bottleneck in Large Language Models (LLMs), limiting context length and inference throughput. While prior compression techniques have targeted various dimensions of the cache, they typically assume a uniform channel allocation for all attention heads, which leads to inaccurate channel pruning and a significant drop in accuracy. This paper introduces a novel head-level key cache channel pruning method that allocates channel budgets based on a new head importance estimation algorithm derived from Rotary Position Embedding 

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