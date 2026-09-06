---
type: literature-corpus-entry
citekey: kim2026mitigating
title: "Mitigating the Echo Chamber Effect in KV Cache Compression via Coverage Optimization"
authors:
  - "Sehyung Kim"
  - "Minseo Yoon"
  - "Sung-Sik Cho"
  - "Sungwook Choi"
  - "Hyunwoo J. Kim"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=W6aYwEA7i3"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Large language models (LLMs) have achieved strong performance on complex tasks ranging from multi-document reasoning to long-dependency question answering. To enable efficient inference, these models rely on key-value (KV) caching, which stores and reuses KV pairs to avoid redundant computation. As the sequence length grows, the KV cache increases linearly, creating a severe GPU memory bottleneck. This issue is commonly addressed by compressing the KV cache using a top-k selection based on attention scores. However, this strategy induces a homogeneity bias, the tendency to repeatedly select si
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
  - kim26
---

# Mitigating the Echo Chamber Effect in KV Cache Compression via Coverage Optimization

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `kim2026mitigating` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Sehyung Kim, Minseo Yoon, Sung-Sik Cho |

## 摘要

Large language models (LLMs) have achieved strong performance on complex tasks ranging from multi-document reasoning to long-dependency question answering. To enable efficient inference, these models rely on key-value (KV) caching, which stores and reuses KV pairs to avoid redundant computation. As the sequence length grows, the KV cache increases linearly, creating a severe GPU memory bottleneck. This issue is commonly addressed by compressing the KV cache using a top-k selection based on attention scores. However, this strategy induces a homogeneity bias, the tendency to repeatedly select si

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