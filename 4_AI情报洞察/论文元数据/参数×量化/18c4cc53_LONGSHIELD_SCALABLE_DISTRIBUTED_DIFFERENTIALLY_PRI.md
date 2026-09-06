---
type: literature-corpus-entry
citekey: yang2026longshield
title: "LONGSHIELD: SCALABLE DISTRIBUTED DIFFERENTIALLY PRIVATE TRAINING FOR LONG-CONTEXT LLMS"
authors:
  - "Dingqing Yang"
  - "Emet Behrendt"
  - "Yiran Jerry Sun"
  - "MohammadHossein Olyaiy"
  - "Prashant J. Nair"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=1Q2NVxcSuS"
pdf_url: ""
object: 参数
method: 量化
cell: "参数×量化"
all_objects: []
all_methods: []
abstract: |
  Large language models excel at in-context learning but can memorize sensitive sequences, enabling membership-inference and extraction attacks. Differential privacy (DP) offers provable protection, yet DP training remains costly at long contexts. Prior work largely targets short-sequence DP fine-tuning, and the strongest public DP pretraining scales only to 1B parameters at 1,024 tokens. Profiling state-of-the-art distributed DP reveals two blockers: **efficiency** losses from a mixed ghost-norm clipping heuristic that wastes compute at longer sequences, and **scalability** limits where FSDP al
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
  - yang26
---

# LONGSHIELD: SCALABLE DISTRIBUTED DIFFERENTIALLY PRIVATE TRAINING FOR LONG-CONTEXT LLMS

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `yang2026longshield` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×量化 |
| **来源** | openreview |
| **作者** | Dingqing Yang, Emet Behrendt, Yiran Jerry Sun |

## 摘要

Large language models excel at in-context learning but can memorize sensitive sequences, enabling membership-inference and extraction attacks. Differential privacy (DP) offers provable protection, yet DP training remains costly at long contexts. Prior work largely targets short-sequence DP fine-tuning, and the strongest public DP pretraining scales only to 1B parameters at 1,024 tokens. Profiling state-of-the-art distributed DP reveals two blockers: **efficiency** losses from a mixed ghost-norm clipping heuristic that wastes compute at longer sequences, and **scalability** limits where FSDP al

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