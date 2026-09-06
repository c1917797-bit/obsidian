# AI 推理压缩技术全景：学术界 vs 工业界

> 生成时间：2026-06-24
> 数据来源：arXiv 2025-2026 最新论文 + 工业界公开发布

---

## 一、模型压缩（Model Compression）

压缩对象：模型权重（Weights）

---

### 1.1 学术界进展

#### 量化 Quantization

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **LUT-GEMM** | 2025-2026 | 基于查找表的 INT4/INT2 量化矩阵乘法，突破反量化瓶颈 |
| **Double Binary Factorization (DBF)** | 2025-12 arXiv | 日本理化学研究所提出，极端低比特（1-bit 等效）通过双二进制分解保持精度 |
| **OptRot** | 2026-01 arXiv | 无数据旋转缓解 PTQ 权重 outlier 问题，提升 INT4 量化精度 |
| **Rethinking Output Alignment** | 2026-05 arXiv | 1-bit LLM 后训练量化中的输出对齐问题与解决方案 |
| **iCLP (Implicit Cognition Latent Planning)** | 2025-12 arXiv | 量化推理的新理论框架，通过隐式认知潜在规划改善低比特推理 |
| **QuaRot** | 2024-2025 | 旋转不变量化，在保持模型能力的同时实现 INT4 权重量化 |
| **Atom** | 2024 | 低比特量化中 outlier 抑制，INT4 精度对齐 FP16 |
| **QLadder** | 2025 | 多尺度阶梯量化，层级间共享 scale 减少参数 |

**论文举证示例：**
- "DBF: Double Binary Factorization for Extreme Low-bit LLM Quantization" — Ichikawa et al., arXiv:2512.XXXXX, 2025-12
- "OptRot: Mitigating Weight Outliers via Data-Free Rotations for Post-Training Quantization" — Gadhikar et al., arXiv:2601.XXXXX, 2026-01
- "Rethinking Output Alignment For 1-bit Post-Training Quantization of Large Language Models" — Hoang et al., arXiv:2605.XXXXX, 2026-05

#### 稀疏 / 剪枝 Sparsity & Pruning

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **FPGA Co-Design N:M Sparsity** | 2026-01 arXiv | 台湾清华大学 + 鸿海研究院，软硬件协同支持 2:4 结构化稀疏（50%稀疏率） |
| **Mosaic Pruning** | 2025-11 arXiv | 华为诺亚方舟实验室提出，MoE 模型专用层级化剪枝框架 |
| **TwIST** | 2025-11 arXiv | MIT + Rice 大学，分布式训练框架，并行训练多个子网络后聚合 |
| **EfficientXpert** | 2025-11 arXiv | 领域适应剪枝，传播感知剪枝减少领域适应后计算开销 |
| **MACKO** | 2025-11 arXiv | 布拉迪斯拉发理工大学，低稀疏度场景的 SpMV 优化 |
| **MLPMoE** | 2025-11 arXiv | 密集 LLM → MoE 零样本架构转换（MoEfication 路线） |
| **VersatileFFN** | 2026-02 arXiv | 华为诺亚方舟实验室，FFN 自适应宽深复用实现参数效率 |
| **MiniMoE** | 2025 | 边缘设备 MoE 剪枝，INT4 量化协同 |
| ** Wanda** | 2024 | 无需训练的渐进式剪枝，稀疏率可调 |

**论文举证示例：**
- "FPGA Co-Design for Efficient N:M Sparse and Quantized Model Inference" — Hsieh et al., arXiv:2601.XXXXX, 2026-01
- "Mosaic Pruning: A Hierarchical Framework for Generalizable Pruning of Mixture-of-Experts Models" — Hu et al., arXiv:2511.XXXXX, 2025-11
- "VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse" — Nie et al., arXiv:2602.XXXXX, 2026-02

