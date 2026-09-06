---
type: literature-corpus-entry
citekey: fang2026router
title: "Router Choice Matters: Rank-Aware Post-Training Quantization for MoE Models"
authors:
  - "Yi-Zeng Fang"
  - "Juinn-Dar Huang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=kPgLp47bJf"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Quantizing Mixture-of-Experts (MoE) language models is challenging since router errors cascade into expert selection and dominate accuracy loss. We study this effect and show that preserving router decisions of the selected experts yields the largest gains, with most errors arising as near-neighbor rank flips around the top-$k$ experts. Motivated by these observations, we present ExpertQuant, a training-free, calibration-only post-training quantization (PTQ) framework tailored to MoE. ExpertQuant combines (i) Expert-Aware Scale to accommodate heterogeneous activation ranges and two router-alig
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
  - 量化
  - fang26
---

# Router Choice Matters: Rank-Aware Post-Training Quantization for MoE Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `fang2026router` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Yi-Zeng Fang, Juinn-Dar Huang |

## 摘要

Quantizing Mixture-of-Experts (MoE) language models is challenging since router errors cascade into expert selection and dominate accuracy loss. We study this effect and show that preserving router decisions of the selected experts yields the largest gains, with most errors arising as near-neighbor rank flips around the top-$k$ experts. Motivated by these observations, we present ExpertQuant, a training-free, calibration-only post-training quantization (PTQ) framework tailored to MoE. ExpertQuant combines (i) Expert-Aware Scale to accommodate heterogeneous activation ranges and two router-alig

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