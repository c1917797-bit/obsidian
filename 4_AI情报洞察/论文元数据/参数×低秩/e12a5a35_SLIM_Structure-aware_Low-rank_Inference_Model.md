---
type: literature-corpus-entry
citekey: yen2026slim
title: "SLIM: Structure-aware Low-rank Inference Model"
authors:
  - "Jui-Nan Yen"
  - "Wei-Cheng Chang"
  - "Si Si"
  - "Ngot Bui"
  - "Inderjit S Dhillon"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=iY0Wi8UIjA"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  This paper introduces a new method for the low-rank compression of large language models. Existing techniques typically compress the weights individually, overlooking the internal dependencies within a transformer block. To address this limitation, we formulate a joint optimization problem to find the optimal low-rank weights for an entire transformer block, thereby minimizing the output reconstruction error. Our formulation allows the incorporation of key architectural elements, including residual connections and normalizations. We then introduce SLIM, an efficient algorithm to solve this opt
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
  - yen26
---

# SLIM: Structure-aware Low-rank Inference Model

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yen2026slim` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Jui-Nan Yen, Wei-Cheng Chang, Si Si |

## 摘要

This paper introduces a new method for the low-rank compression of large language models. Existing techniques typically compress the weights individually, overlooking the internal dependencies within a transformer block. To address this limitation, we formulate a joint optimization problem to find the optimal low-rank weights for an entire transformer block, thereby minimizing the output reconstruction error. Our formulation allows the incorporation of key architectural elements, including residual connections and normalizations. We then introduce SLIM, an efficient algorithm to solve this opt

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