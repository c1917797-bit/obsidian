---
type: literature-corpus-entry
citekey: chen2026beyond
title: "Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training"
authors:
  - "Ruishuo Chen"
  - "Xun Wang"
  - "Rui Hu"
  - "Zhuoran Li"
  - "Longbo Huang"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=xDl2866dmi"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  Generative Flow Networks (GFlowNets) are effective at sampling diverse, high-reward objects, but in many real-world settings where new reward queries are infeasible, they must be trained from offline datasets. The prevailing training methods rely on a proxy model to provide reward feedback for online sampled trajectories. However, in scenarios where constructing a reliable proxy is challenging due to data scarcity or cost, one must turn to static offline trajectories for training. Nevertheless, current proxy-free approaches often rely on coarse constraints that may limit the model's ability to
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
  - chen26
---

# Beyond the Proxy: Trajectory-Distilled Guidance for Offline GFlowNet Training

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `chen2026beyond` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Ruishuo Chen, Xun Wang, Rui Hu |

## 摘要

Generative Flow Networks (GFlowNets) are effective at sampling diverse, high-reward objects, but in many real-world settings where new reward queries are infeasible, they must be trained from offline datasets. The prevailing training methods rely on a proxy model to provide reward feedback for online sampled trajectories. However, in scenarios where constructing a reliable proxy is challenging due to data scarcity or cost, one must turn to static offline trajectories for training. Nevertheless, current proxy-free approaches often rely on coarse constraints that may limit the model's ability to

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