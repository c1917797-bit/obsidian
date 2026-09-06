---
type: literature-corpus-entry
citekey: li2026probabilistic
title: "Probabilistic TopK Sparse Autoencoder for Interpreting the Activations of Large Language Models"
authors:
  - "Raymond Li"
  - "Chuyuan Li"
  - "Anji Ma"
  - "Gabriel Murray"
  - "Giuseppe Carenini"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=zMIIHeKivz"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Sparse Autoencoders (SAEs) have emerged as a popular solution for extracting interpretable features from language model activations, enabling mechanistic understanding by decomposing polysemantic neurons into sparsely activated dictionary components.  However, existing SAE designs suffer from deterministic, activations that starve gradients to ``dead'' components, and produce uncalibrated coefficients that provide no meaningful notion of uncertainty. To address these limitations, we introduce Probabilistic TopK SAEs, a novel approach that augments the TopK autoencoder with probabilistic gating
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
  - 剪枝/稀疏
  - li26
---

# Probabilistic TopK Sparse Autoencoder for Interpreting the Activations of Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026probabilistic` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Raymond Li, Chuyuan Li, Anji Ma |

## 摘要

Sparse Autoencoders (SAEs) have emerged as a popular solution for extracting interpretable features from language model activations, enabling mechanistic understanding by decomposing polysemantic neurons into sparsely activated dictionary components.  However, existing SAE designs suffer from deterministic, activations that starve gradients to ``dead'' components, and produce uncalibrated coefficients that provide no meaningful notion of uncertainty. To address these limitations, we introduce Probabilistic TopK SAEs, a novel approach that augments the TopK autoencoder with probabilistic gating

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