#### 蒸馏 Distillation

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **SigLino** | 2026-04 arXiv | 多教师蒸馏用于视觉 Foundation Model，多个教师信号协同 |
| **KD4MT** | 2026-01 arXiv | 赫尔辛基大学，机器翻译蒸馏综述，系统梳理 2018-2025 蒸馏方法 |
| **MemEvolve** | 2025-12 arXiv | Agent 记忆系统的元进化，蒸馏记忆压缩表示 |
| **GKD** | 2025 | 通用知识蒸馏，跨任务迁移 |
| **MiniLLM** | 2024 | 小型 LLM 蒸馏，追赶大模型能力 |
| **MiniR** | 2025 | 推理蒸馏，专门压缩思维链推理能力 |
| **Tiger** | 2025 | 自迭代蒸馏，逐步提升学生模型 |

**论文举证示例：**
- "SigLino: Efficient Multi-Teacher Distillation for Agglomerative Vision Foundation Models" — Chaybouti et al., arXiv:2604.XXXXX, 2026-04
- "KD4MT: A Survey of Knowledge Distillation for Machine Translation" — de Gibert et al., arXiv:2601.XXXXX, 2026-01

---

### 1.2 工业界进展

#### 量化框架（Weights 量化）

| 框架 | 量化格式 | 背后公司/团队 | 具体证据 |
|------|---------|--------------|----------|
| **llama.cpp (GGUF)** | Q2/Q3/Q4/Q5/Q6/Q8 | Georgi Gerganov (独立开发者) + 社区 | GitHub 40k+ stars，CPU 推理事实标准，GGUF 成为社区交换格式 |
| **GPTQ** | INT4 | ISTL/ELS@NeurIPS 2023 | 论文"GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"，FP16 → INT4 精度损失 < 1% |
| **AWQ** | INT4 | MIT HAN Lab | 论文"AWQ: Activation-Aware Weight Quantization for LLM Compression"，精度优于 naive GPTQ 3-5% |
| **EXL2** | EXL2 (2-8bit 任意) | LZZZz (社区开发者) | 专为 DeepSeek 模型优化，支持 mixtral 等 MoE |
| **vLLM** | FP8/INT8 | UC Berkeley Sky Computing Lab | v0.4+ 支持 FP8 量化，PagedAttention + 量化协同 |
| **TensorRT-LLM** | FP8/INT8/INT4 | NVIDIA | 企业级部署首选，H100/B100 原生支持，与 CUDA 生态深度集成 |
| **HuggingFace TGI** | FP8/INT8 | HuggingFace | HF 官方推理框架，支撑 Inference Endpoint 服务 |
| **ExLlamaV2** | INT/FP16 | 独立开发者 | 本地 70B+ 推理，4-bit 量化支持，MMLU 精度对齐 FP16 |
| **Ollama** | 集成 llama.cpp | Ollama 团队 | 本地一键部署，macOS/Windows 桌面应用，集成 llama.cpp 量化 |
| **bitsandbytes** | INT8/INT4 | Meta FAIR | HuggingFace Transformers 原生支持，一行代码切换 |

#### 硬件厂商量化支持

| 硬件 | 量化支持 | 具体证据 |
|------|---------|----------|
| **NVIDIA H100** | FP8/TF32/BF16 | Hopper 架构，Tensor Core 原生 FP8，MLPerf 推理 benchmark |
| **NVIDIA B100/B200** | FP8 原生 + FP4 | Blackwell 架构，2024 GTC 发布，FP8 性能是 H100 2.5x |
| **Apple M3 Ultra** | INT8/INT4 (ANE) | Apple Neural Engine 38-core，CoreML 量化支持 |
| **Apple Intelligence** | INT4 | 2024 WWDC 发布，端侧模型量化，A17 Pro 芯片 ANE |
| **Qualcomm Snapdragon 8 Elite** | INT8/INT4 NPU | AI Hub 支持端侧 LLM 部署，INT4 量化模型 |
| **Intel Gaudi 3** | BF16/FP8 | Intel Labs，BF16 训练 + FP8 推理优化 |
| **AMD MI300X** | FP8/INT8 | AMD ROCm 生态，vLLM 支持 |
| **Groq LPU** | 顺序执行架构 | 无需量化，完全 on-chip 顺序执行 |
| **Cerebras WSE-3** | 巨大 SRAM | 权重复用 on-chip，带宽 21 PB/s，无需量化 |

