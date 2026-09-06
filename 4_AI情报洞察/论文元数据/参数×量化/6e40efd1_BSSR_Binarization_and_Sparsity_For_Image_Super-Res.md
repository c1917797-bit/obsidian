---
type: literature-corpus-entry
citekey: xin2026bssr
title: "BSSR: Binarization and Sparsity For Image Super-Resolution"
authors:
  - "Jingwei Xin"
  - "Bin Wei"
  - "Nannan Wang"
  - "Jie Li"
  - "Xinbo Gao"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=8Vp3k3EEZi"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Lighter models and faster inference remain the focus in the field of image super-resolution. Quantization and pruning are both effective methods for compressing deep models. Unfortunately, existing approaches often optimize quantization and pruning independently: standalone binarization reduces storage but underutilizes sparsity, while N:M sparsity on weights accelerates inference but leaves high-bit storage overhead. Notably, no prior work has explored N:M sparse binary SR networks. In this paper, we combine quantization and sparsity to propose an extreme compression method for super-resoluti
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
  - xin26
---

# BSSR: Binarization and Sparsity For Image Super-Resolution

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xin2026bssr` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Jingwei Xin, Bin Wei, Nannan Wang |

## 摘要

Lighter models and faster inference remain the focus in the field of image super-resolution. Quantization and pruning are both effective methods for compressing deep models. Unfortunately, existing approaches often optimize quantization and pruning independently: standalone binarization reduces storage but underutilizes sparsity, while N:M sparsity on weights accelerates inference but leaves high-bit storage overhead. Notably, no prior work has explored N:M sparse binary SR networks. In this paper, we combine quantization and sparsity to propose an extreme compression method for super-resoluti

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