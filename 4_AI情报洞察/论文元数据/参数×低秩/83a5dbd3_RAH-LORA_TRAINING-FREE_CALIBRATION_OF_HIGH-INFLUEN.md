---
type: literature-corpus-entry
citekey: kwon2026rah
title: "RAH-LORA: TRAINING-FREE CALIBRATION OF HIGH-INFLUENCE ATTENTION HEADS IN MLLMS"
authors:
  - "Hyeongjun Kwon"
  - "Kwanghoon Sohn"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qiduLvfi63"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Multimodal large language models (MLLMs) suffer from a coordination failure during training—attention heads optimize independently despite sharing inputs, leading many to develop suboptimal specialization patterns.
  We identify that numerous attention heads exhibit high downstream influence yet minimal cross-modal interaction, acting as performance bottlenecks that propagate misaligned patterns throughout the network.
  To address this, we introduce \textbf{RAH-LoRA (Representative Anchor Head Low-Rank Adaptation)}, a training-free calibration method that realigns these problematic heads by trans
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
  - kwon26
---

# RAH-LORA: TRAINING-FREE CALIBRATION OF HIGH-INFLUENCE ATTENTION HEADS IN MLLMS

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `kwon2026rah` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Hyeongjun Kwon, Kwanghoon Sohn |

## 摘要

Multimodal large language models (MLLMs) suffer from a coordination failure during training—attention heads optimize independently despite sharing inputs, leading many to develop suboptimal specialization patterns.
We identify that numerous attention heads exhibit high downstream influence yet minimal cross-modal interaction, acting as performance bottlenecks that propagate misaligned patterns throughout the network.
To address this, we introduce \textbf{RAH-LoRA (Representative Anchor Head Low-Rank Adaptation)}, a training-free calibration method that realigns these problematic heads by trans

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