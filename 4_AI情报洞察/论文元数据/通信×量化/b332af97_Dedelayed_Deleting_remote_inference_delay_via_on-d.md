---
type: literature-corpus-entry
citekey: jacobellis2026dedelayed
title: "Dedelayed: Deleting remote inference delay via on-device correction"
authors:
  - "Dan Jacobellis"
  - "Mateen Ulhaq"
  - "Fabien Racapé"
  - "Hyomin Choi"
  - "Neeraja J. Yadwadkar"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=IYrdD0lEkj"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  Remote inference allows lightweight devices to leverage powerful cloud models. However, communication network latency makes predictions stale and unsuitable for real-time tasks. To address this, we introduce Dedelayed, a delay-corrective method that mitigates arbitrary remote inference delays, allowing the local device to produce low-latency outputs in real time. Our method employs a lightweight local model that processes the current frame and fuses in features that a heavyweight remote model computes from past frames. On video from the BDD100K driving dataset, Dedelayed improves semantic segm
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
  - 通信
  - 量化
  - jacobellis26
---

# Dedelayed: Deleting remote inference delay via on-device correction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `jacobellis2026dedelayed` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Dan Jacobellis, Mateen Ulhaq, Fabien Racapé |

## 摘要

Remote inference allows lightweight devices to leverage powerful cloud models. However, communication network latency makes predictions stale and unsuitable for real-time tasks. To address this, we introduce Dedelayed, a delay-corrective method that mitigates arbitrary remote inference delays, allowing the local device to produce low-latency outputs in real time. Our method employs a lightweight local model that processes the current frame and fuses in features that a heavyweight remote model computes from past frames. On video from the BDD100K driving dataset, Dedelayed improves semantic segm

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