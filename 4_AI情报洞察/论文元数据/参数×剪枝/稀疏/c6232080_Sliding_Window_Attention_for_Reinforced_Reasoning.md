---
type: literature-corpus-entry
citekey: liu2026sliding
title: "Sliding Window Attention for Reinforced Reasoning"
authors:
  - "Kai Liu"
  - "Peijie Dong"
  - "XIE Xinchen"
  - "Jianfei Gao"
  - "Xiaowen Chu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=lHw9TvC3bq"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Large reasoning models such as DeepSeek-R1 employ reinforcement learning (RL) to incentivize the reasoning capability. As the context length growth, the quadratic complexity of self-attention (SA) prohibits scaling to longer contexts. Recently, hybrid, sparse and linear attention methods aim to reduce the cost of SA, yet suffer from costly retraining, high complexity or linear memory growth. To address it, we revisit sliding-window attention (SWA). It not only offers linear-time complexity and constant memory, enabling faster RL rollouts, but also facilitates cheap conversion from pretrained t
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
  - liu26
---

# Sliding Window Attention for Reinforced Reasoning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026sliding` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Kai Liu, Peijie Dong, XIE Xinchen |

## 摘要

Large reasoning models such as DeepSeek-R1 employ reinforcement learning (RL) to incentivize the reasoning capability. As the context length growth, the quadratic complexity of self-attention (SA) prohibits scaling to longer contexts. Recently, hybrid, sparse and linear attention methods aim to reduce the cost of SA, yet suffer from costly retraining, high complexity or linear memory growth. To address it, we revisit sliding-window attention (SWA). It not only offers linear-time complexity and constant memory, enabling faster RL rollouts, but also facilitates cheap conversion from pretrained t

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