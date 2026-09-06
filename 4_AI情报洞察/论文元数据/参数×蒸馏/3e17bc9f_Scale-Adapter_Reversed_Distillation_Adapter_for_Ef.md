---
type: literature-corpus-entry
citekey: zhang2026scale
title: "Scale-Adapter: Reversed Distillation Adapter for Efficient Training of Large Video Diffusion Models"
authors:
  - "Yinhan Zhang"
  - "Yue Ma"
  - "Fangqiu Yi"
  - "Kunyu Feng"
  - "Chenyang Qi"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=c7vpjzlDR9"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  We propose Scale-Adapter, a plug-and-play adapter designed to efficiently bridge conditional knowledge from small adapted models to large video diffusion transformers. Existing controllable video DiT methods face critical inefficiencies: full fine-tuning of billion-parameter models is prohibitively expensive, while cascaded ControlNets introduce significant parameter overhead and exhibit limited flexibility for novel multi-condition compositions. To overcome these issues, Scale-Adapter introduces a novel reversed distillation method that allows a large video diffusion model to inherit precise
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
  - zhang26
---

# Scale-Adapter: Reversed Distillation Adapter for Efficient Training of Large Video Diffusion Models

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhang2026scale` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Yinhan Zhang, Yue Ma, Fangqiu Yi |

## 摘要

We propose Scale-Adapter, a plug-and-play adapter designed to efficiently bridge conditional knowledge from small adapted models to large video diffusion transformers. Existing controllable video DiT methods face critical inefficiencies: full fine-tuning of billion-parameter models is prohibitively expensive, while cascaded ControlNets introduce significant parameter overhead and exhibit limited flexibility for novel multi-condition compositions. To overcome these issues, Scale-Adapter introduces a novel reversed distillation method that allows a large video diffusion model to inherit precise 

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