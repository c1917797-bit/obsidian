---
type: literature-corpus-entry
citekey: fan2026phased
title: "Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals"
authors:
  - "Xiangyu Fan"
  - "Zesong Qiu"
  - "Zhuguanyu Wu"
  - "Fanzhou Wang"
  - "Zhiqian Lin"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=zzJTo7ujql"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Distribution Matching Distillation (DMD) distills score-based generative models into efficient one-step generators,
  without requiring a one-to-one correspondence with the sampling trajectories of their teachers.
  However, limited model capacity causes one-step distilled models underperform on complex generative tasks, e.g.,
  synthesizing intricate object motions in text-to-video generation.
  Directly extending DMD to multi-step distillation increases memory usage and computational depth, leading to instability and reduced efficiency.
  While prior works propose stochastic gradient truncation as a
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
  - fan26
---

# Phased DMD: Few-step Distribution Matching Distillation via Score Matching within Subintervals

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `fan2026phased` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Xiangyu Fan, Zesong Qiu, Zhuguanyu Wu |

## 摘要

Distribution Matching Distillation (DMD) distills score-based generative models into efficient one-step generators,
without requiring a one-to-one correspondence with the sampling trajectories of their teachers.
However, limited model capacity causes one-step distilled models underperform on complex generative tasks, e.g.,
synthesizing intricate object motions in text-to-video generation.
Directly extending DMD to multi-step distillation increases memory usage and computational depth, leading to instability and reduced efficiency. 
While prior works propose stochastic gradient truncation as a 

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