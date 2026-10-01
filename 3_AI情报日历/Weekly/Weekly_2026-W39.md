---
created: 2026-09-25
updated: 2026-09-25
type: weekly-report
window: 2026-W39
status: draft
tags: [AI推理, 周报, radar]
---
# 周报 2026-W39（AI 推理雷达）

窗口: 2026-09-06 → 2026-09-25
生成: 2026-09-25 | 来源: GitHub release + arXiv 自动同步 + 高优先深读

## 本期概览

- 新增信号卡 14 张（6 GitHub release + 8 arXiv 论文），全部 `candidate/verify`（overall 2.5）
- 深读 3 张高优先卡（下述）
- 修复脚本 bug：PS 5.1 下 `ConvertFrom-Json -Depth` 不兼容导致 checkpoint 重置；信号卡模板缺 BOM 导致中文乱码

## 高优先深读摘要

### 1. DeepSeek-V4.1-Flash：KV Cache 压缩天花板信号
- 来源事实：552B MoE + CED 架构，decode 激活 16B/token、prefill 仅 8B；CSA2 跨层 KV 复用 + FP4 → 全局 KV 890 bytes/token（V4-Flash 的 1/4）；SWA Bounded Replay → 持久 KV 降至 1/8；45T tokens 多模态预训练
- Codex 分析：KV 压缩里程碑式信号，方向 = 跨层复用 + 低比特；但压缩绑定自家 CED 架构，非通用 serving 插件
- 待验证：890 bytes/token 测量协议、精度退化幅度、昇腾/vLLM 栈可复现性
- 卡：[[2026-09-25_DeepSeek-V4.1-Flash_ Pushing the Limits of KV Cache Compression]]

### 2. GLM-5.3-Flash 混合状态缓存恢复（落地验证）
- 来源事实：vLLM + LMCache + 4-way TP 下，complete-hit 恢复时 scheduler 少计 1 token；strict-prefix lookup 修复后生成一致性 34/36→36/36，120 请求输出全等；CPU reload 场景 TTFT -46%~-64%、总请求时间 -1.9%~-7.0%（相对 modified cold recomputation）
- Codex 分析：这是雷达 hybrid-attention 主线最直接的落地证据，给出可复现修复路径；但限于单模型（GLM-5.3-Flash NVFP4）+ 受控配置
- 待验证：并发 serving 收益、质量等价、vLLM/LMCache 版本范围
- 卡：[[2026-09-25_Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM and LMCache]]

### 3. KVSET：KV Cache 容量规划
- 来源事实：online analyzer，Mattson stack 算法在线估计命中率、避免逐容量模拟；按目标命中率用最大 LRU depth 反推最小缓存容量；生产 trace 验证接近实测；开源支持 online + offline replay
- Codex 分析：解决"缓存配多大才够"的运营问题，与 LMCache/Mooncake 部署互补，与 #1 #2 形成"压缩+复用+容量规划"闭环
- 待验证：开源实现成熟度、trace 代表性、与昇腾/vLLM 集成收益
- 卡：[[2026-09-25_The KV Cache Working Set_ Online Capacity Planning for LLM Inference Systems]]

## 新增信号一览（非深读）

- vLLM v0.28.0 → **v0.30.0**（serving）
- SGLang v0.5.19 → **v0.5.20**（serving）
- llama.cpp v0.4.0 → **v0.5.0**（compression）
- DeepSpeed v0.19.6 → **v0.19.7**（distributed）
- Megatron-LM core_v0.19.0 → **core_v0.19.2**（distributed）
- LMCache operator-v0.5.4 → **v0.5.5**（memory）
- HySparse2 混合稀疏注意力双层 KV 共享（arXiv 2609.26368）
- Crossflow：agentic serving prefill-decode 弹性（arXiv 2609.27085）
- Weave：MoE megakernel SM 调度（arXiv 2609.21483）
- 并行 drafter 投机解码（arXiv 2609.27396）
- TierKV：端侧多级 KV 缓存（arXiv 2609.21172）

## 建议行动

1. **深读** #1 DeepSeek-V4.1-Flash 正文与 HF checkpoint，确认 890 B/token 测量协议
2. **对照** #1 与昇腾 KV 压缩方案（CANN/分布式解耦）的可行性
3. **跟进** #2 的 strict-prefix 修复是否进入 vLLM/LMCache 上游（关注 [[2026-09-25_LMCache release v0.5.5]]）
4. **试用** #3 KVSET 开源实现跑本地 serving trace
5. 未建卡的约 70 篇 arXiv 相关论文按主题按需补卡
