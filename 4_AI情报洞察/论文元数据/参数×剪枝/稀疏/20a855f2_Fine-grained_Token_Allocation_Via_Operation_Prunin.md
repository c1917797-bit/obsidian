---
type: literature-corpus-entry
citekey: liu2026fine
title: "Fine-grained Token Allocation Via Operation Pruning for Efficient MLLMs"
authors:
  - "Aoming Liu"
  - "Reuben Tan"
  - "Boqing Gong"
  - "Bryan A. Plummer"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=T6np2Ld3ag"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Token reduction accelerates Multimodal Large Language Models (MLLMs) by reducing excessive tokens, but overlooks structural redundancy differences where critical and redundant modules process identical token loads.
  For fine-grained computation control, we define an ``operation" as the computation for a module to process a group of tokens and introduce the operation pruning framework to enable modules to selectively process tokens.
  Built on this framework, we propose \textbf{D}epth-wise \textbf{O}peration \textbf{P}runing (\textbf{DOP}), a data-driven method that searches for strategies to pru
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
  - liu26
---

# Fine-grained Token Allocation Via Operation Pruning for Efficient MLLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026fine` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Aoming Liu, Reuben Tan, Boqing Gong |

## 摘要

Token reduction accelerates Multimodal Large Language Models (MLLMs) by reducing excessive tokens, but overlooks structural redundancy differences where critical and redundant modules process identical token loads. 
For fine-grained computation control, we define an ``operation" as the computation for a module to process a group of tokens and introduce the operation pruning framework to enable modules to selectively process tokens.
Built on this framework, we propose \textbf{D}epth-wise \textbf{O}peration \textbf{P}runing (\textbf{DOP}), a data-driven method that searches for strategies to pru

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