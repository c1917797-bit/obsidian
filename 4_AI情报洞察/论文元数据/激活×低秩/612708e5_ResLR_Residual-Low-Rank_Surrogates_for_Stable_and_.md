---
type: literature-corpus-entry
citekey: zhang2026reslr
title: "ResLR: Residual-Low-Rank Surrogates for Stable and Fast Context Adaptive Computing in Large Language Models"
authors:
  - "Linghe Zhang"
  - "Yuehao Li"
  - "Haifang Jian"
  - "Gaobin Huang"
  - "Hongchang Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=zB84FcNK2m"
pdf_url: ""
object: 激活
method: 低秩
cell: "激活×低秩"
all_objects: []
all_methods: []
abstract: |
  Large Language Models (LLMs) achieve state-of-the-art results on diverse tasks, yet inference remains expensive because every token traverses the full Transformer stack. Recent context adaptive computing methods mitigate this cost by token-wise layer skipping, but their per-layer routing is volatile, leading to accuracy oscillations and an extended fine-tuning process. We trace this instability to two issues: (i) direct skips violate the model’s functional hierarchy, and (ii) per-layer routing fails to exploit the similarity of activations between neighboring layers. We therefore propose a uni
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
  - 激活
  - 低秩
  - zhang26
---

# ResLR: Residual-Low-Rank Surrogates for Stable and Fast Context Adaptive Computing in Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026reslr` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×低秩 |
| **来源** | openreview |
| **作者** | Linghe Zhang, Yuehao Li, Haifang Jian |

## 摘要

Large Language Models (LLMs) achieve state-of-the-art results on diverse tasks, yet inference remains expensive because every token traverses the full Transformer stack. Recent context adaptive computing methods mitigate this cost by token-wise layer skipping, but their per-layer routing is volatile, leading to accuracy oscillations and an extended fine-tuning process. We trace this instability to two issues: (i) direct skips violate the model’s functional hierarchy, and (ii) per-layer routing fails to exploit the similarity of activations between neighboring layers. We therefore propose a uni

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