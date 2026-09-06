---
type: literature-corpus-entry
citekey: wang2026circle
title: "Circle-RoPE: Cone-like Decoupled Rotary Positional Embedding for Vision-Language Models"
authors:
  - "Chengcheng Wang"
  - "Jianyuan Guo"
  - "Hongguang Li"
  - "Yuchuan Tian"
  - "Ying Nie"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=QmBXLMbTSL"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Rotary Position Embedding (RoPE) is a widely adopted technique for encoding relative positional information in large language models (LLMs). However, when extended to vision-language models (VLMs), RoPE and its variants enforce relative positional dependencies separately within text and image tokens, introducing unintended cross-modal positional biases. For example, image tokens depicting semantically consistent content are assigned distinct positional encodings solely due to spatial location variations. As a result, such tokens exhibit entirely different relative positional relationships with
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
  - wang26
---

# Circle-RoPE: Cone-like Decoupled Rotary Positional Embedding for Vision-Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026circle` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Chengcheng Wang, Jianyuan Guo, Hongguang Li |

## 摘要

Rotary Position Embedding (RoPE) is a widely adopted technique for encoding relative positional information in large language models (LLMs). However, when extended to vision-language models (VLMs), RoPE and its variants enforce relative positional dependencies separately within text and image tokens, introducing unintended cross-modal positional biases. For example, image tokens depicting semantically consistent content are assigned distinct positional encodings solely due to spatial location variations. As a result, such tokens exhibit entirely different relative positional relationships with

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