# KV稀疏技术演进：代表论文效果对比

> 数据来源：02_论文精读全部论文提取
> 关注指标：压缩比、吞吐提升、时延降低、精度保持
> 统一基准：LongBench / NIAH / AIME / GSM8K / MMLU

---

## 一、按演进阶段对比

### 第一阶段：Attention统计驱动（2023-2024）

| 论文 | 模型 | KV预算 | LongBench | NIAH | 吞吐/加速 | 时延 |
|------|------|--------|-----------|------|----------|------|
| **H2O** (NeurIPS'23) | LLaMA-2/3/OPT | 20%KV | 接近full | 稀有Token会丢失 | 29倍 vs DeepSpeed | 1.9倍降低 |
| **SnapKV** (NeurIPS'24) | 多模型 | 16%KV | 16个长序列基准≈full | 近无损 | 3.6倍生成加速 | 8.2倍内存提升 |
| **StreamingLLM** (ICLR'24) | LLaMA-2/MPT | sink(4)+窗口 | PPL稳定 | ❌中间Token全丢 | 22.2倍 vs SW重计算 | O(1)内存 |

**阶段小结**：压缩比~5-8倍，但NIAH检索任务不可靠，多query场景90%预算时崩溃。

---

### 第二阶段：检索相关驱动（2024-2025）

| 论文 | 模型 | KV预算 | LongBench | NIAH | 吞吐/加速 | 时延 |
|------|------|--------|-----------|------|----------|------|
| **DuoAttention** (ICLR'25) | LLaMA-3-8B | MHA:39% / GQA:60% | full级 | 3.3M Token@单卡 | MHA:2.18倍decode / GQA:1.50倍 | MHA:1.73倍prefill |
| **ThinK** (ICLR'25) | LLaMA-2/3 | >20%省 | 维持/提升 | 近无损 | ×KIVI=2.8倍峰值显存，5倍batch | - |
| **HeadKV-R2** (ICLR'25) | LLaMA-3-8B | **1.5%KV** | - | **97%**性能 | - | - |
| **ShadowKV** (ICML'25) | 6个模型 | 低秩Key+CPU Value | full级(6模型验证) | RULER+LongBench+NIAH无损 | **3.04倍**吞吐，**6倍**batch | 超越"无限显存"上界 |
| **CompressKV** (2026) | GQA模型 | **3%KV** | **>97%** full-cache | **0.7%→90%** | - | - |
| **MagicPIG** (ICLR'25) | LLaMA-3-8B | LSH采样 | - | 96K ctx | **5倍**吞吐 | **54ms** decode@96K |

**阶段小结**：压缩比提升到10-60倍（HeadKV-R2 1.5%KV→97%），NIAH可靠，开始区分头的功能属性。

---

### 第三阶段：结构模式驱动（2025-2026）

| 论文 | 模型 | KV预算 | LongBench | NIAH/AIME | 吞吐/加速 | 时延 |
|------|------|--------|-----------|-----------|----------|------|
| **PyramidKV** (ACL'25) | LLaMA-3-70B | **12%KV** | =full | **128KV/层→100.0** NIAH | - | - |
| **PyramidKV** | LLaMA-3-70B | **0.7%KV** | - | TREC **+20.5分** | - | - |
| **KeyDiff** (2025) | LLaMA-3-8B | 8K(23%削减) | PPL gap<0.04% | - | - | **30%降低** |
| **TriAttention** (2026) | 多推理模型 | - | - | **AIME25 32K=Full Attention** | **2.5倍**吞吐(或10.7倍内存↓) | - |
| **MAC-Attention** (2026) | - | - | Full Attention级 | KV访问**↓99%** | **14.3倍**attention，**2.6倍**e2e | 128K延迟**↓60%** |
| **DMS** (NeurIPS'25) | Qwen-R1-32B | 8倍压缩 | - | AIME24 **+12.0**，GPQA **+8.6** | 仅需1K步训练 | - |
| **SqueezeAttention** (2025) | - | 30-70%省 | - | - | **2.2倍**吞吐 | - |
| **Locret** (2025) | - | **20倍** | - | - | - | 128K@单卡RTX4090 |
| **EMS** (2025) | - | <2% | **+1.28分** | **95%** NIAH | - | - |

**阶段小结**：引入层级/几何/RoPE距离/时序等结构先验，TriAttention在推理模型上达到AIME=Full Attention。

---

### 第四阶段：语义驱动（2025-2026，当前前沿）

| 论文 | 模型 | KV预算 | AIME/MATH | LongBench | 吞吐/加速 | 时延 |
|------|------|--------|-----------|-----------|----------|------|
| **KVzip** (2025) | LLaMA-3.1/Qwen2.5/Gemma3 | 3-4倍压缩 | - | - | **~2倍** decode加速 | 170K上下文 |
| **R-KV** (2025) | R1-Llama-8B/R1-Qwen-14B | **10%KV** | MATH-500≈**100%** | - | **6.6倍**吞吐 | 90%显存省 |
| **R-KV** | 同上 | 16%KV | **105%**(超full) | - | - | - |
| **ThinKV** (ICLR'26 Oral) | DeepSeek-R1-8B/70B/Qwen14B等 | **<5%KV** | MATH/AIME/GSM8K近无损 | - | **5.8倍**吞吐 | TPOT **1.68倍低于R-KV** |
| **ThinKV** | 同上 | 2.51% | LiveCodeBench近无损 | - | 内存2.51%(R-KV 5.48%) | CT kernel解决R-KV 37倍慢化 |
| **ShotKV** (ICML'26) | - | - | 算术0.75→<0.5@<20% | +9-18%准确率 | - | **-11%**延迟 |
| **RocketKV** (ICML'25) | - | **400倍** | 近无损 | 近无损 | **3.7倍**e2e | 峰值显存↓32.6% |
| **MoE-nD** (2026) | - | **14倍** | AIME **+6到+27** vs最强单层 | - | 1.9GB匹配无压缩 | - |
| **RDKV** (2026) | - | **2.48%KV** | - | **97.81%** full-cache | **4.5倍**decode | 1.9倍峰值显存↓ |
| **Lexico** (ICML'25) | - | 15-25% | GSM8K **90-95%** | - | - | - |

**阶段小结**：ThinKV（ICLR 2026 Oral）是当前SOTA——<5%KV保推理精度，5.8倍吞吐。

---

## 二、同一基准横向对比

### LongBench（长上下文多任务）

| 论文 | KV预算 | LongBench表现 | 备注 |
|------|--------|-------------|------|
| H2O | 20% | 接近full | 稀有Token会丢失 |
| SnapKV | 16% | 16基准≈full | Prefill一次性压缩 |
| PyramidKV | 12% | =full | 金字塔层级分配 |
| ShadowKV | 低秩+CPU | full级(6模型) | 无损验证 |
| RDKV | 2.48% | **97.81%** full | 率失真理论 |
| CompressKV | 3% | **>97%** | SRH头级（⚠️原创性存疑）|
| EMS | <2% | **+1.28分** | 全局-局部评分 |

### NIAH（大海捞针检索）

| 论文 | KV预算 | NIAH准确率 | 备注 |
|------|--------|----------|------|
| StreamingLLM | sink+窗口 | ❌**0%**（中间全丢） | 无法回忆中间Token |
| H2O | 20% | 稀有Token丢失 | Heavy-Hitter无法保证 |
| SnapKV | 16% | **近无损** | 观测窗口投票 |
| PyramidKV | 128KV/层 | **100.0%** | LLaMA-3-70B |
| DuoAttention | retrieval头全量 | **3.3M Token** | 检索头保护 |
| HeadKV-R2 | 1.5% | **97%** | 头级双属性 |
| CompressKV | 0.7% | **90%** | 极端压缩 |
| EMS | <2% | **95%** | Evict-then-Merge |

### AIME/MATH（数学推理）

| 论文 | KV预算 | AIME/MATH表现 | 备注 |
|------|--------|-------------|------|
| SnapKV | 10% | 60%性能 | CoT冗余Token被高attention误保留 |
| R-KV | 10% | **≈100%** | 冗余感知评分(λ=0.1) |
| R-KV | 16% | **105%**(超full) | 去冗余反而提升 |
| ThinKV | <5% | **近无损** | Thought R/E/T差异化 |
| TriAttention | - | **=Full Attention** (AIME25 32K) | Pre-RoPE三角距离 |
| DMS | 8倍压缩 | **+12.0** (AIME24) | 延迟驱逐(Qwen-R1-32B) |
| MoE-nD | 14倍 | **+6到+27** vs最强单层 | 逐层MoE压缩 |

### 吞吐/加速排名

| 排名 | 论文 | 加速比 | 压缩比 | 精度 |
|------|------|--------|--------|------|
| 1 | **R-KV** | 6.6倍吞吐 | 10倍 | ≈100% |
| 2 | **ThinKV** | 5.8倍吞吐 | >20倍 | 近无损 |
| 3 | **MagicPIG** | 5倍吞吐 | - | LSH无偏 |
| 4 | **RDKV** | 4.5倍decode | 40倍 | 97.81% |
| 5 | **RocketKV** | 3.7倍e2e | 400倍 | 近无损 |
| 6 | **ShadowKV** | 3.04倍吞吐 | - | 无损(6模型) |
| 7 | **SnapKV** | 3.6倍生成 | 8.2倍 | ≈full |
| 8 | **TriAttention** | 2.5倍吞吐 | 10.7倍内存 | AIME=Full |
| 9 | **MAC-Attention** | 2.6倍e2e | - | Full级 |
| 10 | **SqueezeAttention** | 2.2倍吞吐 | 3-7倍 | - |

---

## 三、压缩比极限演进

```
H2O (2023)     ██████ 5倍 (20%KV)
SnapKV (2024)  ████████ 8倍 (12%KV)
PyramidKV(2025)██████████ 10倍 (12%KV，深层更激进)
HeadKV-R2(2025)████████████████ 67倍 (1.5%KV)
RDKV (2026)    ██████████████████████ 40倍 (2.48%KV)
RocketKV(2025) ████████████████████████████████████████ 400倍 (两阶段)
                 ↑ 但RocketKV的400倍包含两阶段，实际单阶段~20倍
```

---

## 四、结论

**当前SOTA（2026.06）**：

| 维度 | SOTA论文 | 指标 |
|------|---------|------|
| **推理模型KV压缩** | ThinKV (ICLR'26 Oral) | <5%KV，5.8倍吞吐，AIME近无损 |
| **通用长上下文** | RDKV | 2.48%KV，97.81% LongBench，4.5倍decode |
| **极端压缩** | RocketKV (ICML'25) | 400倍，3.7倍e2e，近无损 |
| **推理任务稳定性** | TriAttention | AIME25 32K = Full Attention |
| **生产部署** | ShadowKV (ICML'25) | 6模型无损，6倍batch，3.04倍吞吐 |
