---
type: literature-corpus-entry
citekey: li2026real
title: "REAL: REtrieval-Augmented and Logic-constructed Attention Behaviors for Robust KV Cache Compression"
authors:
  - "Mengjie Li"
  - "William J. Song"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=XCqrMBh1Uj"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  The growing input sequence length of large language models (LLMs) places increasing pressure on key-value (KV) cache storage, making efficient inference challenging. Existing retrieval-based compression methods neglect the impact of distracted, biased, and widespread attention behaviors, raising robustness concerns. To address these challenges, this paper proposes REtrieval-Augmented and Logic-constructed (REAL) KV cache compression that implements a robust, low-cost, training-free method, capturing diverse attention behaviors. REAL introduces an attention weight confusion matrix (AWCM) to cat
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
  - KV
  - 量化
  - li26
---

# REAL: REtrieval-Augmented and Logic-constructed Attention Behaviors for Robust KV Cache Compression

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026real` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Mengjie Li, William J. Song |

## 摘要

The growing input sequence length of large language models (LLMs) places increasing pressure on key-value (KV) cache storage, making efficient inference challenging. Existing retrieval-based compression methods neglect the impact of distracted, biased, and widespread attention behaviors, raising robustness concerns. To address these challenges, this paper proposes REtrieval-Augmented and Logic-constructed (REAL) KV cache compression that implements a robust, low-cost, training-free method, capturing diverse attention behaviors. REAL introduces an attention weight confusion matrix (AWCM) to cat

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