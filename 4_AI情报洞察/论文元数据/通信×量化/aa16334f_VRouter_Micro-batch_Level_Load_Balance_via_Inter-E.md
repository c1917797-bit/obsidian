---
type: literature-corpus-entry
citekey: wang2026vrouter
title: "VRouter: Micro-batch Level Load Balance via Inter-EP Routing for MoE Training"
authors:
  - "Haiquan Wang"
  - "Zhipeng Zhang"
  - "Guanshujie Fu"
  - "Youhui Bai"
  - "Jiangfei Duan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=h3Uq2wZ20c"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Load imbalance within the Expert Parallel (EP) group leads to poor GPU efficiency when pre-training large-scale Mixture-of-Experts (MoE) models. Though recent approaches have attempted to mitigate this through dynamic expert rearrangement at the global-batch level, they overlook the rapid and dynamic variations in load distribution across different micro-batches. Additionally, relocating or shadowing popular experts at micro-batch level incurs substantial communication overhead due to frequent migrations of expert parameters and gradients.
  
  To address these issues, we introduce VRouter, a nove
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
  - 量化
  - wang26
---

# VRouter: Micro-batch Level Load Balance via Inter-EP Routing for MoE Training

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026vrouter` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Haiquan Wang, Zhipeng Zhang, Guanshujie Fu |

## 摘要

Load imbalance within the Expert Parallel (EP) group leads to poor GPU efficiency when pre-training large-scale Mixture-of-Experts (MoE) models. Though recent approaches have attempted to mitigate this through dynamic expert rearrangement at the global-batch level, they overlook the rapid and dynamic variations in load distribution across different micro-batches. Additionally, relocating or shadowing popular experts at micro-batch level incurs substantial communication overhead due to frequent migrations of expert parameters and gradients.

To address these issues, we introduce VRouter, a nove

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