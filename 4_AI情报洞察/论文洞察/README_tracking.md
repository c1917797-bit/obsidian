# 论文收集体系 - 持续追踪机制

## 当前文件结构

```
4_AI情报洞察/
├── inference_compression_strict.json    # Top 6 venues 2025 (2,757篇)
├── conf_inference_compression_2025.json  # Broader venues 2025 (3,876篇)
├── arxiv_2026_inference_compression.json # arXiv 2026 (65篇)
├── arxiv_2025_inference_compression.json # arXiv + 非top venues 2025 (新增)
├── 论文洞察/
│   ├── _corpus/                         # 按会议分类的markdown
│   ├── trending_papers_tracking.json    # 热门论文追踪 (新增)
│   └── README_tracking.md              # 本文档
```

## 论文来源分类

### Tier 1: Top Venues (严格)
- **会议**: ICLR, NeurIPS, ICML, CVPR, ACL, CoRL
- **年份**: 2025
- **文件**: `inference_compression_strict.json`
- **更新**: 每年会议录取后更新

### Tier 2: Extended Venues
- **会议**: DAC, ICASSP, MLSys, SIGCOMM, ATC, EuroSys, OSDI, ISCA, MICRO, HPCA, NAACL, EMNLP, COLING, AAAI, IJCAI等
- **文件**: `conf_inference_compression_2025.json`
- **更新**: 每年手动补充

### Tier 3: arXiv预印本
- **年份**: 2025, 2026
- **文件**: `arxiv_2026_inference_compression.json`, `arxiv_2025_inference_compression.json`
- **更新频率**: 每月一次

## 热门论文追踪

使用 `trending_papers_tracking.json` 追踪15篇关键论文:

| 论文 | 状态 | 所属文件 |
|------|------|----------|
| TurboQuant | ❌ 缺失 | arxiv_2026 (需补充) |
| PolyKV | ❌ 缺失 | arxiv_2026 (需补充) |
| SHRINKV | ❌ 未找到 | - |
| CurDKV | ✅ NeurIPS 2025 | strict |
| AttentionPredictor | ✅ NeurIPS 2025 | strict |
| ScaleKV | ✅ NeurIPS 2025 | strict |
| InfiniPot-V | ✅ NeurIPS 2025 | strict |
| DMS | ✅ NeurIPS 2025 | conf |
| RocketKV | ✅ ICML 2025 | strict |
| CommVQ | ✅ ICML 2025 | strict |
| ClusterKV | ❌ DAC 2025 | arxiv_2025 (新增) |
| MixKV | ❌ OpenReview | - |
| RelayCaching | ❌ 缺失 | arxiv_2026 (需补充) |
| SemShareKV | ❌ arXiv | arxiv_2025 (新增) |
| KV-CoRE | ❌ ICLR 2026 | - |
| RotateKV | ❌ arXiv | arxiv_2025 (新增) |

## 每月追踪任务

### 每月1日
1. **arXiv搜索**: 运行以下查询
   ```
   "KV cache compression" OR "KV-cache" OR "key-value cache"
   "LLM inference acceleration" OR "LLM inference efficiency"
   "sparse attention" OR "attention compression"
   ```

2. **更新arxiv_2026文件**: 添加新论文

3. **检查顶会**: 关注ICLR/NeurIPS状态

### 每季度
1. **检查trending_papers_tracking.json中的论文状态**
2. **更新论文venue信息**（如arXiv→顶会）
3. **补充非top venues论文**

## arXiv搜索策略

### 关键词组合
```
# KV缓存压缩
"KV cache compression" AND (quantization OR pruning OR sparsification)
"key-value cache" AND (LLM OR transformer)
"KV cache" AND (long-context OR streaming)

# 推理加速
"LLM inference" AND (compression OR efficiency OR acceleration)
"speculative decoding" AND (LLM OR efficiency)
"weight quantization" AND (LLM OR deployment)

# 混合查询
("KV cache" OR "inference compression" OR "LLM efficiency") AND (2025 OR 2026)
```

### 时间筛选
- 2025: `submittedDate:[20250101 TO 20251231]`
- 2026: `submittedDate:[20260101 TO 20261231]`

## 快速检查命令

### 检查热门论文状态
```bash
# 检查trending_papers_tracking.json覆盖率
python -c "import json; d=json.load(open('论文洞察/trending_papers_tracking.json')); print(f\"Total: {len(d['papers'])}, Missing: {sum(1 for p in d['papers'] if not p.get('in_strict_corpus') and not p.get('in_conf_corpus') and not p.get('in_arxiv_2026'))}\")"
```

### 合并所有KV论文
```bash
# 统计所有KV相关论文数量
python -c "
import json
strict = json.load(open('../inference_compression_strict.json'))['papers']
arxiv26 = json.load(open('../arxiv_2026_inference_compression.json'))
arxiv25 = json.load(open('../arxiv_2025_inference_compression.json'))
kv_strict = [p for p in strict if 'kv' in p.get('objects', [])]
print(f'Strict KV: {len(kv_strict)}')
print(f'arXiv 2026 KV: {len(arxiv26)}')
print(f'arXiv 2025 KV: {len(arxiv25)}')
"
```

## 未来扩展

### 2026年顶会追踪
- ICLR 2026 (已开放submission)
- NeurIPS 2026 (submission deadline: May 2026)
- ICML 2026 (submission deadline: Jan 2026)

### 新兴方向关注
- Reasoning模型的KV特点
- Multi-modal KV压缩
- Edge/On-device LLM压缩
- KV缓存的硬件协同设计
