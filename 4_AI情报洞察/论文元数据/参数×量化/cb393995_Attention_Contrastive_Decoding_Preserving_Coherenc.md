---
type: literature-corpus-entry
citekey: chen2026attention
title: "Attention Contrastive Decoding: Preserving Coherence While Mitigating Hallucinations in Large Vision-Language Models"
authors:
  - "Yujia Chen"
  - "Rui Sun"
  - "Wangkai Li"
  - "Huayu Mai"
  - "Bingzhou Wang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=uomCTwGflg"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Large Vision-Language Models (LVLMs) exhibit remarkable multimodal capabilities but frequently produce factually inconsistent hallucinations. While Contrastive Decoding (CD) methods offer a training-free approach to hallucination mitigation, they operate at the logits level, compromising output coherence and diversity. Through systematic analysis, we show that logits-level subtraction disrupts intrinsic language generation mechanisms, requiring restrictive penalty mechanisms that further limit diversity. We propose Attention Contrastive Decoding (ACD), which transfers contrastive operations to
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
  - chen26
---

# Attention Contrastive Decoding: Preserving Coherence While Mitigating Hallucinations in Large Vision-Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026attention` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yujia Chen, Rui Sun, Wangkai Li |

## 摘要

Large Vision-Language Models (LVLMs) exhibit remarkable multimodal capabilities but frequently produce factually inconsistent hallucinations. While Contrastive Decoding (CD) methods offer a training-free approach to hallucination mitigation, they operate at the logits level, compromising output coherence and diversity. Through systematic analysis, we show that logits-level subtraction disrupts intrinsic language generation mechanisms, requiring restrictive penalty mechanisms that further limit diversity. We propose Attention Contrastive Decoding (ACD), which transfers contrastive operations to

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