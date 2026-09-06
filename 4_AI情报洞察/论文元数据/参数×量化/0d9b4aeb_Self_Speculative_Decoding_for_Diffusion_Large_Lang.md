---
type: literature-corpus-entry
citekey: gao2026self
title: "Self Speculative Decoding for Diffusion Large Language Model"
authors:
  - "Yifeng Gao"
  - "Ziang Ji"
  - "Yuxuan Wang"
  - "Biqing Qi"
  - "Hanlin xu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=rKJ7A30lQQ"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Diffusion-based Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive models, offering unique advantages through bidirectional attention mechanisms and iterative denoising processes. However, their practical deployment is hindered by high inference latency, particularly in memory-bound scenarios where traditional acceleration techniques like Key-Value caching are incompatible due to the bidirectional nature of dLLMs. We propose Self Speculative Decoding (SSD), a novel inference acceleration framework that leverages the dLLM itself as both drafter and verifier
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
  - gao26
---

# Self Speculative Decoding for Diffusion Large Language Model

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `gao2026self` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yifeng Gao, Ziang Ji, Yuxuan Wang |

## 摘要

Diffusion-based Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive models, offering unique advantages through bidirectional attention mechanisms and iterative denoising processes. However, their practical deployment is hindered by high inference latency, particularly in memory-bound scenarios where traditional acceleration techniques like Key-Value caching are incompatible due to the bidirectional nature of dLLMs. We propose Self Speculative Decoding (SSD), a novel inference acceleration framework that leverages the dLLM itself as both drafter and verifier 

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