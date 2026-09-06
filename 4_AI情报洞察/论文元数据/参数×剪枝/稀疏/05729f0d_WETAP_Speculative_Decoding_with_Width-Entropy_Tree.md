---
type: literature-corpus-entry
citekey: zheng2026wetap
title: "WETAP: Speculative Decoding with Width-Entropy Tree and Adaptive Pruning for LLMs Inference Acceleration"
authors:
  - "LeiQuan Zheng"
  - "Yuan Liu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=Cae9he70Th"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  In inference acceleration of Large Language Models (LLMs), speculative decoding is used to coordinate draft model and target model, i.e., sequences are generated at the draft model and then verified in parallel at the target model, where the generation quality and speed of the draft model are the key issues. In this paper, we find that in a token tree, most of the child tokens are grew by few parent tokens with large probabilities in the low-entropy layer, and tokens with small probabilities in deeper layers also have potential to be accepted. Based on these observations, we propose WETAP, fir
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
  - 剪枝/稀疏
  - zheng26
---

# WETAP: Speculative Decoding with Width-Entropy Tree and Adaptive Pruning for LLMs Inference Acceleration

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zheng2026wetap` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | LeiQuan Zheng, Yuan Liu |

## 摘要

In inference acceleration of Large Language Models (LLMs), speculative decoding is used to coordinate draft model and target model, i.e., sequences are generated at the draft model and then verified in parallel at the target model, where the generation quality and speed of the draft model are the key issues. In this paper, we find that in a token tree, most of the child tokens are grew by few parent tokens with large probabilities in the low-entropy layer, and tokens with small probabilities in deeper layers also have potential to be accepted. Based on these observations, we propose WETAP, fir

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