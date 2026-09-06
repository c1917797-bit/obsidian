---
type: literature-corpus-entry
citekey: hzl2026object
title: "Object-level self-distillation with bounding-box weak supervision improves vision pretraining"
authors:
  - "Çağlar Hızlı"
  - "Joel Honkamaa"
  - "Çağatay Yıldız"
  - "Pekka Marttinen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=ebbVFo9r4B"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Self-distillation has become a central paradigm for pretraining vision transformers (ViTs). Existing approaches typically operate at the image level and assume that different augmentations of the same image preserve semantic content to be distilled. This premise breaks down in complex scenes with multiple objects with randomly sampled data augmentations. To tackle this, we introduce ODIS (Object-level Self-Distillation), a new framework that refines the self-distillation objective to the level of individual objects using bounding boxes that encapsulate objects. ODIS leverages object-aware crop
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
  - hızlı26
---

# Object-level self-distillation with bounding-box weak supervision improves vision pretraining

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `hzl2026object` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Çağlar Hızlı, Joel Honkamaa, Çağatay Yıldız |

## 摘要

Self-distillation has become a central paradigm for pretraining vision transformers (ViTs). Existing approaches typically operate at the image level and assume that different augmentations of the same image preserve semantic content to be distilled. This premise breaks down in complex scenes with multiple objects with randomly sampled data augmentations. To tackle this, we introduce ODIS (Object-level Self-Distillation), a new framework that refines the self-distillation objective to the level of individual objects using bounding boxes that encapsulate objects. ODIS leverages object-aware crop

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