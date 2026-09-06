---
type: literature-corpus-entry
citekey: nie2026aladdin
title: "Aladdin: Joint Placement and Scaling for SLO-Aware LLM Serving"
authors:
  - "Chengyi Nie"
  - "Weici Pan"
  - "Rodrigo Fonseca"
  - "Zhenhua Liu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=9Gmw9LuAPj"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  The demand for large language model (LLM) inference is gradually dominating artificial intelligence workloads, creating an urgent need for cost-efficient inference serving. While prior work focuses on single-worker optimization, it often overlooks cluster-level coordination across both queries and computing resources. Scheduling requests without considering their uncertainty can lead to SLO violations or overprovisioning, resulting in excessive cost.
  
  In this paper, we present Aladdin, a scheduler that co-adaptively places inference queries and scales computing resources under probabilistic SL
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
  - nie26
---

# Aladdin: Joint Placement and Scaling for SLO-Aware LLM Serving

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `nie2026aladdin` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Chengyi Nie, Weici Pan, Rodrigo Fonseca |

## 摘要

The demand for large language model (LLM) inference is gradually dominating artificial intelligence workloads, creating an urgent need for cost-efficient inference serving. While prior work focuses on single-worker optimization, it often overlooks cluster-level coordination across both queries and computing resources. Scheduling requests without considering their uncertainty can lead to SLO violations or overprovisioning, resulting in excessive cost.

In this paper, we present Aladdin, a scheduler that co-adaptively places inference queries and scales computing resources under probabilistic SL

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