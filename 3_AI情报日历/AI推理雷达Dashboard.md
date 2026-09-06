---
created: 2026-09-06
updated: 2026-09-06
type: dashboard
status: active
tags: [AI推理, radar, dashboard]
---
# AI 推理雷达

## 待核验信号
~~~dataview
TABLE discovered, topic, evidence_score, overall_score, primary_source
FROM "3_AI情报日历/Inbox/InferenceRadar"
WHERE type = "inference-signal" AND (status = "candidate" OR status = "blocked")
SORT overall_score DESC, discovered DESC
~~~

## P0 / P1
~~~dataview
TABLE date, topic, evidence_score, overall_score, confidence, decision
FROM "3_AI情报日历/Inbox/InferenceRadar"
WHERE type = "inference-signal" AND evidence_score >= 2 AND overall_score >= 3.2
SORT overall_score DESC, date DESC
~~~

## 每周复盘
- 什么变化真正改变了性能或成本边界？
- 哪项结论只有厂商自测？
- 哪个信号应进入复现或课题？
- 哪个热门话题应因证据不足降级？