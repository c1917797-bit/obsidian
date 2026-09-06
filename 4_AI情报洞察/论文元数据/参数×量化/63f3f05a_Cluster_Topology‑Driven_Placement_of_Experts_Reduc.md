---
type: literature-corpus-entry
citekey: sivtsov2026cluster
title: "Cluster Topology‑Driven Placement of Experts Reduces Network Traffic in MoE Inference"
authors:
  - "Danil Sivtsov"
  - "Aleksandr Katrutsa"
  - "Ivan Oseledets"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=YW4RkDi5eH"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Efficient deployment of a pre-trained LLM to a cluster with multiple nodes is a critical step for providing fast responses of the service to users' queries. The recent success of Mixture-of-Experts (MoE) LLMs raises the question of how to deploy them efficiently, considering their underlying structure. During the inference in MoE LLMs, only a small part of the experts is selected to process a given token. Moreover, in practice, the experts' load is highly imbalanced. For efficient deployment, one has to distribute the model across a large number of servers using a model placement algorithm. Th
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
  - sivtsov26
---

# Cluster Topology‑Driven Placement of Experts Reduces Network Traffic in MoE Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `sivtsov2026cluster` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Danil Sivtsov, Aleksandr Katrutsa, Ivan Oseledets |

## 摘要

Efficient deployment of a pre-trained LLM to a cluster with multiple nodes is a critical step for providing fast responses of the service to users' queries. The recent success of Mixture-of-Experts (MoE) LLMs raises the question of how to deploy them efficiently, considering their underlying structure. During the inference in MoE LLMs, only a small part of the experts is selected to process a given token. Moreover, in practice, the experts' load is highly imbalanced. For efficient deployment, one has to distribute the model across a large number of servers using a model placement algorithm. Th

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