---
type: literature-corpus-entry
citekey: he2026base
title: "BASE-Q: Bias and Asymmetric Scaling Enhanced Rotational Quantization for Large Language Models"
authors:
  - "Liulu He"
  - "Shenli Zheng"
  - "Kaiwei Sun"
  - "Yufei Zhao"
  - "Hengyu Fang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=hZEp4WvoX7"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Rotation-based methods have become essential for state-of-the-art LLM quantization by effectively mitigating outliers in weights and activations. Current approaches predominantly focus on optimizing the global rotation matrix to achieve marginal accuracy improvements—a strategy that incurs prohibitive computational costs through full-model backpropagation while offering limited practical utility.
  We fundamentally reassess this optimization paradigm and identify two critical error sources that persist even under optimal rotation conditions: (i) channel mean misalignment, which amplifies roundin
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
  - he26
---

# BASE-Q: Bias and Asymmetric Scaling Enhanced Rotational Quantization for Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `he2026base` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Liulu He, Shenli Zheng, Kaiwei Sun |

## 摘要

Rotation-based methods have become essential for state-of-the-art LLM quantization by effectively mitigating outliers in weights and activations. Current approaches predominantly focus on optimizing the global rotation matrix to achieve marginal accuracy improvements—a strategy that incurs prohibitive computational costs through full-model backpropagation while offering limited practical utility.
We fundamentally reassess this optimization paradigm and identify two critical error sources that persist even under optimal rotation conditions: (i) channel mean misalignment, which amplifies roundin

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