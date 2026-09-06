# KV Cache Compression 论文精读推荐列表

**筛选标准**：
- 评分 ≥ 6.0 (ICLR/NeurIPS/ICML 2025)
- 引用数较高
- 代表性工作（首创或突破性）
- 工业落地潜力

---

## 一、KV稀疏化（Sparse KV）- 推荐精读

### 🔥 必读（影响力高）

| 排名 | 论文 | 会议 | 评分 | 引用 | 核心贡献 |
|------|------|------|------|------|----------|
| 1 | **Retrieval Head Mechanistically Explains Long-Context Factuality** | ICLR 2025 | 8.0 | 51 | 揭示Long-Context的事实性来源机制 |
| 2 | **MagicPIG: LSH Sampling for Efficient LLM Generation** | ICLR 2025 | 7.2 | 14 | LSH采样加速LLM生成 |
| 3 | **ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM** | ICLR 2025 | 6.8 | 6 | KV缓存shadow机制 |
| 4 | **HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing** | ICLR 2025 | 6.8 | 0 | 分层KV共享 |
| 5 | **MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation** | ICLR 2025 | 6.8 | 21 | 打破延迟-吞吐权衡 |
| 6 | **CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences** | ICLR 2025 | 6.0 | 0 | 级联自适应KV驱逐 |
| 7 | **LazyLLM: Dynamic Token Pruning for Efficient Long Context LLM Inference** | ICLR 2025 | 5.0 | 25 | 动态Token剪枝 |

### 推荐理由

**Retrieval Head [8.0]**：
- 发现LLM中存在专门的"检索头"
- 解释了为什么某些KV压缩方法有效
- 为后续压缩方法提供理论依据

**MagicPIG [7.2]**：
- LSH (Locality-Sensitive Hashing) 用于高效KV采样
- 可证明的收敛性保证
- 适合长序列生成加速

**ShadowKV [6.8]**：
- KV缓存shadow机制
- 高吞吐长上下文LLM
- 与HShare有互补性

**MagicDec [6.8]**：
- 解决长上下文生成的延迟-吞吐权衡
- 工业价值高

---

## 二、KV量化（Quantized KV）- 推荐精读

### 🔥 必读

| 排名 | 论文 | 会议 | 评分 | 引用 | 核心贡献 |
|------|------|------|------|------|----------|
| 1 | **ThinK: Thinner Key Cache by Query-Driven Pruning** | ICLR 2025 | 6.8 | 18 | Query驱动剪枝 |
| 2 | **DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Decoding** | ICLR 2025 | 6.3 | 34 | 双注意力机制 |
| 3 | **Quamba: A Post-Training Quantization Recipe for Selective State Space Models** | ICLR 2025 | 6.2 | 4 | Mamba后训练量化 |
| 4 | **Palu: KV-Cache Compression with Low-Rank Projection** | ICLR 2025 | 5.0 | 0 | 低秩投影压缩 |

### 推荐理由

**ThinK [6.8]**：
- Query驱动剪枝策略
- 比传统KV压缩更高效
- 引用数18，说明有一定影响力

**DuoAttention [6.3]**：
- 检索和解码分离
- 34引用，高影响力
- 可能是下一个突破点

---

## 三、KV通用优化 - 推荐精读

### 🔥 必读

| 排名 | 论文 | 会议 | 评分 | 引用 | 核心贡献 |
|------|------|------|------|------|----------|
| 1 | **Long Context Compression with Activation Beacon** | ICLR 2025 | 7.0 | 12 | Activation Beacon机制 |
| 2 | **COrAL: Order-Agnostic Language Modeling for Efficient Iterative Refinement** | ICLR 2025 | 5.75 | 2 | 顺序无关语言建模 |
| 3 | **OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs** | ICLR 2025 | 6.0 | 2 | 动态上下文选择 |
| 4 | **MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Projections** | ICLR 2025 | 6.0 | 0 | 可训练正交投影 |

### 推荐理由

**Activation Beacon [7.0]**：
- 直接压缩activations（KV）
- 不依赖soft KV Cache
- 12引用，值得关注

**MatryoshkaKV [6.0]**：
- 多尺度KV压缩
- 类似Matryoshka嵌入思想
- 可训练投影，灵活

