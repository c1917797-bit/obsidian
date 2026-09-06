---
type: literature-corpus-entry
citekey:
title:
authors:
year:
venue:
venue_type:
doi:
url:
abstract:
obtained_via: auto-discovered
obtained_at:
pre_screened_status: unprocessed
pre_screened_reason:
pre_screened_date:
contamination_signals:
  preprint_post_llm_inflection: false
  semantic_scholar_unmatched: null
  openalex_unmatched: null
  crossref_unmatched: null
project:
source_note:
user_notes:
created:
---

# 文献条目: 

> 基于 Academic Research Skills v3.6.4 Convention A (citekey in frontmatter)

---

## 基本信息

| 字段 | 值 |
|------|-----|
| **Citekey** | `<!--ref: -->` |
| **标题** | |
| **作者** | |
| **年份** | |
| **期刊/会议** | |
| **DOI** | |
| **URL** | |

---

## PRE-SCREENED 状态

> 基于 ARS corpus-first, search-fills-gap 协议

**状态：** ⏳ unprocessed / ✅ Included / ❌ Excluded / ⏭️ Skipped

**状态理由：**
- F3 (zero-hit note):
- F4a-F4f (provenance reporting):

**处理日期：**
**处理人：**

---

## 摘要 (Abstract)

> 从原论文/来源提取的摘要

---

## 关键发现 (Key Findings)

1. 
2. 
3. 

---

## 与项目的相关性 (Relevance to Project)

**相关性评分：** /10

**关联点：**
1. 
2. 

---

## 引用锚定 (Citation Anchors)

> 用于 claim-faithfulness 审计
> 格式：`<!--ref:CITEKEY--><!--anchor:KIND:VALUE-->`

### 引用块 (Reference Block)

```markdown
<!--ref: --><!--anchor:quote: -->
> "引文内容"
<!--ref: --><!--anchor:page: -->
p. 
<!--ref: --><!--anchor:section: -->
Section 
```

### 支持的声明 (Supported Claims)

| Claim ID | 声明文本 | 锚点类型 | 锚点值 | 验证状态 |
|----------|----------|----------|--------|----------|
| C01 | | quote | | ⏳ pending |
| C02 | | page | | ⏳ pending |
| C03 | | section | | ⏳ pending |

---

## 引用上下文 (Citation Context)

> 这篇文献在哪些笔记/项目中引用过

```dataview
TABLE file.link, context, date
FROM ""
WHERE contains(outlinks, this.file.link)
```

---

## 污染信号详情 (Contamination Signals Detail)

> Zhao et al. (2026) 发现预印本和文献库不匹配是幻觉引用的重要来源

### 预印本信号
- **preprint_post_llm_inflection**: 
  - 年份 >= 2024 AND (venue in closed-list)
  - 信号说明：2024年后预印本可能受LLM训练数据影响

### 索引不匹配信号
| 索引 | 状态 | 说明 |
|------|------|------|
| Semantic Scholar | | |
| OpenAlex | | |
| Crossref | | |

---

## 元数据

**创建日期：**
**来源笔记：**
**项目关联：**
**最后验证：**

---

*基于 ARS v3.6.4 literature_corpus_entry schema*