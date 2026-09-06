---
type: tech-event
event_type: research_paper
entity: arXiv cs.LG
entity_type: project
tech_categories: research, architecture
importance: P1
confidence: 0.6
stage: emerging
date: 2026-06-02T17:36:06
created: 2026-06-03T15:53:35.723115
tags: [AI-Intelligence, Event, arXiv cs.LG]
---

# MLSkip: Data Skipping for ML Filters via Lightweight Metadata

## 基本信息

- **实体**: arXiv cs.LG
- **类型**: research_paper
- **技术分类**: research, architecture
- **重要性**: P1
- **阶段**: emerging

## 摘要

Database vendors recently released AI functions that can be used in filter predicates. As such functions often rely on costly, black-box ML models, they unveil new data management challenges. Concretely, traditional data skipping techniques for integer and string data fail to be applicable to the new filter type. Indeed, there is no known mechanism for pruning non-qualifying row groups, e.g., when reading files from blob storage.
  In this work, we initiate the study of data skipping techniques for ML filters. We make the case that Parquet's default min-max metadata is enough to enable pruning. To this end, we draw connections to two lines of research: (i) the recently proposed query language for ML models and (ii) neural network verification.
  Our preliminary results on ReLU architectures show that on tables from TPC-H and TPC-DS, the average pruning effectiveness for filters of selectivity below 0.1% amounts to 27.4%. Finally, inspired by research on spatial joins, we propose an enh

## 创新点

未知

## 解决的问题

未知

## 原始链接

https://arxiv.org/abs/2606.03946v1

## 来源

arXiv cs.LG

---
**Event ID**: 1826022ea5010c8f
**Heat Score**: 0.0
**Novelty Score**: 0.0
