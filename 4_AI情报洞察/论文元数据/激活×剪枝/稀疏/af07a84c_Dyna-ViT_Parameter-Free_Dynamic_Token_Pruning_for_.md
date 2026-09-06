---
type: literature-corpus-entry
citekey: rubab2026dyna
title: "Dyna-ViT: Parameter-Free Dynamic Token Pruning for Efficient Vision Transformers"
authors:
  - "Syeda Fiza Rubab"
  - "Arslan Abdul Ghaffar"
  - "Malik Junaid Jami Gul"
  - "Sheriff Murtala"
  - "Ingyu Lee"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=J8lWv7WOZ5"
pdf_url: ""
object: 激活
method: 剪枝/稀疏
cell: "激活×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  Vision Transformers (ViTs) achieve state-of-the-art results, yet their quadratic self-attention is inefficient, largely due to redundant processing of low-information background patches. We introduce Dyna-ViT, a simple, parameter-free framework for dynamic token pruning that ranks patches with an unsupervised saliency proxy and retains only the top-K before the encoder. The backbone remains an unmodified ViT; no extra modules or learnable parameters are added. Across three benchmarks, Dyna-ViT preserves accuracy while reducing compute. On PASCAL VOC, keeping 70% of patches is 25% faster per ep
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
  - rubab26
---

# Dyna-ViT: Parameter-Free Dynamic Token Pruning for Efficient Vision Transformers

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `rubab2026dyna` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Syeda Fiza Rubab, Arslan Abdul Ghaffar, Malik Junaid Jami Gul |

## 摘要

Vision Transformers (ViTs) achieve state-of-the-art results, yet their quadratic self-attention is inefficient, largely due to redundant processing of low-information background patches. We introduce Dyna-ViT, a simple, parameter-free framework for dynamic token pruning that ranks patches with an unsupervised saliency proxy and retains only the top-K before the encoder. The backbone remains an unmodified ViT; no extra modules or learnable parameters are added. Across three benchmarks, Dyna-ViT preserves accuracy while reducing compute. On PASCAL VOC, keeping 70% of patches is 25% faster per ep

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