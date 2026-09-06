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
2. `git add . && git commit -m "chore: update inference radar`n3. `git push origin main`
