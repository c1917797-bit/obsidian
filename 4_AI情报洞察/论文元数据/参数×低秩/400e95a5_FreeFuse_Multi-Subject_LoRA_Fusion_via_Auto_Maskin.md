---
type: literature-corpus-entry
citekey: liu2026freefuse
title: "FreeFuse: Multi-Subject LoRA Fusion via Auto Masking at Test Time"
authors:
  - "Yaoli Liu"
  - "Yao-Xiang Ding"
  - "Kun Zhou"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=bKcBgNiREu"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  This paper proposes FreeFuse, a novel training-free approach for multi-subject text-to-image generation through automatic fusion of multiple subject LoRAs. In contrast to existing methods that either focus on pre-inference LoRA weight merging or rely on segmentation models and complex techniques like noise blending to isolate LoRA outputs, our key insight is that context-aware dynamic subject masks can be automatically derived from cross-attention layer weights. Our analysis shows that constraining each LoRA’s influence to its corresponding subject region via these masks effectively mitigates
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
  - liu26
---

# FreeFuse: Multi-Subject LoRA Fusion via Auto Masking at Test Time

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `liu2026freefuse` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Yaoli Liu, Yao-Xiang Ding, Kun Zhou |

## 摘要

This paper proposes FreeFuse, a novel training-free approach for multi-subject text-to-image generation through automatic fusion of multiple subject LoRAs. In contrast to existing methods that either focus on pre-inference LoRA weight merging or rely on segmentation models and complex techniques like noise blending to isolate LoRA outputs, our key insight is that context-aware dynamic subject masks can be automatically derived from cross-attention layer weights. Our analysis shows that constraining each LoRA’s influence to its corresponding subject region via these masks effectively mitigates 

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