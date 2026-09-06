---
type: literature-corpus-entry
citekey: huo2026c
title: "C2T: Classifier-based Token Tree Construction in Speculative Decoding"
authors:
  - "Feiye Huo"
  - "Jianchao Tan"
  - "Zixu Jiang"
  - "Kefeng Zhang"
  - "Xunliang Cai"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=8pX8He3Yyg"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  With the increasing scale of Large Language Models (LLMs), issues of inference latency and computational costs have become increasingly prominent. Speculative decoding methods have emerged to alleviate these challenges, but existing tree construction strategies exhibit inefficiencies in accurately preparing candidate token trees for the verification stage. To address this, we propose a plug-and-play method named C2T that leverages a lightweight three-feature classifier with only 241 parameters to dynamically generate and pre-prune token trees, which is even applicable to early stopping in toke
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
  - huo26
---

# C2T: Classifier-based Token Tree Construction in Speculative Decoding

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `huo2026c` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Feiye Huo, Jianchao Tan, Zixu Jiang |

## 摘要

With the increasing scale of Large Language Models (LLMs), issues of inference latency and computational costs have become increasingly prominent. Speculative decoding methods have emerged to alleviate these challenges, but existing tree construction strategies exhibit inefficiencies in accurately preparing candidate token trees for the verification stage. To address this, we propose a plug-and-play method named C2T that leverages a lightweight three-feature classifier with only 241 parameters to dynamically generate and pre-prune token trees, which is even applicable to early stopping in toke

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