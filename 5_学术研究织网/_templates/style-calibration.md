---
type: style-calibration
author:
discipline:
journal:
created:
updated:
calibration_status: initial
past_papers_analyzed: 0
---

# 风格校准文件 (Style Calibration Profile)

> 基于 Academic Research Skills v3.2 Style Calibration System
> 学习你的写作声音，应用于论文撰写

---

## 基本信息

**作者：**
**学科领域：**
**目标期刊：**
**校准状态：** initial / calibrated / outdated

---

## 六维风格画像

### 1. 句长分布 (Sentence Length Distribution)

**测量指标：**
- 平均句长 (words)：__
- 标准差：__
- 最短句：__
- 最长句：__

**分析：**
- [ ] 主要使用短句
- [ ] 喜欢长短句交替
- [ ] 偏好复杂长句

**目标期刊典型：**

---

### 2. 修饰偏好 (Hedging Preferences)

**测量指标：** 1 (不保守) - 10 (非常保守)

| 维度 | 评分 | 说明 |
|------|------|------|
| Hedging (不确定性表达) | | |
| 过渡词使用频率 | | |
| 报告动词选择 | | |

**常见修饰语：**
- 保守: "suggests", "may", "appears to", "it is possible that"
- 中立: "indicates", "shows", "demonstrates"
- 自信: "proves", "clearly shows", "undoubtedly"

**你的偏好：**
> 记录你常用的hedging表达

---

### 3. 复杂性维度 (Complexity)

**测量指标：** 1 (简洁) - 10 (复杂)

| 维度 | 评分 | 说明 |
|------|------|------|
| 词汇复杂度 | | |
| 句子结构复杂度 | | |
| 概念嵌套深度 | | |

**分析：**
- [ ] 偏好简单直白的语言
- [ ] 适当使用专业术语
- [ ] 允许复杂句式表达复杂思想

---

### 4. 叙述声音 (Narrative Voice)

**测量指标：**

| 维度 | 偏好 | 说明 |
|------|------|------|
| 人称 | first-person / third-person / passive | |
| 主动vs被动 | active / passive / mixed | |
| 个人vs正式 | personal / formal | |

**你的偏好：**

---

### 5. 引用集成风格 (Citation Integration)

**测量指标：**

| 维度 | 评分 | 说明 |
|------|------|------|
| 引用密度 | # citations per 1000 words | |
| 引用位置 | running / bracketed / mixed | |
| 直接引用vs转述 | | |

**常见引用模式：**

**引用示例（分析你的论文得出）：**
```markdown
1. Author (Year) 指出...
2. 已有研究表明... (Author, Year)
3. "直接引用..." (Author, Year, p.##)
```

---

### 6. 注册转移 (Register Shifts)

**测量指标：**

| 位置 | 注册风格 | 说明 |
|------|----------|------|
| 引言 | | |
| 方法 | | |
| 结果 | | |
| 讨论 | | |

**分析：**
- [ ] 方法部分使用正式技术语言
- [ ] 讨论部分更灵活
- [ ] 引言平衡背景与研究贡献

---

## 优先层级 (Priority Hierarchy)

> 风格冲突时按此顺序解决

| 优先级 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| 1 (最高) | 学科规范 | 学科强制要求 | APA格式、术语标准 |
| 2 | 期刊惯例 | 目标期刊要求 | NeurIPS双栏、ICLR引用格式 |
| 3 (最低) | 个人风格 | 作者偏好 | 句长、hedging程度 |

**冲突时自动解决方案：**
- 学科规范 > 期刊 > 个人
- 当个人风格与期刊冲突时，遵循期刊
- 当期刊沉默时，遵循个人偏好

---

## 受保护的修饰短语 (Protected Hedging Phrases)

> 来自 ARS v3.6.7 参考文档
> 这些短语在你的学科中有特殊含义，不可随意修改

| 短语 | 含义 | 使用场景 |
|------|------|----------|
| | | |
| | | |

---

## 写作质量检查触发器

> 当检测到以下模式时，提醒检查

| 代码 | 模式 | 说明 |
|------|------|------|
| WQ01 | AI高频词汇 | "delve", "crucial", "landscape" |
| WQ02 | 过度em dash | 使用超过3个em dash |
| WQ03 | 开头废话 | "It is important to note that" |
| WQ04 | 结构模式警告 | 三项枚举强迫症、均匀段落 |
| WQ05 | 句长无变化 | 所有句子几乎相同长度 |

**你的典型AI词汇：**
> 从你的论文中提取你实际使用的词汇，与AI典型词汇对比

---

## 校准样本分析

### 已分析的论文

| 论文标题 | 年份 | 字数 | 句长均值 | Hedging评分 |
|----------|------|------|----------|-------------|
| | | | | |
| | | | | |
| | | | | |

### 提取的模式

**高频词汇：**
1. 
2. 
3. 

**典型句式：**
1. 
2. 

**过渡词使用：**
1. 
2. 

---

## 校准输出规则

### 生成论文时的风格指导

```
当撰写时：
1. 优先使用 [学科术语]
2. 引用格式：Author (Year) 或 (Author, Year)
3. 句长：平均 __ 词，允许 ±__ 词波动
4. Hedging：使用 __ 级别的保守表达
5. 主动语态优先，但方法部分可接受被动
6. 每段不超过 __ 句
7. 过渡词：__、__、__
```

---

## 更新记录

| 日期 | 更新内容 | 分析论文数 |
|------|----------|------------|
| | 初始创建 | 0 |
| | 更新 | |
| | 更新 | |

---

*基于 Academic Research Skills v3.2 Style Calibration System*