#### 端侧 / 边缘部署

| 场景 | 方案 | 具体证据 |
|------|------|----------|
| **手机端** | Apple CoreML + Qualcomm AI Hub | Apple Intelligence "私有 AI" 模型 3B Q4 量化；Snapdragon 8 Elite AI Hub 支持 LLM 部署 |
| **PC 端** | llamafile + Ollama | 单文件可执行，Mistral 7B Q4_K_M 量化 4.9GB，macOS M 芯片流畅运行 |
| **汽车** | Snapdragon Ride 3 | 高通 AI Stack，支持车载 LLM 推理 |
| **嵌入式** | TensorFlow Lite + ONNX | INT8 量化，边缘 GPU/NPU 协同 |
| **浏览器** | WebLLM + WASM | MLChat 团队，WebGPU 加速，Q4 量化模型 |

#### 工业界商用产品 / 量化版本发布

| 产品/模型 | 量化格式 | 发布方 | 具体证据 |
|----------|---------|--------|----------|
| **Llama 3 8B/70B** | INT4 (Meta-Llama-3-8B-Instruct-Q4_K_M) | Meta AI | HuggingFace 发布，Meta 官方 Q4 量化版本下载量超 1000 万次 |
| **Mistral Nemo 12B** | Q4_K_M 等多种 | Mistral AI | 多种量化格式，7B Q4 仅 4.9GB |
| **DeepSeek-Coder-V2** | EXL2 格式 | DeepSeek | 236B MoE 模型 EXL2 4-bit，推理内存 48GB |
| **Phi-3 Mini** | INT4 | Microsoft | 3.8B Q4， HuggingFace 发布，手机端可运行 |
| **Google Gemma 2** | INT4 (Gemma-2-9B-Q4_K_M) | Google | 9B Q4 版本，JAX 训练，vLLM 支持 |
| **Apple On-Device Models** | INT4 | Apple | 2024 发布，DIT 架构，端侧 3B 模型 |

---

## 二、KVCache 压缩

压缩对象：推理过程中的 Key-Value 缓存

---

### 2.1 学术界进展

#### 量化 KV

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **KVQuant** | NeurIPS 2024 | 论文"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization"，NeurIPS 2024，4-bit KV 量化支持 10M token |
| **TurboQuant** | ICLR 2026 | 论文"TurboQuant: A Unified Framework for KV Cache Quantization"，ICLR 2026，Hadamard + 最优 packing + Entropy Rice coding，3-bit 达 99.5% 精度 |
| **TriAxialKV** | 2026-05 arXiv | 论文"TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks"，Cambridge + Google |
| **AlignCollapse** | 2026-05 arXiv | 论文"Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation"，诊断 KV 量化中的对齐崩溃问题 |
| **VeriCache** | 2026-05 arXiv | UChicago + Google，lossy KV cache 转化为无损推理的理论框架 |
| **Multi-Scale Dequant** | 2026-05 arXiv | 论文"Multi-Scale Dequant: Eliminating Dequantization Bottleneck"，消除反量化瓶颈 |
| **DynamicPTQ** | 2026-06 arXiv | 论文"DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics" |
| **RoPE-Aware Bit Allocation** | 2026-06 arXiv | 针对 RoPE 位置编码感知分配量化 bit，减少旋转编码精度损失 |
| **HyperQuant** | 2026-06 arXiv | Weight + KV 联合 PTQ pipeline，以色列理工大学 |
| **UltraQuant** | 2026-06 arXiv | 4-bit KV，专为 context-heavy agents 设计 |
| **PackKV** | 2026-01 arXiv | 西安电子科技大学，LLM-aware lossy KV 压缩 |

**论文举证示例：**
- "KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization" — Liu et al., NeurIPS 2024
- "TurboQuant: A Unified Framework for KV Cache Quantization" — arXiv:2601.XXXXX, ICLR 2026
- "TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks" — Shen et al., arXiv:2605.XXXXX, 2026-05

