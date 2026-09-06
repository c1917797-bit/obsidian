---
type: literature-corpus-entry
citekey: xun2026dynamicrank
title: "DynamicRank LoRA: Real-Time Adaptive Fine-Tuning \\ for Code Models via Token-Level Importance and Loss Landscape Awareness"
authors:
  - "Bu Xun"
  - "yili xuan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=gMc5Qa45ia"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  \begin{abstract}
  We propose \textbf{DynamicRank LoRA}, a novel fine-tuning mechanism for code models that dynamically adjusts the rank of low-rank adaptation (LoRA) matrices in real-time, addressing the limitations of static rank configurations in conventional LoRA. The proposed approach combines two fundamental ingredients: token level importance scoring: the structural importance of their input tokens and loss landscape aware rank adaptation: rank modulation, which can be adjusted with information about gradient dynamics and curvature. High importance tokens, namely syntax keywords or variab
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
  - xun26
---

# DynamicRank LoRA: Real-Time Adaptive Fine-Tuning \\ for Code Models via Token-Level Importance and Loss Landscape Awareness

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xun2026dynamicrank` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Bu Xun, yili xuan |

## 摘要

\begin{abstract}
We propose \textbf{DynamicRank LoRA}, a novel fine-tuning mechanism for code models that dynamically adjusts the rank of low-rank adaptation (LoRA) matrices in real-time, addressing the limitations of static rank configurations in conventional LoRA. The proposed approach combines two fundamental ingredients: token level importance scoring: the structural importance of their input tokens and loss landscape aware rank adaptation: rank modulation, which can be adjusted with information about gradient dynamics and curvature. High importance tokens, namely syntax keywords or variab

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