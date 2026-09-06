---
type: literature-corpus-entry
citekey: mehraban2026pickstyle
title: "PickStyle: Video-to-Video Style Transfer with Context-Style Adapters"
authors:
  - "Soroush Mehraban"
  - "Vida Adeli"
  - "Jacob Rommann"
  - "Babak Taati"
  - "Kyryl Truskovskyi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=NRWI7NRaFD"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  We address the task of video style transfer with diffusion models, where the goal is to preserve the context of an input video while rendering it in a target style specified by a text prompt. A major challenge is the lack of paired video data for supervision. We propose PickStyle, a video-to-video style transfer framework that augments pretrained video diffusion backbones with style adapters and benefits from paired still image data with source–style correspondences for training. PickStyle inserts low-rank adapters into the self-attention layers of conditioning modules, enabling efficient spec
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
  - mehraban26
---

# PickStyle: Video-to-Video Style Transfer with Context-Style Adapters

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `mehraban2026pickstyle` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Soroush Mehraban, Vida Adeli, Jacob Rommann |

## 摘要

We address the task of video style transfer with diffusion models, where the goal is to preserve the context of an input video while rendering it in a target style specified by a text prompt. A major challenge is the lack of paired video data for supervision. We propose PickStyle, a video-to-video style transfer framework that augments pretrained video diffusion backbones with style adapters and benefits from paired still image data with source–style correspondences for training. PickStyle inserts low-rank adapters into the self-attention layers of conditioning modules, enabling efficient spec

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