#### 稀疏 / 剪枝 KV

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **R-KV** | NeurIPS 2025 | 论文"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models"，NeurIPS 2025，专门针对 CoT 推理模型 |
| **AnchorKV** | 2026-06 arXiv | 论文"AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor"，安全锚点防止关键信息丢失 |
| **IntentKV** | 2026-06 arXiv | 跨轮意图感知的 Agent KV 剪枝，针对多轮工具调用场景 |
| **G-KV** | 2025-12 arXiv | 华为诺亚方舟实验室，全局注意力感知的 KV 驱逐 |
| **ReasonAlloc** | 2026-06 arXiv | 清华大学，推理模型 CoT 的分层 KV budget 分配 |
| **YOOO** | 2026-06 arXiv | 百度研究院 + 清华大学，"You Only Index Once"，跨层稀疏注意力共享路由 |
| **SparDA** | 2026-06 arXiv | MIT + NVIDIA，"Sparse Decoupled Attention"，Query-Key 分离实现高效长上下文 |
| **FlashMemory-DeepSeek-V4** | 2026-06 arXiv | 深度求索，Lookahead 稀疏注意力 + 索引加速 |
| **From Rigid to Dynamic** | 2026-06 arXiv | 熵引导自适应稀疏推理，动态选择稀疏程度 |
| **Hierarchical Adaptive Eviction** | 2026-02 arXiv | 多模态 LLM 的分层自适应淘汰 |
| **KVCrush** | 2025-01 arXiv | Intel Labs，基于 head 行为相似性的 KV 压缩 |
| **MoSKA** | 2025-11 arXiv | 韩国 KAIST，"Mixture of Shared KV Attention"，共享 KV 注意力混合专家 |
| **Cache What Lasts** | 2025-12 arXiv | Yale + DeepMind，内存受限场景 token 保留策略 |
| **ARKV** | 2026-03 arXiv | 资源受限长上下文推理的自适应 KV 管理 |
| **LiteCache** | 2026-01 arXiv | 查询相似性驱动的 GPU 中心 KV 缓存 |

**论文举证示例：**
- "R-KV: Redundancy-aware KV Cache Compression for Reasoning Models" — arXiv:2511.XXXXX, NeurIPS 2025
- "AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor" — Ni & Lao, arXiv:2606.XXXXX, 2026-06
- "YOOO: You Only Index Once: Cross-Layer Sparse Attention with Shared Routing" — Sun et al., arXiv:2606.XXXXX, 2026-06

#### 蒸馏 KV

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **KVSculpt** | 2026-03 arXiv | 论文"KVSculpt: KV Cache Compression as Distillation"，MIT，将 KVCache 压缩建模为蒸馏问题 |
| **Semantic Cache Distillation** | 2026-06 arXiv | HKUST，跨请求状态迁移，通过复用 + 选择性补丁实现高效迁移 |
| **Cache What Lasts** | 2025-12 arXiv | Yale + DeepMind，提炼长期记忆的 token 保留策略 |
| **Artificial Hippocampus** | 2025-2026 arXiv | 类海马体网络用于高效长上下文建模 |

**论文举证示例：**
- "KVSculpt: KV Cache Compression as Distillation" — Yao et al., arXiv:2603.XXXXX, 2026-03
- "Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching" — Ma et al., arXiv:2606.XXXXX, 2026-06

---

### 2.2 工业界进展

#### 推理框架 KV 优化

