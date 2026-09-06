---
type: literature-corpus-entry
citekey: parkndcodegemm
title: "CodeGEMM: A Codebook-Centric Approach to Efficient GEMM in Quantized LLMs"
authors:
  - "Gunho Park"
  - "Jeongin Bae"
  - "Byeongwook Kim"
  - "Baeseong park"
  - "Jiwon Ryu"
year: ""
venue: NeurIPS 2025
venue_type: conference
arxiv_id: ""
doi: ""
url: ""
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Weight-only quantization is widely used to mitigate the memory-bound nature of LLM inference. Codebook-based methods extend this trend by achieving strong accuracy in the extremely low-bit regime (e.g., 2-bit). However, current kernels rely on dequantization, which repeatedly fetches centroids and r
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "arxiv"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - 参数
  - 量化
  - park
---

# CodeGEMM: A Codebook-Centric Approach to Efficient GEMM in Quantized LLMs

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `parkndcodegemm` |
| **年份** | N/A |
| **会议/期刊** | NeurIPS 2025 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | arXiv |
| **作者** | Gunho Park, Jeongin Bae, Byeongwook Kim |

## 摘要

Weight-only quantization is widely used to mitigate the memory-bound nature of LLM inference. Codebook-based methods extend this trend by achieving strong accuracy in the extremely low-bit regime (e.g., 2-bit). However, current kernels rely on dequantization, which repeatedly fetches centroids and r

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
*生成日期: 2026-07-06 | 来源: arXiv*