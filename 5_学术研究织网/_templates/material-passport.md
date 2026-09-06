---
type: material-passport
project_name:
stage: "1-RESEARCH"
previous_stage:
next_stage: "2-WRITE"
verification_status: pending
ars_mode: full
created: 
updated: 
passport_hash:
---

# 研究项目材料护照 (Material Passport)

> 基于 Academic Research Skills v3.10 Schema 9
> 跟踪研究项目的完整生命周期

---

## 项目概览

**项目名称：**
**创建日期：**
**最后更新：**
**ARS 模式：** `full` / `plan` / `quick` / `systematic-review` / etc.
** Passport Hash：** 

---

## 阶段进度追踪 (Stage Progress Ledger)

```dataview
TABLE stage, status, completed_date, notes
FROM "5_学术研究织网/研究项目"
WHERE project_name = this.project_name
WHERE type = "stage-record"
SORT stage ASC
```

| 阶段 | 状态 | 完成日期 | 备注 |
|------|------|----------|------|
| 1-RESEARCH | 🔄 进行中 | - | |
| 2-WRITE | ⏳ 待开始 | - | |
| 2.5-INTEGRITY | ⏳ 待开始 | - | |
| 3-REVIEW | ⏳ 待开始 | - | |
| 4-REVISE | ⏳ 待开始 | - | |
| 4.5-FINAL_INTEGRITY | ⏳ 待开始 | - | |
| 5-FINALIZE | ⏳ 待开始 | - | |
| 6-PROCESS | ⏳ 待开始 | - | |

**阶段切换记录：**
- 1→2: 
- 2→2.5: 
- 2.5→3: 
- 3→4: 
- 4→4.5: 
- 4.5→5: 
- 5→6: 

---

## 产出物清单 (Artifact Manifest)

> 每个关键产出物都记录在此，包括 SHA-256 哈希用于完整性验证

| 产出物 | 类型 | 创建日期 | Hash | 状态 |
|--------|------|----------|------|------|
| RQ Brief | markdown | | | |
| Methodology Blueprint | markdown | | | |
| Annotated Bibliography | markdown | | | |
| Synthesis Report | markdown | | | |
| Paper Draft | markdown | | | |
| Review Package | markdown | | | |
| Final Paper | markdown | | | |

---

## 文献语料库 (Literature Corpus)

> 基于 ARS v3.6.4 corpus-first, search-fills-gap 协议

```dataview
TABLE citekey, title, year, contamination_signals, pre_screened_status
FROM "4_AI情报洞察/论文洞察/_corpus"
WHERE project = this.project_name
SORT year DESC
```

### PRE-SCREENED 状态统计

| 状态 | 数量 |
|------|------|
| Included | |
| Excluded | |
| Skipped | |

### 污染信号 (Contamination Signals)

| 信号类型 | 检测到 | 说明 |
|----------|--------|------|
| preprint_post_llm_inflection | ☐ | 2024年后预印本 |
| s2_unmatched | ☐ | Semantic Scholar 未匹配 |
| openalex_unmatched | ☐ | OpenAlex 未匹配 |
| crossref_unmatched | ☐ | Crossref 未匹配 |

---

## 重置边界日志 (Reset Boundary Ledger)

> 基于 ARS v3.6.3 可选 passport 重置边界协议

**激活标志：** `ARS_PASSPORT_RESET=1` 时，每个 FULL checkpoint 提升为 context 重置边界

| 类型 | Hash | Stage | 日期 | Pending Decision |
|------|------|-------|------|------------------|
| boundary | | | | |
| boundary | | | | |
| resume | | | | |

---

## 合规历史 (Compliance History)

> 基于 ARS v3.4 Compliance Agent

```dataview
TABLE stage, compliance_type, result, date
FROM "5_学术研究织网"
WHERE type = "compliance_report"
WHERE project = this.project_name
SORT date DESC
```

### PRISMA-trAIce 检查 (系统性回顾模式)

| 检查项 | 状态 |
|--------|------|
| 17项系统性回顾协议 | ☐ |
| RAISE 四原则 | ☐ |
| 8角色矩阵 | ☐ |

---

## 协作深度 (Collaboration Depth)

> 基于 Wang & Zhang (2026) IJETHE 23:11
> **仅供观察，永不阻塞流程**

```dataview
TABLE checkpoint, delegation_intensity, cognitive_vigilance, cognitive_reallocation, zone
FROM "5_学术研究织网"
WHERE type = "collaboration_record"
WHERE project = this.project_name
```

### 协作区域分类

| 区域 | 描述 |
|------|------|
| Zone 1 | 无AI协作 |
| Zone 2 | 浅层/分散AI协作 |
| Zone 3 | 深度伙伴关系 |

### 评分标准

| 维度 | 1-10评分 | 说明 |
|------|----------|------|
| 委派强度 (Delegation Intensity) | | |
| 认知警惕 (Cognitive Vigilance) | | |
| 认知再分配 (Cognitive Reallocation) | | |

---

## 风格校准参考 (Style Calibration Reference)

> 引用项目级别的风格校准文件

**校准文件：** 
**上次更新：**

**关键参数：**
- 句长分布：mean / stddev
- 修饰偏好：hedging / transitions / reporting verbs
- 引用集成风格：
- 学科规范优先级：discipline > journal > personal

---

## 可复现性锁定 (repro_lock)

> 基于 ARS v3.3.5 可选 Artifact 可复现性 Lockfile

```yaml
repro_lock:
  version: "1.0"
  locked_at:
  lock_hash:
  components:
    - name:
      version:
      hash:
```

---

## 备注与注释

**未解决的决策：**
1. 
2. 

**跨阶段备注：**
1. 
2. 

---

## Passport Hash 计算

```
JSON Canonical Form + SHA-256
Version: ARS v3.10 Material Passport Schema 9
```

**计算命令：**
```python
import hashlib
import json

def compute_passport_hash(passport_data: dict) -> str:
    canonical = json.dumps(passport_data, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:12]
```

---

*此护照基于 Academic Research Skills v3.10.0 的 Material Passport Schema 9*