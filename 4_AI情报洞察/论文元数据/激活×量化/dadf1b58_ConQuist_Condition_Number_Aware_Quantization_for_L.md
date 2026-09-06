---
type: literature-corpus-entry
citekey: mishra2026conquist
title: "ConQuist: Condition Number Aware Quantization for LLMs"
authors:
  - "Ritik Mishra"
  - "M. Tanveer"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=EJSzggDNU5"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Post-training quantization (PTQ) of large language models (LLMs) has emerged as a promising technique in reducing the computational cost at inference time. Uniformly quantizing all weights and activations to 4-bit significantly degrades performance, due to the high quantization error caused by outliers present in activations. To mitigate this issue, we propose ConQuist, a PTQ method leveraging mixed precision quantization based on the condition number of each layer. The condition number quantifies the sensitivity of a layer’s output to small perturbations in its activations; hence, layers exhi
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
  - 量化
  - mishra26
---

# ConQuist: Condition Number Aware Quantization for LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `mishra2026conquist` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Ritik Mishra, M. Tanveer |

## 摘要

Post-training quantization (PTQ) of large language models (LLMs) has emerged as a promising technique in reducing the computational cost at inference time. Uniformly quantizing all weights and activations to 4-bit significantly degrades performance, due to the high quantization error caused by outliers present in activations. To mitigate this issue, we propose ConQuist, a PTQ method leveraging mixed precision quantization based on the condition number of each layer. The condition number quantifies the sensitivity of a layer’s output to small perturbations in its activations; hence, layers exhi

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