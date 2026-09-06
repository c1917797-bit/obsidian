---
type: literature-corpus-entry
citekey: feng2026dag
title: "DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts"
authors:
  - "Jiarui Feng"
  - "Hanqing Zeng"
  - "Karish Grover"
  - "Ruizhong Qiu"
  - "Yinglong Xia"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=gdCdukkxKP"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Mixture-of-Experts (MoE) models have become a leading approach for decoupling parameter count from computational cost in large language models. Despite significant progress, effectively scaling MoE performance remains a challenge. Previous work shows that the use of fine-grained experts enlarges the space of expert combinations and can improve flexibility, but it also imposes substantial routing overhead, creating a new scalability bottleneck. In this paper, we explore a complementary axis for scaling --- expert-output mixture. We first analyze the limitations of the standard weighted-summatio
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
  - feng26
---

# DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `feng2026dag` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Jiarui Feng, Hanqing Zeng, Karish Grover |

## 摘要

Mixture-of-Experts (MoE) models have become a leading approach for decoupling parameter count from computational cost in large language models. Despite significant progress, effectively scaling MoE performance remains a challenge. Previous work shows that the use of fine-grained experts enlarges the space of expert combinations and can improve flexibility, but it also imposes substantial routing overhead, creating a new scalability bottleneck. In this paper, we explore a complementary axis for scaling --- expert-output mixture. We first analyze the limitations of the standard weighted-summatio

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