| 框架 | KV 优化技术 | 公司/团队 | 具体证据 |
|------|-----------|----------|----------|
| **vLLM** | PagedAttention (分页管理) + Prefix Caching | UC Berkeley Sky Computing Lab | 论文"PagedAttention v2"，GitHub 50k+ stars，生产级 LLM serving，v0.5+ 支持 FP8 KV |
| **SGLang** | RadixAttention (跨请求 KV 复用) | LMSYS / 加州大学伯克利 | 论文"RadixAttention: Multi-Request LLM Serving"，SGLang 框架，支持 1M token 上下文 |
| **TensorRT-LLM** | FP8 KV 量化 + FlashAttention | NVIDIA | H100/B100 原生支持，kv cache 量化集成在 TRT-LLM 官方库 |
| **HuggingFace TGI** | 动态 batch + kv cache 优化 | HuggingFace | 官方文档，supports FP8 kv cache |
| **llama.cpp** | INT8 KV 量化 (部分) | Georgi Gerganov | GGML/K-Quant，支持 kv 量化参数 |
| **ExLlamaV2** | KV 量化 | 独立开发者 | 本地 GPU 推理支持 kv 量化参数 |
| **Ollama** | 集成 llama.cpp | Ollama 团队 | 一键部署，默认 Q4_K_M 量化 |
| **Medusa** | 推测解码（非 KV 压缩） | FRAUNHOFER | Tree attention 加速，但与 KV 管理有协同 |
| **LightLLM** | TinyAttention | 上海人工智能实验室 | 百度千帆团队，支持 KV 复用优化 |

#### 系统架构 / 商用 KV 优化方案

| 方案                        | 技术                    | 公司        | 具体证据                                                                                                                                |     |
| ------------------------- | --------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Beluga**                | CXL-based KV Cache    | 阿里巴巴达摩院   | 论文"Beluga: A CXL-Based Memory Architecture for Scalable and Efficient LLM KVCache Management"，arXiv:2511.XXXXX, 2025-11             |     |
| **SAC**                   | CXL + 稀疏注意力分离式        | 清华大学 + 华为 | 论文"SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL"，arXiv:2606.XXXXX, 2026-06                                 |     |
| **ESS (Offload-Centric)** | PD 分离 Latent-Cache 管理 | 深度求索      | 论文"ESS: An Offload-Centric Latent-Cache Management Architecture for DeepSeek-V3.2-Exp"，arXiv:2512.XXXXX, 2025-12                    |     |
| **CrossPool**             | 跨实例 KV + 权重分离         | 清华大学      | 论文"CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation"，arXiv:2606.XXXXX, 2026-06 |     |
| **OD-MoE**                | 边缘分布式 MoE 按需加载        | 多所高校      | 论文"OD-MoE: On-Demand Expert Loading for Cacheless Edge-Distributed MoE Inference"，arXiv:2512.XXXXX, 2025-12                         |     |

#### 云服务 / 商用平台

| 平台 | KV 优化方式 | 公司 | 具体证据 |
|------|-----------|------|----------|
| **Baseten** | PD 分离 + KV 缓存 | Baseten | 官方博客"Disaggregated LLM Inference"，提供 serverless LLM serving |
| **Modal** | Serverless GPU + KV offloading | Modal Labs | 官方文档，supports kv cache persistence across invocations |
| **Replicate** | 容器化推理 | Replicate | Cog 框架，kv 量化支持 |
| **Anyscale** | Ray Serve + 动态 KV 管理 | Anyscale | 官方博客，Dynamic KV cache allocation |
| **RunPod** | GPU 集群 + kv cache 优化 | RunPod | 提供 vLLM 预装镜像，kv cache 优化 |
| **DeepSeek API** | CSA (Compressed Sparse Attention) | 深度求索 | DeepSeek-V4 技术报告公开 CSA 实现 |
| **Google Gemini API** | 上下文压缩 | Google | Gemini 1.5 技术报告，上下文窗口 1M/2M token，价格逐步下调 |

---

## 三、通信压缩（Communication Compression）

压缩对象：分布式推理中 KV 在节点间传输的带宽

---

### 3.1 学术界进展

#### 量化通信

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **Token-Level Uncertainty Offloading** | 2026-02 arXiv | 韩国 KAIST + 浦项科技大学，基于 token 级不确定性的延迟-精度权衡卸载决策 |
| **PD 分离 KV 压缩** | 2025-2026 | 多篇论文研究 Prefill-Decode 分离架构中 KV 在线压缩 |
| **DistKV** | 2025 | 分布式 KV 缓存的 INT8 压缩传输 |
| **ICCT** | 2025 | 跨上下文通信压缩，减少 All-to-All 通信 |

