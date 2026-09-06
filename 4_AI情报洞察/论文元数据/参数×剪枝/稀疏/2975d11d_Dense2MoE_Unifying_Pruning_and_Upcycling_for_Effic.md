---
type: literature-corpus-entry
citekey: li2026dense
title: "Dense2MoE: Unifying Pruning and Upcycling for Efficient Large Language Models"
authors:
  - "Fengfa Li"
  - "Yifeng Ding"
  - "Lei Ren"
  - "Chen Wei"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=hYGPetyGSr"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  The Mixture of Experts (MoE) architecture has become a mainstream design in Large Language Models (LLMs) for its ability to flexibly scale parameters while maintaining inference efficiency. However, training MoE models from scratch remains prohibitively expensive due to their high computational demands. Existing upcycling methods reduce costs by converting dense LLMs into MoEs through layer duplication and fine-tuning, but introduce substantial redundancy. While layer pruning can reduce such redundancy, it often leads to notable performance degradation. We propose Dense2MoE, a novel approach t
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
  - li26
---

# Dense2MoE: Unifying Pruning and Upcycling for Efficient Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026dense` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Fengfa Li, Yifeng Ding, Lei Ren |

## 摘要

The Mixture of Experts (MoE) architecture has become a mainstream design in Large Language Models (LLMs) for its ability to flexibly scale parameters while maintaining inference efficiency. However, training MoE models from scratch remains prohibitively expensive due to their high computational demands. Existing upcycling methods reduce costs by converting dense LLMs into MoEs through layer duplication and fine-tuning, but introduce substantial redundancy. While layer pruning can reduce such redundancy, it often leads to notable performance degradation. We propose Dense2MoE, a novel approach t

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