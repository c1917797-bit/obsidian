# obsidian-repo

本仓库用于保存 Obsidian 中可复用的 AI 情报工作台内容，便于与 Codex 对接、版本化和后续维护。

## 已同步内容
- `0_Codex工作台/`：对接说明与工具脚本（含 `tools/`）
- `3_AI情报日历/`：情报雷达与卡片

## 每日检查命令（来自 `0_Codex工作台/tools`）
```powershell
pwsh .\0_Codex工作台\tools\inference-audit.ps1 scan
pwsh .\0_Codex工作台\tools\inference-audit.ps1 report
```

- `scan` 输出统计（TOTAL/BAD/STALE/DUPLICATE）
- `report` 生成/更新 `3_AI情报日历\Inbox\InferenceRadar\问题清单.md`

## 维护建议（围绕一手 AI 推理信息）
1. 新建雷达卡必须保留 frontmatter：
   `type/date/discovered/source_type/primary_source/topic/status/evidence_score/overall_score/confidence/decision`
2. `primary_source` 必须可直接复核（优先官方 release note / paper / code）
3. 将 `status` 与 `decision` 先保持为 `candidate / verify`，待证据齐全后改为 `approved/ignore` 等
4. 每周运行一次 `scan`，把 BAD 条目清单修复后再向下游输出洞察

## 推送更新
1. 本地修改后直接在 `obsidian-repo` 提交
2. `git add . && git commit -m "chore: update inference radar"`
3. `git push origin main`

## 推荐同步范围（精简）

为了减少噪音，建议日常主要维护同步这两部分：

- `0_Codex工作台/tools/`
- `3_AI情报日历/Inbox/InferenceRadar/`

示例：

```powershell
robocopy "C:\Users\Huawei\Documents\code\Obsidian\0_Codex工作台\tools" \
  "C:\Users\Huawei\Documents\code\obsidian-repo\0_Codex工作台\tools" /MIR

robocopy "C:\Users\Huawei\Documents\code\Obsidian\3_AI情报日历\Inbox\InferenceRadar" \
  "C:\Users\Huawei\Documents\code\obsidian-repo\3_AI情报日历\Inbox\InferenceRadar" /MIR
```

## GitHub Action（当前状态）

- 已添加工作流：`.github/workflows/inference-audit-ci.yml`
- 行为：
  - 每日 02:00 UTC 自动运行（及 `workflow_dispatch` 手动运行）
  - 执行 `scan`，若 BAD>0 则 fail
  - 生成 `问题清单.md` 到本仓库目录，并上传为 Artifact
- 说明：当前版本**不自动提交**，仅做检查和归档，避免误改仓库。

如果你确认接受“自动提交”风险，可再给我一个明确确认，我再给你加一版“带写权限自动提交”的 CI（已单独隔离配置）。

## 每日/每周简报

- 生成今日简报（按 `discovered` 日期）
  - `pwsh .\0_Codex工作台\tools\inference-radar.ps1 digest`
- 生成本周简报（按 `status` 与分数过滤）
  - `pwsh .\0_Codex工作台\tools\inference-radar.ps1 digest -Window week -Status verify -MinOverall 2`

## 自动提交工作流（主干）

新增 `inference-audit-autocommit-ci.yml`（与默认只检查流程并行）：

- 触发：`workflow_dispatch`、`push` 到 `main`、每天 UTC 03:00 的定时任务
- 行为：先执行 `scan`，当 `BAD=0` 时生成/更新 `问题清单.md`，有变更则由 `github-actions[bot]` 提交并推送
- 约束：`BAD>0` 时直接 fail，不提交，避免把未达标内容写入主干
- 适合场景：你希望仓库里的 `问题清单.md` 始终保持自动同步最新状态

### 每周归档（周末）

自动提交工作流会在周末（UTC 时间的周六/周日）额外执行归档：
- 复制 `问题清单.md` 到 `3_AI情报日历/Inbox/InferenceRadar/问题清单_归档/问题清单_周报_YYYY-MM-DD.md`
- 与日报同步一起提交，便于周报回溯和比对历史节奏。
## 每周周报提醒（仅通知）

新增 `inference-audit-weekly-reminder.yml`（不推送、不提交）：

- 触发：每周一 UTC 05:00 + `workflow_dispatch`
- 行为：按 `digest -Window week -Status verify -MinOverall 2` 生成“可复核高优先”周报，
  用“卡片”结构展示高优先项（支持快速扫描与复核）。
- 周期：按上周 `Monday ~ Sunday (UTC)` 自动计算，并在 Step Summary 中显示窗口。
- 输出：
  - 上传为 GitHub Artifact（文件名包含周起止日期：`inference-weekly-reminder-YYYYMMDD-YYYYMMDD`）
  - Step Summary 提供高优先事项卡片 + 前 30 行原文预览。
- 失败兜底：若日报生成失败，会在 Step Summary 打印失败告警，避免静默漏报。
