---
type: literature-corpus-entry
citekey: lee2026revealing
title: "Revealing Stochastic Noise of Policy Entropy in Reinforcement Learning"
authors:
  - "Changha Lee"
  - "Tao Tuan Manh"
  - "Chan-Hyun Youn"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=vGpEO5foQ6"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  On-policy MARL remains attractive under non-stationarity but typically relies on a fixed entropy bonus that conflates useful exploration with stochastic fluctuations from concurrently learning agents. We present \emph{Policy Entropy Manipulation (PEM)}, a simple, drop-in alternative that treats entropy as a noisy measurement to be \emph{denoised} rather than uniformly maximized. PEM applies positive--negative momentum to \emph{entropy gradient} to form a high-pass, variance-controlled signal that preserves persistent exploratory trends while suppressing transient spikes. The method integrates
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
  - 低秩
  - lee26
---

# Revealing Stochastic Noise of Policy Entropy in Reinforcement Learning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lee2026revealing` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Changha Lee, Tao Tuan Manh, Chan-Hyun Youn |

## 摘要

On-policy MARL remains attractive under non-stationarity but typically relies on a fixed entropy bonus that conflates useful exploration with stochastic fluctuations from concurrently learning agents. We present \emph{Policy Entropy Manipulation (PEM)}, a simple, drop-in alternative that treats entropy as a noisy measurement to be \emph{denoised} rather than uniformly maximized. PEM applies positive--negative momentum to \emph{entropy gradient} to form a high-pass, variance-controlled signal that preserves persistent exploratory trends while suppressing transient spikes. The method integrates 

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