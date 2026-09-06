---
type: tech-event
event_type: runtime_feature
entity: HuggingFace Papers
entity_type: project
tech_categories: agent_runtime, memory
importance: P1
confidence: 0.6
stage: emerging
date: 2026-07-05T13:40:19.957719
created: 2026-07-05T13:44:32.174069
tags: [AI-Intelligence, Event, HuggingFace Papers]
---

# AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents

## 基本信息

- **实体**: HuggingFace Papers
- **类型**: runtime_feature
- **技术分类**: agent_runtime, memory
- **重要性**: P1
- **阶段**: emerging

## 摘要

Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded across runs of any length, and any single layer can be ablated in isolation. We instantiate the contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require hundreds of tactical and strategic decisions. A public online benchmark of frontier LLMs on the same game reports zero wins at the lowest difficulty across five configurations, and the developer-reported human win rate at the same difficulty is 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://huggingface.co/papers/2607.02255

## 来源

HuggingFace Papers

---
**Event ID**: 50e45f8180d349ea
**Heat Score**: 0.0
**Novelty Score**: 0.0
