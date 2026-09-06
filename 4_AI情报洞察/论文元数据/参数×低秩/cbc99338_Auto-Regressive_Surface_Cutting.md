---
type: literature-corpus-entry
citekey: li2026auto
title: "Auto-Regressive Surface Cutting"
authors:
  - "YANG LI"
  - "Victor Cheung"
  - "Xinhai Liu"
  - "Yuguang Chen"
  - "Zhongjin Luo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=9HeKCYl1zl"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Surface cutting is a fundamental task in computer graphics, with applications in UV parameterization, texture mapping, and mesh decomposition. However, existing methods often produce technically valid but overly fragmented atlases that lack semantic coherence. We introduce SeamGPT, an auto-regressive model that generates cutting seams by mimicking professional workflows. Our key technical innovation lies in formulating surface cutting as a next token prediction task: sample point clouds on mesh vertices and edges, encode them as shape conditions, and employ a GPT-style transformer to sequentia
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
  - li26
---

# Auto-Regressive Surface Cutting

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026auto` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | YANG LI, Victor Cheung, Xinhai Liu |

## 摘要

Surface cutting is a fundamental task in computer graphics, with applications in UV parameterization, texture mapping, and mesh decomposition. However, existing methods often produce technically valid but overly fragmented atlases that lack semantic coherence. We introduce SeamGPT, an auto-regressive model that generates cutting seams by mimicking professional workflows. Our key technical innovation lies in formulating surface cutting as a next token prediction task: sample point clouds on mesh vertices and edges, encode them as shape conditions, and employ a GPT-style transformer to sequentia

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