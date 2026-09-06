---
type: literature-corpus-entry
citekey: hu2026rank
title: "Rank-Preserving Calibration of LLMs Under Model and Distribution Shifts"
authors:
  - "Jian Hu"
  - "Qunli Zhang"
  - "Feng Liu"
  - "zheng hu"
  - "Changjae Oh"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=0crU7lZV8n"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  A central barrier to deploying Large Language Models (LLMs) in safety-critical applications is hallucination, where models generate non-factual content with high confidence. Detecting hallucinations requires well-calibrated confidence estimates, yet calibration is brittle under domain and model shifts. The former renders confidence estimates unreliable in a new environment, while the latter arises because different LLMs exhibit distinct confidence scales, so calibration learned for one model often fails to transfer when another is used at deployment for efficiency or privacy. Addressing this v
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
  - hu26
---

# Rank-Preserving Calibration of LLMs Under Model and Distribution Shifts

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hu2026rank` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Jian Hu, Qunli Zhang, Feng Liu |

## 摘要

A central barrier to deploying Large Language Models (LLMs) in safety-critical applications is hallucination, where models generate non-factual content with high confidence. Detecting hallucinations requires well-calibrated confidence estimates, yet calibration is brittle under domain and model shifts. The former renders confidence estimates unreliable in a new environment, while the latter arises because different LLMs exhibit distinct confidence scales, so calibration learned for one model often fails to transfer when another is used at deployment for efficiency or privacy. Addressing this v

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