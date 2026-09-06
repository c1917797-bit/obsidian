---
type: literature-corpus-entry
citekey: adelw2026bayesian
title: "Bayesian Self-Distillation for Image Classification"
authors:
  - "Anton Adelöw"
  - "Matteo Gamba"
  - "Atsuto Maki"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=ISB008MEaM"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Supervised training of deep neural networks for classification typically relies on hard targets, which promote overconfidence and often limit calibration, generalization, and robustness. Self-distillation methods aim to mitigate this by leveraging inter-class and sample-specific information present in the model’s own predictions, but often remain dependent on hard targets, limiting their effectiveness. With this in mind, we propose Bayesian Self-Distillation (BSD), a principled method for constructing sample-specific target distributions via Bayesian inference using the model’s own predictions
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
  - 蒸馏
  - adelöw26
---

# Bayesian Self-Distillation for Image Classification

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `adelw2026bayesian` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Anton Adelöw, Matteo Gamba, Atsuto Maki |

## 摘要

Supervised training of deep neural networks for classification typically relies on hard targets, which promote overconfidence and often limit calibration, generalization, and robustness. Self-distillation methods aim to mitigate this by leveraging inter-class and sample-specific information present in the model’s own predictions, but often remain dependent on hard targets, limiting their effectiveness. With this in mind, we propose Bayesian Self-Distillation (BSD), a principled method for constructing sample-specific target distributions via Bayesian inference using the model’s own predictions

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