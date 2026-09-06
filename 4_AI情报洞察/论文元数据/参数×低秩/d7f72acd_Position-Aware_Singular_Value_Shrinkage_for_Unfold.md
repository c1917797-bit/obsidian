---
type: literature-corpus-entry
citekey: chen2026position
title: "Position-Aware Singular Value Shrinkage for Unfolded Dynamic MRI Reconstruction"
authors:
  - "Hongtao Chen"
  - "Zhe Yang"
  - "Wenrui Li"
  - "Guanghui Cheng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=JwJiDLvJWm"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Dynamic MRI reconstruction benefits from low-rank priors to exploit spatiotemporal redundancy. Recent deep unfolding networks (DUNs) often adopt Singular Value Thresholding (SVT) to apply low-rank constraints. However, most methods apply uniform or globally scaled thresholds, ignoring the unequal importance of singular values and the resolution-dependent nature of dynamic MR images. This leads to suboptimal shrinkage and poor generalization across anatomical variations. Existing adaptive shrinkage techniques in classical models are not trainable and incompatible with end-to-end learning. To ad
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
  - chen26
---

# Position-Aware Singular Value Shrinkage for Unfolded Dynamic MRI Reconstruction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026position` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Hongtao Chen, Zhe Yang, Wenrui Li |

## 摘要

Dynamic MRI reconstruction benefits from low-rank priors to exploit spatiotemporal redundancy. Recent deep unfolding networks (DUNs) often adopt Singular Value Thresholding (SVT) to apply low-rank constraints. However, most methods apply uniform or globally scaled thresholds, ignoring the unequal importance of singular values and the resolution-dependent nature of dynamic MR images. This leads to suboptimal shrinkage and poor generalization across anatomical variations. Existing adaptive shrinkage techniques in classical models are not trainable and incompatible with end-to-end learning. To ad

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