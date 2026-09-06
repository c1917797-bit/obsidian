---
type: literature-corpus-entry
citekey: li2026eat
title: "EAT: Expert Account Tracker for Efficient MoE Inference"
authors:
  - "Yuexian Li"
  - "Yifei Yang"
  - "zouying cao"
  - "hai zhao"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=GSLoB1myS8"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Mixture-of-Experts (MoE) models have emerged as a revolutionary method to scale Transformer models. However, traditional MoE architecture still suffers from inefficiency since a large number of experts are unnecessarily activated. Existing approaches for reducing the number of activated experts often overlook the historical performance of each expert. In this paper, we propose EAT, a novel method called $\textbf{Expert Account Tracker (EAT)}$, which utilizes history-awareness metrics and adaptive thresholding to dynamically select the most important experts, thereby reducing the activated expe
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
  - li26
---

# EAT: Expert Account Tracker for Efficient MoE Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026eat` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yuexian Li, Yifei Yang, zouying cao |

## 摘要

Mixture-of-Experts (MoE) models have emerged as a revolutionary method to scale Transformer models. However, traditional MoE architecture still suffers from inefficiency since a large number of experts are unnecessarily activated. Existing approaches for reducing the number of activated experts often overlook the historical performance of each expert. In this paper, we propose EAT, a novel method called $\textbf{Expert Account Tracker (EAT)}$, which utilizes history-awareness metrics and adaptive thresholding to dynamically select the most important experts, thereby reducing the activated expe

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