---
type: literature-corpus-entry
citekey: ott2026simplicity
title: "Simplicity is Key: An Unsupervised Pretraining Approach for Sparse Radio Channels"
authors:
  - "Jonathan Ott"
  - "Alexander Mattick"
  - "Maximilian Stahlke"
  - "Tobias Feigl"
  - "Bjoern Eskofier"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=fNC3aaGeIa"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  We introduce Sparse pretrained Radio Transformer (SpaRTran), an unsupervised representation learning approach based on the concept of compressed sensing for wireless channels. SpaRTran learns embeddings that focus on the physical properties of radio propagation to allow for an efficient fine-tuning on radio-based downstream tasks.
  SpaRTran uses a sparse gated autoencoder that induces a simplicity bias to the learned representations, resembling the sparse nature of radio propagation. For signal reconstruction, it learns a dictionary that holds atomic features, which increases flexibility across
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
  - ott26
---

# Simplicity is Key: An Unsupervised Pretraining Approach for Sparse Radio Channels

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `ott2026simplicity` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Jonathan Ott, Alexander Mattick, Maximilian Stahlke |

## 摘要

We introduce Sparse pretrained Radio Transformer (SpaRTran), an unsupervised representation learning approach based on the concept of compressed sensing for wireless channels. SpaRTran learns embeddings that focus on the physical properties of radio propagation to allow for an efficient fine-tuning on radio-based downstream tasks.
SpaRTran uses a sparse gated autoencoder that induces a simplicity bias to the learned representations, resembling the sparse nature of radio propagation. For signal reconstruction, it learns a dictionary that holds atomic features, which increases flexibility across

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