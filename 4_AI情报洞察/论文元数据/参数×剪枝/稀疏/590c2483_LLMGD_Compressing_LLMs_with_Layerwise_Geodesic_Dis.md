---
type: literature-corpus-entry
citekey: shuvo2026llmgd
title: "LLMGD: Compressing LLMs with Layerwise Geodesic Distances"
authors:
  - "Soumen Sikder Shuvo"
  - "Jinwen Wu"
  - "Zhuo Feng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=q9XfCTwaJ6"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Understanding how internal representations evolve across layers in large language models (LLMs) is critical for interpretability, robustness, and efficient model design. We introduce LLMGD, a stability-guided pruning metric grounded in spectral graph theory. For each layer, we estimate a precision matrix from embedding vectors that characterize the model’s internal states, and then compute the geodesic distance on the cone of symmetric positive definite (SPD) matrices between successive layers. This yields a smooth and robust measure of representational distortion, identifying layers with mini
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
  - 剪枝/稀疏
  - shuvo26
---

# LLMGD: Compressing LLMs with Layerwise Geodesic Distances

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `shuvo2026llmgd` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Soumen Sikder Shuvo, Jinwen Wu, Zhuo Feng |

## 摘要

Understanding how internal representations evolve across layers in large language models (LLMs) is critical for interpretability, robustness, and efficient model design. We introduce LLMGD, a stability-guided pruning metric grounded in spectral graph theory. For each layer, we estimate a precision matrix from embedding vectors that characterize the model’s internal states, and then compute the geodesic distance on the cone of symmetric positive definite (SPD) matrices between successive layers. This yields a smooth and robust measure of representational distortion, identifying layers with mini

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