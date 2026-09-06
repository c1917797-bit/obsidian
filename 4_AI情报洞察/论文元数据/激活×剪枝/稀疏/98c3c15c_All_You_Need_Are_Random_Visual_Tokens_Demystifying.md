---
type: literature-corpus-entry
citekey: wang2026all
title: "All You Need Are Random Visual Tokens?  Demystifying Token Pruning in VLLMs"
authors:
  - "Yahong Wang"
  - "Juncheng Wu"
  - "Zhangkai Ni"
  - "Longzhen Yang"
  - "Yihang Liu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=KcIDfNX9ew"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Vision Large Language Models (VLLMs) usually incur high computational costs due to their reliance on hundreds of visual tokens to represent images. While token pruning offers a promising solution for accelerating inference, this paper, however, identifies a key observation: in deeper layers (_e.g._, beyond the 20th), existing training-free pruning methods _perform no better than random pruning_. We hypothesize that this degradation is caused by **"vanishing token information''**, where visual tokens progressively lose their salience with increasing network depth.
  To validate this hypothesis,
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
  - 剪枝/稀疏
  - wang26
---

# All You Need Are Random Visual Tokens?  Demystifying Token Pruning in VLLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026all` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Yahong Wang, Juncheng Wu, Zhangkai Ni |

## 摘要

Vision Large Language Models (VLLMs) usually incur high computational costs due to their reliance on hundreds of visual tokens to represent images. While token pruning offers a promising solution for accelerating inference, this paper, however, identifies a key observation: in deeper layers (_e.g._, beyond the 20th), existing training-free pruning methods _perform no better than random pruning_. We hypothesize that this degradation is caused by **"vanishing token information''**, where visual tokens progressively lose their salience with increasing network depth. 
To validate this hypothesis, 

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