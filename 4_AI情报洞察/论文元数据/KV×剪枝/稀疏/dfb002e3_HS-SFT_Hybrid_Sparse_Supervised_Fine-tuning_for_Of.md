---
type: literature-corpus-entry
citekey: zhang2026hs
title: "HS-SFT: Hybrid Sparse Supervised Fine-tuning for Offline LLM KV Cache Eviction"
authors:
  - "Yuxin Zhang"
  - "Ruobing Xie"
  - "Wenhao Li"
  - "Jun Xia"
  - "Xiawu Zheng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=sZs6MS9yv0"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Long-context LLMs are constrained by the linear growth of key–value (KV) caches during autoregressive decoding, which incurs pronounced latency and memory overhead. KV eviction mitigates this issue, with existing efforts fall into offline policies with fixed eviction patterns and online policies that adaptively discard cache based on attention scores. While online eviction typically preserves accuracy under standard benchmarks, its performance can collapse in practical multi-turn dialogue scenarios where the query positions vary, and integration with pre-fill acceleration remains challenging.
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
  - zhang26
---

# HS-SFT: Hybrid Sparse Supervised Fine-tuning for Offline LLM KV Cache Eviction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026hs` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Yuxin Zhang, Ruobing Xie, Wenhao Li |

## 摘要

Long-context LLMs are constrained by the linear growth of key–value (KV) caches during autoregressive decoding, which incurs pronounced latency and memory overhead. KV eviction mitigates this issue, with existing efforts fall into offline policies with fixed eviction patterns and online policies that adaptively discard cache based on attention scores. While online eviction typically preserves accuracy under standard benchmarks, its performance can collapse in practical multi-turn dialogue scenarios where the query positions vary, and integration with pre-fill acceleration remains challenging. 

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