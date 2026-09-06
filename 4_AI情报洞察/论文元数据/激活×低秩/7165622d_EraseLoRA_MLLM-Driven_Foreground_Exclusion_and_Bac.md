---
type: literature-corpus-entry
citekey: jo2026eraselora
title: "EraseLoRA: MLLM-Driven Foreground Exclusion and Background Subtype Aggregation for Dataset-Free Object Removal"
authors:
  - "Sanghyun Jo"
  - "Donghwan Lee"
  - "Eunji Jung"
  - "Seong Je Oh"
  - "Kyungsu Kim"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=mEspnOwfPv"
pdf_url: ""
object: 激活
method: 低秩
cell: "激活×低秩"
all_objects: []
all_methods: []
abstract: |
  Object removal requires more than erasing a target—it must reconstruct the missing region with high structural fidelity while preserving diverse background context. Existing diffusion-based dataset-free approaches attempt to redirect self-attention away from the masked target but fail in two critical ways: (1) non-target foregrounds are often misinterpreted as background, causing unintended object regeneration, and (2) disruption of short-range activations degrades fine details and prevents coherent integration of multiple background cues. We introduce EraseLoRA, a dataset-free object-removal
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
  - 激活
  - 低秩
  - jo26
---

# EraseLoRA: MLLM-Driven Foreground Exclusion and Background Subtype Aggregation for Dataset-Free Object Removal

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `jo2026eraselora` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×低秩 |
| **来源** | openreview |
| **作者** | Sanghyun Jo, Donghwan Lee, Eunji Jung |

## 摘要

Object removal requires more than erasing a target—it must reconstruct the missing region with high structural fidelity while preserving diverse background context. Existing diffusion-based dataset-free approaches attempt to redirect self-attention away from the masked target but fail in two critical ways: (1) non-target foregrounds are often misinterpreted as background, causing unintended object regeneration, and (2) disruption of short-range activations degrades fine details and prevents coherent integration of multiple background cues. We introduce EraseLoRA, a dataset-free object-removal 

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