---
created: 2026-09-06
updated: 2026-09-11
type: migration-backlog
status: active
tags: [AI推理, radar, 改造]
---
# AI 推理情报体系改造清单

## 第一阶段：已完成

- [x] 建立20个 P0 一手信源白名单
- [x] 建立证据门和价值评分
- [x] 建立统一推理信号卡
- [x] 建立动态雷达看板
- [x] 建立关键研究问题清单
- [x] 建立 new / validate / rank / status 工具
- [x] Codex 根规则接入推理雷达工作流

## 第二阶段：待执行

- [x] 为 P0 开源推理信源建立可持久化 GitHub Release checkpoint（2026-09-06 已建立10项基线）
- [x] 恢复每日采集（2026-09-14：统一入口 `run-daily-collection.ps1` + Windows 计划任务 `IntelligenceInference_DailyCollect` 每日 08:00；state 记录 last_run/fetched_at，source_published 由 arxiv/github checkpoint 维护）
- [x] 将旧 Inbox 分为推理相关、非推理、重复、低证据四组（2026-09-11：451 篇 → 推理相关 338 / 非推理 82 / 重复 31 / 低证据 0）
- [x] 核验“必检论文”清单（2026-09-15：54 篇全库复核 → 卡片命中 32 / 仅 JSON 2 / 缺失 20；报告更新 `论文洞察/must_check_papers_verification.md`；精确 arXiv ID 校验待限流解除后跑）
- [x] 为旧论文卡补 primary_source（2026-09-11：10k 篇已有 arXiv/url；4.4k 篇 hash 卡无源；已交付回填脚本 `4_AI情报洞察/backfill_arxiv.py`，待 arXiv 限流解除后跑；code_url/硬件/benchmark 仍需逐篇调研）
- [x] 清理已确认的完全重复论文卡（2026-09-11：43 篇核实后移入 `.trash/`，活跃卡去重后 14,369 篇唯一）
- [x] 统一质量看守命名（`质量看守` 与脚本输出目录合一，`.gitignore` 只忽略生成数据）
- [x] 归位错位目录（8 个 `×` cell 目录曾误建到库根目录，43 文件已移回 `论文元数据/_重复/` 再入 `.trash/`）
- [x] 补齐工作台内容（首页索引、[[推理Serving公平Benchmark表]]、[[必检论文核验清单]]、工具清单）
- [x] 禁止 0 证据报告进入正式洞察（已在 `obsidian-loop-quality.ps1` 加 `evidence_score=0` 拦截）
- [x] 建立 vLLM / SGLang / TensorRT-LLM 公平 benchmark 表（骨架：[[推理Serving公平Benchmark表]]，数字待实测）
- [x] 每周 Top5 信号晋升规范（[[每周Top5信号晋升规范]]）

## 迁移约束

旧内容不批量删除。先生成预览和统计，经人工确认后再移动、合并或删除。