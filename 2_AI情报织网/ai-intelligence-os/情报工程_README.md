# 情报工程 (Intelligence Factory)

> AI Native 情报工厂 - 自动化技术情报系统

## 快速开始

```bash
# 每日采集 + Obsidian同步
python IntelligenceFactory/run_obsidian.py --mode sync

# 仅同步到Obsidian（使用已有数据）
python IntelligenceFactory/run_obsidian.py --mode daily

# 生成周报
python IntelligenceFactory/run_obsidian.py --mode weekly

# 自然语言查询
python IntelligenceFactory/run_obsidian.py --mode query --question "本周有哪些热门技术？"
```

## 系统架构

```
情报工程/
├── events/           # 事件层
│   ├── event_schema.py    # 8类Event统一定义
│   └── event_store.py     # SQLite存储
├── ontology/         # 技术本体
│   └── tech_ontology.py   # AI Infra技术分类树
├── agents/           # Agent管道
│   ├── crawler_agent.py   # 采集Agent
│   ├── classifier_agent.py # 分类Agent
│   ├── summarizer_agent.py # 摘要Agent
│   └── evolution_agent.py  # 演化Agent + 战略Agent
├── trends/           # 趋势引擎
│   └── trend_engine.py    # 4类趋势分析
├── insights/         # 洞察生成
│   └── insight_agent.py   # 周报/技术路线/收敛报告
├── obsidian_integration.py  # Obsidian对接
├── run_factory.py    # 主协调器
└── run_obsidian.py   # Obsidian同步版
```

## 核心功能

| 模块 | 功能 |
|------|------|
| **CrawlerAgent** | 38个信源自动采集（RSS/arXiv/GitHub） |
| **ClassifierAgent** | 规则预分类 + LLM深度分类 |
| **EventStore** | SQLite存储，支持时序查询 |
| **TrendEngine** | Heat/Convergence/Productionization/Acceleration |
| **InsightAgent** | 周报、技术路线、收敛报告 |
| **ObsidianIntegration** | 对接到Obsidian vault |

## 输出目录

```
C:\Users\Huawei\Documents\code\Obsidian\Inbox\AIIntelligence\
├── Daily/           # 每日情报
├── Weekly/          # 周度技术演化报告
├── Technical/       # 技术事件卡片
├── Industry/        # 公司战略分析
└── Trends/         # 技术趋势报告
```

## 版本

- v1.0 (2026-05-27): 初始版本
- 核心功能: 信源采集 → 事件存储 → 趋势分析 → Obsidian同步