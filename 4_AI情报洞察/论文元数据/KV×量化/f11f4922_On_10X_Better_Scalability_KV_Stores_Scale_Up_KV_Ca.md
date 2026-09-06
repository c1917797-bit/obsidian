---
type: literature-corpus-entry
citekey: yu2026on
title: "On 10X Better Scalability: KV Stores Scale Up KV Cache"
authors:
  - "Weiping Yu"
  - "Ye Jiarui"
  - "He Mengke"
  - "Junfeng Liu"
  - "Siqiang Luo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=QqpbjtPbIc"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Large language models (LLMs) rely on Key-Value (KV) cache to reduce time-
  to-first-token (TTFT) latency, but existing disk-based KV cache systems using
  file-per-object layouts suffer from severe scalability bottlenecks due to file system
  metadata overhead, I/O inefficiency, and poor spatial locality. This paper presents
  SGLANG-LSM, a database-inspired system that leverages Log-Structured Merge-
  tree (LSM-tree) architectures for scalable KV cache management. SGLANG-LSM
  implements a layered system design with three coordinated components: (1) a
  prefix-preserving storage engine that maintains tok
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
  - yu26
---

# On 10X Better Scalability: KV Stores Scale Up KV Cache

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yu2026on` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Weiping Yu, Ye Jiarui, He Mengke |

## 摘要

Large language models (LLMs) rely on Key-Value (KV) cache to reduce time-
to-first-token (TTFT) latency, but existing disk-based KV cache systems using
file-per-object layouts suffer from severe scalability bottlenecks due to file system
metadata overhead, I/O inefficiency, and poor spatial locality. This paper presents
SGLANG-LSM, a database-inspired system that leverages Log-Structured Merge-
tree (LSM-tree) architectures for scalable KV cache management. SGLANG-LSM
implements a layered system design with three coordinated components: (1) a
prefix-preserving storage engine that maintains tok

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