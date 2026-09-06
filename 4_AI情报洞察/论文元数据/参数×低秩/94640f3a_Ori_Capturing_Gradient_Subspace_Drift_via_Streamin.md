---
type: literature-corpus-entry
citekey: luo2026ori
title: "Ori: Capturing Gradient Subspace Drift via Streaming $k$-PCA for Very Low-Rank LLM Training"
authors:
  - "Xinyu Luo"
  - "Jincheng Zhou"
  - "Mengbo Wang"
  - "Zilin Shen"
  - "Nadia Atallah Lanman"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=jKLvOzsMH7"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  A prominent family of low-rank LLM optimizers, pioneered by GaLore, performs gradient-subspace projection: at each step, they project the gradient into a low-dimensional subspace and map the update back to the full model. This type of training reduces memory, but its effectiveness depends on how the algorithm adapts to a changing gradient subspace as the model is being optimized. Existing work either recomputes the gradient subspace at certain intervals, or performs post-hoc adaption to catch up to the moving subspace. In this work, we explicitly identify that in practice, the LLM gradient sub
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
  - luo26
---

# Ori: Capturing Gradient Subspace Drift via Streaming $k$-PCA for Very Low-Rank LLM Training

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `luo2026ori` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Xinyu Luo, Jincheng Zhou, Mengbo Wang |

## 摘要

A prominent family of low-rank LLM optimizers, pioneered by GaLore, performs gradient-subspace projection: at each step, they project the gradient into a low-dimensional subspace and map the update back to the full model. This type of training reduces memory, but its effectiveness depends on how the algorithm adapts to a changing gradient subspace as the model is being optimized. Existing work either recomputes the gradient subspace at certain intervals, or performs post-hoc adaption to catch up to the moving subspace. In this work, we explicitly identify that in practice, the LLM gradient sub

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