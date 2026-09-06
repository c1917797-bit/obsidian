---
type: literature-corpus-entry
citekey: chen2026autoregression
title: "Autoregression with Self-Token Prediction"
authors:
  - "Dengsheng Chen"
  - "Yangming Shi"
  - "Jian Wang"
  - "Enhua Wu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=FpGuLa3S9S"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  \begin{abstract}
  Next-token prediction has been highly effective in language, but its extension to continuous modalities is challenging: regression over correlated latents tends to collapse into near-identity mappings, while discretization via vector-quantized encoders introduces quantization artifacts. Mask-based prediction with diffusion heads mitigates these issues, yet suffers from a train–inference mismatch, inability to use key–value caching, and poor scalability to long sequences. To overcome these limitations, we propose \emph{self-token prediction}, which conditions each token on grou
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
  - 量化
  - chen26
---

# Autoregression with Self-Token Prediction

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026autoregression` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Dengsheng Chen, Yangming Shi, Jian Wang |

## 摘要

\begin{abstract}
Next-token prediction has been highly effective in language, but its extension to continuous modalities is challenging: regression over correlated latents tends to collapse into near-identity mappings, while discretization via vector-quantized encoders introduces quantization artifacts. Mask-based prediction with diffusion heads mitigates these issues, yet suffers from a train–inference mismatch, inability to use key–value caching, and poor scalability to long sequences. To overcome these limitations, we propose \emph{self-token prediction}, which conditions each token on grou

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