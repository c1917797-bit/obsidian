---
type: tech-event
event_type: runtime_feature
entity: arXiv cs.MA (Multiagent Systems)
entity_type: project
tech_categories: agent_runtime, multi_agent
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-18T13:56:12
created: 2026-06-19T10:39:22.910647
tags: [AI-Intelligence, Event, arXiv cs.MA (Multiagent Systems)]
---

# Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs

## 基本信息

- **实体**: arXiv cs.MA (Multiagent Systems)
- **类型**: runtime_feature
- **技术分类**: agent_runtime, multi_agent
- **重要性**: P1
- **阶段**: emerging

## 摘要

We present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test evaluation strategy. Phoenix decomposes the work across six specialized agents. Planner, reproducer, coder, tester, failure analyst and Pull Request (PR) agent, all coordinated by a label-based GitHub webhook state machine. Every change is checked against a baseline test run before a pull request is opened. On a 24-instance slice of SWE-bench Lite. run on the production webhook path, Phoenix oracle-resolves 75% of instances with no pass-to-pass regressions on successful runs; this curated slice is not directly comparable to full-split leaderboard results, and we discuss the limits of the comparison. A complementary pilot on 42 real issues across 14 repositories yields 100% correctness preservation (CP; mean 122s on the hard tier). Manual inspection shows that about half of the resulting pull requests are w

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.20243v1

## 来源

arXiv cs.MA (Multiagent Systems)

---
**Event ID**: b04487ac1734b7f6
**Heat Score**: 0.0
**Novelty Score**: 0.0
