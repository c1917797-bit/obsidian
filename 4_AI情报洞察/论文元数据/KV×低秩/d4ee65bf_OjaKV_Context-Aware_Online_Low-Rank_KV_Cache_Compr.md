---
type: literature-corpus-entry
citekey: zhu2026ojakv
title: "OjaKV: Context-Aware Online Low-Rank KV Cache Compression with Oja’s Rule"
authors:
  - "Yuxuan Zhu"
  - "David H. Yang"
  - "Mohammad Mohammadi Amiri"
  - "Keerthiram Murugesan"
  - "Tejaswini Pedapati"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=XVjgvJhLTY"
pdf_url: ""
object: KV
method: 低秩
cell: "KV×低秩"
all_objects: []
all_methods: []
abstract: |
  The expanding long-context capabilities of large language models are constrained by a significant memory bottleneck: the key-value (KV) cache required for autoregressive generation. This bottleneck is substantial; for instance, a Llama-3.1-8B model processing a 32K-token prompt at a batch size of 4 requires approximately 16GB for its KV cache, a size exceeding the model's weights. While KV-cache compression via low-rank projection is a promising direction, existing methods' rely on a static, offline-learned subspace that performs poorly under data distribution shifts. To overcome these limitat
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
  - zhu26
---

# OjaKV: Context-Aware Online Low-Rank KV Cache Compression with Oja’s Rule

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhu2026ojakv` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×低秩 |
| **来源** | openreview |
| **作者** | Yuxuan Zhu, David H. Yang, Mohammad Mohammadi Amiri |

## 摘要

The expanding long-context capabilities of large language models are constrained by a significant memory bottleneck: the key-value (KV) cache required for autoregressive generation. This bottleneck is substantial; for instance, a Llama-3.1-8B model processing a 32K-token prompt at a batch size of 4 requires approximately 16GB for its KV cache, a size exceeding the model's weights. While KV-cache compression via low-rank projection is a promising direction, existing methods' rely on a static, offline-learned subspace that performs poorly under data distribution shifts. To overcome these limitat

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