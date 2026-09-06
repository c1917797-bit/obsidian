# 多卡协同推理KV Cache瓶颈与通信瓶颈业界进展

> 基于Obsidian信息源整理（2026年最新动态）

---

## 一、KV Cache跨卡瓶颈业界进展

### 核心问题
多卡场景下KV Cache面临三大跨卡难题：
1. **KV迁移**：跨卡/跨节点KV传输延迟高
2. **KV一致性**：分布式KV状态同步困难
3. **KV共享**：共享前缀的高效跨卡复用

---

### 论文进展

#### 1. DéjàVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving
| 属性 | 内容 |
|------|------|
| **会议** | ICML 2024 |
| **ID** | AbGbGZFYOD |
| **作者** | Foteini Strati, Sara McAllister, Amar Phanishayee, Jakub Tarnawski, Ana Klimovic (ETHZ, CMU, Microsoft) |
| **链接** | https://openreview.net/forum?id=AbGbGZFYOD |
| **核心贡献** | KV Cache Streaming + Prompt-Token解聚 + Microbatch Swap + 状态复制容错 |

```bibtex
@inproceedings{strati2024djvu,
title={D\'ej\'aVu: {KV}-cache Streaming for Fast, Fault-tolerant Generative {LLM} Serving},
author={Foteini Strati and Sara McAllister and Amar Phanishayee and Jakub Tarnawski and Ana Klimovic},
booktitle={Forty-first International Conference on Machine Learning},
year={2024},
url={https://openreview.net/forum?id=AbGbZFYOD}
}
```

---

#### 2. HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | Cs6MrbFuMq |
| **作者** | Youhe Jiang, Ran Yan, Binhang Yuan (Cambridge, HKUST) |
| **链接** | https://openreview.net/forum?id=Cs6MrbFuMq |
| **核心贡献** | 异构GPU上PD分离部署，KV通信效率优化，Graph Partitioning+Max-flow联合优化 |

```bibtex
@inproceedings{jiang2025hexgen,
title={HexGen-2: Disaggregated Generative Inference of {LLM}s in Heterogeneous Environment},
author={YOUHE JIANG and Ran Yan and Binhang Yuan},
booktitle={The Thirteenth International Conference on Learning Representations},
year={2025},
url={https://openreview.net/forum?id=Cs6MrbFuMq}
}
```

---

### 框架进展（2026年）

#### TensorRT-LLM
| 功能 | 说明 | 效果 |
|------|------|------|
| **FlexKV** | KV Cache优化 | 提升多卡场景KV效率 |
| **KV cache reuse probing** | 精确KV块哈希 | 识别可复用KV块 |
| **KV cache manager v2** | Python收发器更新 | 支持分布式KV管理 |
| **Disaggregated serving** | PD分离 + block reuse | 混合模型支持 |
| **Ring Attention** | 跨卡注意力 | 长上下文扩展 |

#### SGLang
| 功能 | 说明 | 效果 |
|------|------|------|
| **Chunked Pipeline Parallelism** | 分块流水线并行 | 百万token上下文近线性扩展 |
| **Context Parallelism** | 上下文并行 (CP) | Fused MoE + Multi-batch + FP8 KV |
| **EPD Disaggregation** | Elastic Encoder PD分离 | 视觉语言模型弹性扩展 |
| **Cache-aware routing** | 前缀缓存感知路由 | 10-12x更快，99%内存降低 |

---

## 二、通信瓶颈业界进展

### 核心问题
多卡场景通信瓶颈根因：
- **AllReduce/AllToAll**：MoE Expert路由导致通信爆炸
- **TP同步**：跨卡Tensor Parallelism同步延迟高
- **RDMA瓶颈**：跨节点带宽不足
- **计算-通信重叠不足**：GPU等待通信

---

### 论文进展

#### 1. DeepEP: DeepSeek MoE通信库
| 属性 | 内容 |
|------|------|
| **来源** | DeepSeek开源库 |
| **链接** | https://github.com/deepseek-ai/DeepEP |
| **核心贡献** | All-to-All MoE dispatcher，优化的专家并行通信 |

#### 2. Ulysses / SP (DeepSpeed)
| 功能 | 说明 |
|------|------|
| **Ulysses** | 用于长上下文注意力的并行通信 |
| **AutoSP** | DeepSpeed自动并行优化 |
| **Universal Checkpoint** | AutoTP支持 |

---

### 框架进展（2026年）

#### SGLang / vLLM通信优化
| 功能 | 说明 | 效果 |
|------|------|------|
| **Flashinfer All-to-All MoE Dispatcher** | 高效MoE专家并行通信 | SGLang #14668 |
| **LoRA Weight Loading Overlap** | LoRA权重加载与计算重叠 | TTFT降低~78%, TPOT降低~34.88% |

#### TensorRT-LLM通信优化
| 功能 | 说明 | 效果 |
|------|------|------|
| **TRT-LLM NSA Kernel** | DeepSeek V3.2原生稀疏注意力 | Blackwell平台3-5x加速 |
| **Fused All-Reduce + Norm** | 通信与归一化融合 | Nemotron-H优化 |
| **Dynamic SMEM Block Routing** | MoE动态共享内存路由 | 通信开销降低 |
| **Safe AllGather with Chunking** | 分块安全AllGather | 大模型通信优化 |
| **CuTe DSL single-pass multi-CTA cluster top-k** | 高效Top-K通信 | MoE通信加速 |

#### DeepSpeed通信优化
| 功能 | 说明 |
|------|------|
| **Zero3 Defragmentation** | 减少通信碎片 |
| **Overlap-comm buffer lifetimes** | 通信计算重叠优化 |

---

## 三、关键趋势总结

| 瓶颈 | 核心解法 | 代表进展 |
|------|----------|----------|
| **KV跨卡迁移** | PD分离 + Streaming | DéjàVu, HexGen-2 |
| **KV共享复用** | 前缀缓存 + 块哈希 | TRT-LLM FlexKV, SGLang CP |
| **通信爆炸** | 计算-通信重叠 + 融合 | DeepEP, NSA Kernel |
| **通信墙** | 拓扑感知调度 + RDMA | DeepSpeed Ulysses, SGLang |
| **异构环境** | 图划分 + Max-flow | HexGen-2 |

---

## 四、北极星指标

$$\text{Runtime有效算力ROI} = \frac{\text{稳态有效Token吞吐量} \times \text{Agent会话成功率}}{\text{GPU算力成本} + \text{分布式通信损耗成本} + \text{内存Swap损耗成本}}$$

---

*整理自Obsidian信息源 - 2026-06-01*
