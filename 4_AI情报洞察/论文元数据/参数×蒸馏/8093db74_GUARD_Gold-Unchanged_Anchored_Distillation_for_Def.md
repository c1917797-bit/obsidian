---
type: literature-corpus-entry
citekey: li2026guard
title: "GUARD: Gold-Unchanged Anchored Distillation for Defending LLMs Against Membership Inference Attacks"
authors:
  - "Qiufeng Li"
  - "Shu Hong"
  - "Tian Lan"
  - "Weidong Cao"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=CjAE8ScfTK"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Large language models (LLMs) are widely fine-tuned for many domain-specific tasks that often contain sensitive and private data. This heightens the risk of membership inference attacks (MIAs), which aim to infer whether a particular sample appeared in training. Prior work has developed increasingly strong MIAs for fine-tuned LLMs, but practical and effective defenses remain significantly limited. The core challenge is a privacy-utility tension: fine-tuning improves utility by increasing confidence on the ground-truth (“gold”) token, yet this shift creates statistical differences that reveal me
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
  - 蒸馏
  - li26
---

# GUARD: Gold-Unchanged Anchored Distillation for Defending LLMs Against Membership Inference Attacks

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026guard` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Qiufeng Li, Shu Hong, Tian Lan |

## 摘要

Large language models (LLMs) are widely fine-tuned for many domain-specific tasks that often contain sensitive and private data. This heightens the risk of membership inference attacks (MIAs), which aim to infer whether a particular sample appeared in training. Prior work has developed increasingly strong MIAs for fine-tuned LLMs, but practical and effective defenses remain significantly limited. The core challenge is a privacy-utility tension: fine-tuning improves utility by increasing confidence on the ground-truth (“gold”) token, yet this shift creates statistical differences that reveal me

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