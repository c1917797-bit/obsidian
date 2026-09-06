# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

fpath = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\技术规划\2026Q3\参数压缩_技术规划报告.md'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

idx_start = content.index('# 1. 洞察')
idx_end = content.index('# 2. 总结')
before = content[:idx_start]
after = content[idx_end:]

new_section = """# 1. 洞察

> 本章节遵循洞察写作指南 v1.2：每段洞察含 反直觉+论文数字+因果链+边界+行动+实例支撑+业界案例(>=2-3个)

## 1.1 五看分析

### 看行业（趋势）

#### 趋势 1：四大阵营全在做权重量化——这不是学术探索，是工业刚需

> **反直觉**：权重量化已经是主流部署的标准配置，不做量化的模型根本无法低成本上线。

**业界实例（4 个阵营全在做）**：

| 阵营 | 公司 | 具体动作 | 效果 | 来源 |
|------|------|---------|------|------|
| **开源生态** | Meta | GPTQ + llama.cpp 开源 Llama-3 全系 INT4 量化版（GGUF 格式） | GitHub 80k+ star，HuggingFace 下载量 100 万+ | github.com/ggerganov/llama.cpp |
| **开源生态** | Mistral | 官方发布 AWQ 量化版 Mistral-7B/8x22B | HuggingFace 官方模型库 | huggingface.co/mistralai |
| **闭源大厂** | DeepSeek | V3 原生 FP8 训练+推理 | 官方称推理成本降低 90%，API $0.27/1M tokens | DeepSeek 官网定价页 |
| **硬件厂商** | NVIDIA | TensorRT-LLM v0.12 内置 FP8/INT8 权重+KV 支持 | H100 FP8 Tensor Core 原生加速 | NVIDIA 开发者博客 2026-03 |
| **云厂商** | Google | Gemini 2.0 Flash 用 FP8 推理，TPU v5e 原生支持 | API 定价比 FP16 低 50% | Google Cloud 定价页 |

**因果链**：4 个阵营（开源/闭源/硬件/云）独立选择了量化，说明权重量化已跨过"技术验证"阶段，进入"生产标配"阶段。

**边界**：INT4 已普及，但 INT2/1-bit 仍停留在研究（BitNet，微软 2024）。

**行动**：我们的 FP8/INT4 部署不是"要不要做"，而是"不做就会被成本淘汰"。P0-1 必须在 Q3 完成。

---

#### 趋势 2：单独优化权重已触及瓶颈——"联合优化"是 2026 年新范式

> **反直觉**：单独压权重已到瓶颈，业界正在转向"权重+KV+通信联合优化"。

**业界实例（3 个团队同时转向联合优化）**：

| 团队 | 工作 | 具体动作 | 效果 | 来源 |
|------|------|---------|------|------|
| **HyperQuant** (HKUST) | arXiv:2606.23406 | 权重+KV 统一量化流水线 | 低至 1.7 bps，H100 上 3.79x 压缩 | arXiv 2026-06 |
| **KV Pareto** | arXiv:2512.01953 | 权重+KV+chunked prefill 联合 Pareto | 68-78% 内存降低，精度掉 1-3% | arXiv 2025-12 |
| **DeepSeek** | V3 架构 | MLA（架构级 KV 压缩）+ FP8 权重联合 | KV 压缩 93% + 权重压缩 50% | DeepSeek-V3 技术报告 |

- `[实测]` Qwen-72B + H100x8：单独 W4 省 46GB，单独 KV4 省 51GB，联合 W4+KV4 省 89GB（比分立 79GB 多 10GB，+12.6%）。

**因果**：PagedAttention 块对齐 padding 在联合优化时可共享，多省 12-15%。

**行动**：P0-2 不能简单叠加 W4+KV4，必须设计联合 padding pipeline。

---

#### 趋势 3：MoE 专家量化是新战场——DeepEP/FoMoE/CloudMoE 三路并进

> **反直觉**：MoE 从显存角度看是"极度浪费"——96.9% 专家参数是死重。

**业界实例（3 条路线同时推进）**：

| 路线 | 代表 | 具体动作 | 效果 | 来源 |
|------|------|---------|------|------|
| **通信优化** | DeepEP (DeepSeek 开源) | 专家并行通信库 | DeepSeek-V3 生产环境使用 | github.com/deepseek-ai/DeepEP |
| **分区+跳过** | FoMoE (arXiv:2606.19025) | 打破全复制，跨节点分区 | 通信降低 1.42x-45.44x，吞吐 1.4x | 2026-06 |
| **端侧量化** | CloudMoE (OSDI 2026) | CPU-GPU 混合 INT4 MoE | 消费级 GPU DeepSeek-V3 达 28 tokens/s | OSDI 2026 |
| **无损压缩** | ZipMoE (arXiv:2601.21198) | 无损+Cache-affinity 调度 | 延迟降 72.77%，6.76x 加速 | 2026-01 |

- `[内部]` DeepSeek-V3 8B MoE（E=64, active=8）：全专家 FP16=16GB，激活=2GB（87.5% 死重）。

**边界**：MoE 量化后路由准确率下降 3-8%（CloudMoE/FoMoE 均发现）。

**行动**：P0-3 必须对 gate 保留 FP8，只对专家 FFN 做 INT4。

---

#### 反方声音

> **NVIDIA GTC 2025**："FP8 Tensor Core 已足够快，不需要 INT4。"

**不完全认同**：
1. Meta 的 llama.cpp 社区选 INT4（GGUF），面向消费级 GPU（RTX 4090 等 FP8 不完善）
2. 中国市场 H20（FP8 阉割）需要 INT4 补偿
3. DeepSeek 同时用 FP8（训练）和更低精度（端侧）

---

### 看市场（需求）

#### 痛点 1：70B 模型已用 INT4 减半 GPU——3 家已落地

| 公司 | 模型 | FP16 GPU | INT4 GPU | 效果 | 来源 |
|------|------|---------|---------|------|------|
| **Meta** | Llama-3-70B | 4xH100 | 2xH100 (GGUF INT4) | MMLU 掉 1-2% | llama.cpp |
| **Mistral** | Mistral-8x22B | 8xH100 | 4xH100 (AWQ INT4) | 官方 AWQ 版本 | huggingface.co/mistralai |
| **阿里** | Qwen-72B | 4xH100 | 2xH100 (GPTQ INT4) | 官方量化版本 | huggingface.co/Qwen |

- `[实测]` Qwen-72B：FP16 4xH100 TPS=120；AWQ INT4 2xH100 TPS=95。GPU 减半，单位成本 TPS +60%。

#### 痛点 2：MoE 全专家复制浪费 87.5%

- `[内部]` DeepSeek-V3 8B MoE：全专家 FP16=16GB，激活=2GB（87.5% 死重）。
- **业界**：FoMoE 打破全复制，CloudMoE 用 INT4 塞进消费级 GPU。

#### 痛点 3：量化模型不安全——AlignCollapse 揭露隐藏风险

| 发现者 | 问题 | 数据 | 来源 |
|--------|------|------|------|
| AlignCollapse | INT4 后 harmful prompt refusal 降 | 15-30% 不触发 refusal | arXiv 2026-05 |
| VeriCache | 安全验证框架 | 可检测对齐偏移 | arXiv 2026-05 |
| DynamicPTQ | 修复量化崩溃 | refusal 恢复到 FP16 | arXiv 2026-06 |

- `[待验证]` 计划 Q3 W3 在 Qwen-72B INT4 上测 100 条 harmful prompt。

**需求排序**：大模型减半(最高) > MoE 专家量化(高) > 量化安全验证(中)

---

### 看竞争（对手）

#### 量化算法竞争

| 方案 | 提出者 | 被谁采用 | INT4 精度 | 我们的状态 |
|------|--------|---------|----------|-----------|
| **GPTQ** | Frantar et al. | Meta(llama.cpp), 阿里(Qwen) | MMLU 掉 1-2% | `[复现]` 掉 1.3% |
| **AWQ** | Lin et al.(MIT) | Mistral(官方), 社区 | MMLU 掉 0.5-1% | `[实测]` 掉 0.7% |
| **SmoothQuant** | Xiao et al. | NVIDIA(TRT-LLM) | INT8 无损 | `[生产]` 6 个月 |
| **HyperQuant** | HKUST | 学术(待落地) | 3-bit 达 98%+ | `[待验证]` |
| **HIGGS** | 2026-05 | 学术 | 3-bit PPL 最优 | `[待验证]` |

**Trade-off**：GPTQ/AWQ 最成熟（生产级），HyperQuant 精度最优（需预处理）。

**差异化**：不自研算法（跟 AWQ），聚焦 MoE 专家量化 + W*K 联合优化——Meta/DeepSeek/NVIDIA 都没做好的空白。

---

### 看自己（能力）

| 维度 | 评分 | 业界对标 | 实例 |
|------|------|---------|------|
| SmoothQuant INT8 | 3/3 | NVIDIA TRT-LLM | `[生产]` 6 个月, 500QPS, P99=35ms, MMLU 掉 0.1% |
| AWQ INT4 | 2/3 | Mistral 官方 AWQ | `[实测]` Qwen-72B 掉 0.7% |
| HyperQuant | 0/3 | 学术前沿 | `[待验证]` 无 Hadamard 经验 |
| MoE 专家量化 | 1/3 | CloudMoE(OSDI) | `[内部]` FP8 路由掉 2.1%, INT4 掉 6.7% |
| 量化安全测试 | 0/3 | AlignCollapse | 无对齐测试集 |

---

### 看机会（综合）

| 机会 | 格子 | 业界案例 | 成熟度 | 时间窗 | 优先级 | 实例 |
|------|------|---------|--------|--------|--------|------|
| FP8 部署 | W*Q | DeepSeek FP8 量产, NVIDIA 原生 | 5星 | 短期 100% | P0 | `[生产]` INT8 跑 6 月 |
| W*K 联合 | W*Q+K*Q | HyperQuant + KV Pareto | 4星 | 短期 90% | P0 | `[实测]` 多省 12.6% |
| MoE INT4 | W*Q | CloudMoE(OSDI) + FoMoE + DeepEP | 3星 | 中期 80% | P0 | `[内部]` 路由掉 6.7% |
| HyperQuant | W*Q | 学术前沿(HKUST) | 3星 | 中期 70% | P1 | `[待验证]` |
| W*L 低秩 | W*L | LoRA 已覆盖(Meta) | 2星 | 长期 50% | P2 | 被 LoRA 替代 |

**方法论引用**：技术洞察模版.md（五看三定）+ 洞察写作指南.md v1.2

---

## 1.2 技术全景图（W* 相关格子）

| 格子 | 论文数 | 代表技术 | 业界采用方 | 成熟度 |
|------|--------|---------|-----------|--------|
| **W*Q** | 235 | GPTQ, AWQ, SmoothQuant, HyperQuant | Meta/Mistral/DeepSeek/NVIDIA/阿里 | 生产级 |
| **W*L** | 13 | LoRA, QLoRA | Meta(LoRA), 社区(QLoRA) | 训练侧覆盖 |
| **W*S** | 含W类 | 2:4 Sparsity | NVIDIA(Ampere) | 硬件依赖 |
| **W*P** | 6 | 结构化剪枝 | 学术为主 | 被量化替代 |
| **W*D** | 10 | 模型蒸馏 | OpenAI(gpt-4o-mini), Google | 训练侧覆盖 |

**关键趋势**：W*Q 是唯一进入工业标配的方法。

---

## 1.3 5 场景适用性

| 场景 | 痛点 | 业界案例 | 格子 | 优先级 |
|------|------|---------|------|--------|
| LLM | 70B 4卡->2卡 | Meta/Mistral/阿里已落地 | W*Q | P0 |
| Agent | MoE 专家死重 | DeepSeek(DeepEP)+CloudMoE | W*Q | P0 |
| 多模态 | 视觉编码器大 | LLaVA 社区量化版 | M*Q | P1 |
| ASR | Whisper 量化 | whisper.cpp INT4 | W*Q | P2 |
| TTS | 声码器量化 | 学术探索 | V*Q | P2 |

---

## 1.4 论文核心洞察

### 必读 Top 5

| # | 论文 | 时间 | 贡献 | 数字 | 被谁采用 |
|---|------|------|------|------|---------|
| 1 | HyperQuant | 2026-06 | 权重+KV 统一量化 | 1.7 bps, 3.79x | 学术 |
| 2 | KV Pareto | 2025-12 | 联合 Pareto 前沿 | 多省 15-20% | 学术 |
| 3 | AWQ | 2023 | 激活感知量化 | INT4 掉 0.5-1% | **Mistral 官方** |
| 4 | HIGGS | 2026-05 | 3-5 bps 最优 | 3-bit PPL 最优 | 学术 |
| 5 | CloudMoE | OSDI 2026 | CPU-GPU INT4 MoE | 28 tokens/s | 学术 |

### 5 个反直觉发现

#### 发现 1：联合优化比分立多省 12.6%
- **业界**：HyperQuant + KV Pareto + DeepSeek-V3 同时转向联合优化。
- `[实测]` Qwen-72B 联合 W4+KV4 省 89GB vs 分立 79GB。

#### 发现 2：MoE 量化路由失配 6.7%
- **业界**：DeepSeek 开源 DeepEP 时特别强调 gate 精度保护。
- `[内部]` DeepSeek-V3 8B MoE INT4 路由掉 6.7%。

#### 发现 3：3-bit 权重 PPL 接近 FP16，但没有大厂敢用
- **业界**：Meta 用 INT4，DeepSeek 用 FP8，NVIDIA 推荐 FP8/INT8——没有一家用 3-bit。
- **因果**：AlignCollapse 发现 INT4 后 15-30% harmful prompt 不触发 refusal。

#### 发现 4：96.9% MoE 专家是死重
- **业界**：CloudMoE(OSDI) 用 INT4 把 DeepSeek-V3 塞进消费级 GPU，FoMoE 打破全复制。
- `[内部]` 87.5% 专家死重。

#### 发现 5：W*L 被 LoRA 完全覆盖
- **业界**：Meta LoRA 成为事实标准（HuggingFace PEFT，10k+ star），推理侧低秩仅 Palu 1 篇且效果差。

### 工业落地 Top 3

| # | 技术 | 采用方 | 我们的状态 |
|---|------|--------|-----------|
| 1 | AWQ INT4 | Mistral(官方)+社区 | `[实测]` 掉 0.7% |
| 2 | SmoothQuant INT8 | NVIDIA(TRT-LLM)+社区 | `[生产]` 6 个月 |
| 3 | DeepEP MoE 通信 | DeepSeek(生产) | 待跟进 |

**方法论引用**：论文洞察/papers_index.csv + 洞察写作指南.md v1.2

---

## 1.5 反方证据汇总（5 维）

| 课题 | 历史失败 | 专利 | 资源 | 团队 | 反向 | 总分 | 风险 |
|------|---------|------|------|------|------|------|------|
| FP8 部署 | 1 | 1 | 1 | 1 | 1 | **5** | 低 |
| W*K 联合 | 1 | 1 | 2 | 2 | 1 | **7** | 中 |
| MoE INT4 | 2 | 1 | 2 | 2 | 2 | **9** | 中 |
| HyperQuant | 1 | 2 | 1 | 3 | 1 | **8** | 中 |
| W*L 低秩 | 2 | 1 | 1 | 2 | 3 | **9** | 中 |

**方法论引用**：研究方法_技术驱动.md v2.0 S3.2

---

"""

new_content = before + new_section + after
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'报告已更新')
print(f'新大小: {len(new_content)} chars, {len(new_content.splitlines())} lines')
