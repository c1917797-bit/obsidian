---
type: literature-corpus-entry
citekey: adepu2026fine
title: "Fine-Tuning of Transformer models with Frames"
authors:
  - "Harshavardhan Adepu"
  - "Li Zhang"
  - "Sanjiv Kumar"
  - "Vikas Singh"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=V5PHmFqsiY"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  Fine-tuning large-scale pre-trained models for downstream tasks remains a challenge, particularly as model sizes continue to grow. While Parameter-Efficient Fine-Tuning (PEFT) strategies such as Low-Rank Adaptation (LoRA) have emerged as effective solutions,
  their memory requirements scale linearly with the size of the model, $\mathcal{O}(dr)$, where $d$ is the hidden dimension of the model and $r$ is the rank.
  In this work, we present FrameFT, a novel PEFT method based on Fusion Frames. We model the parameter update $\Delta W$ with a sparse coefficient matrix in the Fusion Frame representatio
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
  - adepu26
---

# Fine-Tuning of Transformer models with Frames

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `adepu2026fine` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Harshavardhan Adepu, Li Zhang, Sanjiv Kumar |

## 摘要

Fine-tuning large-scale pre-trained models for downstream tasks remains a challenge, particularly as model sizes continue to grow. While Parameter-Efficient Fine-Tuning (PEFT) strategies such as Low-Rank Adaptation (LoRA) have emerged as effective solutions,
their memory requirements scale linearly with the size of the model, $\mathcal{O}(dr)$, where $d$ is the hidden dimension of the model and $r$ is the rank.
In this work, we present FrameFT, a novel PEFT method based on Fusion Frames. We model the parameter update $\Delta W$ with a sparse coefficient matrix in the Fusion Frame representatio

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