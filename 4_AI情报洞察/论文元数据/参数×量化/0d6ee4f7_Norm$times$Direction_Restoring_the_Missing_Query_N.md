---
type: literature-corpus-entry
citekey: meng2026norm
title: "Norm$\times$Direction: Restoring the Missing Query Norm in Vision Linear Attention"
authors:
  - "Weikang Meng"
  - "Yadan Luo"
  - "Liangyu Huo"
  - "Yingjian Li"
  - "Yaowei Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=aOjy0qREsu"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Linear attention mitigates the quadratic complexity of softmax attention but suffers from a critical loss of expressiveness. We identify two primary causes: (1) The normalization operation cancels the query norm, which breaks the correlation between a query's norm and the spikiness (entropy) of the attention distribution as in softmax attention. (2) Standard techniques for enforcing non-negativity cause destructive information loss by nullifying valid inner-product interactions. To address these challenges, we introduce **NaLaFormer**, a novel linear attention mechanism built upon a norm\$\tim
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
  - meng26
---

# Norm$\times$Direction: Restoring the Missing Query Norm in Vision Linear Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `meng2026norm` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Weikang Meng, Yadan Luo, Liangyu Huo |

## 摘要

Linear attention mitigates the quadratic complexity of softmax attention but suffers from a critical loss of expressiveness. We identify two primary causes: (1) The normalization operation cancels the query norm, which breaks the correlation between a query's norm and the spikiness (entropy) of the attention distribution as in softmax attention. (2) Standard techniques for enforcing non-negativity cause destructive information loss by nullifying valid inner-product interactions. To address these challenges, we introduce **NaLaFormer**, a novel linear attention mechanism built upon a norm\$\tim

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