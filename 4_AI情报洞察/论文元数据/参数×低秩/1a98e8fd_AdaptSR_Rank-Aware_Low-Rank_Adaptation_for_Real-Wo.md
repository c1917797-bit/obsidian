---
type: literature-corpus-entry
citekey: korkmaz2026adaptsr
title: "AdaptSR: Rank-Aware Low-Rank Adaptation for Real-World Super-Resolution"
authors:
  - "Cansu Korkmaz"
  - "Nancy Mehta"
  - "Radu Timofte"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Ml2bDkzNeq"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Recovering high-frequency details from low-resolution images remains a central challenge in super-resolution (SR), particularly under complex and unknown real-world degradations. While GAN-based methods improve perceptual sharpness, they are unstable and introduce artifacts, and diffusion models achieve strong fidelity but demand excessive computation, even in few-step variants. We present AdaptSR, a rank-aware low-rank adaptation framework that efficiently repurposes bicubic-trained CNN and Transformer SR backbones for real-world tasks. Unlike full fine-tuning, AdaptSR inserts lightweight LoR
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
  - korkmaz26
---

# AdaptSR: Rank-Aware Low-Rank Adaptation for Real-World Super-Resolution

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `korkmaz2026adaptsr` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Cansu Korkmaz, Nancy Mehta, Radu Timofte |

## 摘要

Recovering high-frequency details from low-resolution images remains a central challenge in super-resolution (SR), particularly under complex and unknown real-world degradations. While GAN-based methods improve perceptual sharpness, they are unstable and introduce artifacts, and diffusion models achieve strong fidelity but demand excessive computation, even in few-step variants. We present AdaptSR, a rank-aware low-rank adaptation framework that efficiently repurposes bicubic-trained CNN and Transformer SR backbones for real-world tasks. Unlike full fine-tuning, AdaptSR inserts lightweight LoR

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