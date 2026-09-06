---
created: 2026-09-06
updated: 2026-09-06
type: research-agenda
status: active
tags: [AI推理, research-agenda]
---
# AI 推理关键问题清单

1. Prefill/decode 分离在什么并发、网络和上下文下真正占优？
2. KV 压缩节省的显存能否转化为端到端吞吐？
3. 投机解码在不同模型、温度、batch 和负载下的接受率与尾延迟如何？
4. MoE 推理何时从计算瓶颈转为 all-to-all 通信瓶颈？
5. FP8、INT8、INT4 在不同硬件上的单位 Token 成本和质量损失如何？
6. vLLM、SGLang、TensorRT-LLM 的公平同条件比较是什么？

完成条件：至少两个一手来源；至少一个复现实验或标准 benchmark；明确硬件、模型、版本、负载和质量约束；形成可证伪结论；给出观察、复现、投入或停止建议。

泛 Agent、融资新闻和无推理机制细节的产品发布不进入本清单。