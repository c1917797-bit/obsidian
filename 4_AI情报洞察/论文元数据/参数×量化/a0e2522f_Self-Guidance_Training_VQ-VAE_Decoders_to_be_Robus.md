---
type: literature-corpus-entry
citekey: li2026self
title: "Self-Guidance: Training VQ-VAE Decoders to be Robust to Quantization Artifacts for High-Fidelity Neural Speech Codec"
authors:
  - "Xiang Li"
  - "Yixuan Zhou"
  - "Jingran Xie"
  - "Zhiyong Wu"
  - "Yue Yu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=lCaU7NlZ1I"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Neural speech codecs, predominantly based on Vector-Quantized Variational Autoencoders (VQ-VAEs), serve as fundamental audio tokenizers for speech large language models (SLLMs). However, their reconstruction fidelity is limited by quantization errors introduced during latent space discretization. Existing solutions typically increase model complexity through larger codebooks or hierarchical quantization, which subsequently intensify the modeling challenge for downstream SLLMs. Inspired by the key insight that the codec decoder produces superior output from continuous pre-quantize embeddings, w
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
  - li26
---

# Self-Guidance: Training VQ-VAE Decoders to be Robust to Quantization Artifacts for High-Fidelity Neural Speech Codec

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `li2026self` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Xiang Li, Yixuan Zhou, Jingran Xie |

## 摘要

Neural speech codecs, predominantly based on Vector-Quantized Variational Autoencoders (VQ-VAEs), serve as fundamental audio tokenizers for speech large language models (SLLMs). However, their reconstruction fidelity is limited by quantization errors introduced during latent space discretization. Existing solutions typically increase model complexity through larger codebooks or hierarchical quantization, which subsequently intensify the modeling challenge for downstream SLLMs. Inspired by the key insight that the codec decoder produces superior output from continuous pre-quantize embeddings, w

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