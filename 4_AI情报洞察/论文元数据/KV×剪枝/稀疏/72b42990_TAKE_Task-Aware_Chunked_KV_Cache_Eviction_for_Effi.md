---
type: literature-corpus-entry
citekey: hu2026take
title: "TAKE: Task-Aware Chunked KV Cache Eviction for Efficient Long-Context LLM Prefill"
authors:
  - "Long Hu"
  - "Nan Jia"
  - "Rui Wang"
  - "Jiahui Li"
  - "Qingyi Yang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=kMLfUshPwo"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  The rapid development of large language models (LLMs) enhances various language generation applications, but it remains a serious memory usage challenge in long-context inference. Existing global pruning aims to reduce memory in the decoding process, ignoring the prefill peaks to delay the time-to-first-token. In this paper, we present Task-Aware Chunked KV Cache Eviction (TAKE), a training-free framework to optimize KV cache memory during the prefill stage of LLM inference.
  TAKE partitions long sequences into chunks and incrementally performs task-aware KV fusion and eviction, thereby avoidin
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
  - 剪枝/稀疏
  - hu26
---

# TAKE: Task-Aware Chunked KV Cache Eviction for Efficient Long-Context LLM Prefill

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hu2026take` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Long Hu, Nan Jia, Rui Wang |

## 摘要

The rapid development of large language models (LLMs) enhances various language generation applications, but it remains a serious memory usage challenge in long-context inference. Existing global pruning aims to reduce memory in the decoding process, ignoring the prefill peaks to delay the time-to-first-token. In this paper, we present Task-Aware Chunked KV Cache Eviction (TAKE), a training-free framework to optimize KV cache memory during the prefill stage of LLM inference.
TAKE partitions long sequences into chunks and incrementally performs task-aware KV fusion and eviction, thereby avoidin

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