---
type: literature-corpus-entry
citekey: wang2026test
title: "Test-Real-Time Adaptation against Sparse Knowledge Bottleneck"
authors:
  - "Guowei Wang"
  - "Yan Huang"
  - "Fan Lyu"
  - "Changxing Ding"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=bEaUEFTT3N"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Test-time adaptation (TTA) typically involves adaptation delays due to self-training, which conflict with real-time deployment where inference cannot pause for adaptation. We introduce Test-Real-Time Adaptation (TRTA), which requires uninterrupted prediction while adaptation runs in the background, leaving few update opportunities. In TTA, later reliable signals enable error correction and steady knowledge accumulation, whereas in TRTA, such signals are rare, so knowledge growth stalls. We term this the sparse-knowledge bottleneck, where limited updates hinder error correction and increase the
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
  - wang26
---

# Test-Real-Time Adaptation against Sparse Knowledge Bottleneck

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026test` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Guowei Wang, Yan Huang, Fan Lyu |

## 摘要

Test-time adaptation (TTA) typically involves adaptation delays due to self-training, which conflict with real-time deployment where inference cannot pause for adaptation. We introduce Test-Real-Time Adaptation (TRTA), which requires uninterrupted prediction while adaptation runs in the background, leaving few update opportunities. In TTA, later reliable signals enable error correction and steady knowledge accumulation, whereas in TRTA, such signals are rare, so knowledge growth stalls. We term this the sparse-knowledge bottleneck, where limited updates hinder error correction and increase the

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