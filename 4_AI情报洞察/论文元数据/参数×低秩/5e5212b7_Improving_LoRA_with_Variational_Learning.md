---
type: literature-corpus-entry
citekey: cong2026improving
title: "Improving LoRA with Variational Learning"
authors:
  - "Bai Cong"
  - "Nico Daheim"
  - "Yuesong Shen"
  - "Rio Yokota"
  - "Mohammad Emtiyaz Khan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=oY4CQ2GJkC"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Bayesian methods have recently been used to improve calibration of LoRA fine-tuning but there is still room for improvements. For instance, with Laplace's method no effective gains in accuracy are seen while variational learning can sometimes even harm it and increase both runtime and implementation complexity. Here, we propose two simple modifications to variational learning that fix all of these issues. First, we reduce cost and simplify implementation by adapting the recently proposed IVON optimizer for LoRA training. Second, we propose new scaling and pruning techniques for posteriors to i
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
  - cong26
---

# Improving LoRA with Variational Learning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `cong2026improving` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Bai Cong, Nico Daheim, Yuesong Shen |

## 摘要

Bayesian methods have recently been used to improve calibration of LoRA fine-tuning but there is still room for improvements. For instance, with Laplace's method no effective gains in accuracy are seen while variational learning can sometimes even harm it and increase both runtime and implementation complexity. Here, we propose two simple modifications to variational learning that fix all of these issues. First, we reduce cost and simplify implementation by adapting the recently proposed IVON optimizer for LoRA training. Second, we propose new scaling and pruning techniques for posteriors to i

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