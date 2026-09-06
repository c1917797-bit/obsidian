---
type: literature-corpus-entry
citekey: hsu2026tucker
title: "Tucker-KV: Provable Tucker Compression of KV Caches with Monotone Refinement and Near-Optimal Budgeting"
authors:
  - "Hung-Min Hsu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=aQ6RiOijal"
pdf_url: ""
object: KV
method: 低秩
cell: "KV×低秩"
all_objects: []
all_methods: []
abstract: |
  Key-Value (KV) caches enable fast Transformer decoding but their memory and compute scale linearly with context length. Prior KV compression works are largely matrix low-rank heuristics, leaving multilinear guarantees underexplored. We present Tucker-KV, a Tucker-based framework with provable properties for compressing KV tensors over (L, S, H). Our analysis establishes: (i) HOSVD-style error upper bounds and monotone refinement via HOOI; (ii) grouped-head separability enabling parallelizable compression; (iii) a (1-1/e) guarantee for greedy budget allocation under mild DR-submodularity; and (
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
  - 低秩
  - hsu26
---

# Tucker-KV: Provable Tucker Compression of KV Caches with Monotone Refinement and Near-Optimal Budgeting

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hsu2026tucker` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×低秩 |
| **来源** | openreview |
| **作者** | Hung-Min Hsu |

## 摘要

Key-Value (KV) caches enable fast Transformer decoding but their memory and compute scale linearly with context length. Prior KV compression works are largely matrix low-rank heuristics, leaving multilinear guarantees underexplored. We present Tucker-KV, a Tucker-based framework with provable properties for compressing KV tensors over (L, S, H). Our analysis establishes: (i) HOSVD-style error upper bounds and monotone refinement via HOOI; (ii) grouped-head separability enabling parallelizable compression; (iii) a (1-1/e) guarantee for greedy budget allocation under mild DR-submodularity; and (

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