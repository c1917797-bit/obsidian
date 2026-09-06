---
type: literature-corpus-entry
citekey: shi2026dynamic
title: "Dynamic Mask Attention: End-to-End Trainable Content-aware Sparse Attention"
authors:
  - "Jingze Shi"
  - "Yifan Wu"
  - "Yiran Peng"
  - "Bingheng Wu"
  - "Liangdong Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=vrBZs2UL5n"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Self-attention's computational cost, which scales quadratically with sequence length, creates a fundamental bottleneck for long-context modeling in LLMs, limiting applications such as document understanding, multi-turn reasoning, and code generation. Sparse attention has been proposed to mitigate this issue. Early content-agnostic designs such as sliding-window and block-sparse attention reduce computational complexity based on fixed patterns. However, theirstatic structure often overlook important long-range dependencies and lack adaptivity to diverse query contexts. Recent content-aware meth
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
  - 参数
  - 剪枝/稀疏
  - shi26
---

# Dynamic Mask Attention: End-to-End Trainable Content-aware Sparse Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `shi2026dynamic` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Jingze Shi, Yifan Wu, Yiran Peng |

## 摘要

Self-attention's computational cost, which scales quadratically with sequence length, creates a fundamental bottleneck for long-context modeling in LLMs, limiting applications such as document understanding, multi-turn reasoning, and code generation. Sparse attention has been proposed to mitigate this issue. Early content-agnostic designs such as sliding-window and block-sparse attention reduce computational complexity based on fixed patterns. However, theirstatic structure often overlook important long-range dependencies and lack adaptivity to diverse query contexts. Recent content-aware meth

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