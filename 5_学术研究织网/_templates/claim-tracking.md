---
type: claim-tracking
audit_status: pending
project:
paper_section:
claims_total: 0
claims_verified: 0
claims_failed: 0
claims_pending: 0
high_warn_count: 0
created:
updated:
---

# Claim-Faithfulness 审计跟踪

> 基于 Academic Research Skills v3.8 L3 Claim-Faithfulness System
> 验证每条引用是否真正支撑论文中的声明

---

## 审计概览

| 指标 | 数值 |
|------|------|
| **总声明数** | |
| **已验证** | |
| **失败** | |
| **待处理** | |
| **HIGH-WARN 数量** | |

**审计状态：**
- ⏳ pending - 等待审计
- 🔄 in-progress - 审计进行中
- ✅ verified - 审计完成，无问题
- ⚠️ failed - 审计完成，存在问题
- 🔴 high-warn - 存在 HIGH-WARN 类别

---

## 声明清单 (Claim Manifest)

> 格式：`<!--ref:CITEKEY--><!--anchor:KIND:VALUE-->`

| Claim ID | 声明文本 | 来源 | 锚点类型 | 锚点值 | 支持状态 | HIGH-WARN 类别 |
|----------|----------|------|----------|--------|----------|----------------|
| C01 | | | quote | | ⏳ pending | - |
| C02 | | | page | | ⏳ pending | - |
| C03 | | | section | | ⏳ pending | - |
| C04 | | | paragraph | | ⏳ pending | - |
| C05 | | | none | | ⏳ pending | - |

---

## HIGH-WARN 类别

> 🔴 **以下类别会在 Formatter Terminal Hard Gate 阻止输出**

| 类别代码 | 类别名称 | 说明 |
|----------|----------|------|
| **HW01** | claim-not-supported | 引用来源不支持该声明 |
| **HW02** | negative-constraint-violation | 引用来源明确否定该声明 |
| **HW03** | fabricated-reference | 引用来源完全不存在 |
| **HW04** | anchorless | 声明有引用但无锚点 |
| **HW05** | constraint-violation-uncited | 约束违反但引用缺失 |

---

## 未声明断言 (Uncited Assertions)

> 有声明但没有对应引用的段落

| 位置 | 断言文本 | 建议操作 |
|------|----------|----------|
| | | |
| | | |

---

## 约束违反 (Constraint Violations)

| 违反 ID | 约束内容 | 违反类型 | 来源 | 处理建议 |
|---------|----------|----------|------|----------|
| V01 | | | | |
| V02 | | | | |

---

## 引用-声明对齐验证 (Citation-Claim Alignment)

> 逐条验证引用来源是否真正支撑声明

### 验证模板

```markdown
**声明 (C01):** [声明文本]

**引用锚点:** <!--ref:CITEKEY--><!--anchor:quote:[引文内容片段]-->

**引用原文:**
> [从来源提取的原文]

**验证结果:**
- [ ] 引文确实包含支撑声明的内容
- [ ] 引文的上下文与声明意图一致
- [ ] 无断章取义或过度推广

**判断:** ✅ SUPPORTED / ⚠️ WEAKLY_SUPPORTED / ❌ NOT_SUPPORTED

**备注:**
```

---

## 污染三角验证 (Contamination Triangulation)

> 基于 ARS v3.9.0 三索引三角验证（可选 strict 模式）

| 索引 | 匹配状态 | 说明 |
|------|----------|------|
| Semantic Scholar | | |
| OpenAlex | | |
| Crossref | | |

**三角验证结果：**
- k=0: 无不匹配 → 无标注
- k=1: 单索引不匹配 → LOW-WARN
- k=2: 双索引不匹配 → PARTIAL-UNMATCH
- k=3: 三索引都不匹配 → TRIANGULATION-UNMATCHED

---

## 审计工具失败记录 (Audit Tool Failure Log)

> 当审计工具无法完成某条声明验证时记录在此

| 失败 ID | 声明 ID | 故障类型 | 处理方式 |
|---------|---------|----------|----------|
| UAF01 | | judge_timeout | 重试下一轮 |
| UAF02 | | judge_api_error | 已记录 |
| UAF03 | | cache_corruption | 已记录 |

---

## 最终审计报告

### 摘要

**HIGH-WARN 声明数量：**
**需要修复的声明：**
**建议：**

### 通过条件

> ✅ **审计通过条件：**
> - HIGH-WARN 数量 = 0
> - 所有声明已验证或明确标记为 NOT_APPLICABLE
> - 无 FABRICATED-REFERENCE

> 🔴 **审计阻塞条件：**
> - HIGH-WARN 数量 > 0
> - 存在任何 HW01-HW05 类别

### 审计结论

| 结果 | 条件 |
|------|------|
| **✅ PASSED** | 无 HIGH-WARN |
| **🔴 FAILED** | 存在 HIGH-WARN |

**最终状态：**
**审计人：**
**审计日期：**

---

## 修复跟踪

> HIGH-WARN 声明的修复进度

| Claim ID | 原状态 | 修复措施 | 修复后状态 | 修复日期 |
|----------|--------|----------|------------|----------|
| | | | | |
| | | | | |

---

*此审计基于 Academic Research Skills v3.8 L3 Claim-Faithfulness System*