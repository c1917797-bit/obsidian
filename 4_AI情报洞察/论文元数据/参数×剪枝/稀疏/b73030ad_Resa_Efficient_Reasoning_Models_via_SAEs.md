---
type: literature-corpus-entry
citekey: wang2026resa
title: "Resa: Efficient Reasoning Models via SAEs"
authors:
  - "Shangshang Wang"
  - "Julian Asilis"
  - "Ömer Faruk Akgül"
  - "Enes Burak Bilgin"
  - "Ollie Liu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=vUrZaERt8b"
pdf_url: ""
object: 参数
method: 剪枝/稀疏
cell: "参数×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  How cost-effectively can we elicit strong reasoning abilities in language models by leveraging their underlying representations? We present Resa, a family of reasoning models trained via an efficient sparse autoencoder tuning (SAE‑Tuning) procedure. This method first trains an SAE to capture reasoning abilities from a source model, and then uses the trained SAE to guide a standard supervised fine-tuning process to elicit such abilities in a target model, all using verified question-answer data *without any reasoning traces*. When applied to certain Qwen-style models before further RL training,
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

# Resa: Efficient Reasoning Models via SAEs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026resa` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Shangshang Wang, Julian Asilis, Ömer Faruk Akgül |

## 摘要

How cost-effectively can we elicit strong reasoning abilities in language models by leveraging their underlying representations? We present Resa, a family of reasoning models trained via an efficient sparse autoencoder tuning (SAE‑Tuning) procedure. This method first trains an SAE to capture reasoning abilities from a source model, and then uses the trained SAE to guide a standard supervised fine-tuning process to elicit such abilities in a target model, all using verified question-answer data *without any reasoning traces*. When applied to certain Qwen-style models before further RL training,

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