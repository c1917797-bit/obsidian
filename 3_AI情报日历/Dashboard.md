---
type: dashboard
title: AI 情报看板
created: 2026-06-03
tags: [AI-Intelligence, Dashboard]
---

# AI 情报看板

> 提供快速检索视图，支持按日期、类型、标签过滤报告

---

## 最新日报

```dataview
TABLE date, type, tags
FROM "3_AI情报日历/Daily"
WHERE type = "daily-report"
SORT date DESC
LIMIT 10
```

---

## 本周报告

```dataview
TABLE period, type, tags
FROM "3_AI情报日历"
WHERE date >= 2026-06-01
SORT date DESC
LIMIT 20
```

---

## 论文洞察 (最新)

```dataview
TABLE date, venue, relevance_score, citekey
FROM "4_AI情报洞察/论文洞察/Daily"
WHERE type = "paper-card"
SORT date DESC
LIMIT 15
```

---

## 按标签检索

### KV Cache 相关

```dataview
TABLE date, venue, relevance_score
FROM "4_AI情报洞察/论文洞察/Daily"
WHERE type = "paper-card" AND contains(tags, "KV Cache")
SORT relevance_score DESC
```

### Agent 相关

```dataview
TABLE date, venue, relevance_score
FROM "4_AI情报洞察/论文洞察/Daily"
WHERE type = "paper-card" AND contains(tags, "Agent")
SORT relevance_score DESC
```

### 推理优化

```dataview
TABLE date, venue, relevance_score
FROM "4_AI情报洞察/论文洞察/Daily"
WHERE type = "paper-card" AND contains(tags, "Latency")
SORT relevance_score DESC
```

---

## 问题空间分布

```dataview
TABLE length(file.etags) as tag_count
FROM "4_AI情报洞察/论文洞察/Daily"
WHERE type = "paper-card"
GROUP BY file.folder
```

---

## 统计

- 日报数量：

```dataview
TABLE length(filter(rows, r => r.type = "daily-report")) as count
FROM "3_AI情报日历/Daily"
GROUP BY ""
```

- 论文洞察数量：

```dataview
TABLE length(filter(rows, r => r.type = "paper-card")) as count
FROM "4_AI情报洞察/论文洞察/Daily"
GROUP BY ""
```

---

## 🧭 学术研究织网 (ARS)

> 基于 Academic Research Skills v3.10 的研究流程
> 支持 Socratic 对话、Integrity Gates、Claim-Faithfulness 审计

### 研究项目进度

```dataview
TABLE project_name, stage, verification_status, ars_mode, updated
FROM "5_学术研究织网/研究项目"
WHERE type = "material-passport"
SORT updated DESC
LIMIT 10
```

### 阶段分布

```dataview
TABLE WITHOUT ID
  stage AS "当前阶段",
  length(rows) AS "项目数"
FROM "5_学术研究织网/研究项目"
WHERE type = "material-passport"
GROUP BY stage
```

### Integrity Gates 状态

```dataview
TABLE stage, mode_1_status, mode_2_status, mode_3_status, block_status, created
FROM "5_学术研究织网/整合检查"
WHERE type = "integrity-gate"
SORT created DESC
LIMIT 5
```

### 活跃 Socratic 对话

```dataview
TABLE project, intent, layer_name, dialogue_turn_count, dialogue_health, status
FROM "5_学术研究织网/对话日志"
WHERE type = "socratic-dialogue"
WHERE status = "in-progress"
SORT last_updated DESC
LIMIT 5
```

### 对话健康警告

```dataview
TABLE project, intent, dialogue_turn_count, health_alerts
FROM "5_学术研究织网/对话日志"
WHERE type = "socratic-dialogue"
WHERE dialogue_health = "critical" OR dialogue_health = "warning"
SORT last_updated DESC
```

### 文献语料库状态

```dataview
TABLE WITHOUT ID
  pre_screened_status AS "状态",
  length(rows) AS "数量"
FROM "4_AI情报洞察/论文洞察/_corpus"
GROUP BY pre_screened_status
```

### Claim 审计进度

```dataview
TABLE project, audit_status, claims_total, claims_verified, claims_failed, high_warn_count
FROM "5_学术研究织网/claim_audit"
WHERE type = "claim-tracking"
SORT created DESC
LIMIT 5
```

### HIGH-WARN Claims

```dataview
TABLE project, claim_id, high_warn_category, audit_status
FROM "5_学术研究织网/claim_audit"
WHERE type = "claim-tracking"
WHERE high_warn_count > 0
SORT project ASC
```

### 协作深度分布

```dataview
TABLE WITHOUT ID
  zone AS "协作区域",
  length(rows) AS "记录数"
FROM "5_学术研究织网/研究项目"
WHERE type = "collaboration_record"
GROUP BY zone
```

### 模式使用统计

```dataview
TABLE WITHOUT ID
  ars_mode AS "研究模式",
  length(rows) AS "使用次数"
FROM "5_学术研究织网/研究项目"
WHERE type = "material-passport"
GROUP BY ars_mode
SORT "使用次数" DESC
```

---

*Dashboard 扩展: ARS Integration v1.0 | 2026-06-03*
