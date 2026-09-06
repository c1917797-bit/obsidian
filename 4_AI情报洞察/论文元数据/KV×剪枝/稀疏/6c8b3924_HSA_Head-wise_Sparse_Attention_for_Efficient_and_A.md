---
type: literature-corpus-entry
citekey: liu2026hsa
title: "HSA: Head-wise Sparse Attention for Efficient and Accurate Long-context Inference"
authors:
  - "Jing Liu"
  - "Jianqiao Lu"
  - "Yao Luo"
  - "Yuan Yang"
  - "Chen Zheng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=WytruI9uM3"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Transformer architectures have become the foundation of large language models (LLMs), excelling at sequential modeling via the self-attention mechanism. However, the quadratic computational complexity and linear KV cache growth of self-attention limit scalability in long-context scenarios. Sparse attention mechanisms, especially sliding window attention (SWA), help reduce these costs but inevitably constrain access to global context, which can degrade performance in tasks requiring long-range dependencies. While hybrid architectures that alternate between full-attention and SWA layers help mit
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
  - KV
  - 剪枝/稀疏
  - liu26
---

# HSA: Head-wise Sparse Attention for Efficient and Accurate Long-context Inference

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026hsa` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Jing Liu, Jianqiao Lu, Yao Luo |

## 摘要

Transformer architectures have become the foundation of large language models (LLMs), excelling at sequential modeling via the self-attention mechanism. However, the quadratic computational complexity and linear KV cache growth of self-attention limit scalability in long-context scenarios. Sparse attention mechanisms, especially sliding window attention (SWA), help reduce these costs but inevitably constrain access to global context, which can degrade performance in tasks requiring long-range dependencies. While hybrid architectures that alternate between full-attention and SWA layers help mit

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