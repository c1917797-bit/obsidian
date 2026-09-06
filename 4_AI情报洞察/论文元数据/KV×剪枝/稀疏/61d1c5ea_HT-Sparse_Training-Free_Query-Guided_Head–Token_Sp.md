---
type: literature-corpus-entry
citekey: cai2026ht
title: "HT-Sparse: Training-Free Query-Guided Head–Token Sparsification for Long-Video Multimodal Inference"
authors:
  - "Zhuangzhuang Cai"
  - "Yuxiang Ma"
  - "Ling Xie"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=3Oc8Pg7Kij"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Long-video multimodal inference is limited by the quadratic cost of dense attention, cumulative KV-cache growth during decoding, and cross-modal interference, while retraining sparsity-aware variants is often impractical. We present HT-Sparse, a training-free, query-guided hierarchical sparsification that performs joint head–token computation to reduce both latency and memory without parameter updates. The method comprises two components executed adaptively across layers: (i) query-conditioned head sparsification, which ranks attention heads via analytically stable saliency statistics to retai
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
  - KV
  - 剪枝/稀疏
  - cai26
---

# HT-Sparse: Training-Free Query-Guided Head–Token Sparsification for Long-Video Multimodal Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `cai2026ht` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Zhuangzhuang Cai, Yuxiang Ma, Ling Xie |

## 摘要

Long-video multimodal inference is limited by the quadratic cost of dense attention, cumulative KV-cache growth during decoding, and cross-modal interference, while retraining sparsity-aware variants is often impractical. We present HT-Sparse, a training-free, query-guided hierarchical sparsification that performs joint head–token computation to reduce both latency and memory without parameter updates. The method comprises two components executed adaptively across layers: (i) query-conditioned head sparsification, which ranks attention heads via analytically stable saliency statistics to retai

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