---
type: tech-event
event_type: runtime_feature
entity: MachineLearning
entity_type: project
tech_categories: agent_runtime, tool_use
importance: P1
confidence: 0.6
stage: emerging
date: 2026-07-05T07:49:09
created: 2026-07-05T13:44:32.226289
tags: [AI-Intelligence, Event, MachineLearning]
---

# Competence Gate: gating tool-use on a small model's internal confidence signal instead of its verbalised one — Qwen3.5-4B, open weights [P]

## 基本信息

- **实体**: MachineLearning
- **类型**: runtime_feature
- **技术分类**: agent_runtime, tool_use
- **重要性**: P1
- **阶段**: emerging

## 摘要

I made a 10MB LoRA adapter for Qwen3.5-4B plus a small orchestration layer. It decides, per query, whether to answer directly, search the web, or retrieve from your own local documents and it refuses to make things up when it can't verify an answer. It runs locally (Apple Silicon / MLX, with a GGUF build for llama.cpp/Ollama). Basically small instruct models are poor at telling users how confident they really are. They can't verbalise it and tend to say they are confident for everyhting. In my past research I tested seven 3-9b models and they all hit a confidence ceiling. But the information is there in the internal activations. The adapter reads the internal signal directly and gates tool use on it. The main elements are that: - it catches its own errors better than the base model's tool calling (d′ improvement of 0.46 (95% CI [0.01, 0.89])). Of the cases the gate flagged that the base model didn't, 87% were genuinely wrong answers. - it is less likely to leak your private queries to 

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/

## 来源

Reddit r/MachineLearning

---
**Event ID**: 53c7b6a12c0ae663
**Heat Score**: 0.0
**Novelty Score**: 0.0
