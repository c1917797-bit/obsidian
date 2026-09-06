---
type: integrity-gate
stage: 2.5
project:
created: 
status: pending
mode_1_status: pending
mode_2_status: pending
mode_3_status: pending
mode_4_status: pending
mode_5_status: pending
mode_6_status: pending
mode_7_status: pending
block_status: cleared
user_acknowledgement: false
---

# 学术诚信闸门 — Stage 2.5/4.5

> 基于 Lu et al. (2026, Nature 651:914-919) AI Scientist 研究
> 7类AI研究失败模式检查清单

---

## 项目信息

**项目名称：**
**研究阶段：** 
**检查点类型：** FULL checkpoint
**检查日期：**
**检查者：**

---

## 7类AI研究失败模式检查清单

> ⚠️ **重要**：此检查清单为强制性阻断机制。任何 SUSPECTED 状态都必须解决才能继续。

| 模式 | 描述 | 检查状态 | 详情 |
|------|------|----------|------|
| **M1** | 实现错误通过AI自审 | ⏳ | |
| **M2** | 幻觉引用（虚构文献） | ⏳ | |
| **M3** | 幻觉实验结果 | ⏳ | |
| **M4** | 捷径依赖（取巧特征依赖） | ⏳ | |
| **M5** | 实现错误被包装成"意外发现" | ⏳ | |
| **M6** | 方法论伪造 | ⏳ | |
| **M7** | 框架锁定（在早期阶段锁定） | ⏳ | |

### M1: 实现错误通过AI自审

**检查项目：**
- [ ] 代码/实现是否经过独立验证？
- [ ] 是否有单元测试覆盖关键路径？
- [ ] 实现错误是否被误认为是真实发现？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**备注：**

### M2: 幻觉引用

**检查项目：**
- [ ] 所有引用是否真实存在？
- [ ] 作者名字是否正确？
- [ ] 年份和期刊信息是否匹配？
- [ ] 是否有Vibe Citing（捏造引用）模式？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**参考文献列表：**
```dataview
TABLE citekey, title, year, verification_status
FROM "5_学术研究织网"
WHERE type = "literature-corpus-entry"
SORT citekey ASC
```

**备注：**

### M3: 幻觉实验结果

**检查项目：**
- [ ] 实验结果是否有原始数据支撑？
- [ ] 数据是否经过多次运行验证？
- [ ] 统计显著性是否有明确报告？
- [ ] 是否有p-hacking或假设检验操纵的迹象？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**数据验证：**
- [ ] 原始数据文件存在
- [ ] 数据处理脚本可复现
- [ ] 结果数字核对无误

**备注：**

### M4: 捷径依赖

**检查项目：**
- [ ] 模型是否依赖"作弊"特征？
- [ ] 测试集和训练集是否完全分离？
- [ ] 是否有过拟合迹象？
- [ ] 结果是否在独立测试集上验证？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**备注：**

### M5: 实现错误被包装成"意外发现"

**检查项目：**
- [ ] 发现的"新现象"是否真实？
- [ ] 是否排除实现错误的可能性？
- [ ] 异常结果是否被仔细审查？
- [ ] 是否存在"幸存者偏差"？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**备注：**

### M6: 方法论伪造

**检查项目：**
- [ ] 实验设计是否合理？
- [ ] 对照组设置是否正确？
- [ ] 样本量是否足够？
- [ ] 是否存在选择性报告？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**备注：**

### M7: 框架锁定

**检查项目：**
- [ ] 研究问题是否过于狭窄？
- [ ] 是否考虑了替代解释？
- [ ] 是否有确认偏误迹象？
- [ ] 方法论选择是否受到先入为主的观念影响？

**状态：** CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE

**备注：**

---

## 阻断条件检查

> 🔴 **如果以下任一条件满足，Pipeline 必须停止：**
> - 任何模式的 **SUSPECTED** 状态
> - M1/M3/M5/M6 的 **INSUFFICIENT_EVIDENCE** 状态

| 条件 | 是否触发 | 说明 |
|------|----------|------|
| 存在 SUSPECTED | ☐ | 需解决后才能继续 |
| M1 INSUFFICIENT | ☐ | 必须补充证据 |
| M3 INSUFFICIENT | ☐ | 必须补充证据 |
| M5 INSUFFICIENT | ☐ | 必须补充证据 |
| M6 INSUFFICIENT | ☐ | 必须补充证据 |

---

## 学术诚信总结

### 风险评估

| 风险等级 | 说明 |
|----------|------|
| 🟢 LOW | 所有模式 CLEAR |
| 🟡 MEDIUM | 存在 NOT_APPLICABLE 但无 SUSPECTED |
| 🔴 HIGH | 存在 SUSPECTED 或关键 INSUFFICIENT |

**总体评估：** 

### 发现的潜在问题

1. 
2. 
3. 

### 修复建议

1. 
2. 
3. 

---

## 用户确认 (User Acknowledgement)

> ⚠️ **Stage 2.5 必须通过此确认才能进入 Stage 3 (同行评审)**

我已审查上述所有检查项目，并确认：

- [ ] 所有 CLEAR 状态都经过了我的个人验证
- [ ] 任何 NOT_APPLICABLE 状态都有合理说明
- [ ] 所有潜在问题都已记录并有修复计划
- [ ] 我理解如果存在 SUSPECTED 状态，Pipeline 将被阻塞

**确认人：**
**确认时间：**
**签名：**

---

## 闸门结果

| 结果 | 条件 |
|------|------|
| ✅ **CLEARED** | 所有检查通过，无 SUSPECTED，无关键 INSUFFICIENT |
| 🔴 **BLOCKED** | 存在 SUSPECTED 或关键 INSUFFICIENT |

**最终状态：** 
**如果 BLOCKED，必须解决以下问题：**
1. 
2. 
3. 

---

## 检查记录

**Stage 2.5 检查：** 
**Stage 4.5 检查：** 

*此检查清单基于 Lu et al. (2026) Nature 651:914-919 研究中的 AI Scientist 系统*