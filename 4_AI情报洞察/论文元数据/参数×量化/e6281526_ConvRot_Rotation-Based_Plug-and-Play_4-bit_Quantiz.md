---
type: literature-corpus-entry
citekey: huang2026convrot
title: "ConvRot: Rotation-Based Plug-and-Play 4-bit Quantization for Diffusion Transformers"
authors:
  - "Feice Huang"
  - "Zuliang Han"
  - "Xing Zhou"
  - "Yihuang Chen"
  - "Lifei Zhu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=SCC11m676G"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Diffusion models have demonstrated strong capabilities in generating high-quality images. However, as model size increases, the growing memory footprint and inference latency pose significant challenges for practical deployment. Recent studies in large language models (LLMs) show that rotation-based techniques can smooth outliers and enable 4-bit quantization, but these approaches often incur substantial overhead and struggle with row-wise outliers in diffusion transformers. To address these challenges, we develop a theoretical framework: we define column discrepancy to quantify imbalance in H
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
  - huang26
---

# ConvRot: Rotation-Based Plug-and-Play 4-bit Quantization for Diffusion Transformers

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `huang2026convrot` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Feice Huang, Zuliang Han, Xing Zhou |

## 摘要

Diffusion models have demonstrated strong capabilities in generating high-quality images. However, as model size increases, the growing memory footprint and inference latency pose significant challenges for practical deployment. Recent studies in large language models (LLMs) show that rotation-based techniques can smooth outliers and enable 4-bit quantization, but these approaches often incur substantial overhead and struggle with row-wise outliers in diffusion transformers. To address these challenges, we develop a theoretical framework: we define column discrepancy to quantify imbalance in H

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