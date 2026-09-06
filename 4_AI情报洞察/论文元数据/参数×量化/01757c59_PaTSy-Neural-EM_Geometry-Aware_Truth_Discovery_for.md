---
type: literature-corpus-entry
citekey: koreddi2026patsy
title: "PaTSy-Neural-EM: Geometry-Aware Truth Discovery for Real-Time Multi-Agent Perception"
authors:
  - "Shiva Koreddi"
  - "Sravani Sowrupilli"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=24xsYuKKnt"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  We revisit truth discovery (TD) for multi-agent perception and present PaTSy-
  Neural-EM, a geometry-aware EM framework that learns state-conditioned reliability
  while preserving the interpretability of Dawid–Skene (DS) confusion
  matrices. In dynamic V2X scenes, reliability varies with range, incidence angle,
  occlusion, latency, and agent identity. PaTSy injects this context via a log-linear
  reliability head whose outputs additively correct DS logits and are renormalized
  with a softmax to yield valid context-dependent confusion columns. To stabilize
  joint learning, we introduce a gentle-Π sched
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
  - koreddi26
---

# PaTSy-Neural-EM: Geometry-Aware Truth Discovery for Real-Time Multi-Agent Perception

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `koreddi2026patsy` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Shiva Koreddi, Sravani Sowrupilli |

## 摘要

We revisit truth discovery (TD) for multi-agent perception and present PaTSy-
Neural-EM, a geometry-aware EM framework that learns state-conditioned reliability
while preserving the interpretability of Dawid–Skene (DS) confusion
matrices. In dynamic V2X scenes, reliability varies with range, incidence angle,
occlusion, latency, and agent identity. PaTSy injects this context via a log-linear
reliability head whose outputs additively correct DS logits and are renormalized
with a softmax to yield valid context-dependent confusion columns. To stabilize
joint learning, we introduce a gentle-Π sched

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