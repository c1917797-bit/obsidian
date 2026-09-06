---
type: literature-corpus-entry
citekey: song2026cleanedit
title: "CleanEdit: Retention-Aware Pruning and Bounded Replay for Lifelong Model Editing"
authors:
  - "Haoyuan Song"
  - "Haihua Luo"
  - "Ming Wang"
  - "Yisu Wang"
  - "Qi Xu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=pguFq8hyd4"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  While lifelong model editing allows deployed systems to be updated continuously, the accumulation of edits often leads to performance decay and instability. This decay stems from the unchecked growth of the edit memory, where redundant or harmful entries corrupt the model's knowledge and increase inference costs. We address this challenge with CleanEdit, a self-maintaining mechanism that actively manages the edit memory. The core of CleanEdit is a principled maintenance loop. It first diagnoses the impact of each edit by estimating its counterfactual harm. A sequential hypothesis test then mak
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
  - song26
---

# CleanEdit: Retention-Aware Pruning and Bounded Replay for Lifelong Model Editing

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `song2026cleanedit` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Haoyuan Song, Haihua Luo, Ming Wang |

## 摘要

While lifelong model editing allows deployed systems to be updated continuously, the accumulation of edits often leads to performance decay and instability. This decay stems from the unchecked growth of the edit memory, where redundant or harmful entries corrupt the model's knowledge and increase inference costs. We address this challenge with CleanEdit, a self-maintaining mechanism that actively manages the edit memory. The core of CleanEdit is a principled maintenance loop. It first diagnoses the impact of each edit by estimating its counterfactual harm. A sequential hypothesis test then mak

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