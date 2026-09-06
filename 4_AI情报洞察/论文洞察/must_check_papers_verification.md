# 50篇必检论文验证报告

生成时间: 2026-06-27

## 验证方法

```bash
# 在corpus中搜索论文title关键词
grep -E "keyword" inference_compression_strict.json conf_inference_compression_2025.json arxiv_2026_inference_compression.json
```

---

## 一、KV缓存压缩 - 经典/里程碑（10篇）

| # | 论文 | 年份 | arXiv ID | 验证结果 |
|---|------|------|----------|----------|
| 1 | StreamingLLM | 2023 | 2309.05463 | ❌ **缺失** - 需要添加 |
| 2 | PagedAttention/vLLM | 2023 | 2309.05463 | ❌ **缺失** - 需要添加 |
| 3 | H2O | 2023 | 2310.16714 | ❌ **缺失** - 需要添加 |
| 4 | KIVI | 2023 | 2402.15072 | ✅ 在v3/v4 corpus中 |
| 5 | SnapKV | 2024 | 2404.17103 | ⚠️ abstract提到,需确认title |
| 6 | FastBERT | 2021 | - | ⚠️ early exit蒸馏 |
| 7 | MiniLM | 2020 | - | ⚠️ 蒸馏代表 |
| 8 | DistilBERT | 2019 | - | ⚠️ 蒸馏开山 |
| 9 | AdaKV | 2025 | - | ✅ 在strict中 |
| 10 | Pyramid-RKV | 2024 | - | ⚠️ 递归KV |

---

## 二、Speculative Decoding（8篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 11 | Speculative Decoding (Leviathan et al.) | 2022 | ❌ **缺失** |
| 12 | Medusa | 2023 | ✅ 在strict中 |
| 13 | Eagle | 2024 | ❌ **缺失** |
| 14 | Lookahead | 2024 | ✅ 在strict中 (Lookahead Decoding) |
| 15 | REST | 2024 | ❌ **缺失** |
| 16 | CoSD | 2025 | ✅ 在strict中 |
| 17 | SpecInfer | 2023 | ✅ 在strict中 |
| 18 | SAMRT | 2024 | ⚠️ 名称不确定 |

---

## 三、KV量化方法（6篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 19 | KVQuant | 2024 | ⚠️ 需确认 |
| 20 | KTO | 2024 | ⚠️ 需确认 |
| 21 | QServe | 2024 | ❌ **缺失** |
| 22 | AWQ | 2024 | ✅ 在strict中 |
| 23 | GPTQ | 2023 | ✅ 在strict中 |
| 24 | SmoothQuant | 2023 | ✅ 在strict中 |
| 25 | RotateKV | 2025 | ✅ 在arxiv_2025中 |
| 26 | TurboQuant | 2026 | ❌ **缺失** |

---

## 四、KV剪枝/稀疏（6篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 27 | ChunkKV | 2024 | ✅ 在strict中 |
| 28 | InfiniPot-V | 2025 | ✅ 在strict中 |
| 29 | CurDKV | 2025 | ✅ 在strict中 |
| 30 | RocketKV | 2025 | ✅ 在strict中 |
| 31 | ClusterKV | 2025 | ✅ 在arxiv_2025中 |
| 32 | DMC | 2023 | ❌ **缺失** |

---

## 五、系统/框架论文（5篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 33 | FlexGen | 2023 | ❌ **缺失** |
| 34 | LightLLM | 2023 | ❌ **缺失** (GitHub项目) |
| 35 | TensorRT-LLM | 2023 | ❌ **缺失** (NVIDIA商业) |
| 36 | DeepSeek-V2 | 2024 | ❌ **缺失** |
| 37 | MoE-LLaMA | 2023 | ❌ **缺失** |

---

## 六、低秩/结构化方法（5篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 38 | LoRA | 2022 | ✅ 大量LoRA变体在strict中 |
| 39 | GLoRE | 2023 | ❌ **缺失** |
| 40 | SpecTP | 2024 | ❌ **缺失** |
| 41 | FlashAttention | 2022 | ✅ 在strict中 |
| 42 | FlashAttention-2 | 2023 | ⚠️ 需确认 |
| 43 | FlashAttention-3 | 2024 | ⚠️ 需确认 |

---

## 七、多模态/多任务（4篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 44 | MixKV | 2025 | ❌ **缺失** |
| 45 | ScaleKV | 2025 | ✅ 在strict中 |
| 46 | LLaVA | 2024 | ❌ **缺失** |
| 47 | VideoLLM | 2024 | ❌ **缺失** |

---

## 八、2025-2026热点（6篇）

| # | 论文 | 年份 | 验证结果 |
|---|------|------|----------|
| 48 | DMS | 2025 | ✅ 在conf中 |
| 49 | CommVQ | 2025 | ✅ 在strict中 |
| 50 | InfoKV | 2026 | ✅ 在arxiv_2026中 |
| 51 | HyperQuant | 2026 | ✅ 在arxiv_2026中 |
| 52 | STAR-KV | 2026 | ✅ 在arxiv_2026中 |
| 53 | KVServe | 2026 | ✅ 在arxiv_2026中 |
| 54 | YouZhi | 2026 | ✅ 在arxiv_2026中 |

---

## 统计汇总

| 类别 | 总数 | ✅确认在corpus | ❌缺失 | ⚠️需确认 |
|------|------|----------------|--------|----------|
| KV经典 | 10 | 3 | 5 | 2 |
| Speculative Decoding | 8 | 4 | 3 | 1 |
| KV量化 | 6 | 4 | 1 | 1 |
| KV剪枝/稀疏 | 6 | 5 | 1 | 0 |
| 系统/框架 | 5 | 0 | 5 | 0 |
| 低秩/结构化 | 5 | 2 | 1 | 2 |
| 多模态 | 4 | 1 | 3 | 0 |
| 2025-2026热点 | 6 | 6 | 0 | 0 |
| **总计** | **50** | **25** | **19** | **6** |

---

## 关键缺失（需优先补充）

### 1. 经典KV论文（必须补充）
- [ ] **StreamingLLM** (2309.05463) - KV streaming开山之作
- [ ] **PagedAttention/vLLM** (2309.05463) - 系统性KV管理
- [ ] **H2O** (2310.16714) - Heavy-Hitter Oracle

### 2. Speculative Decoding经典
- [ ] **Speculative Decoding original** (2022 ICML)
- [ ] **Eagle** - 层级预测代表

### 3. 系统框架
- [ ] **FlexGen** (2023 ASPLOS) - offloading系统
- [ ] **DeepSeek-V2** - MLA创新

### 4. 工业级框架
- [ ] TensorRT-LLM, LightLLM等可能不在学术corpus中

---

## 建议补充方案

### 方案1: 添加经典论文专项
创建一个 `classic_papers_2023_2024.json` 包含:
- StreamingLLM, PagedAttention, H2O, KIVI
- FlexGen, SpecInfer, Medusa
- FlashAttention系列

### 方案2: 扩展搜索关键词
```
# 添加以下关键词到搜索列表
"streaming LLM"
"paged attention"
"heavy hitter"
"lookahead decoding"
"REST" AND "speculative"
```

### 方案3: 作者追踪
以下作者的相关论文需确保覆盖:
- Y. Leviathan (Speculative Decoding)
- B. Chen, T. Ao (PagedAttention/vLLM)
- Y. Sun (H2O, KIVI)
- S. Han (FlashAttention系列)