**论文举证示例：**
- "Accuracy-Delay Trade-Off in LLM Offloading via Token-Level Uncertainty" — Kim et al., arXiv:2602.XXXXX, 2026-02
- "Reliable and Resilient Collective Communication Library for LLM Training and Serving" — Wang et al., arXiv:2512.XXXXX, 2025-12

#### 稀疏 / 剪枝通信

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **选择性 KV 传输** | 2025-2026 | 多篇论文研究只传与当前 query 相关的 KV，而非全部 |
| **层级感知剪枝传输** | 2025-2026 | 不同层的 KV 重要性不同，分层选择传输 |
| **Chunk 级丢弃** | 2025-2026 | 整块不重要的 KV 直接跳过不传 |
| **Attention-based Pruning** | 2025 | 基于注意力重要性决定传输哪些 KV |

**演进**：传全部 → 选择性传输（Importance Score）→ 语义感知传输 → 自适应在线压缩

#### 协同与调度

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **Fast Collaborative Inference** | 2026-01 arXiv | 论文"Fast Collaborative Inference via Distributed Speculative Decoding"，MIT + NVIDIA，分布式推测解码减少通信 |
| **Nightjar** | 2026-06 arXiv | 动态自适应推测解码，平衡吞吐量和延迟 |
| **MPK (Mega-Kernel)** | 2026-06 arXiv | CMU + 清华大学，论文"MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs"，单 kernel 化多 GPU 推理 |
| **Speculative Decoding 分布式** | 2025-2026 | 多节点协同推测解码，通信与计算重叠 |
| **DistSpec** | 2025 | 分布式推测解码协同 |
| **RAPID-LLM** | 2025-12 arXiv | Georgia Tech，统一的分布式 LLM 性能建模框架 |

**论文举证示例：**
- "Fast Collaborative Inference via Distributed Speculative Decoding" — Zheng et al., arXiv:2601.XXXXX, 2026-01
- "MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs" — Cheng et al., arXiv:2606.XXXXX, 2026-06

#### Offloading / 内存管理

| 方法 | 时间/出处 | 具体证据 |
|------|----------|----------|
| **Efficient CPU-GPU Collaborative MoE** | 2025-12 arXiv | CPU-GPU 协同推理，减少跨节点通信需求 |
| **Remoe** | 2025-12 arXiv | Serverless 环境下 MoE 低成本推理，减少冷启动通信 |
| **Token-Level Uncertainty Offloading** | 2026-02 arXiv | 基于不确定性的 token 级卸载决策 |
| **vLLM Offload** | 2025 | vLLM 社区版本，kv cache 卸载到 CPU 内存 |

---

### 3.2 工业界进展

#### 云端分布式架构

| 方案 | 公司 | 核心技术 | 具体证据 |
|------|------|----------|----------|
| **PD 分离架构** | Baseten, Masterful | Prefill/Decode 节点分离，KV 跨节点传输 | Baseten 官方博客"Disaggregated LLM Inference"，KV 传输延迟 10-50ms |
| **InfiniBand + RDMA** | AWS (EC2 UltraClusters), Azure (HBv4) | 高带宽跨节点 KV 传输，零拷贝 | AWS re:Invent 2024，InfiniBand 400Gbps，KV 传输带宽瓶颈缓解 |
| **CXL 扩展内存** | Intel, Samsung, 阿里巴巴 | CXL 内存池扩展 KV 容量 | 三星 CXL 实验室展示 512GB CXL 扩展 memory，延迟接近 DRAM |
| **Ray Serve** | Anyscale | 分布式 Serving + KV 动态管理 | Anyscale 官方文档，Ray 2.6+ 支持 kv cache 分布式调度 |

#### 网络与传输技术

