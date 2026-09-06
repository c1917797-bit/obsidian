---
type: literature-corpus-entry
citekey: xu2026bridging
title: "Bridging Non-Intrusive Tracing and Fine-Grained Cross-Layer Representations for LLM Inference Diagnosis"
authors:
  - "Ruilin Xu"
  - "Junyi Li"
  - "Zongxuan Xie"
  - "Pengfei chen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=S9iB7BA3Zq"
pdf_url: ""
object: 通信
method: 量化
cell: "通信×量化"
all_objects: []
all_methods: []
abstract: |
  LLM inference spans the inference engine, compute backend, host operators, and GPU kernels, where asynchrony and concurrency make request-level end-to-end observability and diagnosis challenging. We present $\textbf{Truffld}$, a non-intrusive and cross-layer framework that provides fine-grained representations for diagnosis in large-scale LLM inference. For data collection, $\textbf{Truffld}$ activates NVTX markers and CUPTI callbacks to capture raw events from vertical (intra-node stack execution) and horizontal (cross-node communication) perspectives. We then propose a call-chain merging alg
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
  - xu26
---

# Bridging Non-Intrusive Tracing and Fine-Grained Cross-Layer Representations for LLM Inference Diagnosis

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `xu2026bridging` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 通信×量化 |
| **来源** | openreview |
| **作者** | Ruilin Xu, Junyi Li, Zongxuan Xie |

## 摘要

LLM inference spans the inference engine, compute backend, host operators, and GPU kernels, where asynchrony and concurrency make request-level end-to-end observability and diagnosis challenging. We present $\textbf{Truffld}$, a non-intrusive and cross-layer framework that provides fine-grained representations for diagnosis in large-scale LLM inference. For data collection, $\textbf{Truffld}$ activates NVTX markers and CUPTI callbacks to capture raw events from vertical (intra-node stack execution) and horizontal (cross-node communication) perspectives. We then propose a call-chain merging alg

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