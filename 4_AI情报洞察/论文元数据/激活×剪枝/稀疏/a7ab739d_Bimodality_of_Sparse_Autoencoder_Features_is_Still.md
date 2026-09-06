---
type: literature-corpus-entry
citekey: brzozowski2026bimodality
title: "Bimodality of Sparse Autoencoder Features is Still There and Can Be Fixed"
authors:
  - "Michał Brzozowski"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=soMC0uESuz"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Sparse autoencoders (SAE) are a widely used method for decomposing LLM activations into a dictionary of interpretable features. We observe that this dictionary often exhibits a bimodal distribution, which can be leveraged to categorize features into two groups: those that are monosemantic and those that are artifacts of SAE training. The cluster of noninterpretable or polysemantic features undermines the purpose of sparse autoencoders and represents a waste of potential, akin to dead features. This phenomenon is prevalent across autoencoders utilizing both ReLU and alternative activation funct
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
  - 剪枝/稀疏
  - brzozowski26
---

# Bimodality of Sparse Autoencoder Features is Still There and Can Be Fixed

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `brzozowski2026bimodality` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Michał Brzozowski |

## 摘要

Sparse autoencoders (SAE) are a widely used method for decomposing LLM activations into a dictionary of interpretable features. We observe that this dictionary often exhibits a bimodal distribution, which can be leveraged to categorize features into two groups: those that are monosemantic and those that are artifacts of SAE training. The cluster of noninterpretable or polysemantic features undermines the purpose of sparse autoencoders and represents a waste of potential, akin to dead features. This phenomenon is prevalent across autoencoders utilizing both ReLU and alternative activation funct

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