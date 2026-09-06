---
type: literature-corpus-entry
citekey: xian2026mode
title: "MoDE: Weight Denoising Towards Better LLM Performance through a Mixture of Domain Experts"
authors:
  - "Yuchen Xian"
  - "Yixuan Han"
  - "Fan Ma"
  - "Yi Yang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=L3ETLxmb7N"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Pruning in large language models (LLMs) is widely assumed to degrade performance, since most weights are considered essential contributors to model capacity; thus, existing methods primarily rely on training to retain accuracy. However, our findings show that weight importance is domain-dependent rather than globally consistent, revealing the existence of noise weights whose removal can enhance domain-specific performance. To this end, we first present the DENoise (Domain Expert weight deNoising) algorithm, which effectively removes domain-aware noise weights without requiring fine-tuning to a
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
  - xian26
---

# MoDE: Weight Denoising Towards Better LLM Performance through a Mixture of Domain Experts

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xian2026mode` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Yuchen Xian, Yixuan Han, Fan Ma |

## 摘要

Pruning in large language models (LLMs) is widely assumed to degrade performance, since most weights are considered essential contributors to model capacity; thus, existing methods primarily rely on training to retain accuracy. However, our findings show that weight importance is domain-dependent rather than globally consistent, revealing the existence of noise weights whose removal can enhance domain-specific performance. To this end, we first present the DENoise (Domain Expert weight deNoising) algorithm, which effectively removes domain-aware noise weights without requiring fine-tuning to a

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