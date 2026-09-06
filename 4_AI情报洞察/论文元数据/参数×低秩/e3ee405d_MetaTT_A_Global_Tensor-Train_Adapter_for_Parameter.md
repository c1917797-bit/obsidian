---
type: literature-corpus-entry
citekey: lopezpiqueres2026metatt
title: "MetaTT: A Global Tensor-Train Adapter for Parameter-Efficient Fine-Tuning"
authors:
  - "Javier Lopez-Piqueres"
  - "Pranav Deshpande"
  - "Archan Ray"
  - "Mattia Jacopo Villani"
  - "Marco Pistoia"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=mp0rPiYHPi"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  We present MetaTT, a Tensor Train (TT) adapter framework for fine-tuning of
  pre-trained transformers. MetaTT enables flexible and parameter-efficient model
  adaptation by using a single shared TT to factorize transformer sub-modules. This
  factorization indexes key structural dimensions, including layer and matrix type,
  and can optionally incorporate heads and tasks. This design allows MetaTT’s pa-
  rameter count to scale with the sum, rather than the product, of the modes, resulting
  in a substantially more compact adapter. Our benchmarks compare MetaTT with
  LoRA along with recent state-of-the-ar
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
  - 低秩
  - lopez-piqueres26
---

# MetaTT: A Global Tensor-Train Adapter for Parameter-Efficient Fine-Tuning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lopezpiqueres2026metatt` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Javier Lopez-Piqueres, Pranav Deshpande, Archan Ray |

## 摘要

We present MetaTT, a Tensor Train (TT) adapter framework for fine-tuning of
pre-trained transformers. MetaTT enables flexible and parameter-efficient model
adaptation by using a single shared TT to factorize transformer sub-modules. This
factorization indexes key structural dimensions, including layer and matrix type,
and can optionally incorporate heads and tasks. This design allows MetaTT’s pa-
rameter count to scale with the sum, rather than the product, of the modes, resulting
in a substantially more compact adapter. Our benchmarks compare MetaTT with
LoRA along with recent state-of-the-ar

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