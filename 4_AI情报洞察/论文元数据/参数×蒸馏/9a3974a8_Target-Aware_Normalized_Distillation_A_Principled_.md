---
type: literature-corpus-entry
citekey: wen2026target
title: "Target-Aware Normalized Distillation: A Principled Framework for Robust Knowledge Transfer"
authors:
  - "Hongwei Wen"
  - "Ke Xu"
  - "YuqiZhou"
  - "Jingyi Cui"
  - "Hanyuan Hang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=XDUtRsxxwi"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  \textit{Knowledge Distillation} (\textit{KD}) has become a cornerstone for model compression, semi-supervised learning, and self-training.
  Despite its success, the standard KL-based objective suffers from a structural flaw: it \emph{couples} supervision on target and non-target classes. This coupling links the estimation of target probability mass to the loss on non-target probabilities, thereby amplifying mass mismatch and destabilizing optimization under noise or teacher miscalibration. To address this issue, we propose \emph{Target-Aware Normalized Distillation} (\textit{TAND}), a principl
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
  - wen26
---

# Target-Aware Normalized Distillation: A Principled Framework for Robust Knowledge Transfer

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wen2026target` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Hongwei Wen, Ke Xu, YuqiZhou |

## 摘要

\textit{Knowledge Distillation} (\textit{KD}) has become a cornerstone for model compression, semi-supervised learning, and self-training. 
Despite its success, the standard KL-based objective suffers from a structural flaw: it \emph{couples} supervision on target and non-target classes. This coupling links the estimation of target probability mass to the loss on non-target probabilities, thereby amplifying mass mismatch and destabilizing optimization under noise or teacher miscalibration. To address this issue, we propose \emph{Target-Aware Normalized Distillation} (\textit{TAND}), a principl

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