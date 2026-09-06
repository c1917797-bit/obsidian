---
created: 2026-09-06
updated: 2026-09-06
type: source-registry
status: active
tags: [AI推理, 一手信源, radar]
---
# AI 推理一手信源清单

目标：优先发现改变推理性能、成本、架构或产品决策的信号。媒体和聚合站只用于发现线索，正式结论必须回到一手来源。

## P0 每日增量

|方向|来源|入口|检查对象|
|---|---|---|---|
|Serving|vLLM|https://github.com/vllm-project/vllm|Release、关键 PR、RFC、benchmark|
|Serving|SGLang|https://github.com/sgl-project/sglang|Release、性能 PR、runtime 设计|
|Serving|TensorRT-LLM|https://github.com/NVIDIA/TensorRT-LLM|Release、benchmark、kernel|
|端侧|llama.cpp|https://github.com/ggml-org/llama.cpp|Release、量化、后端性能|
|Kernel|FlashAttention|https://github.com/Dao-AILab/flash-attention|Release、论文、性能|
|Distributed|DeepSpeed|https://github.com/deepspeedai/DeepSpeed|Inference、FastGen|
|Distributed|Megatron-LM|https://github.com/NVIDIA/Megatron-LM|TP、PP、EP、MoE|
|Cache|LMCache|https://github.com/LMCache/LMCache|KV 复用、分层缓存|
|Cache|Mooncake|https://github.com/kvcache-ai/Mooncake|KVCache、分离式推理|
|MoE|DeepEP|https://github.com/deepseek-ai/DeepEP|低延迟通信|
|论文|arXiv|https://arxiv.org/|cs.DC、cs.PF、cs.LG、cs.CL|
|论文|OpenReview|https://openreview.net/|ICLR、MLSys|
|Benchmark|MLPerf Inference|https://mlcommons.org/benchmarks/inference-datacenter/|标准推理成绩|
|芯片|NVIDIA Developer|https://developer.nvidia.com/blog|CUDA、TensorRT、Blackwell|
|芯片|AMD ROCm|https://rocm.blogs.amd.com/|ROCm、MI、kernel|
|软件栈|PyTorch|https://pytorch.org/blog/|Inductor、TorchAO|
|实验室|DeepSeek|https://github.com/deepseek-ai|报告、kernel、通信|
|实验室|Meta AI|https://ai.meta.com/research/|Llama 推理系统|
|实验室|Google Research|https://research.google/|TPU、XLA、JAX|
|国产栈|MindSpore|https://gitee.com/mindspore|昇腾推理栈|

## P1 每周

MLSys、OSDI、SOSP、ASPLOS、ISCA、MICRO、HPCA、EuroSys、NeurIPS、ICML，以及 AWS Trainium/Inferentia、Intel oneAPI、Google TPU、华为昇腾/CANN。

## 只作线索

Hugging Face Daily Papers、媒体、Twitter/X、Reddit、a16z。它们不能单独支撑“突破”“显著提升”或选型结论。

## 固定主题

Serving；Kernel；Memory/KV Cache；Compression；Distributed/MoE；Hardware economics。

只有包含原始 URL、日期或版本、精确 claim、实验条件和证据评分的条目，才能晋升。