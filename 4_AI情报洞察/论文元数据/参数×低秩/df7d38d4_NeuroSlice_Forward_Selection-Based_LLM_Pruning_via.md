---
type: literature-corpus-entry
citekey: zhou2026neuroslice
title: "NeuroSlice: Forward Selection-Based LLM Pruning via Neuron Contribution Decomposition"
authors:
  - "Hanzhang Zhou"
  - "Zijian Feng"
  - "Zixiao Zhu"
  - "Tianjiao Li"
  - "Junlang Qian"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=M3N7z1mgJ1"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Large language models (LLMs) have dramatically advanced natural language processing, but their deployment is often hindered by exorbitant computational and memory demands. LLM pruning offers a promising pathway to efficiency, yet most pruning methods rely on the layer output as the signal for parameter importance estimation. In this work, we revisit this issue and demonstrate that the layer output is not an atomic unit. Leveraging matrix identity transformations, we decompose each layer's output into an additive summation of individual neuron contributions, thereby reshaping the original token
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
  - zhou26
---

# NeuroSlice: Forward Selection-Based LLM Pruning via Neuron Contribution Decomposition

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhou2026neuroslice` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Hanzhang Zhou, Zijian Feng, Zixiao Zhu |

## 摘要

Large language models (LLMs) have dramatically advanced natural language processing, but their deployment is often hindered by exorbitant computational and memory demands. LLM pruning offers a promising pathway to efficiency, yet most pruning methods rely on the layer output as the signal for parameter importance estimation. In this work, we revisit this issue and demonstrate that the layer output is not an atomic unit. Leveraging matrix identity transformations, we decompose each layer's output into an additive summation of individual neuron contributions, thereby reshaping the original token

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