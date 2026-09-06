---
type: literature-corpus-entry
citekey: sivtsov2026diagonal
title: "Diagonal Batching Unlocks Parallelism in Recurrent Memory Transformers for Long Contexts"
authors:
  - "Danil Sivtsov"
  - "Ivan Rodkin"
  - "Gleb Kuzmin"
  - "Yuri Kuratov"
  - "Ivan Oseledets"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=z1yPH2Rska"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Long-context inference with Transformers is constrained by quadratic attention
  and linear memory growth. Many linear-time alternatives require pretraining from
  scratch, whereas Recurrent Memory Transformers (RMTs) convert pretrained
  models into segment-recurrent variants via finetuning without modifying the original
  model architecture. However, their sequential memory updates underutilize GPUs.
  We show that RMT-style architectures with layer-level memory (PRMTs)
  (e.g., ARMT) can be among the most latency-efficient linear approaches when scheduled
  properly. We introduce Diagonal Batching, a c
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
  - sivtsov26
---

# Diagonal Batching Unlocks Parallelism in Recurrent Memory Transformers for Long Contexts

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `sivtsov2026diagonal` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Danil Sivtsov, Ivan Rodkin, Gleb Kuzmin |

## 摘要

Long-context inference with Transformers is constrained by quadratic attention
and linear memory growth. Many linear-time alternatives require pretraining from
scratch, whereas Recurrent Memory Transformers (RMTs) convert pretrained 
models into segment-recurrent variants via finetuning without modifying the original
model architecture. However, their sequential memory updates underutilize GPUs.
We show that RMT-style architectures with layer-level memory (PRMTs) 
(e.g., ARMT) can be among the most latency-efficient linear approaches when scheduled
properly. We introduce Diagonal Batching, a c

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