---
type: literature-corpus-entry
citekey: yin2026dart
title: "DART: Differentiable Dynamic Adaptive Region Tokenizer for Vision Foundation Models"
authors:
  - "Shicheng Yin"
  - "Kaixuan Yin"
  - "Yang Liu"
  - "Weixing Chen"
  - "Liang Lin"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=82XCBdf8G2"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  The content-agnostic, fixed-grid tokenizers used by standard large-scale vision models like Vision Transformer (ViT) and Vision Mamba (Vim) represent a fundamental performance bottleneck, creating a trade-off between capturing fine-grained detail and suffering from redundant computation. To resolve this dilemma, we introduce DART, a fully differentiable Dynamic Adaptive Region Tokenizer. DART employs learnable region scores and quantile-based partitioning to create content-aware patches of varying sizes, intelligently allocating a higher token density to information-rich regions. The impact of
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
  - yin26
---

# DART: Differentiable Dynamic Adaptive Region Tokenizer for Vision Foundation Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yin2026dart` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Shicheng Yin, Kaixuan Yin, Yang Liu |

## 摘要

The content-agnostic, fixed-grid tokenizers used by standard large-scale vision models like Vision Transformer (ViT) and Vision Mamba (Vim) represent a fundamental performance bottleneck, creating a trade-off between capturing fine-grained detail and suffering from redundant computation. To resolve this dilemma, we introduce DART, a fully differentiable Dynamic Adaptive Region Tokenizer. DART employs learnable region scores and quantile-based partitioning to create content-aware patches of varying sizes, intelligently allocating a higher token density to information-rich regions. The impact of

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