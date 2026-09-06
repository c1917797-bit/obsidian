---
type: literature-corpus-entry
citekey: sadeghi2026eliminating
title: "Eliminating the first moment state in Adam optimizer"
authors:
  - "Mohammad Amin Sadeghi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=xRxh48OAAM"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  The Adam optimizer and its variants are widely used in large-scale machine learning, but their memory footprint is high because they maintain two state variables per parameter. In Adam, the exponential moving average (EMA) of gradients (m) serves as a first-moment estimator, but it also carries variance information that can be exploited to estimate the second moment. Furthermore, the gradient buffer can be repurposed to handle both gradient accumulation and a proxy for the first moment, effectively folding m into the gradient buffer itself. These modifications reduce the number of optimizer st
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
  - sadeghi26
---

# Eliminating the first moment state in Adam optimizer

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `sadeghi2026eliminating` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Mohammad Amin Sadeghi |

## 摘要

The Adam optimizer and its variants are widely used in large-scale machine learning, but their memory footprint is high because they maintain two state variables per parameter. In Adam, the exponential moving average (EMA) of gradients (m) serves as a first-moment estimator, but it also carries variance information that can be exploited to estimate the second moment. Furthermore, the gradient buffer can be repurposed to handle both gradient accumulation and a proxy for the first moment, effectively folding m into the gradient buffer itself. These modifications reduce the number of optimizer st

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