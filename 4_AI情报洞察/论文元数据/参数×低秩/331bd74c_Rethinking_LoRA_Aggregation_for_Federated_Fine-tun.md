---
type: literature-corpus-entry
citekey: li2026rethinking
title: "Rethinking LoRA Aggregation for Federated Fine-tuning of Foundation Models"
authors:
  - "Shuai Li"
  - "Fan Qi"
  - "Xiaoshan Yang"
  - "Changsheng Xu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=k5SgTEKdA2"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  The application of Low-Rank Adaptation (LoRA) in Federated Learning (FL) systems provides an effective solution for Foundation Models (FMs) to leverage distributed private data. However, the heterogeneous distribution of client-side data has hindered the performance of federated systems from reaching. Through an in-depth investigation of this issue, we discover that LoRA parameter aggregation among clients gives rise to fine-grained conflicts and introduces the cross-term noise interference for subsequent rounds. Both factors disadvantage the efficient convergence of federated fine-tuning perf
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
  - li26
---

# Rethinking LoRA Aggregation for Federated Fine-tuning of Foundation Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026rethinking` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Shuai Li, Fan Qi, Xiaoshan Yang |

## 摘要

The application of Low-Rank Adaptation (LoRA) in Federated Learning (FL) systems provides an effective solution for Foundation Models (FMs) to leverage distributed private data. However, the heterogeneous distribution of client-side data has hindered the performance of federated systems from reaching. Through an in-depth investigation of this issue, we discover that LoRA parameter aggregation among clients gives rise to fine-grained conflicts and introduces the cross-term noise interference for subsequent rounds. Both factors disadvantage the efficient convergence of federated fine-tuning perf

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