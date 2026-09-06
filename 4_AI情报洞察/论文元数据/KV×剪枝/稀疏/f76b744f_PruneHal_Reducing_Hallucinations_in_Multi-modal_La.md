---
type: literature-corpus-entry
citekey: sun2026prunehal
title: "PruneHal: Reducing Hallucinations in Multi-modal Large Language Models through Adaptive KV Cache Pruning"
authors:
  - "Fengyuan Sun"
  - "Hui Chen"
  - "Xinhao Xu"
  - "DanDan Zheng"
  - "Jingdong Chen"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=sMjESVShz3"
pdf_url: ""
object: KV
method: 剪枝/稀疏
cell: "KV×剪枝/稀疏"
all_objects: []
all_methods: []
abstract: |
  While multi-modal large language models (MLLMs) have made significant progress in recent years, the issue of their hallucinations remains a major challenge. To mitigate this phenomenon, existing solutions either introduce additional data for further training or incorporate external or internal information during inference. However, these approaches inevitably introduce extra computational costs. In this paper, we observe that the occurrence of hallucinations in MLLMs is closely associated with low attention distribution on visual tokens. Moreover, due to the redundancy of visual tokens, the re
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
  - KV
  - 剪枝/稀疏
  - sun26
---

# PruneHal: Reducing Hallucinations in Multi-modal Large Language Models through Adaptive KV Cache Pruning

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `sun2026prunehal` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×剪枝/稀疏 |
| **来源** | openreview |
| **作者** | Fengyuan Sun, Hui Chen, Xinhao Xu |

## 摘要

While multi-modal large language models (MLLMs) have made significant progress in recent years, the issue of their hallucinations remains a major challenge. To mitigate this phenomenon, existing solutions either introduce additional data for further training or incorporate external or internal information during inference. However, these approaches inevitably introduce extra computational costs. In this paper, we observe that the occurrence of hallucinations in MLLMs is closely associated with low attention distribution on visual tokens. Moreover, due to the redundancy of visual tokens, the re

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