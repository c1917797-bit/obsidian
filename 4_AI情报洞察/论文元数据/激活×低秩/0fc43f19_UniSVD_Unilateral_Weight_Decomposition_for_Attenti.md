---
type: literature-corpus-entry
citekey: yu2026unisvd
title: "UniSVD: Unilateral Weight Decomposition for Attention-based Vision Models"
authors:
  - "Hyunwoo Yu"
  - "Yubin Cho"
  - "Kyeongbo Kong"
  - "Suk-Ju Kang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=MJsHf2oHzP"
pdf_url: ""
object: 激活
method: 低秩
cell: "激活×低秩"
all_objects: []
all_methods: []
abstract: |
  Transformers have achieved remarkable success across diverse domains, but their ever-growing scale results in prohibitive computational and memory costs. Low-rank matrix decomposition with Singular Value Decomposition (SVD) has emerged as an effective compression technique. Recent studies, such as ASVD, SVD-LLM, and FLAR-SVD, have improved decomposition quality by incorporating activation-aware method. However, these methods do not consider the unique mechanism of MHA, where query-key ($Q$-$K$) and value–output ($V$-$O$) computations are linear and allow pre-computation. To effectively leverag
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
  - 低秩
  - yu26
---

# UniSVD: Unilateral Weight Decomposition for Attention-based Vision Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yu2026unisvd` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×低秩 |
| **来源** | openreview |
| **作者** | Hyunwoo Yu, Yubin Cho, Kyeongbo Kong |

## 摘要

Transformers have achieved remarkable success across diverse domains, but their ever-growing scale results in prohibitive computational and memory costs. Low-rank matrix decomposition with Singular Value Decomposition (SVD) has emerged as an effective compression technique. Recent studies, such as ASVD, SVD-LLM, and FLAR-SVD, have improved decomposition quality by incorporating activation-aware method. However, these methods do not consider the unique mechanism of MHA, where query-key ($Q$-$K$) and value–output ($V$-$O$) computations are linear and allow pre-computation. To effectively leverag

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