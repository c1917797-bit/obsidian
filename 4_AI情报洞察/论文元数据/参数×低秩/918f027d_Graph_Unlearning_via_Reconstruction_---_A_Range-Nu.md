---
type: literature-corpus-entry
citekey: yin2026graph
title: "Graph Unlearning via Reconstruction --- A Range-Null Space Decomposition Approach"
authors:
  - "Hang Yin"
  - "Xiaoyong Peng"
  - "Zipeng Liu"
  - "Liyao Xiang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=YaKWwVIoWN"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Graph unlearning is a machine unlearning technique tailored to graph neural networks (GNNs) to remove nodes or edges from the training graph. Conventional methods such as retraining is highly inefficient, while influence function-based approaches merely work on minor removal, like 10\% or less of the graph edges. To resolve the problems, we reverse the aggregation process in GNN training by modeling the interaction between unlearned nodes and their neighbors. Given one unlearned node, its embedding is roughly disassembled and assigned to its neighbours by reconstruction, and then removed from
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
  - 低秩
  - yin26
---

# Graph Unlearning via Reconstruction --- A Range-Null Space Decomposition Approach

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yin2026graph` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Hang Yin, Xiaoyong Peng, Zipeng Liu |

## 摘要

Graph unlearning is a machine unlearning technique tailored to graph neural networks (GNNs) to remove nodes or edges from the training graph. Conventional methods such as retraining is highly inefficient, while influence function-based approaches merely work on minor removal, like 10\% or less of the graph edges. To resolve the problems, we reverse the aggregation process in GNN training by modeling the interaction between unlearned nodes and their neighbors. Given one unlearned node, its embedding is roughly disassembled and assigned to its neighbours by reconstruction, and then removed from 

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