---
type: literature-corpus-entry
citekey: cao2026orthonormal
title: "Orthonormal Regularization in Low-Rank Adaptation"
authors:
  - "Yang Cao"
  - "Zhao Song"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qE5RqmebGG"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Performance degradation on tasks outside the fine-tuning domain is often observed while performing parameter-efficient fine-tuning (PEFT) on neural networks with limited data. For example, fine-tuning on mathematical datasets may impair the large language model’s coding ability. We analyze this issue and identify the condition number of weight matrices as a key factor contributing to such degradation. To address this, we propose Singular Values and Orthonormal Regularized Singular Vectors Adaptation, or SORSA,
  a novel PEFT method that explicitly improves the conditioning of the adapted model p
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
  - cao26
---

# Orthonormal Regularization in Low-Rank Adaptation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `cao2026orthonormal` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Yang Cao, Zhao Song |

## 摘要

Performance degradation on tasks outside the fine-tuning domain is often observed while performing parameter-efficient fine-tuning (PEFT) on neural networks with limited data. For example, fine-tuning on mathematical datasets may impair the large language model’s coding ability. We analyze this issue and identify the condition number of weight matrices as a key factor contributing to such degradation. To address this, we propose Singular Values and Orthonormal Regularized Singular Vectors Adaptation, or SORSA,
a novel PEFT method that explicitly improves the conditioning of the adapted model p

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