---

## 四、KV蒸馏 - 精读建议

| 排名 | 论文 | 会议 | 评分 | 引用 | 核心贡献 |
|------|------|------|------|------|----------|
| 1 | **Beyond Autoregression: Fast LLMs via Self-Distillation Through Time** | ICLR 2025 | 7.0 | 1 | 自蒸馏加速 |
| 2 | **Learning Harmonized Representations for Speculative Sampling** | ICLR 2025 | 6.0 | 7 | 投机采样蒸馏 |

### ⚠️ 注意
- KV蒸馏方向论文较少（~10篇）
- 大部分集中在Prefill阶段
- **Decoding阶段蒸馏仍是空白**

---

## 五、经典论文（需补充阅读）

以下论文可能不在2025顶会数据集中，但仍是必读经典：

| 论文 | 年份 | 引用 | 核心贡献 |
|------|------|------|----------|
| **SnapKV** | NeurIPS 2024 | 高 | 语义聚类锚点，内存效率↑8.2倍 |
| **H2O** | 2023 | 高 | 基于注意力分数的KV选择 |
| **StreamingLLM** | 2023 | 高 | Attention Sink机制 |
| **KIVI** | ICLR 2024 | 高 | 2-bit KV量化 |
| **R-KV** | 2025 | 中 | 10% KV保持近100%性能 |

---

## 六、精读优先级建议

### 第一优先级（必读，1-2周内）
1. **Retrieval Head** [8.0] - 理论依据
2. **MagicPIG** [7.2] - 高效采样
3. **ShadowKV** [6.8] - 吞吐优化
4. **ThinK** [6.8] - Query驱动剪枝

### 第二优先级（推荐，2-4周内）
5. **DuoAttention** [6.3] - 双注意力
6. **Activation Beacon** [7.0] - 激活压缩
7. **MagicDec** [6.8] - 延迟-吞吐权衡
8. **LazyLLM** [5.0] - 动态剪枝

### 第三优先级（选读）
9. HShare, CAKE, MatryoshkaKV, OmniKV

---

---

## 八、通信压缩论文推荐（补充）

### 通信压缩专项论文（极少，只有7篇）

| 论文 | 评分 | 引用 | 核心贡献 |
|------|------|------|----------|
| MoE++ | 8.0 | 4 | 零计算专家减少通信 |
| LoCoDL | 7.5 | 3 | 本地训练+通信压缩 |
| Mixture Compressor | 6.8 | 0 | MoE量化+剪枝 |
| TPI-LLM | 4.0 | 2 | 边缘70B LLM服务 |

### arXiv最新MoE通信压缩论文

| 论文 | 时间 | 会议 | 核心贡献 |
|------|------|------|----------|
| **AlphaQ** | 2026-06 | arXiv | 无校准MoE量化，3.5比特接近全精度 |
| **KBVQ-MoE** | 2026-02 | ICLR 2026 | KLT引导的MoE向量量化 |
| **D²MoE** | 2025-04 | MobiCom 2025 | 动态专家调度 |

### 通信压缩研究方向建议

1. **分布式推理的KV通信压缩**（极度空白）
2. **MoE Decoding阶段的专家激活压缩**
3. **边缘-云协同的通信压缩**

详见：`通信压缩论文精读笔记.md`

---

## 八、工业落地评估

| 论文 | 技术成熟度 | 工业落地 | 实现难度 | 备注 |
|------|-----------|---------|---------|------|
| Retrieval Head | TRL 3 | 低 | 低 | 理论指导为主 |
| MagicPIG | TRL 4 | 中 | 中 | LSH实现复杂 |
| ShadowKV | TRL 4 | 高 | 中 | 高吞吐场景 |
| ThinK | TRL 4 | 高 | 中 | 直接可落地 |
| DuoAttention | TRL 4 | 高 | 中 | 解码加速 |
| Activation Beacon | TRL 3 | 中 | 高 | 需改模型结构 |
| MagicDec | TRL 4 | 高 | 中 | 框架集成 |

---

*推荐生成日期：2026-06-27*
*数据来源：inference_compression_strict.json + conf_inference_compression_2025.json*
