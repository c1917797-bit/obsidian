---
created: 2026-09-06
updated: 2026-09-06
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
- [ ] 恢复每日采集，并记录 last_seen / fetched_at / source_published
- [ ] 将 449 篇旧 Inbox 分为推理相关、非推理、重复、低证据四组
- [ ] 核验“必检论文”清单的论文身份、arXiv ID、录用状态
- [ ] 为旧论文卡补 primary_source、代码、硬件和 benchmark 条件
- [ ] 清理已确认的完全重复论文卡
- [ ] 禁止 0 证据报告进入正式洞察
- [ ] 建立 vLLM / SGLang / TensorRT-LLM 公平 benchmark 表
- [ ] 每周只晋升 Top 5 信号，并记录为什么其他信号被淘汰

## 迁移约束

旧内容不批量删除。先生成预览和统计，经人工确认后再移动、合并或删除。