---
type: literature-corpus-entry
citekey: liu2026condiquant
title: "CondiQuant: Condition Number Based Low-Bit Quantization for Image Super-Resolution"
authors:
  - "Kai Liu"
  - "Dehui Wang"
  - "Zhiteng Li"
  - "Zheng Chen"
  - "Yong Guo"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=UVpLVGFYS2"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Low-bit model quantization for image super-resolution (SR) is a longstanding task which is renowned for its surprising compression and acceleration ability.
  However, accuracy degradation is inevitable when compressing the full-precision (FP) model to ultra-low bit widths ($2\sim4$ bits).
  Experimentally, we observed the degradation of quantization is mainly attributed to the quantization of activation instead of model weights.
  In numerical analysis, the condition number of weights could measure how much the output value of the function can change for a small change in the input argument, inhere
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
  - 量化
  - liu26
---

# CondiQuant: Condition Number Based Low-Bit Quantization for Image Super-Resolution

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026condiquant` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Kai Liu, Dehui Wang, Zhiteng Li |

## 摘要

Low-bit model quantization for image super-resolution (SR) is a longstanding task which is renowned for its surprising compression and acceleration ability.
However, accuracy degradation is inevitable when compressing the full-precision (FP) model to ultra-low bit widths ($2\sim4$ bits).
Experimentally, we observed the degradation of quantization is mainly attributed to the quantization of activation instead of model weights.
In numerical analysis, the condition number of weights could measure how much the output value of the function can change for a small change in the input argument, inhere

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