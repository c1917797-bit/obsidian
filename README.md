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
