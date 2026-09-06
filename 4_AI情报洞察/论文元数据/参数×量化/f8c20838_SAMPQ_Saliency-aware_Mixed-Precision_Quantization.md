---
type: literature-corpus-entry
citekey: ma2026sampq
title: "SAMPQ: Saliency-aware Mixed-Precision Quantization"
authors:
  - "Lianbo Ma"
  - "Huanxi Zhang"
  - "Jianlun Ma"
  - "kaifang long"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=OkQtDD2uHM"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Although mixed-precision quantization (MPQ) achieves a remarkable accuracy-complexity trade-off, conventional gradient-based MPQ methods are susceptible to input noise, which leads to suboptimal bit-width allocation strategies. Through saliency analysis, we indicate that treating sample feature regions as equally significant exacerbates the quantization error in MPQ. To mitigate this issue, we propose saliency-aware MPQ (SAMPQ), a novel framework designed to dynamically evaluate the sample saliency. In particular, SAMPQ is formulated as a three-stage cascade-optimized training procedure. At th
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
  - ma26
---

# SAMPQ: Saliency-aware Mixed-Precision Quantization

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `ma2026sampq` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Lianbo Ma, Huanxi Zhang, Jianlun Ma |

## 摘要

Although mixed-precision quantization (MPQ) achieves a remarkable accuracy-complexity trade-off, conventional gradient-based MPQ methods are susceptible to input noise, which leads to suboptimal bit-width allocation strategies. Through saliency analysis, we indicate that treating sample feature regions as equally significant exacerbates the quantization error in MPQ. To mitigate this issue, we propose saliency-aware MPQ (SAMPQ), a novel framework designed to dynamically evaluate the sample saliency. In particular, SAMPQ is formulated as a three-stage cascade-optimized training procedure. At th

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