---
type: literature-corpus-entry
citekey: anonndinference
title: "Inference-Friendly Models With MixAttention"
authors: []
year: ""
venue: iclr2025
venue_type: conference
arxiv_id: ""
doi: ""
url: ""
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  The size of the key-value (KV) cache plays a critical role in determining both the maximum context length and the number of concurrent requests supported during inference in modern language models. The KV cache size grows proportionally with the number of attention heads and the tokens processed, leading to increased memory consumption and slower inference for long inputs. In this work, we explore the use of MixAttention, a model architecture modification closely related to a blog published by C
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "arxiv"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - KV
  - 量化
---

# Inference-Friendly Models With MixAttention

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `anonndinference` |
| **年份** | N/A |
| **会议/期刊** | iclr2025 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | arXiv |
| **作者** | N/A |

## 摘要

The size of the key-value (KV) cache plays a critical role in determining both the maximum context length and the number of concurrent requests supported during inference in modern language models. The KV cache size grows proportionally with the number of attention heads and the tokens processed, leading to increased memory consumption and slower inference for long inputs. In this work, we explore the use of MixAttention, a model architecture modification closely related to a blog published by C

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
*生成日期: 2026-07-06 | 来源: arXiv*