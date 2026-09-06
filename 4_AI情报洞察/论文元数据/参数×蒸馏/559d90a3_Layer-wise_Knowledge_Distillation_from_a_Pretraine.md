---
type: literature-corpus-entry
citekey: kumarasinghe2026layer
title: "Layer-wise Knowledge Distillation from a Pretrained Network Improves Hypernetwork Convergence"
authors:
  - "Prabhash Kumarasinghe"
  - "Bernd Meyer"
  - "Anuja Dharmaratne"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=jn1fUQ5KN6"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Hypernetworks that generate weights of another network often exhibit lower test accuracy and slower convergence due to implicit weight updates. The recently proposed HyperLight framework (Magnitude Invariant Parameterisations, MIP) addresses this convergence issue by bounding the scale of the hypernetwork's input encoding using sine-cosine transforms and by introducing additive weights.
  Preliminary experiments revealed that when deeper primary networks are fully hypernetised, MIP achieves lower test accuracy compared to a canonically trained network. This paper investigates layer-wise knowledg
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
  - 蒸馏
  - kumarasinghe26
---

# Layer-wise Knowledge Distillation from a Pretrained Network Improves Hypernetwork Convergence

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `kumarasinghe2026layer` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Prabhash Kumarasinghe, Bernd Meyer, Anuja Dharmaratne |

## 摘要

Hypernetworks that generate weights of another network often exhibit lower test accuracy and slower convergence due to implicit weight updates. The recently proposed HyperLight framework (Magnitude Invariant Parameterisations, MIP) addresses this convergence issue by bounding the scale of the hypernetwork's input encoding using sine-cosine transforms and by introducing additive weights.
Preliminary experiments revealed that when deeper primary networks are fully hypernetised, MIP achieves lower test accuracy compared to a canonically trained network. This paper investigates layer-wise knowledg

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