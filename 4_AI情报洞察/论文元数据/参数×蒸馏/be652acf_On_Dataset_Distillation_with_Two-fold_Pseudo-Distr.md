---
type: literature-corpus-entry
citekey: liu2026on
title: "On Dataset Distillation with Two-fold Pseudo-Distribution Matching"
authors:
  - "Yutao Liu"
  - "Xiaobo Zhang"
  - "Hao Wang"
  - "Yan Yang"
  - "Wei Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=2f3gBOiVBG"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  The goal of dataset distillation (DD) is to learn a compact synthetic dataset that maintains comparable generalization performance with the original. Distribution matching (DM), a leading DD approach, excels in addressing model scalability. However, current methods struggle with inherent feature and distribution shifts, facing a trade-off between efficiency and effectiveness. This paper reveals that in DM, models should prioritize similar samples (similar samples) when the image-per-class (IPC) is low, while incorporating diverse samples (diverse samples) as IPC increases to capture broader in
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
  - liu26
---

# On Dataset Distillation with Two-fold Pseudo-Distribution Matching

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026on` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Yutao Liu, Xiaobo Zhang, Hao Wang |

## 摘要

The goal of dataset distillation (DD) is to learn a compact synthetic dataset that maintains comparable generalization performance with the original. Distribution matching (DM), a leading DD approach, excels in addressing model scalability. However, current methods struggle with inherent feature and distribution shifts, facing a trade-off between efficiency and effectiveness. This paper reveals that in DM, models should prioritize similar samples (similar samples) when the image-per-class (IPC) is low, while incorporating diverse samples (diverse samples) as IPC increases to capture broader in

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