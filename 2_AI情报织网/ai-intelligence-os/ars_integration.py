"""
ARS Research Pipeline Integration
将 Academic Research Skills 研究流程集成到 IntelligenceOS

功能:
1. detect_research_intent() - 检测是否触发 ARS 研究
2. run_ars_research_pipeline() - 运行完整 ARS 研究流程
3. sync_to_obsidian() - 同步结果到 Obsidian

集成点:
- paper_insights.py 中的 PaperCard 可以触发研究
- deep_research.py 可以调用 ARS 流程
"""
import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import hashlib

# 路径常量
OBSIDIAN_ROOT = Path("C:/Users/Huawei/Documents/code/Obsidian")
AI_OS_ROOT = Path(__file__).parent.parent
ARS_SCRIPTS_DIR = OBSIDIAN_ROOT / "5_学术研究织网/_scripts"
PROJECT_DIR = OBSIDIAN_ROOT / "5_学术研究织网/研究项目"
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"

# 问题空间配置
PROBLEM_SPACES_FILE = AI_OS_ROOT / "config/problem_spaces.json"


def load_problem_spaces() -> List[str]:
    """加载问题空间列表"""
    if PROBLEM_SPACES_FILE.exists():
        try:
            data = json.loads(PROBLEM_SPACES_FILE.read_text(encoding="utf-8"))
            return data.get("problem_spaces", [])
        except Exception:
            pass
    return ["KV Cache", "Distributed Inference", "Agent", "Memory", "Latency"]


def compute_passport_hash(data: Dict) -> str:
    """计算 Material Passport Hash"""
    canonical = json.dumps(data, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:12]


