---
type: literature-corpus-entry
citekey: saikumar2026signal
title: "Signal Collapse in One-Shot Pruning: When Sparse Models Fail to Distinguish Neural Representations"
authors:
  - "Dhananjay Saikumar"
  - "Blesson Varghese"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=ev9gLf4piX"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  The size of modern neural networks has made inference increasingly resource-intensive. Network pruning reduces model size by sparsifying parameters. One-shot pruning, which selects parameters via impact-based importance scores and applies second-order parameter updates, often incurs severe accuracy loss. We identify for the first time that this degradation occurs due to a phenomenon we refer to as signal collapse, which is a significant reduction in activation variance across layers, rather than the removal of `important' parameters. To address this, we introduce REFLOW, which restores layer-w
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
  - saikumar26
---

# Signal Collapse in One-Shot Pruning: When Sparse Models Fail to Distinguish Neural Representations

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `saikumar2026signal` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Dhananjay Saikumar, Blesson Varghese |

## 摘要

The size of modern neural networks has made inference increasingly resource-intensive. Network pruning reduces model size by sparsifying parameters. One-shot pruning, which selects parameters via impact-based importance scores and applies second-order parameter updates, often incurs severe accuracy loss. We identify for the first time that this degradation occurs due to a phenomenon we refer to as signal collapse, which is a significant reduction in activation variance across layers, rather than the removal of `important' parameters. To address this, we introduce REFLOW, which restores layer-w

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