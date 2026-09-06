---
type: literature-corpus-entry
citekey: zhang2026quantize
title: "Quantize-then-Rectify: Accelerating VQ-VAE Training in Latent Feature Space"
authors:
  - "Borui Zhang"
  - "Qihang Rao"
  - "Wenzhao Zheng"
  - "Jie Zhou"
  - "Jiwen Lu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=6193b311kq"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Visual tokenizers are pivotal in multimodal large models, acting as bridges between continuous inputs and discrete token. Nevertheless, training high-compression-rate VQ-VAEs remains computationally demanding, often necessitating thousands of GPU hours. This work demonstrates that a pre-trained VAE can be efficiently transformed into a VQ-VAE by controlling quantization noise within the VAE's tolerance threshold. We present \textbf{Quantize-then-Rectify (ReVQ)}, a framework leveraging pre-trained VAEs to enable rapid VQ-VAE training with minimal computational overhead. By integrating \textbf{c
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
  - zhang26
---

# Quantize-then-Rectify: Accelerating VQ-VAE Training in Latent Feature Space

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026quantize` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Borui Zhang, Qihang Rao, Wenzhao Zheng |

## 摘要

Visual tokenizers are pivotal in multimodal large models, acting as bridges between continuous inputs and discrete token. Nevertheless, training high-compression-rate VQ-VAEs remains computationally demanding, often necessitating thousands of GPU hours. This work demonstrates that a pre-trained VAE can be efficiently transformed into a VQ-VAE by controlling quantization noise within the VAE's tolerance threshold. We present \textbf{Quantize-then-Rectify (ReVQ)}, a framework leveraging pre-trained VAEs to enable rapid VQ-VAE training with minimal computational overhead. By integrating \textbf{c

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