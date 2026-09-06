---
type: literature-corpus-entry
citekey: luo2026non
title: "Non-Additive Time-Series Forecasting via Cross-Decomposition and Linear Attention"
authors:
  - "Binli Luo"
  - "Han Zhou"
  - "Shiyuan Teng"
  - "Ning Gui"
  - "Xianhan Tan"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=JWQtXbVRbs"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Many multivariate forecasters model additive effects well but miss non-additive interactions among temporal bases, variables, and exogenous drivers, which harms long-horizon accuracy and attribution. We present  time-series interaction machine (${TIM}$), an all-MLP forecaster designed from the ANOVA/Hoeffding target: the regression function is decomposed into main effects and an orthogonal interaction component. TIM assigns the interaction to a DCN-style cross stack that explicitly synthesizes bounded-degree polynomial crosses with controllable CP rank, while lightweight branches capture main
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
  - luo26
---

# Non-Additive Time-Series Forecasting via Cross-Decomposition and Linear Attention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `luo2026non` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Binli Luo, Han Zhou, Shiyuan Teng |

## 摘要

Many multivariate forecasters model additive effects well but miss non-additive interactions among temporal bases, variables, and exogenous drivers, which harms long-horizon accuracy and attribution. We present  time-series interaction machine (${TIM}$), an all-MLP forecaster designed from the ANOVA/Hoeffding target: the regression function is decomposed into main effects and an orthogonal interaction component. TIM assigns the interaction to a DCN-style cross stack that explicitly synthesizes bounded-degree polynomial crosses with controllable CP rank, while lightweight branches capture main 

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