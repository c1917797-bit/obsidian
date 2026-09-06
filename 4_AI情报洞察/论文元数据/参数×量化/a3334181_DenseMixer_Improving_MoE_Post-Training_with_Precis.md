---
type: literature-corpus-entry
citekey: yao2026densemixer
title: "DenseMixer: Improving MoE Post-Training with Precise Router Gradient"
authors:
  - "Feng Yao"
  - "Junxia Cui"
  - "Ruohan Zhang"
  - "Liyuan Liu"
  - "Shibo Hao"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=4HGIIekCx3"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Mixture-of-Experts (MoE) models are notoriously harder to train compared with dense models. Existing approaches either rely on imprecise router gradient or freeze router parameters entirely, limiting training effectiveness. We introduce DenseMixer, a novel MoE post-training technique that trades one extra forward pass on inactive experts for a more precise router gradient estimation. Our method consistently outperforms conventional methods across different MoE scales (7B, 14B, 16B, 30B), architectures (with/without shared experts), pre-training methods (from scratch/up-cycling), and post-train
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
  - yao26
---

# DenseMixer: Improving MoE Post-Training with Precise Router Gradient

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yao2026densemixer` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Feng Yao, Junxia Cui, Ruohan Zhang |

## 摘要

Mixture-of-Experts (MoE) models are notoriously harder to train compared with dense models. Existing approaches either rely on imprecise router gradient or freeze router parameters entirely, limiting training effectiveness. We introduce DenseMixer, a novel MoE post-training technique that trades one extra forward pass on inactive experts for a more precise router gradient estimation. Our method consistently outperforms conventional methods across different MoE scales (7B, 14B, 16B, 30B), architectures (with/without shared experts), pre-training methods (from scratch/up-cycling), and post-train

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