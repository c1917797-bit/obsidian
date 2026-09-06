---
type: literature-corpus-entry
citekey: su2026anchor
title: "Anchor–MoE: A Mean-Anchored Mixture of Experts for Probabilistic Regression"
authors:
  - "Baozhuo Su"
  - "Zhengxian Qu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=5k1vfgXgom"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  We present Anchor-MoE, an anchored mixture-of-experts for probabilistic and point regression. A base anchor prediction is concatenated with the inputs and mapped to a compact latent space. A learnable metric window with a soft top-$k$ router induces sparse weights over lightweight MDN experts, which output residual corrections and heteroscedastic scales. Training uses negative log-likelihood with an optional held-out linear calibration to refine point accuracy. Theoretically, under Hölder-smooth targets and fixed partition-of-unity weights with bounded overlap, Anchor-MoE attains the minimax-o
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
  - su26
---

# Anchor–MoE: A Mean-Anchored Mixture of Experts for Probabilistic Regression

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `su2026anchor` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Baozhuo Su, Zhengxian Qu |

## 摘要

We present Anchor-MoE, an anchored mixture-of-experts for probabilistic and point regression. A base anchor prediction is concatenated with the inputs and mapped to a compact latent space. A learnable metric window with a soft top-$k$ router induces sparse weights over lightweight MDN experts, which output residual corrections and heteroscedastic scales. Training uses negative log-likelihood with an optional held-out linear calibration to refine point accuracy. Theoretically, under Hölder-smooth targets and fixed partition-of-unity weights with bounded overlap, Anchor-MoE attains the minimax-o

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