class ARSIntegration:
    """
    ARS 研究流程集成

    当 paper insight 满足以下条件时触发研究:
    1. relevance_score >= 85
    2. topic 匹配 problem_spaces.json 中的问题空间
    """

    def __init__(self):
        self.problem_spaces = load_problem_spaces()
        self.project_count = 0

    def detect_research_intent(self, paper_card: Dict) -> bool:
        """
        检测是否应该触发 ARS 研究

        Args:
            paper_card: PaperCard dict with fields:
                - title: str
                - relevance_score: float
                - matched_problems: List[str]
                - matched_techs: List[str]
                - venue: str
                - year: int

        Returns:
            True if should trigger ARS research
        """
        # 检查 relevance_score
        relevance_score = paper_card.get("relevance_score", 0)
        if relevance_score < 85:
            return False

        # 检查是否匹配问题空间
        matched_problems = paper_card.get("matched_problems", [])
        for problem in matched_problems:
            if any(ps.lower() in problem.lower() for ps in self.problem_spaces):
                return True

        return False

    def run_ars_research_pipeline(
        self,
        project_name: str,
        topic: str,
        paper_cards: List[Dict],
        ars_mode: str = "full"
    ) -> Dict[str, Any]:
        """
        运行完整 ARS 研究流程

        Args:
            project_name: 项目名称
            topic: 研究主题
            paper_cards: 相关论文卡片列表
            ars_mode: ARS 模式 (full / socratic / systematic-review)

        Returns:
            Dict with project info and output paths
        """
        print(f"\n🧠 ARS 研究流程启动")
        print(f"   项目: {project_name}")
        print(f"   主题: {topic}")
        print(f"   论文数: {len(paper_cards)}")
        print(f"   模式: {ars_mode}")
        print("-" * 50)

        # Step 1: 创建项目目录
        project_dir = PROJECT_DIR / project_name
        artifacts_dir = project_dir / "artifacts"
        corpus_dir = project_dir / "literature_corpus"
        project_dir.mkdir(parents=True, exist_ok=True)
        artifacts_dir.mkdir(exist_ok=True)
        corpus_dir.mkdir(exist_ok=True)

        # Step 2: 同步论文到文献语料库
        print("\n📚 Step 1: 同步论文到文献语料库...")
        corpus_entries = self._sync_papers_to_corpus(paper_cards, corpus_dir)
        print(f"   同步了 {len(corpus_entries)} 篇论文")

        # Step 3: 创建 Material Passport
        print("\n📋 Step 2: 创建 Material Passport...")
        passport = self._create_material_passport(
            project_name=project_name,
            topic=topic,
            ars_mode=ars_mode,
            corpus_entries=corpus_entries,
            project_dir=project_dir
        )

        # Step 4: 生成 Socratic 对话笔记
        print("\n💬 Step 3: 生成 Socratic 对话启动笔记...")
        dialogue_note = self._create_socratic_dialogue_note(project_name, topic, project_dir)

        # Step 5: 生成 Mode Selection 笔记
        print("\n🎯 Step 4: 生成 Mode Selection 笔记...")
        mode_note = self._create_mode_selection_note(project_name, ars_mode, project_dir)

        # Step 6: 生成 Integrity Gate Checklist
        print("\n🔒 Step 5: 生成 Integrity Gate Checklist...")
        integrity_note = self._create_integrity_gate_note(project_name, project_dir)

        print("\n" + "=" * 50)
        print(f"✅ ARS 研究项目创建完成!")
        print(f"   项目目录: {project_dir}")
        print(f"   Passport: {project_dir / 'passport.md'}")

        return {
            "project_name": project_name,
            "project_dir": str(project_dir),
            "passport_path": str(project_dir / "passport.md"),
            "corpus_count": len(corpus_entries),
            "stage": "1-RESEARCH",
            "ars_mode": ars_mode,
            "created_at": datetime.now().isoformat()
        }

    def _sync_papers_to_corpus(
        self,
        paper_cards: List[Dict],
        corpus_dir: Path
    ) -> List[Dict[str, Any]]:
        """将论文卡片同步到文献语料库"""
        entries = []

        for i, card in enumerate(paper_cards):
            # 生成 citekey
            title_words = card.get("title", "untitled").split()[:3]
            citekey = f"{''.join(w[0] for w in title_lines if w[0].isalnum())[:6]}{card.get('year', 2024)}"

            # 构建文献笔记
            entry = {
                "citekey": citekey,
                "title": card.get("title", ""),
                "authors": card.get("authors", "Unknown"),
                "year": card.get("year", 2024),
                "venue": card.get("venue", ""),
                "relevance_score": card.get("relevance_score", 0),
                "abstract": card.get("abstract", ""),
                "url": card.get("url", ""),
                "citations": card.get("citation_count", 0),
                "pre_screened_status": "Included",
                "contamination_signals": {
                    "preprint_post_llm_inflection": False,
                    "semantic_scholar_unmatched": None,
                    "openalex_unmatched": None,
                    "crossref_unmatched": None
                }
            }

            # 写入 markdown 文件
            filename = f"{citekey}.md"
            filepath = corpus_dir / filename

            # 如果已存在，跳过
            if not filepath.exists():
                content = self._format_corpus_entry_md(entry)
                filepath.write_text(content, encoding="utf-8")

            entries.append(entry)

        # 同时复制到 _corpus 目录（主语料库）
        CORPUS_DIR.mkdir(parents=True, exist_ok=True)
        for entry in entries:
            citekey = entry["citekey"]
            filename = f"{citekey}.md"
            filepath = CORPUS_DIR / filename

            if not filepath.exists():
                content = self._format_corpus_entry_md(entry)
                filepath.write_text(content, encoding="utf-8")

        return entries

    def _format_corpus_entry_md(self, entry: Dict) -> str:
        """格式化文献条目 markdown"""
        contamination = entry.get("contamination_signals", {})

        content = f"""---
type: literature-corpus-entry
citekey: {entry.get('citekey', '')}
title: "{entry.get('title', '')}"
authors: {entry.get('authors', '')}
year: {entry.get('year', '')}
venue: {entry.get('venue', '')}
relevance_score: {entry.get('relevance_score', 0)}
pre_screened_status: {entry.get('pre_screened_status', 'Included')}
contamination_signals:
  preprint_post_llm_inflection: {contamination.get('preprint_post_llm_inflection', False)}
  semantic_scholar_unmatched: {contamination.get('semantic_scholar_unmatched', '')}
  openalex_unmatched: {contamination.get('openalex_unmatched', '')}
  crossref_unmatched: {contamination.get('crossref_unmatched', '')}
abstract: |
{entry.get('abstract', '')}
url: {entry.get('url', '')}
created: {datetime.now().isoformat()}
---

# {entry.get('title', '')}

**{entry.get('venue', '')} {entry.get('year', '')}** | Citations: {entry.get('citations', 0)}

## 摘要

{entry.get('abstract', '无摘要')}

## 关键贡献

- 相关性评分: {entry.get('relevance_score', 0)}/100

## 引用格式

```bibtex
<!--ref:{entry.get('citekey', '')}-->
```

---

*由 ARS Integration 自动导入 | {datetime.now().strftime('%Y-%m-%d')}*
"""

        return content

    def _create_material_passport(
        self,
        project_name: str,
        topic: str,
        ars_mode: str,
        corpus_entries: List[Dict],
        project_dir: Path
    ) -> Dict:
        """创建 Material Passport"""
        passport_data = {
            "type": "material-passport",
            "project_name": project_name,
            "topic": topic,
            "stage": "1-RESEARCH",
            "ars_mode": ars_mode,
            "verification_status": "pending",
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat(),
            "passport_hash": "",
            "literature_corpus_count": len(corpus_entries),
            "corpus_entries": corpus_entries
        }

        # 计算 hash
        passport_data["passport_hash"] = compute_passport_hash(passport_data)

        # 写入 passport.md
        passport_path = project_dir / "passport.md"
        content = self._format_passport_md(passport_data)
        passport_path.write_text(content, encoding="utf-8")

        # 写入 passport.json
        json_path = project_dir / "passport.json"
        json_path.write_text(json.dumps(passport_data, ensure_ascii=False, indent=2), encoding="utf-8")

        return passport_data

    def _format_passport_md(self, passport: Dict) -> str:
        """格式化 Passport markdown"""
        corpus_count = passport.get("literature_corpus_count", 0)

        content = f"""---
type: material-passport
project_name: {passport.get('project_name', '')}
stage: {passport.get('stage', '1-RESEARCH')}
verification_status: {passport.get('verification_status', 'pending')}
ars_mode: {passport.get('ars_mode', 'full')}
created: {passport.get('created', '')}
updated: {passport.get('updated', '')}
passport_hash: {passport.get('passport_hash', '')}
---

# 研究项目材料护照 (Material Passport)

> 基于 Academic Research Skills v3.10 Schema 9

---

## 项目信息

| 字段 | 值 |
|------|-----|
| **项目名称** | {passport.get('project_name', '')} |
| **研究主题** | {passport.get('topic', '')} |
| **ARS 模式** | {passport.get('ars_mode', 'full')} |
| **当前阶段** | {passport.get('stage', '1-RESEARCH')} |
| **Passport Hash** | `{passport.get('passport_hash', '')}` |
| **创建时间** | {passport.get('created', '')} |

---

## 阶段进度追踪

| 阶段 | 状态 | 完成日期 |
|------|------|----------|
| 1-RESEARCH | 🔄 进行中 | - |
| 2-WRITE | ⏳ 待开始 | - |
| 2.5-INTEGRITY | ⏳ 待开始 | - |
| 3-REVIEW | ⏳ 待开始 | - |
| 4-REVISE | ⏳ 待开始 | - |
| 4.5-FINAL_INTEGRITY | ⏳ 待开始 | - |
| 5-FINALIZE | ⏳ 待开始 | - |
| 6-PROCESS | ⏳ 待开始 | - |

---

## 文献语料库

**论文数量**: {corpus_count}

```dataview
TABLE citekey, title, year, venue, relevance_score
FROM "4_AI情报洞察/论文洞察/_corpus"
WHERE pre_screened_status = "Included"
SORT relevance_score DESC
LIMIT 20
```

---

## 下一步行动

1. 📖 阅读文献语料库中的论文
2. 💬 开始 Socratic 对话明确研究问题
3. 📝 根据 Mode Selection 确定具体研究模式
4. 🔒 完成后运行 Integrity Gate 检查

---

*Passport Hash: {passport.get('passport_hash', '')} | ARS v3.10*
"""

        return content

    def _create_socratic_dialogue_note(
        self,
        project_name: str,
        topic: str,
        project_dir: Path
    ) -> Path:
        """创建 Socratic 对话启动笔记"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_id = f"socratic_{project_name}_{timestamp}"

        note_path = project_dir / f"{session_id}.md"

        content = f"""---
