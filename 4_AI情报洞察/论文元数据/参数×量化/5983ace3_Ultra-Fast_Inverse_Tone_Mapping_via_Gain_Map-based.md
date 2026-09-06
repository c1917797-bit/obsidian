---
type: literature-corpus-entry
citekey: guan2026ultra
title: "Ultra-Fast Inverse Tone Mapping via Gain Map-based LUT"
authors:
  - "Yuanshen Guan"
  - "Ruikang Xu"
  - "Chang Chen"
  - "Yinuo Liao"
  - "Dehua Song"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=qUr6mVmjwn"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  We aim to introduce Look-Up Tables (LUTs), a highly efficient approach, for ultra-fast inverse tone mapping (ITM).
  However, as LUT size scales exponentially with increasing bit-depth, it remains challenging to employ dense sampling for high bit-depth accuracy.
  This inevitably introduces quantization artifacts and degrades the fidelity of ITM.
  To address this issue, we propose GMLUT, which encodes high-bit-depth HDR information into a low-bit-depth learnable Gain Map (GM), thereby facilitating the application of LUTs.
  Nevertheless, since the LUT alone can only perform global mapping, it is insu
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
  - guan26
---

# Ultra-Fast Inverse Tone Mapping via Gain Map-based LUT

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `guan2026ultra` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Yuanshen Guan, Ruikang Xu, Chang Chen |

## 摘要

We aim to introduce Look-Up Tables (LUTs), a highly efficient approach, for ultra-fast inverse tone mapping (ITM).
However, as LUT size scales exponentially with increasing bit-depth, it remains challenging to employ dense sampling for high bit-depth accuracy.
This inevitably introduces quantization artifacts and degrades the fidelity of ITM.
To address this issue, we propose GMLUT, which encodes high-bit-depth HDR information into a low-bit-depth learnable Gain Map (GM), thereby facilitating the application of LUTs.
Nevertheless, since the LUT alone can only perform global mapping, it is insu

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