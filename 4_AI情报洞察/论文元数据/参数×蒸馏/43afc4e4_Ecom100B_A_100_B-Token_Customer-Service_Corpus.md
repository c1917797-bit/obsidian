---
type: literature-corpus-entry
citekey: zhao2026ecom
title: "Ecom100B: A 100 B-Token Customer-Service Corpus"
authors:
  - "Ruiyu Zhao"
  - "Yang Liu"
  - "Chenghan Yang"
  - "Yizhe Huang"
  - "Xiaolong Zhong"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=kA08ZjElv0"
pdf_url: ""
object: 参数
method: 蒸馏
cell: "参数×蒸馏"
all_objects: []
all_methods: []
abstract: |
  We introduce E-Com100B, a 100-billion-token English-centric corpus distilled from Common Crawl for pre-training customer-service-oriented language models.  Following the FineWeb-Edu recipe, we prompt a lightweight scorer (Qwen3-1.7B) to rate every raw document on its pedagogical value to an aspiring e-commerce support agent on a 0--5 Likert scale, keeping only documents rated 4--5.  This single filtering step yields a corpus that is 3.2× cleaner and 2.1× more task-relevant than the next-largest open alternative, while completely suppressing PII. Continued pre-training of Qwen-14B on E-Com100B
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
  - zhao26
---

# Ecom100B: A 100 B-Token Customer-Service Corpus

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `zhao2026ecom` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×蒸馏 |
| **来源** | openreview |
| **作者** | Ruiyu Zhao, Yang Liu, Chenghan Yang |

## 摘要

We introduce E-Com100B, a 100-billion-token English-centric corpus distilled from Common Crawl for pre-training customer-service-oriented language models.  Following the FineWeb-Edu recipe, we prompt a lightweight scorer (Qwen3-1.7B) to rate every raw document on its pedagogical value to an aspiring e-commerce support agent on a 0--5 Likert scale, keeping only documents rated 4--5.  This single filtering step yields a corpus that is 3.2× cleaner and 2.1× more task-relevant than the next-largest open alternative, while completely suppressing PII. Continued pre-training of Qwen-14B on E-Com100B 

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