# 学术研究织网 (ARS Research Layer)

> 基于 Academic Research Skills v3.10 的研究流程
> 集成到你的 AI 情报系统

---

## 🎯 这是什么

这是你的 Obsidian 情报系统的**第5层**，专门用于**深度学术研究**。

与现有的4层系统（信源→织网→日历→洞察）无缝衔接：

```
信源层 → 织网层 → 日历层 → 洞察层 → 研究层
293源   自动化   时序      论文     学术研究
                         洞察     (新增)
```

---

## 📁 目录结构

```
5_学术研究织网/
├── _templates/                    # 7个研究模板
│   ├── socratic-dialogue.md      # 苏格拉底对话
│   ├── integrity-gate-checklist.md # 学术诚信闸门
│   ├── material-passport.md       # 项目护照
│   ├── literature-corpus-entry.md # 文献条目
│   ├── claim-tracking.md         # 声明追踪
│   ├── mode-selection.md          # 模式选择
│   └── style-calibration.md       # 风格校准
├── _queries/                      # 7个 Dataview 查询
├── _scripts/                       # 4个 Python 自动化脚本
│   ├── corpus_adapter.py          # 文献语料库适配器
│   ├── socratic_session.py        # 苏格拉底对话管理器
│   ├── integrity_gate_runner.py   # 诚信闸门运行器
│   └── claim_audit_runner.py       # 声明审计运行器
├── 对话日志/                       # Socratic 对话会话
├── 研究项目/                       # Material Passports
├── 整合检查/                       # Integrity Gate 报告
└── claim_audit/                   # Claim-Faithfulness 审计
```

---

## 🚀 快速开始

### 1. 从论文洞察触发研究

当论文洞察的 `relevance_score >= 85` 且匹配问题空间时：

```bash
python _scripts/corpus_adapter.py --project "my-research"
```

### 2. 运行完整研究流程

```bash
# 在 IntelligenceOS 中集成
python ars_integration.py
```

### 3. 使用苏格拉底对话

```bash
python _scripts/socratic_session.py --project "my-research" --topic "分布式推理优化" --interactive
```

### 4. 运行学术诚信检查

```bash
python _scripts/integrity_gate_runner.py --project "my-research" --stage 2.5
```

---

## 📋 模板说明

| 模板 | 用途 | 关键字段 |
|------|------|----------|
| `socratic-dialogue.md` | 5层苏格拉底对话 | intent, layer, dialogue_health |
| `integrity-gate-checklist.md` | 7类AI失败模式检查 | mode_1-7_status |
| `material-passport.md` | 项目全生命周期追踪 | stage, passport_hash |
| `literature-corpus-entry.md` | 单篇文献条目 | citekey, contamination_signals |
| `claim-tracking.md` | 声明-引用对齐审计 | audit_status, high_warn_count |
| `mode-selection.md` | 25种模式选择指南 | ars_mode |
| `style-calibration.md` | 6维写作风格画像 | hedging, complexity |

---

## 🔧 Dataview 查询

在 Dashboard.md 中新增了以下查询：

- **研究项目进度** - 追踪所有项目的阶段
- **Integrity Gates 状态** - 7模式检查状态
- **活跃 Socratic 对话** - 对话健康状态
- **文献语料库状态** - PRE-SCREENED 统计
- **Claim 审计进度** - 声明验证追踪
- **协作深度分布** - Zone 1/2/3 分类
- **模式使用统计** - ARS 模式分布

---

## 🎓 ARS 核心概念

### 7类AI研究失败模式 (Lu et al. 2026 Nature)

| 模式 | 描述 |
|------|------|
| M1 | 实现错误通过AI自审 |
| M2 | 幻觉引用 |
| M3 | 幻觉实验结果 |
| M4 | 捷径依赖 |
| M5 | Bug伪装成发现 |
| M6 | 方法论伪造 |
| M7 | 框架锁定 |

### 5层苏格拉底对话

1. **问题定义** - 你真正想知道什么？
2. **方法反思** - 你将如何回答？
3. **证据视角** - 证据说了什么？
4. **启示探索** - 这意味着什么？
5. **综合** - 你学到了什么？

### 3大模式类别

- **Fidelity (保真)** - 56%，模板化、可预测
- **Balanced (平衡)** - 28%，默认行为
- **Originality (原创)** - 16%，探索性

---

## 🔗 与现有系统集成

### IntelligenceOS → ARS

论文洞察自动同步到 `_corpus` 目录：
```
paper_insights.py → save_paper_card() → _corpus/{citekey}.md
                                       ↓
                              relevance_score >= 85
                                       ↓
                              ARS 研究流程触发
```

### ARS → 洞察层

```
ARS 研究成果 → 4_AI情报洞察/论文洞察/
             → 报告可被日历层引用
```

---

## 📊 Dashboard 新增面板

查看 `3_AI情报日历/Dashboard.md` 获取以下新面板：

- 研究项目进度表
- Integrity Gates 状态
- 活跃 Socratic 对话
- 文献语料库统计
- Claim 审计进度
- 协作深度分布

---

## ⚙️ 配置

### 问题空间 (Problem Spaces)

编辑 `2_AI情报织网/ai-intelligence-os/config/problem_spaces.json` 定义触发 ARS 研究的问题领域。

### MiniMax API

所有脚本使用与 IntelligenceOS 相同的 MiniMax API 配置。

---

## 🆘 故障排除

**Q: Dataview 查询不显示结果**
A: 确保 frontmatter 字段名匹配查询中的字段名

**Q: Python 脚本导入失败**
A: 确保在 `2_AI情报织网/ai-intelligence-os/` 目录运行，或设置 PYTHONPATH

**Q: 学术诚信闸门被 BLOCKED**
A: 检查报告中 SUSPECTED 的模式，解决后重新运行

---

*基于 Academic Research Skills v3.10.0 | 2026-06-03*