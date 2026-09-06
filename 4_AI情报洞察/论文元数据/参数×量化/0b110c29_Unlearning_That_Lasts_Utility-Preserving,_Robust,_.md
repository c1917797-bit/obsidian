---
type: literature-corpus-entry
citekey: singh2026unlearning
title: "Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting in LLMs"
authors:
  - "Naman Deep Singh"
  - "Maximilian Müller"
  - "Francesco Croce"
  - "Matthias Hein"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qZPIyCf5ke"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Unlearning in large language models (LLMs) involves precisely removing specific information from a pre-trained model. This is crucial to ensure safety of LLMs by deleting private data or harmful knowledge acquired during pre-training. However, existing unlearning methods often fall short when subjected to thorough evaluation. To overcome this, we introduce JensUn, where we leverage the Jensen-Shannon Divergence as the training objective for both forget and retain sets for more stable and effective unlearning dynamics compared to commonly used loss functions.
  In extensive experiments, JensUn
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
  - singh26
---

# Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting in LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `singh2026unlearning` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Naman Deep Singh, Maximilian Müller, Francesco Croce |

## 摘要

Unlearning in large language models (LLMs) involves precisely removing specific information from a pre-trained model. This is crucial to ensure safety of LLMs by deleting private data or harmful knowledge acquired during pre-training. However, existing unlearning methods often fall short when subjected to thorough evaluation. To overcome this, we introduce JensUn, where we leverage the Jensen-Shannon Divergence as the training objective for both forget and retain sets for more stable and effective unlearning dynamics compared to commonly used loss functions.  
In extensive experiments, JensUn 

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