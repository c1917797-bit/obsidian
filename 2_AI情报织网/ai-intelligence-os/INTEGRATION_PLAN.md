# AI Intelligence OS - 能力集成规划

## 集成目标
将 paperlists、Paper-Analysis-Renew、drawio-skill 等能力整合进 ai-intelligence-os

## 集成架构

```
ai-intelligence-os/
├── third_party/
│   └── paperlists/              # 38个顶会论文数据
├── layers/
│   ├── paper_analysis/
│   │   ├── __init__.py         # PaperAnalysis, DrawIO, SocialMedia, Video 集成
│   │   ├── conference_papers.py # paperlists 论文数据
│   │   ├── deep_research.py    # oh-my-hermes 深度研究
│   │   └── litrep_report.py    # litprog-skill 文学编程报告
│   └── ...
└── config/
    └── sources_conferences.json # 顶会信源配置
```

## 能力对照表

| 能力 | 来源 | 集成方式 |
|------|------|----------|
| 顶会论文数据 | paperlists | ConferencePaperStore |
| 论文筛选CLI | Paper-Analysis-Renew | PaperAnalysisIntegration |
| 质量门禁 | Paper-Analysis-Renew | 复用已有quality_gate |
| HTML报告 | Paper-Analysis-Renew | PaperAnalysisIntegration.generate_html_report |
| 图表生成 | drawio-skill | DrawIOIntegration |
| 社交舆情 | x-twitter-scraper | SocialMediaIntegration |
| 视频字幕 | youtube-skills | VideoContentIntegration |
| 深度研究 | oh-my-hermes | DeepResearchPipeline |
| 文学编程 | litprog-skill | LiteraryProgrammingReport |

## 新增CLI模式

```bash
# 论文搜索
python main.py --mode papers --venue iclr --year 2025 --keyword transformer

# 图表生成
python main.py --mode diagram --question "multi-agent architecture"

# 深度研究
python main.py --mode research --topic "speculative decoding"
```

## 已集成 ✅
- [x] 多源采集 (RSS/Atom/arXiv/GitHub/Web)
- [x] 四维度评分过滤
- [x] 日/周/月报生成
- [x] Obsidian同步
- [x] paperlists 论文数据集成 (ConferencePaperStore)
- [x] drawio-skill 图表生成 (DrawIOIntegration)
- [x] Paper-Analysis-Renew 工作流 (PaperAnalysisIntegration)
- [x] x-twitter-scraper 社交舆情 (SocialMediaIntegration)
- [x] youtube-skills 视频内容 (VideoContentIntegration)
- [x] oh-my-hermes 深度研究 (DeepResearchPipeline)
- [x] litprog-skill 文学编程报告 (LiteraryProgrammingReport)