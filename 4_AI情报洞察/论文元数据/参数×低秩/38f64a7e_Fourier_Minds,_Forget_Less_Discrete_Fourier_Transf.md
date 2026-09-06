---
type: literature-corpus-entry
citekey: lin2026fourier
title: "Fourier Minds, Forget Less: Discrete Fourier Transform for Fast and Robust Continual Learning in LLMs"
authors:
  - "Haokun Lin"
  - "Shujun Xia"
  - "Haobo Xu"
  - "Teng Wang"
  - "Jingyi Su"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=cQ8VPIMbfN"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Continual learning (CL) for large language models (LLMs) is challenged by both catastrophic forgetting and efficiency constraints when facing long sequential tasks. While low-rank adaptation in LoRA-based approaches reduces per-task trainable parameters, the cumulative parameter budget grows with stream length and can be substantial. This limits their applicability in lifelong learning scenarios, especially under strict resource constraints. In this work, we explore the potential of the parameter-efficient Sparse Fourier Transform (SFT) in the context of continual learning. Our preliminary exp
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
  - lin26
---

# Fourier Minds, Forget Less: Discrete Fourier Transform for Fast and Robust Continual Learning in LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lin2026fourier` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Haokun Lin, Shujun Xia, Haobo Xu |

## 摘要

Continual learning (CL) for large language models (LLMs) is challenged by both catastrophic forgetting and efficiency constraints when facing long sequential tasks. While low-rank adaptation in LoRA-based approaches reduces per-task trainable parameters, the cumulative parameter budget grows with stream length and can be substantial. This limits their applicability in lifelong learning scenarios, especially under strict resource constraints. In this work, we explore the potential of the parameter-efficient Sparse Fourier Transform (SFT) in the context of continual learning. Our preliminary exp

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