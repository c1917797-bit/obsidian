---
type: literature-corpus-entry
citekey: wang2026rl
title: "RL$^2$eak: Reinforcement Learning Enhanced Prompt Leakage Attack in Multi-tenant Large Language Model Services"
authors:
  - "Longxiang Wang"
  - "Xiang Zheng"
  - "Xuhao Zhang"
  - "Yao Zhang"
  - "Ye Wu"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=LmGSD6CedJ"
pdf_url: ""
object: KV
method: 量化
cell: "KV×量化"
all_objects: []
all_methods: []
abstract: |
  Large Language Models (LLMs) have become a transformative technology in both academia and industry. In practice, LLM services are typically deployed using multi-tenant serving frameworks. Popular inference frameworks such as vLLM and SGLang both employ Key-Value cache sharing among users to enhance computational efficiency. However, this shared caching mechanism may lead to potential leakage of the private user prompts. Previous works have demonstrated the impact of this information. Nevertheless, these works mainly focus on expanding the attack surface brought by the cache sharing mechanism,
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
  - 量化
  - wang26
---

# RL$^2$eak: Reinforcement Learning Enhanced Prompt Leakage Attack in Multi-tenant Large Language Model Services

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `wang2026rl` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | KV×量化 |
| **来源** | openreview |
| **作者** | Longxiang Wang, Xiang Zheng, Xuhao Zhang |

## 摘要

Large Language Models (LLMs) have become a transformative technology in both academia and industry. In practice, LLM services are typically deployed using multi-tenant serving frameworks. Popular inference frameworks such as vLLM and SGLang both employ Key-Value cache sharing among users to enhance computational efficiency. However, this shared caching mechanism may lead to potential leakage of the private user prompts. Previous works have demonstrated the impact of this information. Nevertheless, these works mainly focus on expanding the attack surface brought by the cache sharing mechanism, 

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