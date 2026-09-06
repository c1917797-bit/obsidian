---
type: literature-corpus-entry
citekey: hsu2026five
title: "Five-Mode Tucker-LoRA for Video Diffusion on Conv3D Backbones"
authors:
  - "Hung-Min Hsu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=BamabJR7Ed"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Parameter-efficient fine-tuning for text-to-video diffusion remains challenging. Most LoRA-style adapters either flatten 3D kernels into 2D matrices or add temporal-only modules, which breaks the native structure of Conv3D backbones. We present a five-mode Tucker-LoRA that learns a Tucker residual directly on the 5-D convolutional weight update across output/input channels, time, height, and width. This preserves spatio-temporal geometry and enables mode-wise rank budgets; setting some ranks to one (or the temporal rank to zero) recovers common 2D or temporal-only adapters. We instantiate the
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
  - hsu26
---

# Five-Mode Tucker-LoRA for Video Diffusion on Conv3D Backbones

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hsu2026five` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Hung-Min Hsu |

## 摘要

Parameter-efficient fine-tuning for text-to-video diffusion remains challenging. Most LoRA-style adapters either flatten 3D kernels into 2D matrices or add temporal-only modules, which breaks the native structure of Conv3D backbones. We present a five-mode Tucker-LoRA that learns a Tucker residual directly on the 5-D convolutional weight update across output/input channels, time, height, and width. This preserves spatio-temporal geometry and enables mode-wise rank budgets; setting some ranks to one (or the temporal rank to zero) recovers common 2D or temporal-only adapters. We instantiate the 

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