---
type: literature-corpus-entry
citekey: he2026trianglemix
title: "TriangleMix: Accelerating Prefilling via Decoding-time Contribution Sparsity"
authors:
  - "Zhiyuan He"
  - "Yike Zhang"
  - "Chengruidong Zhang"
  - "Huiqiang Jiang"
  - "Yuqing Yang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=batLZG0bDw"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Large Language Models (LLMs) incur quadratic attention complexity with input length, creating a major time bottleneck in the prefilling stage. Existing acceleration methods largely exploit attention score sparsity by estimating blocks with high attention scores and applying dynamic sparse attention. In this work, we identify another untapped form of sparsity in the prefilling stage, namely decoding-time contribution sparsity, where many attention blocks exhibit nontrivial attention scores during prefilling yet contribute negligibly to subsequent decoding, as indicated by gradient-based analysi
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
  - he26
---

# TriangleMix: Accelerating Prefilling via Decoding-time Contribution Sparsity

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `he2026trianglemix` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Zhiyuan He, Yike Zhang, Chengruidong Zhang |

## 摘要

Large Language Models (LLMs) incur quadratic attention complexity with input length, creating a major time bottleneck in the prefilling stage. Existing acceleration methods largely exploit attention score sparsity by estimating blocks with high attention scores and applying dynamic sparse attention. In this work, we identify another untapped form of sparsity in the prefilling stage, namely decoding-time contribution sparsity, where many attention blocks exhibit nontrivial attention scores during prefilling yet contribute negligibly to subsequent decoding, as indicated by gradient-based analysi

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