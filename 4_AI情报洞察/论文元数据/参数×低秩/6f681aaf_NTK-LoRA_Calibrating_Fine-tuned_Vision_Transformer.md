---
type: literature-corpus-entry
citekey: leibl2026ntk
title: "NTK-LoRA: Calibrating Fine-tuned Vision Transformers using Gaussian Processes"
authors:
  - "Marek Leibl"
  - "Meelis Kull"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qBNrcneFy3"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Fine-tuning remains essential for adapting foundation models to domains where high precision is required, such as medical imaging or autonomous driving. However, this often leads to overconfident and poorly calibrated models, especially when fine-tuned on small datasets. We propose NTK-LoRA, a simple and effective post-hoc calibration method for fine-tuned Transformer models (e.g., Vision Transformers and LLMs) that leverages the Gaussian process view of neural networks to perform Laplace approximation of the posterior.
  Our method is almost as straightforward to implement as temperature scalin
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
  - leibl26
---

# NTK-LoRA: Calibrating Fine-tuned Vision Transformers using Gaussian Processes

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `leibl2026ntk` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Marek Leibl, Meelis Kull |

## 摘要

Fine-tuning remains essential for adapting foundation models to domains where high precision is required, such as medical imaging or autonomous driving. However, this often leads to overconfident and poorly calibrated models, especially when fine-tuned on small datasets. We propose NTK-LoRA, a simple and effective post-hoc calibration method for fine-tuned Transformer models (e.g., Vision Transformers and LLMs) that leverages the Gaussian process view of neural networks to perform Laplace approximation of the posterior.
Our method is almost as straightforward to implement as temperature scalin

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