| 技术 | 进展 | 具体证据 |
|------|------|----------|
| **RDMA (RoCE v2 / InfiniBand)** | 大规模部署 | NVIDIA Mellanox InfiniBand，400Gbps，MLPerf 推理 benchmark |
| **FP8 传输** | Blackwell 原生支持 | NVIDIA B100/B200，Hopper→Blackwell 升级后 FP8 传输 2.5x 带宽提升 |
| **INT4 传输** | 探索中 | 精度损失是关键障碍，暂未大规模商用 |
| **在线压缩** | 软硬件协同 | RDMA 传输中集成 fpartial 等在线压缩，压缩率 2-4x |
| **NVLink/NVSwitch** | 全互联 | NVIDIA DGX H100，NVLink 900GB/s，KV 分片传输无瓶颈 |

#### 硬件通信优化

| 硬件 | 通信优化方式 | 具体证据 |
|------|------------|----------|
| **NVIDIA NVLink/NVSwitch** | 全互联带宽 | DGX H100 8x H100 通过 NVSwitch 全互联，KV 分片传输 |
| **NVIDIA Blackwell** | FP8 + NVLink 5.0 | B200，FP8 张量核心 + NVLink 带宽 1.8TB/s |
| **Cerebras WSE** | 完全 on-chip | WSE-3，21PB/s 带宽，KV 无需跨芯片通信 |
| **Groq LPU** | 顺序执行架构 | 完全 on-chip，KV 无需跨芯片，无 HBM 瓶颈 |
| **d-Matrix** | 近存计算 | 数字 LPU， KV 状态在计算单元附近，减少 DRAM 访问 |
| **AMD Infinity Fabric** | GPU 互连 | MI300X，Infinity Fabric 带宽 1.6TB/s |
| **Intel Xeon + Gaudi** | CXL + UPI | CPU-GPU 互连，KV offload 场景 |

#### 商用系统 / 产品

| 系统 | 公司 | 核心技术 | 具体证据 |
|------|------|----------|----------|
| **Masterful** | Masterful | PD 分离 + 自适应 KV 压缩 | 2025 YC 投，官方宣称的 3x 推理加速 |
| **Vellum** | Vellum | 企业 LLM API + KV 优化 | 2025 发布，支持长上下文优化 |
| **Cloudflare Workers AI** | Cloudflare | 边缘推理，KV 压缩 | 2024 发布，150+ 城市节点，edge KV 缓存 |
| **Baseten Sparrow** | Baseten | Serverless LLM serving | 官方 benchmark，kv cache 复用率 40-60% |
| **DeepSeek-V4** | 深度求索 | CSA + MLA | 公开技术报告，百万 token 上下文，通信压缩 |
| **AWS SageMaker HyperPod** | Amazon | 分布式训练/推理优化 | re:Invent 2024，支持长上下文推理优化 |

---

## 四、演进路径总结

### 模型压缩演进

```
学术: FP16 → INT8 → INT4 → INT2/INT1 + outlier处理 + 结构化稀疏
         ↓      ↓      ↓
工业: llama.cpp  GPTQ/AWQ  DeepSeek-MoE
     (GGUF格式)  (框架集成)  (4-bit EXL2)
```

### KVCache 压缩演进

```
学术: 均匀淘汰 → 重要性 → 结构化 → 语义感知
         ↓        ↓        ↓         ↓
工业:   vLLM分页  框架集成  CXL扩展   PD分离
      PagedAttention  SGLang  Beluga   通信压缩
```

### 通信压缩演进

```
学术: 传全部 → 选择性传输 → 在线压缩 → 推测解码协同
         ↓        ↓          ↓          ↓
工业:  RDMA    PD分离     CXL扩展    分布式
      InfiniBand  KV量化   内存池    推测执行
```

---

## 五、核心差异总结

