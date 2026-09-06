# 推理压缩论文必检清单（50篇）

## 一、KV缓存压缩 - 经典/里程碑（10篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 1 | StreamingLLM | 2023 | arXiv | KV streaming开山之作 |
| 2 | PagedAttention/vLLM | 2023 | SOSP | 系统性KV管理典范 |
| 3 | H2O | 2023 | NeurIPS | KV剪枝经典 |
| 4 | KIVI | 2023 | arXiv | 2-bit KV量化先驱 |
| 5 | SnapKV | 2024 | ACL | 懒评估剪枝代表 |
| 6 | FastBERT | 2021 | ACL | Early exit蒸馏代表 |
| 7 | MiniLM | 2020 | EMNLP | 蒸馏经典 |
| 8 | DistilBERT | 2019 | NAACL | 蒸馏开山 |
| 9 | AdaKV | 2025 | ICLR | 自适应KV压缩 |
| 10 | Pyramid-RKV | 2024 | EMNLP | 递归KV压缩 |

## 二、Speculative Decoding（8篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 11 | Speculative Decoding (Leviathan et al.) | 2022 | ICML | SD开山之作 |
| 12 | Medusa | 2023 | arXiv | 多头自测 |
| 13 | Eagle | 2024 | arXiv | 层级预测 |
| 14 | Lookahead | 2024 | NeurIPS | n-gram预测 |
| 15 | REST | 2024 | ICML | 检索增强推测 |
| 16 | Collaborative Speculative Decoding (CoSD) | 2025 | ICLR | 协作SD |
| 17 | SpecInfer | 2023 | OSDI | 系统性SD |
| 18 | SAMRT Self-Speculative Decoding | 2024 | ACL | 自推测 |

## 三、KV量化方法（6篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 19 | KVQuant | 2024 | NeurIPS | KV量化基准 |
| 20 | KTO | 2024 | NeurIPS | KV蒸馏量化 |
| 21 | QServe | 2024 | OSDI | W8A16量化 |
| 22 | AWQ | 2024 | MICRO | activation-aware |
| 23 | GPTQ | 2023 | arXiv | 经典后训练量化 |
| 24 | SmoothQuant | 2023 | ICML | 迁移量化 |
| 25 | RotateKV | 2025 | arXiv | outlier-aware 2-bit |
| 26 | TurboQuant | 2026 | ICLR 2026 | 3-bit零损失 |

## 四、KV剪枝/稀疏（6篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 27 | ChunkKV | 2024 | NeurIPS | 语义chunk剪枝 |
| 28 | InfiniPot-V | 2025 | NeurIPS | 视频流KV |
| 29 | CurDKV | 2025 | NeurIPS | CUR分解剪枝 |
| 30 | RocketKV | 2025 | ICML | 两阶段剪枝 |
| 31 | ClusterKV | 2025 | DAC | 语义可召回 |
| 32 | DMC | 2023 | ACL | 动态稀疏 |

## 五、系统/框架论文（5篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 33 | FlexGen | 2023 | ASPLOS | offloading系统 |
| 34 | LightLLM | 2023 | GitHub | 高效推理框架 |
| 35 | TensorRT-LLM | 2023 | NVIDIA | 工业级框架 |
| 36 | DeepSeek-V2 | 2024 | arXiv | MLA创新 |
| 37 | MoE-LLaMA | 2023 | arXiv | MoE稀疏 |

## 六、低秩/结构化方法（5篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 38 | LoRA | 2022 | arXiv | 低秩适配代表 |
| 39 | GLoRE | 2023 | NeurIPS | 梯度低秩 |
| 40 | SpecTP | 2024 | OSDI | tensor parallelism |
| 41 | FlashAttention | 2022 | ICML | IO感知attention |
| 42 | FlashAttention-2 | 2023 | arXiv | 升级版 |
| 43 | FlashAttention-3 | 2024 | arXiv | FP8支持 |

## 七、多模态/多任务（4篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 44 | MixKV | 2025 | OpenReview | VLLM KV |
| 45 | ScaleKV | 2025 | NeurIPS | VAR模型KV |
| 46 | LLaVA | 2024 | NeurIPS | 多模态压缩 |
| 47 | VideoLLM | 2024 | CVPR | 视频时序压缩 |

## 八、2025-2026热点（6篇）

| # | 论文 | 年份 | 会议/arXiv | 必检原因 |
|---|------|------|------------|----------|
| 48 | DMS | 2025 | NeurIPS | 动态记忆稀疏 |
| 49 | CommVQ | 2025 | ICML | 交换量化 |
| 50 | InfoKV | 2026 | arXiv | 信息论剪枝 |
| 51 | HyperQuant | 2026 | arXiv | 统一权重KV量化 |
| 52 | STAR-KV | 2026 | arXiv | 低秩+量化混合 |
| 53 | KVServe | 2026 | SIGCOMM | 服务感知压缩 |
| 54 | YouZhi | 2026 | arXiv | GQA→MLA蒸馏 |

---

## 验证清单

使用以下命令验证50篇论文的覆盖情况：

```bash
# 检查StreamingLLM, PagedAttention, H2O, KIVI, SnapKV是否在strict corpus
grep -E "StreamingLLM|PagedAttention|H2O|KIVI|SnapKV" inference_compression_strict.json | wc -l

# 检查AWQ, GPTQ, SmoothQuant, KVQuant
grep -E "AWQ|GPTQ|SmoothQuant|KVQuant" inference_compression_strict.json | wc -l

# 检查FlashAttention系列
grep -E "FlashAttention" inference_compression_strict.json | wc -l
```
