# AI Intelligence OS

四层Agent情报工作流系统：从信号采集到战略洞察的完整自动化流水线。

## 核心特性（整合Paper-Analysis优秀设计）

### 1. Signal采集层增强
- **多源类型支持**：RSS/Atom/HuggingFace API/GitHub/arXiv/Web
- **信源优先级体系**：P0/P1分级，优先采集高优先级信源
- **增量更新**：去重机制，已采集内容不重复抓取
- **信号持久化**：采集结果存储到本地JSON，支持历史回溯
- **BeautifulSoup解析**：Web页面链接提取
- **重试机制**：requests重试 + 指数退避

### 2. Filtering过滤层
- **自动去重**：基于MD5的信号ID去重
- **四维度评分**：技术深度 × 工程影响 × 趋势强度 × 行业影响
- **三分级输出**：Top Signal(8-10分) / Weak Signal(4-7分) / Noise(1-3分)
- **问题空间绑定**：自动关联到5个预设问题空间

### 3. Knowledge知识图谱层
- **技术关联建模**：依赖/替代/演化/上下游关系梳理
- **问题空间绑定**：信号自动归类到PS1-PS5
- **新兴方向识别**：发现新技术方向时自动标记

### 4. Insight洞察报告层
- **日报**：每日08:30自动生成，包含Top信号、异常预警
- **周报**：每周日20:00生成，包含趋势判断、短期预判
- **月报**：每月末21:00生成，包含战略预测、布局建议

## 快速开始

### 1. 安装依赖

```bash
pip install feedparser requests beautifulsoup4
```

### 2. 运行

```bash
# 每日工作流
python main.py --mode daily

# 主题分析（如"模型量化"）
python main.py --mode topic --topic "模型量化"

# 完整流水线
python main.py --mode full

# 周报
python main.py --mode weekly

# 月报
python main.py --mode monthly
```

## 数据流程

```
信源配置 (config/sources_rss.json)
    ↓
SignalCollector 采集 (layers/signal/)
    ↓
信号存储 (data/articles/signals.json) ← 持久化
    ↓
FilteringAgent 过滤 (layers/filtering/)
    ↓
三级分类: Top/Weak/Noise
    ↓
KnowledgeAgent 图谱 (layers/filtering/)
    ↓
问题空间绑定 PS1-PS5
    ↓
InsightAgent 报告 (layers/insight/)
    ↓
输出: data/reports/{daily,weekly,monthly}_{date}.txt
```

## 五个核心问题空间

| ID | 问题空间 | 核心问题 |
|----|----------|----------|
| PS1 | 推理吞吐与延迟优化 | Decode瓶颈、吞吐提升 |
| PS2 | Agent Runtime稳定性 | 资源抢占、任务颠簸 |
| PS3 | 系统成本与ROI | 单Token成本、算力效率 |
| PS4 | 多Agent协同 | 跨Agent通信与协作 |
| PS5 | 持久化记忆与存储 | Agent记忆系统构建 |

## 配置信源

编辑 `config/sources_rss.json`，添加新的RSS/Atom源：

```json
{
  "id": "my_source",
  "name": "My Source",
  "url": "https://example.com/feed.xml",
  "type": "rss",
  "category": "tech_blog",
  "priority": "P0",
  "language": "en"
}
```

## 已知问题

**MiniMax-M2.7模型输出较长思考过程**：模型默认输出verbose的思考过程，影响纯文本提取效率。如需纯净输出，建议后续切换至GPT-4o或Claude-3.5。

## 与Paper-Analysis工具整合

本系统整合了 `Paper-Analysis` 工具的优秀设计：
- **SourceManager**：配置化信源管理，支持优先级/分类筛选
- **SignalStore**：增量更新的信号持久化存储
- **Article数据结构**：包含authors、tags、language等丰富元数据
- **BeautifulSoup解析**：Web页面链接提取
- **重试机制**：requests重试 + 指数退避