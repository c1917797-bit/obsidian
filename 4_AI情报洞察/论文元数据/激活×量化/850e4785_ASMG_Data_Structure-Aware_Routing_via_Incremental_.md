---
type: literature-corpus-entry
citekey: park2026asmg
title: "ASMG: Data Structure-Aware Routing via Incremental Subspace Learning for MoE"
authors:
  - "Sumin Park"
  - "Noseong Park"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=xsqiDQjSvV"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Mixture-of-Experts (MoE) models scale model capacity efficiently by selectively
  routing inputs to a subset of specialized experts. However, their performance
  critically hinges on the gating mechanism, which is typically implemented as
  a shallow linear projection followed by a softmax or sigmoid activation. This
  minimal design lacks the representational capacity to capture structural variations
  in the input, often resulting in weak expert specialization and suboptimal routing.
  To address this limitation, we propose Adaptive Structure-Aware MoE Gating
  (ASMG), a data-driven gating mechanism that
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
  - 激活
  - 量化
  - park26
---

# ASMG: Data Structure-Aware Routing via Incremental Subspace Learning for MoE

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `park2026asmg` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Sumin Park, Noseong Park |

## 摘要

Mixture-of-Experts (MoE) models scale model capacity efficiently by selectively
routing inputs to a subset of specialized experts. However, their performance
critically hinges on the gating mechanism, which is typically implemented as
a shallow linear projection followed by a softmax or sigmoid activation. This
minimal design lacks the representational capacity to capture structural variations
in the input, often resulting in weak expert specialization and suboptimal routing.
To address this limitation, we propose Adaptive Structure-Aware MoE Gating
(ASMG), a data-driven gating mechanism that 

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