---
type: literature-corpus-entry
citekey: bessonnitsyn2026ssonn
title: "SSONN: Self-Scaled Optimized Neural Network"
authors:
  - "Evgeny Bessonnitsyn"
  - "Mironov Ivan"
  - "Fedor Kutergin"
  - "Danil Fedorov"
  - "Aleksandr Ustinov"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=tal1W7XOoJ"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Current approaches to lightweight neural network design face a fundamental trade-off: reducing model size inevitably compromises accuracy.
  Distillation and pruning are the most commonly used methods, they require an initially over-parameterized pretrained architecture that increases computational costs while training.
  This work introduces a novel Self-Scaled Optimized Neural Network (SSONN) method that eliminates the need for redundant initial models.
  Instead of following a \textit{train-then-compress} paradigm, SSONN starts with a single linear layer and dynamically increases its com
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
  - bessonnitsyn26
---

# SSONN: Self-Scaled Optimized Neural Network

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `bessonnitsyn2026ssonn` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Evgeny Bessonnitsyn, Mironov Ivan, Fedor Kutergin |

## 摘要

Current approaches to lightweight neural network design face a fundamental trade-off: reducing model size inevitably compromises accuracy. 
  Distillation and pruning are the most commonly used methods, they require an initially over-parameterized pretrained architecture that increases computational costs while training. 
  This work introduces a novel Self-Scaled Optimized Neural Network (SSONN) method that eliminates the need for redundant initial models. 
  Instead of following a \textit{train-then-compress} paradigm, SSONN starts with a single linear layer and dynamically increases its com

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