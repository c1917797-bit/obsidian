---
created: 2026-09-15
type: insight-report
status: active
tags: [codex, gdn, 推理优化, 流水线演示, 增量采集]
---

# GDN 推理优化 · 增量流水线演示报告

> 目的：演示「采集 → 检索 → 筛选 → 洞察」全链路，以 GDN 推理优化为例，跑最新增量数据。

## 采集

- 采集批次：2026-09-11（271 篇新论文，来源 arXiv API）
- 库当前状态：16,636 篇（`inference_compression_v8.json`）

## 检索

- 关键词：`gated deltanet / linear attention / delta rule / recurrent state / mamba / linear recurrent / subquadratic`
- 命中：5 篇

## 筛选（无损约束）

- 约束：不改权重 / 不重训 / 不量化 / 不删层或 token / 不用投机解码
- 全部淘汰：4 篇为非 LLM 视觉/医疗域外论文，1 篇为量化方法

## 结论

> 当前增量批次中**无可用的 GDN 无损推理加速**候选。下次采集后自动重检。

---

*关联：[[0_Codex工作台/tools/run-daily-collection.ps1]] · [[4_AI情报洞察/backfill_arxiv.py]]*