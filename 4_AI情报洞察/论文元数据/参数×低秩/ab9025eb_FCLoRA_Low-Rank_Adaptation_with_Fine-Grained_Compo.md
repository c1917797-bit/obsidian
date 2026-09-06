---
type: literature-corpus-entry
citekey: wi2026fclora
title: "FCLoRA: Low-Rank Adaptation with Fine-Grained Component Injection"
authors:
  - "Hyowon Wi"
  - "Noseong Park"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Y4g1XjT0qd"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  In recent years, low-rank adaptation (LoRA) has emerged as a significant paradigm, which freezes the pre-trained weights and introduces small, learnable adapters instead of fine-tuning the full set of parameters. In this work, we uncover several key insights regarding to the $\textit{singular}$ components of the network parameters based on Singular Value Decomposition (SVD). Firstly, the dominant singular components with large singular values in pre-trained network parameters can be effectively reused during fine-tuning, whereas the fine-grained components with smaller singular values are more
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
  - wi26
---

# FCLoRA: Low-Rank Adaptation with Fine-Grained Component Injection

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wi2026fclora` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Hyowon Wi, Noseong Park |

## 摘要

In recent years, low-rank adaptation (LoRA) has emerged as a significant paradigm, which freezes the pre-trained weights and introduces small, learnable adapters instead of fine-tuning the full set of parameters. In this work, we uncover several key insights regarding to the $\textit{singular}$ components of the network parameters based on Singular Value Decomposition (SVD). Firstly, the dominant singular components with large singular values in pre-trained network parameters can be effectively reused during fine-tuning, whereas the fine-grained components with smaller singular values are more

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