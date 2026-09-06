---
type: literature-corpus-entry
citekey: chen2026amdp
title: "AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training"
authors:
  - "Ling Chen"
  - "Houming Wu"
  - "Wenjie Yu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=cfZNOO6ZHf"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Pipeline parallelism has become a critical technique for scaling up the training of large models. However, existing asynchronous pipeline approaches often suffer from degraded convergence due to parameter mismatch between forward and backward passes. To address this, we propose Asynchronous Multi-Directional Pipeline parallelism (AMDP). AMDP limits stage 0 of each pipeline to read only two minibatches before initiating the first backward pass, thereby reducing the number of parameter updates that occur between the forward and backward passes of each minibatch. To mitigate the pipeline bubbles
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
  - chen26
---

# AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026amdp` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Ling Chen, Houming Wu, Wenjie Yu |

## 摘要

Pipeline parallelism has become a critical technique for scaling up the training of large models. However, existing asynchronous pipeline approaches often suffer from degraded convergence due to parameter mismatch between forward and backward passes. To address this, we propose Asynchronous Multi-Directional Pipeline parallelism (AMDP). AMDP limits stage 0 of each pipeline to read only two minibatches before initiating the first backward pass, thereby reducing the number of parameter updates that occur between the forward and backward passes of each minibatch. To mitigate the pipeline bubbles 

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