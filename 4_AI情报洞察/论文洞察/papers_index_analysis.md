# 3876篇论文索引分析报告

> 生成时间: 2026-06-28
> 工具: build_corpus_index.py + recategorize_papers.py + update_papers_index.py
> 数据源: 4_AI情报洞察/论文洞察/_corpus/

---

## 一、总体情况

| 项目 | 数值 |
|------|------|
| 扫描文件 | 1466 个 .md |
| 成功解析 | 1461 篇（99.6%） |
| 解析失败 | 5 个（summary 文件，无 YAML） |
| 已分类 grid | 774 篇（53.0%） |
| 已分类 scenario | 1295 篇（88.6%） |
| 未分类 grid | 687 篇（47.0%） |
| 未分类 scenario | 166 篇（11.4%） |

---

## 二、42格分布

| 格子 | 论文数 | 占比 | 热度 |
|------|--------|------|------|
| S×G | 236 | 16.2% | 🔥🔥🔥🔥🔥 |
| W×Q | 235 | 16.1% | 🔥🔥🔥🔥🔥 |
| C×G | 183 | 12.5% | 🔥🔥🔥🔥 |
| K×Q | 90 | 6.2% | 🔥🔥🔥 |
| W×L | 13 | 0.9% | 🔥 |
| W×D | 10 | 0.7% | 🔥 |
| W×P | 6 | 0.4% | 🔥 |
| K×G | 1 | 0.1% | 观察 |
| Unclassified | 687 | 47.0% | - |

**关键观察**：
- S×G 主要是投机解码 + Agent 调度（与你 P0 Topic 强相关）
- W×Q 主要是权重量化（GPTQ/AWQ/SmoothQuant 等）
- C×G 主要是多卡通信优化（NCCL/TP/PP/EP）
- K×Q 主要是 KV Cache 量化

---

## 三、场景分布

| 场景 | 论文数 | 占比 |
|------|--------|------|
| Agent | 865 | 59.2% |
| LLM | 422 | 28.9% |
| 多模态 | 7 | 0.5% |
| ASR | 1 | 0.1% |
| TTS | 0 | 0% |
| Unclassified | 166 | 11.4% |

**关键观察**：
- 语料严重偏向 Agent 方向（59.2%），符合当前 P0 Topic 设定
- TTS 方向 0 篇，建议补充信源
- 多模态/ASR/TTS 都需要扩展语料

---

## 四、改进建议

### 4.1 短期（1周）
1. **针对 687 篇未分类论文**：
   - 写一个 LLM 分类器，对每篇做摘要+分类
   - 或人工标注一批（50-100篇）作为种子集
2. **TTS/多模态 信源补全**：
   - 添加 TTS 顶会（ICASSP/Interspeech）扫描
   - 添加 CVPR/ICCV 视觉压缩扫描

### 4.2 中期（1月）
1. **元数据增强**：
   - 提取 abstract 关键贡献（用 LLM 摘要）
   - 提取性能数据（speedup, memory reduction）
   - 提取代码链接（reproducibility marker）
2. **检索能力建设**：
   - 建立向量索引（FAISS/ChromaDB）
   - 提供关键词+向量混合检索 API

### 4.3 长期（季度）
1. **自动化流水线**：
   - 每日 arxiv 扫描 → 自动摘要 → 自动分类
   - 每周统计 + 趋势分析
   - 每月报告 + 异常警报

---

## 五、数据质量

### 5.1 已知问题
- 5 个 summary 文件无法被 YAML 解析（建议转格式或跳过）
- 943 篇原始论文无 matched_techs 字段（依赖 abstract 关键词补分类）
- 部分论文 abstract 缺失

### 5.2 下一步清洗
- 补全 5 个 summary 文件的解析逻辑
- 对 687 篇未分类论文做 LLM 辅助分类
- 校验元数据完整性（abstract/year/venue）

---

## 六、文件清单

| 文件 | 路径 | 用途 |
|------|------|------|
| papers_meta.json | 4_AI情报洞察/论文洞察/ | v1 索引（943 未分类） |
| papers_meta_v2.json | 4_AI情报洞察/论文洞察/ | v2 索引（687 未分类） |
| papers_index.csv | 4_AI情报洞察/论文洞察/ | 可用 Excel 打开的索引 |
| build_corpus_index.py | 2_AI情报织网/ai-intelligence-os/ | v1 索引构建 |
| recategorize_papers.py | 2_AI情报织网/ai-intelligence-os/ | v2 重分类 |
| update_papers_index.py | 2_AI情报织网/ai-intelligence-os/ | CSV 更新 |

---

## 七、配套建议

配合 4_AI情报洞察/12格追踪/12格月度趋势追踪表.md 使用：
- 每月跑一次 `recategorize_papers.py` 更新分布
- 每月对比上月变化
- 触发自更新警报（如某格子月增>20%）

---

*生成工具: update_papers_index.py + recategorize_papers.py*
*维护人: 情报工程师*
*下次更新: 2026-07-28*
