---
type: literature-corpus-entry
citekey: gelo2026feedback
title: "Feedback-driven Behavioral Shaping for Safe Offline RL"
authors:
  - "Ebenezer Gelo"
  - "Geraud Nangue Tasse"
  - "Benjamin Rosman"
  - "Steven James"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=i7vS325TzM"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Learning safe policies in offline reinforcement learning (RL) requires access to a cost function, but dense annotations are rarely available. In practice, experts typically provide only sparse supervision by truncating trajectories at the first unsafe action, leaving a single terminal cost label. We frame this challenge as a credit assignment problem: the agent must determine which earlier actions contributed to the violation to learn safer behavior. To address this, we propose an approach that redistributes sparse stop-feedback into dense per-step costs using return decomposition, and then in
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
  - gelo26
---

# Feedback-driven Behavioral Shaping for Safe Offline RL

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `gelo2026feedback` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Ebenezer Gelo, Geraud Nangue Tasse, Benjamin Rosman |

## 摘要

Learning safe policies in offline reinforcement learning (RL) requires access to a cost function, but dense annotations are rarely available. In practice, experts typically provide only sparse supervision by truncating trajectories at the first unsafe action, leaving a single terminal cost label. We frame this challenge as a credit assignment problem: the agent must determine which earlier actions contributed to the violation to learn safer behavior. To address this, we propose an approach that redistributes sparse stop-feedback into dense per-step costs using return decomposition, and then in

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