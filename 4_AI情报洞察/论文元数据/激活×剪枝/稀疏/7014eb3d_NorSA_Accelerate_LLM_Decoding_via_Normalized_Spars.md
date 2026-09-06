---
type: literature-corpus-entry
citekey: gu2026norsa
title: "NorSA: Accelerate LLM Decoding via Normalized Sparse Activation"
authors:
  - "Tianteng Gu"
  - "Bo Xiao"
  - "Ke Zeng"
  - "Yanmin Qian"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=F20XWCnZdk"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Sparse activation accelerates  the decoding of large language models by eliminating redundant computations and reducing memory access during matrix multiplications. Current approaches have potential limitations as they rely on the strong assumption that "values across different dimensions of hidden states are drawn from independent and identically distributed random variables." Our research challenges this assumption by analyzing how causal dependencies exist between tokens and correlations exist between different dimensions of hidden states. Building on this insight, we introduce Normalized S
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
  - gu26
---

# NorSA: Accelerate LLM Decoding via Normalized Sparse Activation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `gu2026norsa` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Tianteng Gu, Bo Xiao, Ke Zeng |

## 摘要

Sparse activation accelerates  the decoding of large language models by eliminating redundant computations and reducing memory access during matrix multiplications. Current approaches have potential limitations as they rely on the strong assumption that "values across different dimensions of hidden states are drawn from independent and identically distributed random variables." Our research challenges this assumption by analyzing how causal dependencies exist between tokens and correlations exist between different dimensions of hidden states. Building on this insight, we introduce Normalized S

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