type: socratic-dialogue
stage: "1-RESEARCH"
intent: exploratory
dialogue_turn_count: 0
layer: 1
layer_name: 问题定义
status: in-progress
project: {project_name}
dialogue_health: healthy
health_alerts: []
insights_gathered: []
created: {datetime.now().isoformat()}
last_updated: {datetime.now().isoformat()}
---

# 苏格拉底对话研究: {topic}

**项目**: {project_name}
**会话ID**: {session_id}
**主题**: {topic}

---

## 研究主题

{topic}

---

## 5层对话结构

| 层级 | 名称 | 状态 | 描述 |
|------|------|------|------|
| L1 | 问题定义 | 🔄 进行中 | 明确真正想研究的问题 |
| L2 | 方法反思 | ⏳ 未开始 | 反思研究方法 |
| L3 | 证据视角 | ⏳ 未开始 | 评估证据质量 |
| L4 | 启示探索 | ⏳ 未开始 | 探索研究发现的意义 |
| L5 | 综合 | ⏳ 未开始 | 整合所学，形成研究计划 |

---

## 对话记录

*从这里开始你的苏格拉底对话*

---

## 洞察收集

*对话过程中发现的洞察会记录在此*

---

*基于 ARS v3.10 Socratic Mentoring System | 会话ID: {session_id}*
"""

        note_path.write_text(content, encoding="utf-8")
        return note_path

    def _create_mode_selection_note(
        self,
        project_name: str,
        ars_mode: str,
        project_dir: Path
    ) -> Path:
        """创建 Mode Selection 笔记"""
        note_path = project_dir / "mode-selection.md"

        content = f"""---
