---
created: 2026-09-15
updated: 2026-09-15
type: summary-report
status: active
tags: [codex, 改造报告, 推理情报体系, 复盘]
---

# AI 推理情报体系改造完成报告

> 覆盖 2026-09-11 ~ 09-15 的体系整理与自动化改造，全部成果已落地。对应 [[AI推理情报体系改造清单]]（已全部勾清）。

## 一、自动化采集（已上线）

- 统一入口 `0_Codex工作台/tools/run-daily-collection.ps1`：`full` / `arxiv` / `github` / `pipeline` / `radar` 分步跑。
- 顺序：arXiv 同步 → GitHub 同步 → 情报流水线（无 `MINIMAX_API_KEY` 自动跳过）→ 雷达 digest。
- Windows 计划任务 `IntelligenceInference_DailyCollect`（每日 08:00）。
- 状态记录：`1_AI情报溯源/状态/daily-collection-state.json`（last_run/fetched_at/history）。

## 二、根因 bug 修复（重要）

- **8 个 `.ps1` 工具补回 UTF-8 BOM**：`inference-audit / inference-radar / obsidian-codex / obsidian-loop-quality / sync-inference-arxiv / sync-inference-github / run_daily / _run_pipeline`。
- 根因：无 BOM 的 UTF-8 被 PowerShell 5.1 按 ANSI 读，中文乱码——这正是之前乱码目录 `0_Codexå·¥ä½œå°` 的源头，也导致雷达工具一直解析失败。修复后 `radar digest` 正常跑通。

## 三、论文库整理

| 项 | 结果 |
|---|---|
| 增量采集 | 2026-09-03→09-11 新增 271 篇入库（v8 / full_tagged 各 +271） |
| 去重 | 43 篇重复卡核实后移入 `.trash/`，活跃卡 14,369 篇唯一 |
| 归位 | 8 个误建到根目录的 `×` cell 目录，43 文件归位后入 `.trash/` |
| 回填脚本 | `4_AI情报洞察/backfill_arxiv.py`（标题反查 arXiv，断点续传，待限流解除跑） |

## 四、Inbox 分组

451 篇旧 Inbox → `_推理相关/` 338、`_非推理/` 82、`_重复/` 31、低证据 0（confidence 全为默认 0.6，无区分度）。

## 五、工作台内容补齐

- 首页完整索引（6 工具清单 + 模板 + 知识层路由 + 进行中洞察）
- [[推理Serving公平Benchmark表]]（vLLM/SGLang/TRT-LLM 对比骨架）
- [[必检论文核验清单]]（身份/录用/源码/许可核验）
- [[每周Top5信号晋升规范]]（流程 + 4 淘汰原因 + 记录模板）
- 质量看守命名统一（`质量看守` 与脚本输出目录合一）

## 六、必检论文核验

54 篇必检论文全库复核：卡片命中 32 / 仅 JSON 2 / **缺失 20**（多为 2020-2023 经典，如 FastBERT/MiniLM/QServe/FlashAttention-2/3/DeepSeek-V2/TensorRT-LLM）。报告：`4_AI情报洞察/论文洞察/must_check_papers_verification.md`。

## 七、质量与安全

- 质量门禁新增 `evidence_score=0` 拦截（禁止 0 证据报告进入洞察）。
- 清理 GitHub Token + AWMCP 注入指令；`run_daily.ps1` 密钥改读环境变量。

## 八、遗留事项（唯一外部依赖）

- [ ] **arXiv 限流解除后**：跑 `backfill_arxiv.py` 回填 4.4k 篇 hash 卡的 arXiv 链接（`python 4_AI情报洞察/backfill_arxiv.py --limit 20 --dry-run` 先试跑）。
- [ ] Benchmark 表、必检论文精确 ID 校验需实测/API，尚未填数字。

---

*生成 2026-09-15 · 入口：[[0_Codex工作台/首页]]*
