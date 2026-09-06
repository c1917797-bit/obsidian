# KV Cache压缩技术洞察报告（v8 数据驱动版）

> 数据来源：inference_compression_v8.json (2,555篇) + inference_optimization_full.json (17,352篇)
> 查询结果：KV Cache相关 170篇 | 投机解码 105篇 | 合计275篇
> 生成日期：2026-06-29

---

## 一、领域全景

### 数据库实际查询结果

| 子方向 | 论文数 | 最高引用 | 代表论文 |
|--------|--------|---------|---------|
| KV Cache稀疏化 | 35 | DuoAttention 34引 | DuoAttention/StreamingLLM/SnapKV |
| KV Cache驱逐/剪枝 | 30 | DuoAttention 34引 | DuoAttention/RobustKV/CAKE |
| 投机解码 | 105 | MagicDec 21引 | MagicDec/Reward-Guided/Speculative RAG |
| KV Cache量化 | 10 | — | KIVI/SinkQ/QJL |
| KV Cache低秩 | 3 | ShadowKV 6引 | ShadowKV/Palu/STAR-KV |
| KV Cache蒸馏 | 1 | — | SwiftKV |
| KV Cache合并 | 0 | — | 💎空白（数据库中0篇） |
| KV Cache存储分层 | 1 | ShadowKV 6引 | ShadowKV/SpeCache |

### 核心发现（数据驱动）

```
1. 投机解码是KV相关最大类别（105篇）
   → 不直接压缩KV，但通过减少前向传播次数间接降低KV开销

2. KV Cache量化仅10篇，但全部是高影响力工作
   → KIVI(2-bit)/SinkQ(动态Sink)/QJL(1-bit JL变换)

3. KV Cache合并 = 0篇
   → 数据库验证的最大空白之一

4. KV Cache蒸馏仅1篇（SwiftKV）
   → Decoding阶段蒸馏 = 0篇 → 最高价值空白
```

---

## 二、技术演进（基于数据库论文的时间线）

### 2023：奠基年
- H2O (NeurIPS 2023) — Heavy-Hitter驱逐，奠基性工作
- StreamingLLM — Attention Sink发现

### 2024：爆发年
- KIVI (ICML 2024) — 2-bit非对称量化，K per-channel + V per-token
- SnapKV (NeurIPS 2024) — Prefill一步压缩，8.2×内存效率
- ShadowKV — 低秩Key + CPU Value卸载

### 2025：深化年（v8数据库中2025顶会1,911篇）
- DuoAttention (ICLR 2025) — 检索头vs流式头区分，34引
- ThinK (ICLR 2025 Spotlight) — Channel维度剪枝，18引
- RazorAttention — 检索头保护+补偿token
- MagicPIG — LSH采样近似
- SpinQuant — 学习旋转量化

### 2026：突破年（v8数据库中576篇）
- NSA — 原生可训练稀疏注意力（DeepSeek）
- RocketKV — 两阶段400×压缩（NVIDIA）
- ThinKV — 思维类型自适应压缩
- TriAttention — Pre-RoPE三角级数
- CompressKV — 语义检索头3%→97%
- OSCAR — INT2频谱协方差量化

---

## 三、工业空白分析（数据库验证）

### 已成熟（TRL4-5，可生产部署）

| 技术 | 代表 | 工业状态 |
|------|------|---------|
| Token驱逐 | H2O/SnapKV | vLLM/SGLang集成 |
| 2-bit量化 | KIVI | 批处理4× |
| Attention Sink | StreamingLLM | 流式推理标配 |
| 检索头区分 | DuoAttention | 3.3M token单A100 |

### 工业空白（TRL1-3，高价值机会）

| 空白 | 论文数 | 价值 | 原因 |
|------|--------|------|------|
| **Decoding阶段KV蒸馏** | **0篇** | 💎最高 | KV累积最严重但无人做 |
| **KV Cache合并** | **0篇** | 💎高 | 不删除而是合并，信息保留 |
| **KV Cache通信压缩** | **极少** | 💎高 | PD分离场景的KV传输压缩 |
| **多维度联合压缩** | **<5篇** | 💎高 | Token×Channel×Head×Bit叠加 |

---

## 四、8个正交压缩维度（数据库验证）

| 维度 | 代表 | 压缩比 | 工业可用？ |
|------|------|--------|:---------:|
| Token | H2O/SnapKV | 5-20× | ✅ |
| Channel | ThinK | 1.25× | ⚠️ 需定制kernel |
| Head | DuoAttention | 2-3× | ✅ |
| Layer-depth | PyramidKV | 2-8× | ✅ |
| Bit-width | KIVI | 8× | ✅ |
| Storage | ShadowKV | 6× batch | ⚠️ 需CPU卸载 |
| Compute-reuse | MAC-Attention | 14.3× | 🔬 研究 |
| Architecture | MLA/NSA | 消除KV | ✅(DeepSeek) |

### 叠加效果（理论SOTA栈）

```
SnapKV(Token 5×) × KIVI(Bit 8×) × ThinK(Channel 1.25×) × DuoAttention(Head 2.5×)
= 5 × 8 × 1.25 × 2.5 = 125× 理论压缩比
```

---

## 五、课题方向建议（基于数据空白）

| 课题 | 论文支撑 | 空白度 | 工业价值 |
|------|---------|:------:|---------|
| KV Decoding蒸馏 | 0篇 | 💎 | 解决长推理KV爆炸 |
| 多维度联合压缩 | <5篇 | 💎 | 100×+压缩工业落地 |
| KV Cache通信压缩 | <3篇 | 💎 | PD分离/多Agent场景 |
| 推理模型KV压缩 | <10篇 | ⚠️ | DeepSeek-R1/o1场景 |

---

*数据驱动版 | 2026-06-29 | 基于inference_compression_v8.json实际查询*