type: mode-selection
project: {project_name}
selected_mode: {ars_mode}
created: {datetime.now().isoformat()}
---

# 研究模式选择: {project_name}

**项目**: {project_name}
**选定模式**: `{ars_mode}`

---

## 当前选择的模式

```dataview
TABLE mode, spectrum, output, oversight
FROM "5_学术研究织网/_templates/mode-selection.md"
WHERE mode = "{ars_mode}"
```

### 模式说明

根据你的研究目标，已选择 **{ars_mode}** 模式。

---

## 可用模式参考

详见: [[5_学术研究织网/_templates/mode-selection]]

---

*ARS v3.10 Mode Selection | {datetime.now().strftime('%Y-%m-%d')}*
"""

        note_path.write_text(content, encoding="utf-8")
        return note_path

    def _create_integrity_gate_note(
        self,
        project_name: str,
        project_dir: Path
    ) -> Path:
        """创建 Integrity Gate Checklist 笔记"""
        note_path = project_dir / "integrity-gate-2.5.md"

        # 复制模板内容
        template_path = OBSIDIAN_ROOT / "5_学术研究织网/_templates/integrity-gate-checklist.md"
        if template_path.exists():
            content = template_path.read_text(encoding="utf-8")
            # 替换项目名
            content = content.replace("project:", f"project: {project_name}")
            content = content.replace("stage: 2.5", "stage: 2.5")
            content = content.replace("status: pending", "status: pending")
        else:
            content = f"""---
