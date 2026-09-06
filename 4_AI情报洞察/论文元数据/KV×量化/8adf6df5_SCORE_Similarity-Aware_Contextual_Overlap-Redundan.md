---
type: literature-corpus-entry
citekey: lee2026score
title: "SCORE: Similarity-Aware Contextual Overlap-Redundancy Eviction for Efficient KV Cache Compression in LLMs"
authors:
  - "Gilha lee"
  - "Seungil Lee"
  - "Hyun Kim"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=HTlkxdEDWo"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Recent advances in large language models (LLMs) have unlocked remarkable long-context capabilities, enabling breakthroughs across diverse NLP tasks. However, despite architectural progress and compression techniques such as quantization, the key-value (KV) cache remains a critical memory bottleneck during inference. Prior work has explored cache optimization via eviction strategies, yet most rely on heuristic or single-axis importance metrics, neglecting the nuanced and dynamic interplay between layers and attention heads. In this paper, we propose SCORE (Similarity-aware Contextual Overlap-Re
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
  - lee26
---

# SCORE: Similarity-Aware Contextual Overlap-Redundancy Eviction for Efficient KV Cache Compression in LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lee2026score` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Gilha lee, Seungil Lee, Hyun Kim |

## 摘要

Recent advances in large language models (LLMs) have unlocked remarkable long-context capabilities, enabling breakthroughs across diverse NLP tasks. However, despite architectural progress and compression techniques such as quantization, the key-value (KV) cache remains a critical memory bottleneck during inference. Prior work has explored cache optimization via eviction strategies, yet most rely on heuristic or single-axis importance metrics, neglecting the nuanced and dynamic interplay between layers and attention heads. In this paper, we propose SCORE (Similarity-aware Contextual Overlap-Re

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