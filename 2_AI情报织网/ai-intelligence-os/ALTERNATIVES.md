# AI Intelligence OS - 替代工具配置指南

## 已安装工具

| 工具 | 用途 | 状态 |
|------|------|------|
| `feedparser` | RSS采集 | ✅ 已内置 |
| `requests` | HTTP请求 | ✅ 已内置 |
| `beautifulsoup4` | HTML解析 | ✅ 已内置 |
| MiniMax API | LLM调用 | ✅ 已配置 |

## 待安装工具（可选）

如需更全面的采集能力，可手动安装：

```powershell
# Twitter/X 采集
python -m pip install snscrape

# YouTube 下载
winget install yt-dlp.yt-dlp

# 视频字幕提取
pip install openai-whisper

# 架构图生成（可选）
pip install mermaid-cli
```

## 替代Hermes Skills的功能映射

| Hermes Skill | 替代方案 | 实现方式 |
|--------------|----------|----------|
| `youtube-skills` | `yt-dlp` + `whisper` | 视频下载+字幕转写 |
| `x-twitter-scraper` | `snscrape` | Twitter内容抓取 |
| `oh-my-hermes` (多Agent) | 已有 `FilteringAgent` | 已实现多Agent编排 |
| `drawio-skill` | `mermaid` / diagrams.net | 架构图导出PNG/SVG |
| `litprog-skill` | `jupyter` + `pandoc` | 文学编程报告 |

## 快速测试

### 1. 测试RSS采集
```python
import feedparser
feed = feedparser.parse("https://huggingface.co/papers/feed")
print(f"获取到 {len(feed.entries)} 条论文")
```

### 2. 测试信号过滤
```bash
cd ai-intelligence-os
python main.py --mode topic --topic "quantization"
```

### 3. 生成报告
```bash
python main.py --mode daily
python main.py --mode weekly
```

## 定时任务配置

### Windows计划任务
```powershell
# 每日08:00
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-NoExit -Command "cd C:\Users\Huawei\Documents\code\ai-intelligence-os; python main.py --mode daily"'
$trigger = New-ScheduledTaskTrigger -Daily -At '08:00'
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "AIIntelligenceOS_Daily"
```

### 每周日20:00周报
```powershell
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-NoExit -Command "cd C:\Users\Huawei\Documents\code\ai-intelligence-os; python main.py --mode weekly"'
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At '20:00'
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "AIIntelligenceOS_Weekly"
```

## 问题排查

### pip安装后模块找不到
```powershell
# 检查Python路径
python -c "import sys; print(sys.path)"

# 检查pip安装位置
python -m pip show <package_name>
```

### API调用失败
```bash
# 测试API连接
cd ai-intelligence-os
python -c "from core.minimax_client import get_client; c = get_client(); print(c.chat([{'role': 'user', 'content': 'hi'}]))"
```

## 当前系统能力

你的 `ai-intelligence-os` 已实现：

- ✅ **Signal采集层**：RSS/GitHub/arXiv/HuggingFace API
- ✅ **Filtering过滤层**：去重、评分(1-10)、三分级(Top/Weak/Noise)
- ✅ **Knowledge知识图谱**：问题空间绑定、技术关联
- ✅ **Insight报告层**：日/周/月报告生成

配合你的264个信息源，可以替代大部分Hermes Skills的数据采集和初步分析功能。