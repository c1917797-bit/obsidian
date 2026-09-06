---
type: literature-corpus-entry
citekey: song2026dynamic
title: "Dynamic Context Adapters: Efficiently Infusing History into Vision-and-Language Models"
authors:
  - "Yuhang Song"
  - "Bor-Jiun Lin"
  - "Jiaxu Liu"
  - "Te-Chuan Chiu"
  - "Anh Nguyen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=rkTNAk3QSh"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Transformer-based Vision-and-Language Models (VLMs) have set new benchmarks across diverse multimodal tasks by effectively aligning visual and linguistic inputs. Despite their remarkable success, existing VLMs process each visual input independently, which brings limitations to downstreamtasks that require integrating sequential historical context. Naively incorporating historical frames directly into Transformer inputs results in quadratic complexity in self-attention, excessive memory usage. Prior attempts using token concatenation methods severely inflate computational costs, while recurren
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
  - song26
---

# Dynamic Context Adapters: Efficiently Infusing History into Vision-and-Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `song2026dynamic` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yuhang Song, Bor-Jiun Lin, Jiaxu Liu |

## 摘要

Transformer-based Vision-and-Language Models (VLMs) have set new benchmarks across diverse multimodal tasks by effectively aligning visual and linguistic inputs. Despite their remarkable success, existing VLMs process each visual input independently, which brings limitations to downstreamtasks that require integrating sequential historical context. Naively incorporating historical frames directly into Transformer inputs results in quadratic complexity in self-attention, excessive memory usage. Prior attempts using token concatenation methods severely inflate computational costs, while recurren

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