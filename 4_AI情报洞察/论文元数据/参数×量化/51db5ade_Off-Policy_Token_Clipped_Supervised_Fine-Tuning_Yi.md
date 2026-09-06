---
type: literature-corpus-entry
citekey: liu2026off
title: "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start"
authors:
  - "Tian-Shuo Liu"
  - "Chengxing Jia"
  - "Haoyu Liu"
  - "Pengyuan Wang"
  - "Shiyuan Zhang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qJLKOryYeR"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Supervised Fine-Tuning (SFT) is a critical step for adapting Large Language Models (LLMs) to specialized domains, often serving as a cold-start for subsequent reinforcement learning (RL). However, SFT's tendency to memorize a small set of expert data for a downstream task can impair generalization and lead to catastrophic forgetting of prior knowledge, undermining the promise of effective RL. In this paper, we demonstrate that this degradation primarily results from tokens in the expert data to which the base model assigns low probability. Specifically, we frame these as 'off-policy' tokens, a
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
  - 量化
  - liu26
---

# Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026off` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Tian-Shuo Liu, Chengxing Jia, Haoyu Liu |

## 摘要

Supervised Fine-Tuning (SFT) is a critical step for adapting Large Language Models (LLMs) to specialized domains, often serving as a cold-start for subsequent reinforcement learning (RL). However, SFT's tendency to memorize a small set of expert data for a downstream task can impair generalization and lead to catastrophic forgetting of prior knowledge, undermining the promise of effective RL. In this paper, we demonstrate that this degradation primarily results from tokens in the expert data to which the base model assigns low probability. Specifically, we frame these as 'off-policy' tokens, a

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