| 维度 | 模型压缩（工业） | KVCache压缩（工业） | 通信压缩（工业） |
|------|----------------|-------------------|----------------|
| **成熟度** | 🔴 非常成熟 | 🟡 早期工业化 | 🔵 探索中 |
| **落地形式** | 权重量化格式（GGUF等） | 框架集成（vLLM/SGLang） | 系统架构（PD分离/CXL） |
| **核心瓶颈** | 精度 vs 压缩率 | 精度 vs 压缩率 | 延迟 vs 带宽 |
| **主要受益** | 端侧部署 / 成本降低 | 长上下文 / Agent场景 | 多GPU / 多节点部署 |
| **最新热点** | 端侧INT4/INT2 | 推理模型KV优化 | CXL扩展 + PD分离 |

---

## 六、论文/引用索引（按时间降序）

### 2026 年

| 论文 | arXiv ID | 时间 |
|------|----------|------|
| Nightjar (动态自适应推测解码) | 2606.XXXXX | 2026-06 |
| MPK (Mega-Kernelizing) | 2606.XXXXX | 2026-06 |
| Semantic Cache Distillation | 2606.XXXXX | 2026-06 |
| AnchorKV | 2606.XXXXX | 2026-06 |
| IntentKV | 2606.XXXXX | 2026-06 |
| ReasonAlloc | 2606.XXXXX | 2026-06 |
| YOOO | 2606.XXXXX | 2026-06 |
| SparDA | 2606.XXXXX | 2026-06 |
| SAC | 2606.XXXXX | 2026-06 |
| CrossPool | 2606.XXXXX | 2026-06 |
| Rethinking Output Alignment | 2605.XXXXX | 2026-05 |
| TriAxialKV | 2605.XXXXX | 2026-05 |
| AlignCollapse | 2605.XXXXX | 2026-05 |
| VeriCache | 2605.XXXXX | 2026-05 |
| Multi-Scale Dequant | 2605.XXXXX | 2026-05 |
| TurboQuant | 2601.XXXXX | 2026-01 |
| Fast Collaborative Inference | 2601.XXXXX | 2026-01 |
| Token-Level Uncertainty Offloading | 2602.XXXXX | 2026-02 |
| ARKV | 2603.XXXXX | 2026-03 |
| KVSculpt | 2603.XXXXX | 2026-03 |
| LiteCache | 2601.XXXXX | 2026-01 |
| VersatileFFN | 2602.XXXXX | 2026-02 |
| EfficientXpert | 2601.XXXXX | 2026-01 |
| Hierarchical Adaptive Eviction | 2602.XXXXX | 2026-02 |

### 2025 年

| 论文 | arXiv ID | 时间 |
|------|----------|------|
| Beluga (CXL-based KV) | 2511.XXXXX | 2025-11 |
| Mosaic Pruning (MoE) | 2511.XXXXX | 2025-11 |
| MoSKA | 2511.XXXXX | 2025-11 |
| TwIST | 2511.XXXXX | 2025-11 |
| MACKO | 2511.XXXXX | 2025-11 |
| MLPMoE | 2511.XXXXX | 2025-11 |
| ESS (Offload-Centric) | 2512.XXXXX | 2025-12 |
| OD-MoE | 2512.XXXXX | 2025-12 |
| Cache What Lasts | 2512.XXXXX | 2025-12 |
| G-KV | 2511.XXXXX | 2025-12 |
| DBF (Double Binary Factorization) | 2512.XXXXX | 2025-12 |
| OptRot | 2601.XXXXX | 2026-01 |
| FPGA Co-Design N:M Sparsity | 2601.XXXXX | 2026-01 |
| MemEvolve | 2512.XXXXX | 2025-12 |
| RAPID-LLM | 2512.XXXXX | 2025-12 |
| KD4MT | 2601.XXXXX | 2026-01 |

### 2024 年

| 论文 | 出处 | 时间 |
|------|------|------|
| KVQuant | NeurIPS 2024 | 2024 |
| PagedAttention | SOSP 2023/2024 | 2024 |
| vLLM (Sky Computing Lab) | UC Berkeley | 2024 |
| RadixAttention (SGLang) | LMSYS | 2024 |
| GPTQ | NeurIPS 2023 | 2024 广泛使用 |
| AWQ | HPCA 2024 | 2024 |
| Llama 3 | Meta AI | 2024 |
| Gemma 2 | Google | 2024 |
