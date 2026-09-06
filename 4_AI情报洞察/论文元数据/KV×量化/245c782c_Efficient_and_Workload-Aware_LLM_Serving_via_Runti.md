---
type: literature-corpus-entry
citekey: su2026efficient
title: "Efficient and Workload-Aware LLM Serving via Runtime Layer Swapping and KV Cache Resizing"
authors:
  - "Zhaoyuan Su"
  - "Tingfeng Lan"
  - "Zirui Wang"
  - "Juncheng Yang"
  - "Yue Cheng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=1JyePezdlF"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Efficiently serving large language models (LLMs) under dynamic and bursty workloads remains a key challenge for real-world deployment. Existing serving frameworks and static model compression techniques fail to adapt to workload fluctuations, leading to either service-level objective (SLO) violations under full-precision serving or persistent accuracy degradation with static quantization. We present MorphServe, a dynamic, workload-aware LLM serving framework based on morphological adaptation. MorphServe introduces two asynchronous, token-level runtime mechanisms: quantized layer swapping, whic
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
  - KV
  - 量化
  - su26
---

# Efficient and Workload-Aware LLM Serving via Runtime Layer Swapping and KV Cache Resizing

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `su2026efficient` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Zhaoyuan Su, Tingfeng Lan, Zirui Wang |

## 摘要

Efficiently serving large language models (LLMs) under dynamic and bursty workloads remains a key challenge for real-world deployment. Existing serving frameworks and static model compression techniques fail to adapt to workload fluctuations, leading to either service-level objective (SLO) violations under full-precision serving or persistent accuracy degradation with static quantization. We present MorphServe, a dynamic, workload-aware LLM serving framework based on morphological adaptation. MorphServe introduces two asynchronous, token-level runtime mechanisms: quantized layer swapping, whic

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