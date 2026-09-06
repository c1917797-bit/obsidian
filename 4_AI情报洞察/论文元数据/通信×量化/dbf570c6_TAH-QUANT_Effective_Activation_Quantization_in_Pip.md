---
type: literature-corpus-entry
citekey: he2026tah
title: "TAH-QUANT: Effective Activation Quantization in Pipeline Parallelism over Slow Network"
authors:
  - "Guangxin He"
  - "Yuan Cao"
  - "Yutong He"
  - "Tianyi Bai"
  - "Kun Yuan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=cEkVJeMwSd"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Decentralized training of large language models offers the opportunity to pool computational resources across geographically distributed participants but faces significant network communication bottlenecks, particularly in pipeline-parallel settings. While pipeline parallelism partitions model layers across devices to handle large-scale models, it necessitates frequent communication of intermediate activations, creating challenges when network bandwidth is limited. Existing activation compression methods, such as AQ-SGD, mitigate quantization-induced errors through error compensation but impos
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
  - he26
---

# TAH-QUANT: Effective Activation Quantization in Pipeline Parallelism over Slow Network

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `he2026tah` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Guangxin He, Yuan Cao, Yutong He |

## 摘要

Decentralized training of large language models offers the opportunity to pool computational resources across geographically distributed participants but faces significant network communication bottlenecks, particularly in pipeline-parallel settings. While pipeline parallelism partitions model layers across devices to handle large-scale models, it necessitates frequent communication of intermediate activations, creating challenges when network bandwidth is limited. Existing activation compression methods, such as AQ-SGD, mitigate quantization-induced errors through error compensation but impos

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