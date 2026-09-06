---
type: literature-corpus-entry
citekey: chen2026s
title: "S-ATM: Self-Boosting Visual Reasoning via Adaptive Token Merging"
authors:
  - "Lingjun Chen"
  - "Xiangyan Liu"
  - "Jinghan Zhang"
  - "Fanqing Meng"
  - "Zijian Wu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=YpPMb1tC5N"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Vision-language models, often adapted from large language models, tend to show degraded reasoning capabilities when visual inputs are introduced. To address this issue, we propose S-ATM, a training-free decoding strategy that enhances visual reasoning without relying on external priors. For each input, two parallel pathways are constructed: one using the original image–text input and the other using a self-generated caption–text input. Their decoding distributions are adaptively merged at each step, with the merging weight guided by the model’s attention to visual tokens. A momentum-based smoo
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
  - chen26
---

# S-ATM: Self-Boosting Visual Reasoning via Adaptive Token Merging

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026s` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Lingjun Chen, Xiangyan Liu, Jinghan Zhang |

## 摘要

Vision-language models, often adapted from large language models, tend to show degraded reasoning capabilities when visual inputs are introduced. To address this issue, we propose S-ATM, a training-free decoding strategy that enhances visual reasoning without relying on external priors. For each input, two parallel pathways are constructed: one using the original image–text input and the other using a self-generated caption–text input. Their decoding distributions are adaptively merged at each step, with the merging weight guided by the model’s attention to visual tokens. A momentum-based smoo

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