---
type: mode-selection
created:
purpose: research-mode-selection
---

# 研究模式选择器

> 基于 Academic Research Skills v3.10 Mode Spectrum
> 25种模式，3大类别

---

## 模式光谱 (Mode Spectrum)

| 类别 | 数量 | 特点 | 适用场景 |
|------|------|------|----------|
| **Fidelity (保真)** | 14 (56%) | 模板化、可预测输出 | 格式转换、引用检查、快速简报 |
| **Balanced (平衡)** | 7 (28%) | 默认行为 | 完整研究、论文撰写 |
| **Originality (原创)** | 4 (16%) | 探索性、模板轻 | 苏格拉底引导、深度研究 |

---

## Deep Research 模式 (7种)

```dataview
TABLE mode, spectrum, output, oversight, triggers
WHERE type = "mode-reference"
WHERE skill = "deep-research"
```

| 模式 | 光谱 | 输出 | 监督等级 | 触发关键词 |
|------|------|------|----------|------------|
| **full** | Balanced | 完整研究报告 (3000-8000词 APA格式) | High | "research [topic]", "deep research" |
| **quick** | Fidelity | 简报 (500-1500词) | Medium | "quick brief", "30 minute summary" |
| **review** | Balanced | 论文评审报告 | High | "review this paper", "evaluate" |
| **lit-review** | Fidelity | 带注释的文献目录 | Medium | "literature review", "annotated bibliography" |
| **fact-check** | Fidelity | 逐声明验证报告 | Medium | "verify claims", "fact-check" |
| **socratic** | Originality | 研究计划摘要 + INSIGHT | Very High | "guide my research", "help me think" |
| **systematic-review** | Fidelity | PRISMA 报告 (5000-15000词) | Medium | "systematic review", "meta-analysis", "PRISMA" |

---

## Academic Paper 模式 (10种)

| 模式 | 光谱 | 输出 | 监督等级 | 触发关键词 |
|------|------|------|----------|------------|
| **full** | Balanced | 完整论文 (IMRaD) | High | "write a paper", "academic paper" |
| **plan** | Originality | 章节计划 + INSIGHT (苏格拉底) | Very High | "guide my paper", "help me plan" |
| **outline-only** | Balanced | 详细大纲 + 证据图 | High | "paper outline", "just need an outline" |
| **revision** | Fidelity | 修订稿 + 逐点回应 | High | "revise paper", "incorporate feedback" |
| **revision-coach** | Balanced | 修订路线图 + 回复信骨架 | Medium | "parse reviews", "I got reviewer comments" |
| **abstract-only** | Fidelity | 双语摘要 (中文+英文) | Medium | "write abstract" |
| **lit-review** | Fidelity | 文献综述论文 | Medium | "literature review paper" |
| **format-convert** | Fidelity | 格式化文档 (LaTeX/DOCX/PDF) | Low | "convert to LaTeX", "convert citations" |
| **citation-check** | Fidelity | 引用错误报告 | Low | "check citations", "verify references" |
| **disclosure** | Fidelity | 场地特定AI使用声明 | Low | "AI disclosure for [venue]" |

---

## Academic Paper Reviewer 模式 (6种)

| 模式 | 光谱 | 输出 | 监督等级 | 触发关键词 |
|------|------|------|----------|------------|
| **full** | Balanced | 5份评审报告 + 主编决定 | High | "review paper", "peer review" |
| **re-review** | Fidelity | 修订验证清单 + 残留问题 | Medium | "check revisions", "verification review" |
| **quick** | Fidelity | 主编快速评估 + 关键问题 | Low | "quick review", "quick look" |
| **methodology-focus** | Fidelity | 方法论深度评审 | Medium | "check methodology", "focus on methods" |
| **guided** | Originality | 苏格拉底式逐问题对话 | Very High | "guide me to improve" |
| **calibration** | Fidelity | 校准报告 (FNR/FPR/AUC) | Medium | "calibrate reviewer" |

---

## 监督等级说明

| 等级 | 含义 |
|------|------|
| **Very High** | 用户主导对话或每阶段强制检查点 |
| **High** | 用户确认关键决策 (RQ、大纲、配置) |
| **Medium** | 结构性格式，有限决策点 |
| **Low** | 机械/模板驱动，最小人工输入 |

---

## 快速选择指南

### 根据你的目标选择

```
我的目标是：
├── 只想快速了解某个话题 → deep-research quick
├── 想深入研究并形成报告 → deep-research full
├── 需要同行评审 → academic-paper-reviewer full
├── 从头写一篇论文 → academic-paper full
├── 引导式规划论文 → academic-paper plan
├── 已有初稿需要修订 → academic-paper revision
├── 做系统性文献回顾 → deep-research systematic-review
└── 只想核实引用 → academic-paper citation-check
```

### 根据研究阶段选择

```
当前阶段：研究
├── 探索阶段，想法不明确 → deep-research socratic
├── 想法明确，需要全面调研 → deep-research full
└── 需要系统回顾 → deep-research systematic-review

当前阶段：写作
├── 不知道如何组织 → academic-paper plan
├── 知道要写什么 → academic-paper full
└── 已有初稿 → academic-paper revision

当前阶段：评审
├── 想了解改进方向 → academic-paper-reviewer guided
├── 需要正式评审 → academic-paper-reviewer full
└── 验证修订 → academic-paper-reviewer re-review
```

---

## 推荐路径

### 典型研究→论文流程

```
deep-research (socratic) 
    → 明确研究问题
    ↓
deep-research (full)
    → 文献调研 + RQ Brief
    ↓
academic-paper (plan)
    → 引导式规划
    ↓
academic-paper (full)
    → 完整论文初稿
    ↓
Stage 2.5 INTEGRITY GATE
    → 学术诚信检查
    ↓
academic-paper-reviewer (full)
    → 同行评审
    ↓
academic-paper (revision)
    → 修订
    ↓
Stage 4.5 FINAL INTEGRITY
    → 最终诚信检查
    ↓
academic-paper (format-convert)
    → 格式化输出
```

---

## 模式选择记录

**选定的研究技能：**
**选定的写作技能：**
**选定的评审技能：**

**选择理由：**

**预期输出：**

---

*基于 Academic Research Skills v3.10.0 Mode Spectrum*