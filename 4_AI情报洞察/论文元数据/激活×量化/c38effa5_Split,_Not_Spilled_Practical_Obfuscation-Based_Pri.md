---
type: literature-corpus-entry
citekey: pegoraro2026split
title: "Split, Not Spilled: Practical Obfuscation-Based Privacy-Preserving Split Learning"
authors:
  - "Alessandro Pegoraro"
  - "Kavita Kumari"
  - "Elissa Mollakuqe"
  - "Ahmad-Reza Sadeghi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=XQlcvkzMuv"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Split Learning (SL) partitions a deep neural network between client and server, enabling collaborative training while reducing the client’s computational load. However, it has been shown that the intermediate activations (“smashed data”) of the client’s model, shared with the server, leak sensitive information. Existing defenses are limited: many assume only passive adversaries, degrade accuracy significantly, or have already been bypassed by recent reconstruction attacks. In this work, we propose SEAL, a client-side obfuscation framework for SL. By applying secret, client-specific periodic tr
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
  - 量化
  - pegoraro26
---

# Split, Not Spilled: Practical Obfuscation-Based Privacy-Preserving Split Learning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `pegoraro2026split` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Alessandro Pegoraro, Kavita Kumari, Elissa Mollakuqe |

## 摘要

Split Learning (SL) partitions a deep neural network between client and server, enabling collaborative training while reducing the client’s computational load. However, it has been shown that the intermediate activations (“smashed data”) of the client’s model, shared with the server, leak sensitive information. Existing defenses are limited: many assume only passive adversaries, degrade accuracy significantly, or have already been bypassed by recent reconstruction attacks. In this work, we propose SEAL, a client-side obfuscation framework for SL. By applying secret, client-specific periodic tr

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