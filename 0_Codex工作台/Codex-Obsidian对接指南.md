---
created: 2026-09-06
updated: 2026-09-06
type: guide
status: active
tags: [codex, obsidian, workflow]
---

# Codex × Obsidian 对接指南

Obsidian 保存长期知识，Codex 负责检索、研究、整理和质量检查。默认流程：先检索 → 生成到 Inbox → 校验 → 人工确认后归档。

## 一句话用法

- `搜索我的 Obsidian 中关于 <主题> 的内容，列出证据和双链。`
- `把 <链接/文件/内容> 整理为 Obsidian 笔记，先放 Codex Inbox。`
- `汇总 <日期范围> 的 Daily 和相关洞察，生成周报草稿并标注来源双链。`
- `检查 Inbox 中的 <笔记>，只给出归档、合并和补链建议，等我确认。`

## 可重复工具

```powershell
powershell -File "0_Codex工作台/tools/obsidian-codex.ps1" status
powershell -File "0_Codex工作台/tools/obsidian-codex.ps1" search -Query "KV Cache"
powershell -File "0_Codex工作台/tools/obsidian-codex.ps1" recent -Limit 20
powershell -File "0_Codex工作台/tools/obsidian-codex.ps1" new -Title "主题名称" -Source "来源链接或路径"
powershell -File "0_Codex工作台/tools/obsidian-codex.ps1" validate -Path "0_Codex工作台/Inbox/主题名称.md"
```

## 知识路由

- `1_AI情报溯源`：信源和筛选规则。
- `2_AI情报织网`：实体关系、趋势关联和流水线。
- `3_AI情报日历`：按日、周、月组织的时序记录。
- `4_AI情报洞察`：技术与产业综合判断。
- `5_学术研究织网`：论文、论证、方法和研究完整性。
- 无法确定时：留在 [[0_Codex工作台/Inbox/收件箱说明|Codex Inbox]]。

新笔记必须区分来源事实、Codex 分析、待验证问题，并补充关联双链。密码、令牌和私钥不得写入知识库。

相关入口：[[0_Codex工作台/首页]] · [[0_Codex工作台/任务模板]] · [[📋_目录导航]]

## 推理开源项目增量监控

首次建立基线：
powershell -File "0_Codex工作台/tools/sync-inference-github.ps1" baseline

后续检查新 Release：
powershell -File "0_Codex工作台/tools/sync-inference-github.ps1" sync

首次运行不会创建历史情报；后续只有版本变化才会生成候选信号卡。
