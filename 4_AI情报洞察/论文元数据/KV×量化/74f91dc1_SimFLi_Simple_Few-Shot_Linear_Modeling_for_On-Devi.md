---
type: literature-corpus-entry
citekey: song2026simfli
title: "SimFLi: Simple Few-Shot Linear Modeling for On-Device LLM Latency Profiling"
authors:
  - "WooYoung Song"
  - "Juyoung Lee"
  - "Taesik Gong"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=iWfIzLcSif"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  On-device inference of large language models (LLMs) is increasingly central to
  mobile and edge AI, yet profiling their latency remains challenging: existing
  methods are often server-centric, rely on operator-level instrumentation, or in-
  cur overheads that make them impractical for constrained devices. We present
  Simple Few-Shot Lining (SimFLi), a lightweight and training-free profiler that
  decomposes inference into prefill (time-to-first-token) and decode phases, and
  estimates latency from only a few token-length probes. Despite its simplicity,
  SimFLi achieves accurate latency surfaces withou
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
  - song26
---

# SimFLi: Simple Few-Shot Linear Modeling for On-Device LLM Latency Profiling

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `song2026simfli` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | WooYoung Song, Juyoung Lee, Taesik Gong |

## 摘要

On-device inference of large language models (LLMs) is increasingly central to
mobile and edge AI, yet profiling their latency remains challenging: existing
methods are often server-centric, rely on operator-level instrumentation, or in-
cur overheads that make them impractical for constrained devices. We present
Simple Few-Shot Lining (SimFLi), a lightweight and training-free profiler that
decomposes inference into prefill (time-to-first-token) and decode phases, and
estimates latency from only a few token-length probes. Despite its simplicity,
SimFLi achieves accurate latency surfaces withou

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