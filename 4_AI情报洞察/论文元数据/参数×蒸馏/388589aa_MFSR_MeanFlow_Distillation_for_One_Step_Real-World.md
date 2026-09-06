---
type: literature-corpus-entry
citekey: wang2026mfsr
title: "MFSR: MeanFlow Distillation for One Step Real-World Image Super Resolution"
authors:
  - "Ruiqing Wang"
  - "Yuanzhi Zhu"
  - "Kai Zhang"
  - "Hanshu Yan"
  - "Shilin Lu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qDg8KNq0Fm"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Diffusion- and flow-based models have advanced real-world image super-resolution (Real-ISR), but their multi-step sampling makes inference slow and hard to deploy. One-step distillation alleviates the cost, yet often degrades restoration quality and removes the option to refine with more steps. We present Mean Flows for Super-Resolution (MFSR), a new distillation framework that produces photorealistic, high-fidelity results in a single step while still allowing an optional multi-step path for further improvement. Our approach uses MeanFlow as the learning target, enabling the student to approx
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
  - wang26
---

# MFSR: MeanFlow Distillation for One Step Real-World Image Super Resolution

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026mfsr` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Ruiqing Wang, Yuanzhi Zhu, Kai Zhang |

## 摘要

Diffusion- and flow-based models have advanced real-world image super-resolution (Real-ISR), but their multi-step sampling makes inference slow and hard to deploy. One-step distillation alleviates the cost, yet often degrades restoration quality and removes the option to refine with more steps. We present Mean Flows for Super-Resolution (MFSR), a new distillation framework that produces photorealistic, high-fidelity results in a single step while still allowing an optional multi-step path for further improvement. Our approach uses MeanFlow as the learning target, enabling the student to approx

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