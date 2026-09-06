---
type: literature-corpus-entry
citekey: zhu2026safetylock
title: "Safetylock: Guarding LLM againt FuneTuning Risks with Efficient Inference-time Addon"
authors:
  - "Minjun Zhu"
  - "Yixuan Weng"
  - "Linyi Yang"
  - "Qiujie Xie"
  - "Yifan Wei"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=tZ8cgf8X4T"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Fine-tuning large language models (LLMs) on additional datasets is often necessary to optimize them for specific downstream tasks. However, existing safety alignment measures, which restrict harmful behavior during inference, are insufficient to mitigate safety risks during fine-tuning. Alarmingly, fine-tuning with only 10 toxic sentences can significantly degrade a model’s safety. Moreover, considering the proliferation of fine-tuned models, the per-model cost of existing safety restoration methods becomes prohibitive. To address these challenges, we propose \textbf{SafetyLock}, a novel align
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
  - zhu26
---

# Safetylock: Guarding LLM againt FuneTuning Risks with Efficient Inference-time Addon

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhu2026safetylock` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Minjun Zhu, Yixuan Weng, Linyi Yang |

## 摘要

Fine-tuning large language models (LLMs) on additional datasets is often necessary to optimize them for specific downstream tasks. However, existing safety alignment measures, which restrict harmful behavior during inference, are insufficient to mitigate safety risks during fine-tuning. Alarmingly, fine-tuning with only 10 toxic sentences can significantly degrade a model’s safety. Moreover, considering the proliferation of fine-tuned models, the per-model cost of existing safety restoration methods becomes prohibitive. To address these challenges, we propose \textbf{SafetyLock}, a novel align

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