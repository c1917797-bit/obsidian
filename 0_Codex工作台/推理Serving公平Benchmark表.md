---
created: 2026-09-11
updated: 2026-09-11
type: reference
status: active
tags: [codex, benchmark, serving, vllm, sglang, tensorrt-llm]
---

# 推理 Serving 公平 Benchmark 表

> 用途：vLLM / SGLang / TensorRT-LLM 三框架在**同一模型、同一硬件、同一精度、同一 batch/context** 下的横向对比。数字必须来自实测，禁止搬论文/README 声称值。

## 公平对比前提（不满足则数字不可比）

- 同一模型权重 + 同一精度（BF16/FP8/W8A8 各列分开）
- 同一硬件（Ascend 910B4 / TP4 或指定 GPU）
- 同一 prompt 集（含长/短、中文/代码混合）
- 同一 batch 与 context 区间（c1 / c5 / c8 / c16 各分列）
- 区分 **冷启动 / 热启动**，区分 **prefill-bound / decode-bound**
- 记录框架版本、CANN/CUDA 版本、driver、commit SHA

## 统一指标定义

| 指标 | 定义 | 备注 |
|---|---|---|
| TTFT (P50/P95/P99) | 首 token 时延 | prefill 主导 |
| TPOT (P50/P95/P99) | 每 token 时延（decode） | 逐 token 均值 |
| Throughput (tok/s) | 稳态输出吞吐 | 需标注并发档 |
| Peak Memory | 峰值显存/HBM | 含 KV 池 |
| Quality delta | 与 BF16 基线输出对比 | 零回退要求时必测 |

## 对比表（空骨架，实测后填写）

| 框架 | 精度 | c1 TTFT P95 | c16 TTFT P95 | c1 TPOT P95 | c16 TPOT P95 | 吞吐(c16) | 峰值显存 | 质量回退 |
|---|---|---|---|---|---|---|---|---|
| vLLM | BF16 | | | | | | | |
| SGLang | BF16 | | | | | | | |
| TensorRT-LLM | BF16 | | | | | | | |

## 备注

- 昇腾侧 vLLM-Ascend / MindIE 可作第 4 列补充，但单独标出，不混入三框架主表。
- 每次重跑记录 `benchmark run` 的 SHA256 与原始 log，见 [[0_Codex工作台/工作区协作约定]] 的质量门禁要求。
