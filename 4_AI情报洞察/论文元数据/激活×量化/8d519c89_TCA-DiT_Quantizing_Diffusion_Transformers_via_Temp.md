---
type: literature-corpus-entry
citekey: zheng2026tca
title: "TCA-DiT: Quantizing Diffusion Transformers via Temporal Channel Alignment"
authors:
  - "Wenjie Zheng"
  - "Haoji Hu"
  - "Zou Xingze"
  - "Jing Wang"
  - "Lianrui Mu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=SBVqQAmYkC"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Diffusion Transformers (DiTs) have achieved remarkable success in generative modeling, but their deployment is hindered by massive model sizes and high inference costs. Post-Training Quantization (PTQ) offers a retraining-free compression paradigm, yet its application to DiTs is particularly challenging due to timestep-varying, channel-wise activation anomalies. These anomalies vary dynamically across timesteps, undermining existing rotation- or scaling-based PTQ methods and leaving residual misaligned anomaly channels that impair quantization fidelity. We propose **TCA-DiT**—**T**emporal **C*
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
  - zheng26
---

# TCA-DiT: Quantizing Diffusion Transformers via Temporal Channel Alignment

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zheng2026tca` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Wenjie Zheng, Haoji Hu, Zou Xingze |

## 摘要

Diffusion Transformers (DiTs) have achieved remarkable success in generative modeling, but their deployment is hindered by massive model sizes and high inference costs. Post-Training Quantization (PTQ) offers a retraining-free compression paradigm, yet its application to DiTs is particularly challenging due to timestep-varying, channel-wise activation anomalies. These anomalies vary dynamically across timesteps, undermining existing rotation- or scaling-based PTQ methods and leaving residual misaligned anomaly channels that impair quantization fidelity. We propose **TCA-DiT**—**T**emporal **C*

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