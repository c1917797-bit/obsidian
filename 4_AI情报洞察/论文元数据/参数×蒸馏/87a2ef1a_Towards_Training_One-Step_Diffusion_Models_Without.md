---
type: literature-corpus-entry
citekey: zhang2026towards
title: "Towards Training One-Step Diffusion Models Without Distillation"
authors:
  - "Mingtian Zhang"
  - "Wenlin Chen"
  - "Jiajun He"
  - "Zijing Ou"
  - "José Miguel Hernández-Lobato"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=hCy2mld5DK"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Recent advances in training one-step diffusion models typically follow a two-stage pipeline: first training a teacher diffusion model and then distilling it into a one-step student model. This process often depends on both the teacher’s score function for supervision and its weights for initializing the student model. In this paper, we explore whether one-step diffusion models can be trained directly without this distillation procedure. We introduce a family of new training methods that entirely forgo teacher score supervision, yet outperforms most teacher-guided distillation approaches. This
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
  - zhang26
---

# Towards Training One-Step Diffusion Models Without Distillation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026towards` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Mingtian Zhang, Wenlin Chen, Jiajun He |

## 摘要

Recent advances in training one-step diffusion models typically follow a two-stage pipeline: first training a teacher diffusion model and then distilling it into a one-step student model. This process often depends on both the teacher’s score function for supervision and its weights for initializing the student model. In this paper, we explore whether one-step diffusion models can be trained directly without this distillation procedure. We introduce a family of new training methods that entirely forgo teacher score supervision, yet outperforms most teacher-guided distillation approaches. This 

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