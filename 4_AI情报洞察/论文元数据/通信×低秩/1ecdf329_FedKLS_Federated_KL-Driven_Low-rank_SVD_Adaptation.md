---
type: literature-corpus-entry
citekey: quan2026fedkls
title: "FedKLS: Federated KL-Driven Low-rank SVD Adaptation in Non-IID Data Distributions"
authors:
  - "Pham Khanh Quan"
  - "Khoa Nguyen"
  - "Leo Yu Zhang"
  - "madhusanka Liyanage"
  - "Taehong Kim"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=gxKvAhqhmT"
pdf_url: ""
object: 通信
method: 低秩
cell: "通信×低秩"
all_objects: []
all_methods: []
abstract: |
  Federated learning faces two key challenges: handling non-IID client distributions and reducing communication costs in adapting large models. To address these issues, we propose FedKLS, a framework that combines KL-divergence-based personalization with low-rank SVD-based adaptations. FedKLS chooses spectral components in a dynamical manner by mapping the heterogeneity of client distribution to the singular value spectrum, then builds specialized LoRA-style adapters, which allow aggregation at scale and client-specific specialization. Extensive experiments on 20NewsGroup and Banking77 with Dist
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
  - 通信
  - 低秩
  - quan26
---

# FedKLS: Federated KL-Driven Low-rank SVD Adaptation in Non-IID Data Distributions

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `quan2026fedkls` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×低秩 |
| **来源** | openreview |
| **作者** | Pham Khanh Quan, Khoa Nguyen, Leo Yu Zhang |

## 摘要

Federated learning faces two key challenges: handling non-IID client distributions and reducing communication costs in adapting large models. To address these issues, we propose FedKLS, a framework that combines KL-divergence-based personalization with low-rank SVD-based adaptations. FedKLS chooses spectral components in a dynamical manner by mapping the heterogeneity of client distribution to the singular value spectrum, then builds specialized LoRA-style adapters, which allow aggregation at scale and client-specific specialization. Extensive experiments on 20NewsGroup and Banking77 with Dist

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