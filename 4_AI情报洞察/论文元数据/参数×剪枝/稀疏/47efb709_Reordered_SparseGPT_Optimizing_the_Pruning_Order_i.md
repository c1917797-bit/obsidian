---
type: literature-corpus-entry
citekey: su2026reordered
title: "Reordered SparseGPT: Optimizing the Pruning Order in Second-Order LLM Pruning"
authors:
  - "Mingluo Su"
  - "Huan Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=NlMXI17iou"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Pruning is widely recognized as an effective method for reducing the parameters of large language models (LLMs), potentially leading to more efficient inference. One classic and prominent path of one-shot LLM pruning is to leverage the second-order gradients (i.e., Hessian), represented by the pioneering works like SparseGPT (Frantar & Alistarh, 2023). However, the predefined left-to-right pruning order in SparseGPT leads to suboptimal performance when the weights exhibit columnar patterns. This paper studies the effect of pruning order under the SparseGPT framework. The analyses lead us to pr
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
  - su26
---

# Reordered SparseGPT: Optimizing the Pruning Order in Second-Order LLM Pruning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `su2026reordered` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Mingluo Su, Huan Wang |

## 摘要

Pruning is widely recognized as an effective method for reducing the parameters of large language models (LLMs), potentially leading to more efficient inference. One classic and prominent path of one-shot LLM pruning is to leverage the second-order gradients (i.e., Hessian), represented by the pioneering works like SparseGPT (Frantar & Alistarh, 2023). However, the predefined left-to-right pruning order in SparseGPT leads to suboptimal performance when the weights exhibit columnar patterns. This paper studies the effect of pruning order under the SparseGPT framework. The analyses lead us to pr

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