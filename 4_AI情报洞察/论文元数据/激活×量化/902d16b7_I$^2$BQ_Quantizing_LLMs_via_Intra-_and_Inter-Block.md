---
type: literature-corpus-entry
citekey: wang2026i
title: "I$^2$BQ: Quantizing LLMs via Intra- and Inter-Block Optimization"
authors:
  - "Hailing Wang"
  - "Jianglin Lu"
  - "Yitian Zhang"
  - "Yun Fu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=uMzI444w7A"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Post-training quantization (PTQ) has emerged as a promising solution for reducing the memory and computation overhead of large language models (LLMs), enabling efficient deployment without requiring full model retraining. However, existing PTQ methods struggle with weight–activation joint quantization and extreme weight quantization. The main challenge stems from the depth and cross-layer dependencies of LLMs, which cause quantization errors to propagate and accumulate across layers, leading to degraded performance. In this paper, we present I$^2$BQ, a simple yet effective framework that simul
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
  - 激活
  - 量化
  - wang26
---

# I$^2$BQ: Quantizing LLMs via Intra- and Inter-Block Optimization

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026i` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Hailing Wang, Jianglin Lu, Yitian Zhang |

## 摘要

Post-training quantization (PTQ) has emerged as a promising solution for reducing the memory and computation overhead of large language models (LLMs), enabling efficient deployment without requiring full model retraining. However, existing PTQ methods struggle with weight–activation joint quantization and extreme weight quantization. The main challenge stems from the depth and cross-layer dependencies of LLMs, which cause quantization errors to propagate and accumulate across layers, leading to degraded performance. In this paper, we present I$^2$BQ, a simple yet effective framework that simul

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