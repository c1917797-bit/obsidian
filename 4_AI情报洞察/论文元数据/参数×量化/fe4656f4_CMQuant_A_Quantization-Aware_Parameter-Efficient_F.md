---
type: literature-corpus-entry
citekey: xu2026cmquant
title: "CMQuant: A Quantization-Aware Parameter-Efficient Fine-Tuning Framework for 4-Bit Consistency Models"
authors:
  - "Chen Xu"
  - "Dawei Yang"
  - "Mingjia Shi"
  - "Xing Hu"
  - "Jiangyong Yu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=cNn18vs23o"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Consistency Models (CMs), built on diffusion models, use model state trajectory fitting to reduce iterations required for sample generation. However, they still maintain high per-iteration computational costs and large model parameter sizes, which hinder deployment on resource-constrained devices. Quantization, an effective model compression technique with notable success in Large Language Models, remains largely unexplored for CMs. We observe that the unique characteristics of CMs pose significant obstacles to effective quantization. First, the trajectory fitting errors inherent to CMs accumu
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
  - xu26
---

# CMQuant: A Quantization-Aware Parameter-Efficient Fine-Tuning Framework for 4-Bit Consistency Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xu2026cmquant` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Chen Xu, Dawei Yang, Mingjia Shi |

## 摘要

Consistency Models (CMs), built on diffusion models, use model state trajectory fitting to reduce iterations required for sample generation. However, they still maintain high per-iteration computational costs and large model parameter sizes, which hinder deployment on resource-constrained devices. Quantization, an effective model compression technique with notable success in Large Language Models, remains largely unexplored for CMs. We observe that the unique characteristics of CMs pose significant obstacles to effective quantization. First, the trajectory fitting errors inherent to CMs accumu

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