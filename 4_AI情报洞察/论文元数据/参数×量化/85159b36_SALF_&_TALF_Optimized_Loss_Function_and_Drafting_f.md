---
type: literature-corpus-entry
citekey: lee2026salf
title: "SALF & TALF: Optimized Loss Function and Drafting for Tree-based Speculative Decoding"
authors:
  - "Gunjun Lee"
  - "Jongmin Kim"
  - "Jaiyoung Park"
  - "Jung Ho Ahn"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=3V559xWIWc"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Speculative decoding (SpD) has emerged as a promising approach to accelerate the slow autoregressive inference of large language models (LLMs).
  SpD leverages a lightweight draft model to propose candidate tokens, which are then verified in parallel by the target LLM.
  Recent advances in tree-based SpD significantly improve efficiency by drafting token trees, enabling the verification of multiple sequences at once.
  Given its strong empirical performance reported across numerous studies, tree-based SpD is rapidly becoming dominant.
  However, existing draft model training methods overlook the tree
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
  - lee26
---

# SALF & TALF: Optimized Loss Function and Drafting for Tree-based Speculative Decoding

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `lee2026salf` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Gunjun Lee, Jongmin Kim, Jaiyoung Park |

## 摘要

Speculative decoding (SpD) has emerged as a promising approach to accelerate the slow autoregressive inference of large language models (LLMs).
SpD leverages a lightweight draft model to propose candidate tokens, which are then verified in parallel by the target LLM.
Recent advances in tree-based SpD significantly improve efficiency by drafting token trees, enabling the verification of multiple sequences at once.
Given its strong empirical performance reported across numerous studies, tree-based SpD is rapidly becoming dominant.
However, existing draft model training methods overlook the tree 

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