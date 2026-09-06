---
type: literature-corpus-entry
citekey: wang2026gaugekv
title: "GaugeKV: Composable Exact KV Cache Compression"
authors:
  - "Hong Wang"
  - "Kelly Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=rSxYPLzyBu"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  The key–value (KV) cache is a dominant memory cost in long-context Transformer inference. We introduce GaugeKV, a training-free method that leverages the head-wise gauge symmetry of attention to reduce KV memory both exactly and with certificates. A one-time gauge canonicalization rewrites weights so that values are orthonormal and queries/keys are scale-balanced; thereafter the model produces K/V in a compression-friendly basis without changing its function or runtime FLOPs. Combined with lossless hot/cold staging, this yields bit-identical outputs (FP32 deterministic) with measurable KV redu
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
  - wang26
---

# GaugeKV: Composable Exact KV Cache Compression

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026gaugekv` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Hong Wang, Kelly Wang |

## 摘要

The key–value (KV) cache is a dominant memory cost in long-context Transformer inference. We introduce GaugeKV, a training-free method that leverages the head-wise gauge symmetry of attention to reduce KV memory both exactly and with certificates. A one-time gauge canonicalization rewrites weights so that values are orthonormal and queries/keys are scale-balanced; thereafter the model produces K/V in a compression-friendly basis without changing its function or runtime FLOPs. Combined with lossless hot/cold staging, this yields bit-identical outputs (FP32 deterministic) with measurable KV redu

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