---
type: literature-corpus-entry
citekey: lin2026enhancing
title: "Enhancing LoRA with Shared Random-Span Augmentation for Parameter-Efficient Visual Adaptation"
authors:
  - "Zhijun Lin"
  - "Wenyi Zhao"
  - "Man Jiang"
  - "Junsheng Wu"
  - "Hao Luo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=pON6HlMkoK"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low-rank Adaptation (LoRA) efficiently adapts large pre-trained models to downstream tasks by learning low-rank adapters, significantly reducing computational and memory costs without sacrificing performance. Recent studies highlight the promise of rank adaptation methods in improving the flexibility and performance of LoRA. Grounded in Singular Value Decomposition (SVD) theory, these methods decompose the weight update into parameterized unitary matrices and learnable scaling coefficients, thereby allowing dynamic rank allocation of adapters based on coefficients. However, the parameterized c
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

# Enhancing LoRA with Shared Random-Span Augmentation for Parameter-Efficient Visual Adaptation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lin2026enhancing` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Zhijun Lin, Wenyi Zhao, Man Jiang |

## 摘要

Low-rank Adaptation (LoRA) efficiently adapts large pre-trained models to downstream tasks by learning low-rank adapters, significantly reducing computational and memory costs without sacrificing performance. Recent studies highlight the promise of rank adaptation methods in improving the flexibility and performance of LoRA. Grounded in Singular Value Decomposition (SVD) theory, these methods decompose the weight update into parameterized unitary matrices and learnable scaling coefficients, thereby allowing dynamic rank allocation of adapters based on coefficients. However, the parameterized c

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