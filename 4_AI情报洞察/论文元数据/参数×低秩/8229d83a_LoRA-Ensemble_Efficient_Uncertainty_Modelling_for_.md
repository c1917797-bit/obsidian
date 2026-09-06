---
type: literature-corpus-entry
citekey: mhlematter2026lora
title: "LoRA-Ensemble: Efficient Uncertainty Modelling for Self-Attention Networks"
authors:
  - "Dominik J. Mühlematter"
  - "Michelle Halbheer"
  - "Alexander Becker"
  - "Dominik Narnhofer"
  - "Helge Aasen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=nraPBoEJfU"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Numerous real-world decisions rely on machine learning algorithms and require calibrated uncertainty estimates. However, modern methods often yield overconfident, uncalibrated predictions. The dominant approach to quantifying the uncertainty inherent in the model is to train an ensemble of separate predictors and measure their empirical variance. In an explicit implementation the ensemble has high computational cost and memory footprint, especially if the base model itself is already large, like modern transformers. This motivates efforts to develop implicit ensemble methods that emulate the e
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
  - mühlematter26
---

# LoRA-Ensemble: Efficient Uncertainty Modelling for Self-Attention Networks

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `mhlematter2026lora` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Dominik J. Mühlematter, Michelle Halbheer, Alexander Becker |

## 摘要

Numerous real-world decisions rely on machine learning algorithms and require calibrated uncertainty estimates. However, modern methods often yield overconfident, uncalibrated predictions. The dominant approach to quantifying the uncertainty inherent in the model is to train an ensemble of separate predictors and measure their empirical variance. In an explicit implementation the ensemble has high computational cost and memory footprint, especially if the base model itself is already large, like modern transformers. This motivates efforts to develop implicit ensemble methods that emulate the e

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