type: integrity-gate
stage: 2.5
project: {project_name}
created: {datetime.now().isoformat()}
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

# 学术诚信闸门 - Stage 2.5

**项目**: {project_name}
**阶段**: Stage 2.5
**创建时间**: {datetime.now().isoformat()}

---

## 7类AI研究失败模式检查清单

(详细检查项见模板)

| 模式 | 状态 |
|------|------|
| M1: 实现错误通过AI自审 | ⏳ |
| M2: 幻觉引用 | ⏳ |
| M3: 幻觉实验结果 | ⏳ |
| M4: 捷径依赖 | ⏳ |
| M5: Bug伪装成发现 | ⏳ |
| M6: 方法论伪造 | ⏳ |
| M7: 框架锁定 | ⏳ |

---

*基于 ARS v3.10 Integrity Gate*
"""

        note_path.write_text(content, encoding="utf-8")
        return note_path

    def sync_paper_insight_to_corpus(self, paper_card: Dict) -> Optional[Path]:
        """
        将单个论文卡片同步到语料库

        Returns:
            Path to created corpus entry, or None if skipped
        """
        # 生成 citekey
        title = paper_card.get("title", "untitled")
        year = paper_card.get("year", 2024)
        title_words = [w for w in title.split() if w.isalnum()][:3]
        citekey = f"{''.join(w[0].upper() for w in title_words)}{year}"

        # 检查是否已存在
        filepath = CORPUS_DIR / f"{citekey}.md"
        if filepath.exists():
            return None

        # 写入
        entry = {
            "citekey": citekey,
            "title": title,
            "authors": paper_card.get("authors", "Unknown"),
            "year": year,
            "venue": paper_card.get("venue", ""),
            "relevance_score": paper_card.get("relevance_score", 0),
            "abstract": paper_card.get("abstract", ""),
            "url": paper_card.get("url", ""),
            "citations": paper_card.get("citation_count", 0),
            "pre_screened_status": "Included",
            "contamination_signals": {
                "preprint_post_llm_inflection": False,
                "semantic_scholar_unmatched": None,
                "openalex_unmatched": None,
                "crossref_unmatched": None
            }
        }

        CORPUS_DIR.mkdir(parents=True, exist_ok=True)
        content = self._format_corpus_entry_md(entry)
        filepath.write_text(content, encoding="utf-8")

        return filepath


def detect_and_trigger_ars_research(paper_cards: List[Dict]) -> List[Dict]:
    """
    检测论文卡片是否触发 ARS 研究，并运行研究流程

    集成到 IntelligenceOS 的入口函数

    Args:
        paper_cards: PaperCard dicts with relevance_score

    Returns:
        List of triggered ARS research projects
    """
    integrator = ARSIntegration()
    triggered = []

    for card in paper_cards:
        if integrator.detect_research_intent(card):
            # 触发 ARS 研究
            project_name = f"ars_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            topic = card.get("title", "")

            result = integrator.run_ars_research_pipeline(
                project_name=project_name,
                topic=topic,
                paper_cards=[card],
                ars_mode="full"
            )
            triggered.append(result)

    return triggered


# 测试入口
if __name__ == "__main__":
    # 测试检测功能
    test_cards = [
        {
            "title": "Efficient Memory Management for Large Language Models",
            "relevance_score": 92,
            "matched_problems": ["Memory", "Latency"],
            "matched_techs": ["KV Cache"],
            "venue": "NeurIPS",
            "year": 2024
        },
        {
            "title": "Quick Summary",
            "relevance_score": 45,
            "matched_problems": ["Other"],
            "matched_techs": [],
            "venue": "Blog",
            "year": 2024
        }
    ]

    integrator = ARSIntegration()

    print("测试检测功能:")
    for card in test_cards:
        should_trigger = integrator.detect_research_intent(card)
        print(f"  {card['title'][:40]}... (score={card['relevance_score']}): {'✅ 触发' if should_trigger else '⏭️ 跳过'}")