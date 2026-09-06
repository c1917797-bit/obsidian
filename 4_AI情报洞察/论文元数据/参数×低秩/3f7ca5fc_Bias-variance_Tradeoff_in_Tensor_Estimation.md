---
type: literature-corpus-entry
citekey: kumar2026bias
title: "Bias-variance Tradeoff in Tensor Estimation"
authors:
  - "Shivam Kumar"
  - "Haotian Xu"
  - "Carlos Misael Madrid Padilla"
  - "Yuehaw Khoo"
  - "OSCAR HERNAN MADRID PADILLA"
year: 2026
venue: ICLR 2026
venue_type: conference
arxiv_id: ""
doi: ""
url: "https://openreview.net/forum?id=lxqTU8Ofb2"
pdf_url: ""
object: 参数
method: 低秩
cell: "参数×低秩"
all_objects: []
all_methods: []
abstract: |
  We study denoising of a third-order tensor when the ground-truth tensor is **not** necessarily Tucker low-rank. Specifically, we observe
  $$
  Y=X^\\ast+Z\in \\mathbb{R}^{p_{1} \\times p_{2} \\times p_{3}},
  $$
  where $X^\\ast$ is the ground-truth tensor, and $Z$ is the noise tensor. We propose a simple variant of the higher-order tensor SVD estimator $\\widetilde{X}$. We show that uniformly over all user-specified Tucker ranks $(r_{1},r_{2},r_{3})$,
  $$
  \\| \\widetilde{X} - X^\ast \\|^2_{\\mathrm{F}} = O \\Big( \\kappa^2 \\Big\\{ r_{1}r_{2}r_{3} + \\sum_{k=1}^{3} p_{k} r_{k} \\Big\\} \\; + \\; \\xi
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
  - kumar26
---

# Bias-variance Tradeoff in Tensor Estimation

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `kumar2026bias` |
| **年份** | 2026 |
| **会议/期刊** | ICLR 2026 |
| **arXiv** | N/A |
| **4×5分类** | 参数×低秩 |
| **来源** | openreview |
| **作者** | Shivam Kumar, Haotian Xu, Carlos Misael Madrid Padilla |

## 摘要

We study denoising of a third-order tensor when the ground-truth tensor is **not** necessarily Tucker low-rank. Specifically, we observe
$$
Y=X^\\ast+Z\in \\mathbb{R}^{p_{1} \\times p_{2} \\times p_{3}},
$$
where $X^\\ast$ is the ground-truth tensor, and $Z$ is the noise tensor. We propose a simple variant of the higher-order tensor SVD estimator $\\widetilde{X}$. We show that uniformly over all user-specified Tucker ranks $(r_{1},r_{2},r_{3})$,
$$
\\| \\widetilde{X} - X^\ast \\|^2_{\\mathrm{F}} = O \\Big( \\kappa^2 \\Big\\{ r_{1}r_{2}r_{3} + \\sum_{k=1}^{3} p_{k} r_{k} \\Big\\} \\; + \\; \\xi

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