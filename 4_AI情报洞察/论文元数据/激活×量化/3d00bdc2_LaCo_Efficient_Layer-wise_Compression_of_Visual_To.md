---
type: literature-corpus-entry
citekey: liu2026laco
title: "LaCo: Efficient Layer-wise Compression of Visual Tokens for Multimodal Large Language Models"
authors:
  - "Juntao Liu"
  - "Liqiang Niu"
  - "Wenchao Chen"
  - "Jie Zhou"
  - "Fandong Meng"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=UDCiCnVGhq"
pdf_url: ""
object: 激活
method: 量化
cell: "激活×量化"
all_objects: []
all_methods: []
abstract: |
  Existing visual token compression methods for Multimodal Large Language Models (MLLMs) predominantly operate as post-encoder modules, limiting efficiency.
  % limiting their potential for efficiency gains.
  To address this limitation, we propose LaCo (Layer-wise Visual Token Compression), a novel framework for effective token compression within the vision encoder's intermediate layers. LaCo introduces two core components: 1) a layer-wise pixel-shuffle mechanism that systematically merges adjacent tokens through space-to-channel transformations, and 2) a residual learning architecture with non-par
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

# LaCo: Efficient Layer-wise Compression of Visual Tokens for Multimodal Large Language Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026laco` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 激活×量化 |
| **来源** | openreview |
| **作者** | Juntao Liu, Liqiang Niu, Wenchao Chen |

## 摘要

Existing visual token compression methods for Multimodal Large Language Models (MLLMs) predominantly operate as post-encoder modules, limiting efficiency.
% limiting their potential for efficiency gains.
To address this limitation, we propose LaCo (Layer-wise Visual Token Compression), a novel framework for effective token compression within the vision encoder's intermediate layers. LaCo introduces two core components: 1) a layer-wise pixel-shuffle mechanism that systematically merges adjacent tokens through space-to-channel transformations, and 2) a residual learning architecture with non-par

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