---
type: literature-corpus-entry
citekey: kim2026happi
title: "HAPPI: Efficient KV cache compression with Hadamard PCA-based Power iteration"
authors:
  - "Seonggon Kim"
  - "Taehyeon Kim"
  - "Eunhyeok Park"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=BRDgQzdtWr"
pdf_url: ""
object: KV
method: 低秩
cell: "KV×低秩"
all_objects: []
all_methods: []
abstract: |
  Truncated Singular Value Decomposition (SVD) has recently attracted renewed attention for its effectiveness in model optimizations, such as LoRA initialization and KV-cache compression. However, exact SVD remains computationally expensive, while approximate methods like power iteration often introduce non-negligible errors. In this paper, we present Hadamard PCA-based Power Iteration (HaPPI), a new algorithm that significantly improves the accuracy of low-rank approximation while retaining efficiency. Compared to prior methods, HaPPI achieves the lowest approximation error at a practical compu
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
  - 低秩
  - kim26
---

# HAPPI: Efficient KV cache compression with Hadamard PCA-based Power iteration

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `kim2026happi` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×低秩 |
| **来源** | openreview |
| **作者** | Seonggon Kim, Taehyeon Kim, Eunhyeok Park |

## 摘要

Truncated Singular Value Decomposition (SVD) has recently attracted renewed attention for its effectiveness in model optimizations, such as LoRA initialization and KV-cache compression. However, exact SVD remains computationally expensive, while approximate methods like power iteration often introduce non-negligible errors. In this paper, we present Hadamard PCA-based Power Iteration (HaPPI), a new algorithm that significantly improves the accuracy of low-rank approximation while retaining efficiency. Compared to prior methods, HaPPI achieves the lowest approximation error at a practical compu

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