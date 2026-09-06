---
type: literature-corpus-entry
citekey: hamidi2026exponential
title: "Exponential Low-Rank Adapters"
authors:
  - "Shayan Mohajer Hamidi"
  - "Mert Pilanci"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=JVyPNQCT8E"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Low rank adaptation (LoRA) is a standard parameter efficient fine tuning method, but its updates are rank limited and act as local additive perturbations of the weights.  We introduce exponential low rank adapters (ELRA), which replace LoRA’s additive update $\Delta W=AB$ with a multiplicative transformation $W_{\mathrm{new}}=\exp(\eta AB)\,W_0$, where $A\in\mathbb{R}^{d\times r}$ and $B\in\mathbb{R}^{r\times d}$ define a low rank generator and $W_0$ is the frozen pretrained weight. The matrix exponential lifts the generator to a full rank, invertible map that acts coherently on $W_0$. Geometr
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
  - hamidi26
---

# Exponential Low-Rank Adapters

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hamidi2026exponential` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Shayan Mohajer Hamidi, Mert Pilanci |

## 摘要

Low rank adaptation (LoRA) is a standard parameter efficient fine tuning method, but its updates are rank limited and act as local additive perturbations of the weights.  We introduce exponential low rank adapters (ELRA), which replace LoRA’s additive update $\Delta W=AB$ with a multiplicative transformation $W_{\mathrm{new}}=\exp(\eta AB)\,W_0$, where $A\in\mathbb{R}^{d\times r}$ and $B\in\mathbb{R}^{r\times d}$ define a low rank generator and $W_0$ is the frozen pretrained weight. The matrix exponential lifts the generator to a full rank, invertible map that acts coherently on $W_0$. Geometr

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