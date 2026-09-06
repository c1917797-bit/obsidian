---
type: literature-corpus-entry
citekey: noci2026thinking
title: "Thinking into the Future: Latent Lookahead Training for Language Models"
authors:
  - "Lorenzo Noci"
  - "Gregor Bachmann"
  - "Seyed-Mohsen Moosavi-Dezfooli"
  - "Moin Nabi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=QpRZY8rLxk"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Autoregressive language models trained with next-token prediction generate text by sampling one discrete token at a time. This forces the model to commit early, preventing exploration of multiple plausible continuations. Furthermore, each token is predicted in a single forward pass, which might limit the model’s expressiveness in cases where difficult tokens require inherently more compute. Towards this end, we introduce latent lookahead, a training strategy that enables models to think before answering: at selected positions in the sequence, before committing to the next token, the model perf
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
  - 低秩
  - noci26
---

# Thinking into the Future: Latent Lookahead Training for Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `noci2026thinking` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Lorenzo Noci, Gregor Bachmann, Seyed-Mohsen Moosavi-Dezfooli |

## 摘要

Autoregressive language models trained with next-token prediction generate text by sampling one discrete token at a time. This forces the model to commit early, preventing exploration of multiple plausible continuations. Furthermore, each token is predicted in a single forward pass, which might limit the model’s expressiveness in cases where difficult tokens require inherently more compute. Towards this end, we introduce latent lookahead, a training strategy that enables models to think before answering: at selected positions in the sequence, before committing to the next token, the model perf

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