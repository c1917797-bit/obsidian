---
type: literature-corpus-entry
citekey: zhou2026beyond
title: "Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization"
authors:
  - "Xianlei Zhou"
  - "Xiangdi Meng"
  - "Yu He"
  - "Tianyu Qi"
  - "Jian Zhang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=eUVOUBYKyr"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Policy optimization (PO) has advanced Large Language Models (LLMs), yet training remains constrained by a stability–exploration trade-off. We analyze the coupling between the input environment and the policy in LLM RL, and decouple parameter regularization from the optimization objective by moving regularization to the input side. Concretely, we propose **Environment-Regularized Policy Optimization (ERPO)**, instantiated with **Query-KL (QKL)**, which penalizes the KL divergence between the evolving query distribution and a fixed reference. By regularizing the input (query) distribution rather
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
  - zhou26
---

# Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhou2026beyond` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Xianlei Zhou, Xiangdi Meng, Yu He |

## 摘要

Policy optimization (PO) has advanced Large Language Models (LLMs), yet training remains constrained by a stability–exploration trade-off. We analyze the coupling between the input environment and the policy in LLM RL, and decouple parameter regularization from the optimization objective by moving regularization to the input side. Concretely, we propose **Environment-Regularized Policy Optimization (ERPO)**, instantiated with **Query-KL (QKL)**, which penalizes the KL divergence between the evolving query distribution and a fixed reference. By regularizing the input (query) distribution rather

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