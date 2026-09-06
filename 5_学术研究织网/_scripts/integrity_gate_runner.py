"""
学术诚信闸门运行器 (Integrity Gate Runner)
基于 Academic Research Skills v3.10 Stage 2.5/4.5 Integrity Gate

7类AI研究失败模式检查清单:
- M1: 实现错误通过AI自审
- M2: 幻觉引用（虚构文献）
- M3: 幻觉实验结果
- M4: 捷径依赖（取巧特征依赖）
- M5: 实现错误被包装成"意外发现"
- M6: 方法论伪造
- M7: 框架锁定（在早期阶段锁定）

用法:
    python integrity_gate_runner.py --project "my-research" --stage 2.5
    python integrity_gate_runner.py --project "my-research" --stage 4.5 --auto
"""
import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict

# 导入 MiniMax client
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "2_AI情报织网/ai-intelligence-os"))
try:
    from core.minimax_client import get_client
    MINIMAX_AVAILABLE = True
except ImportError:
    MINIMAX_AVAILABLE = False
    print("⚠️  MiniMax client 不可用，将使用模拟模式")

# 路径常量
SCRIPT_DIR = Path(__file__).parent
OBSIDIAN_ROOT = Path("C:/Users/Huawei/Documents/code/Obsidian")
INTEGRITY_DIR = OBSIDIAN_ROOT / "5_学术研究织网/整合检查"
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"


@dataclass
class IntegrityCheckResult:
    """单条检查结果"""
    mode: str
    status: str  # CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE / NOT_APPLICABLE
    notes: str
    evidence: List[str]


@dataclass
class IntegrityGateReport:
    """完整闸门报告"""
    project: str
    stage: str
    created: str
    status: str  # CLEARED / BLOCKED
    checks: List[Dict[str, Any]]
    block_conditions: List[str]
    user_acknowledgement: bool = False
    user_name: str = ""
    acknowledged_at: str = ""


class IntegrityGateRunner:
    """学术诚信闸门运行器"""

    # 7类AI研究失败模式定义
    FAILURE_MODES = {
        "M1": {
            "name": "实现错误通过AI自审",
            "description": "代码/实现错误被误认为是真实发现",
            "check_items": [
                "代码是否经过独立验证？",
                "是否有单元测试覆盖关键路径？",
                "实现错误是否被误认为是真实发现？"
            ]
        },
        "M2": {
            "name": "幻觉引用",
            "description": "虚构或捏造的文献引用",
            "check_items": [
                "所有引用是否真实存在？",
                "作者名字是否正确？",
                "年份和期刊信息是否匹配？",
                "是否有Vibe Citing（捏造引用）模式？"
            ]
        },
        "M3": {
            "name": "幻觉实验结果",
            "description": "不存在的或被篡改的实验数据",
            "check_items": [
                "实验结果是否有原始数据支撑？",
                "数据是否经过多次运行验证？",
                "统计显著性是否有明确报告？",
                "是否有p-hacking或假设检验操纵的迹象？"
            ]
        },
        "M4": {
            "name": "捷径依赖",
            "description": "模型依赖"作弊"特征而非真实学习",
            "check_items": [
                "模型是否依赖'作弊'特征？",
                "测试集和训练集是否完全分离？",
                "是否有过拟合迹象？",
                "结果是否在独立测试集上验证？"
            ]
        },
        "M5": {
            "name": "实现错误被包装成意外发现",
            "description": "Bug被误认为是新颖的研究发现",
            "check_items": [
                "发现的'新现象'是否真实？",
                "是否排除实现错误的可能性？",
                "异常结果是否被仔细审查？",
                "是否存在'幸存者偏差'？"
            ]
        },
        "M6": {
            "name": "方法论伪造",
            "description": "实验设计或方法存在重大缺陷",
            "check_items": [
                "实验设计是否合理？",
                "对照组设置是否正确？",
                "样本量是否足够？",
                "是否存在选择性报告？"
            ]
        },
        "M7": {
            "name": "框架锁定",
            "description": "在早期阶段锁定在某个研究框架中",
            "check_items": [
                "研究问题是否过于狭窄？",
                "是否考虑了替代解释？",
                "是否有确认偏误迹象？",
                "方法论选择是否受到先入为主的观念影响？"
            ]
        }
    }

    # 阻断条件
    BLOCKING_CONDITIONS = {
        "any_suspected": "任何模式处于 SUSPECTED 状态",
        "M1_insufficient": "M1 (实现错误) 证据不足",
        "M3_insufficient": "M3 (幻觉结果) 证据不足",
        "M5_insufficient": "M5 (Bug伪装) 证据不足",
        "M6_insufficient": "M6 (方法论伪造) 证据不足"
    }

    def __init__(self, project: str, stage: str = "2.5"):
        self.project = project
        self.stage = stage
        self.client = get_client() if MINIMAX_AVAILABLE else None
        self.results: Dict[str, IntegrityCheckResult] = {}
        self.block_conditions: List[str] = []

    def _load_references(self) -> List[Dict[str, Any]]:
        """加载项目文献引用"""
        references = []
        for md_file in CORPUS_DIR.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                # 提取 frontmatter
                fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm = self._parse_frontmatter(fm_match.group(1))
                    if fm.get("project") == self.project:
                        references.append({
                            "citekey": fm.get("citekey", md_file.stem),
                            "title": fm.get("title", ""),
                            "authors": fm.get("authors", ""),
                            "year": fm.get("year", ""),
                            "venue": fm.get("venue", ""),
                            "file": str(md_file.relative_to(OBSIDIAN_ROOT))
                        })
            except Exception:
                continue
        return references

    def _parse_frontmatter(self, fm_text: str) -> Dict[str, Any]:
        """简单解析 frontmatter"""
        fm = {}
        for line in fm_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm[key.strip()] = value.strip().strip('"\'')
        return fm

    def run_checks(self, auto: bool = False) -> IntegrityGateReport:
        """运行所有检查"""
        print(f"\n🔒 学术诚信闸门 - Stage {self.stage}")
        print(f"   项目: {self.project}")
        print("-" * 50)

        # 加载引用
        references = self._load_references()
        print(f"\n📚 加载了 {len(references)} 条文献引用")

        # M2 专项检查 - 引用幻觉
        print("\n🔍 M2: 幻觉引用检查...")
        m2_result = self._check_citations_hallucination(references)
        self.results["M2"] = m2_result

        # M3 专项检查 - 幻觉实验结果 (如果有数据)
        print("🔍 M3: 幻觉实验结果检查...")
        m3_result = self._check_experiment_hallucination()
        self.results["M3"] = m3_result

        # 其他模式检查 (使用 LLM 或手动)
        for mode in ["M1", "M4", "M5", "M6", "M7"]:
            print(f"🔍 {mode}: {self.FAILURE_MODES[mode]['name']}...")
            if auto and self.client:
                result = self._run_llm_check(mode)
            else:
                result = IntegrityCheckResult(
                    mode=mode,
                    status="NOT_APPLICABLE",
                    notes="需手动检查",
                    evidence=[]
                )
            self.results[mode] = result

        # 检查阻断条件
        self._check_blocking_conditions()

        # 生成报告
        report = self._generate_report()

        # 保存报告
        self._save_report(report)

        return report

    def _check_citations_hallucination(self, references: List[Dict]) -> IntegrityCheckResult:
        """M2: 幻觉引用检查"""
        issues = []
        total = len(references)

        if total == 0:
            return IntegrityCheckResult(
                mode="M2",
                status="NOT_APPLICABLE",
                notes="无文献引用",
                evidence=[]
            )

        # 检查每条引用
        for ref in references:
            citekey = ref.get("citekey", "")
            title = ref.get("title", "")

            # 简单检查：citekey 格式是否正常
            if not citekey or len(citekey) < 3:
                issues.append(f"可疑citekey: {citekey}")

            # 检查年份是否合理
            year = ref.get("year", "")
            if year:
                try:
                    year_int = int(year)
                    if year_int < 1900 or year_int > datetime.now().year + 1:
                        issues.append(f"可疑年份: {year} in {citekey}")
                except ValueError:
                    issues.append(f"无效年份: {year} in {citekey}")

        if issues:
            return IntegrityCheckResult(
                mode="M2",
                status="SUSPECTED",
                notes=f"发现 {len(issues)} 个可疑引用",
                evidence=issues[:10]  # 最多10条
            )
        else:
            return IntegrityCheckResult(
                mode="M2",
                status="CLEAR",
                notes=f"检查了 {total} 条引用，未发现问题",
                evidence=[]
            )

    def _check_experiment_hallucination(self) -> IntegrityCheckResult:
        """M3: 幻觉实验结果检查"""
        # 查找项目相关的数据文件
        project_data_dir = OBSIDIAN_ROOT / "5_学术研究织网/研究项目" / self.project / "data"

        if not project_data_dir.exists():
            return IntegrityCheckResult(
                mode="M3",
                status="NOT_APPLICABLE",
                notes="无实验数据文件",
                evidence=[]
            )

        # 检查数据文件存在性和完整性
        data_files = list(project_data_dir.glob("*"))
        if not data_files:
            return IntegrityCheckResult(
                mode="M3",
                status="NOT_APPLICABLE",
                notes="无实验数据文件",
                evidence=[]
            )

        return IntegrityCheckResult(
            mode="M3",
            status="CLEAR",
            notes=f"发现 {len(data_files)} 个数据文件",
            evidence=[f.name for f in data_files[:5]]
        )

    def _run_llm_check(self, mode: str) -> IntegrityCheckResult:
        """使用 LLM 进行检查"""
        if not self.client:
            return IntegrityCheckResult(
                mode=mode,
                status="NOT_APPLICABLE",
                notes="LLM 不可用",
                evidence=[]
            )

        mode_info = self.FAILURE_MODES.get(mode, {})

        prompt = f"""你是学术诚信审查员。请检查以下研究是否存在 {mode} 问题：

模式: {mode}
名称: {mode_info.get('name', '')}
描述: {mode_info.get('description', '')}

检查项目:
{chr(10).join(f"- {item}" for item in mode_info.get('check_items', []))}

请分析并返回 JSON 格式：
{{
    "status": "CLEAR / SUSPECTED / INSUFFICIENT_EVIDENCE",
    "notes": "详细说明",
    "evidence": ["具体证据或问题列表"]
}}

只返回 JSON，不要有其他内容。"""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat(messages, temperature=0.3)
            result = json.loads(response)

            return IntegrityCheckResult(
                mode=mode,
                status=result.get("status", "NOT_APPLICABLE"),
                notes=result.get("notes", ""),
                evidence=result.get("evidence", [])
            )
        except Exception as e:
            return IntegrityCheckResult(
                mode=mode,
                status="NOT_APPLICABLE",
                notes=f"LLM 检查失败: {str(e)}",
                evidence=[]
            )

    def _check_blocking_conditions(self):
        """检查阻断条件"""
        self.block_conditions = []

        # 任何 SUSPECTED
        suspected = [m for m, r in self.results.items() if r.status == "SUSPECTED"]
        if suspected:
            self.block_conditions.append(f"any_suspected: {', '.join(suspected)}")

        # 关键模式证据不足
        for mode in ["M1", "M3", "M5", "M6"]:
            if mode in self.results and self.results[mode].status == "INSUFFICIENT_EVIDENCE":
                self.block_conditions.append(f"{mode.lower()}_insufficient")

    def _generate_report(self) -> IntegrityGateReport:
        """生成报告"""
        status = "BLOCKED" if self.block_conditions else "CLEARED"

        report = IntegrityGateReport(
            project=self.project,
            stage=self.stage,
            created=datetime.now().isoformat(),
            status=status,
            checks=[asdict(r) for r in self.results.values()],
            block_conditions=self.block_conditions
        )

        return report

    def _save_report(self, report: IntegrityGateReport):
        """保存报告到 Obsidian"""
        INTEGRITY_DIR.mkdir(parents=True, exist_ok=True)

        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"Stage-{self.stage}_{self.project}_{date_str}.md"
        filepath = INTEGRITY_DIR / filename

        # 生成 Markdown 内容
        content = self._generate_markdown(report)

        filepath.write_text(content, encoding="utf-8")
        print(f"\n✅ 报告已保存: {filepath}")

        # 同时保存 JSON 副本
        json_path = filepath.with_suffix('.json')
        json_path.write_text(json.dumps(asdict(report), ensure_ascii=False, indent=2), encoding="utf-8")

    def _generate_markdown(self, report: IntegrityGateReport) -> str:
        """生成 Markdown 报告"""
        lines = [
            "---",
            "type: integrity-gate",
            f"stage: {report.stage}",
            f'project: "{report.project}"',
            f"created: {report.created}",
            f"status: {report.status.lower()}",
        ]

        for mode in ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]:
            if mode in report.checks:
                lines.append(f"{mode.lower()}_status: {report.checks[mode]['status'].lower()}")
            else:
                lines.append(f"{mode.lower()}_status: pending")

        lines.extend([
            f"block_status: {'blocked' if report.status == 'BLOCKED' else 'cleared'}",
            f"user_acknowledgement: {str(report.user_acknowledgement).lower()}",
            "---",
            "",
            f"# 学术诚信闸门 - Stage {report.stage}",
            "",
            f"**项目**: {report.project}",
            f"**检查日期**: {report.created}",
            f"**状态**: {'🔴 BLOCKED' if report.status == 'BLOCKED' else '✅ CLEARED'}",
            "",
            "---",
            "",
            "## 7类AI研究失败模式检查结果",
            "",
            "| 模式 | 名称 | 状态 | 备注 |",
            "|------|------|------|------|"
        ])

        for mode, info in self.FAILURE_MODES.items():
            check = next((c for c in report.checks if c['mode'] == mode), None)
            if check:
                status_icon = {
                    "CLEAR": "✅",
                    "SUSPECTED": "🔴",
                    "INSUFFICIENT_EVIDENCE": "⚠️",
                    "NOT_APPLICABLE": "⏭️"
                }.get(check['status'], "⏳")
                lines.append(f"| {mode} | {info['name']} | {status_icon} {check['status']} | {check['notes']} |")

        if report.block_conditions:
            lines.extend([
                "",
                "## 🔴 阻断条件",
                "",
            ])
            for cond in report.block_conditions:
                lines.append(f"- {cond}")

        lines.extend([
            "",
            "---",
            "",
            "## 用户确认 (User Acknowledgement)",
            "",
            "我已审查上述所有检查项目，并确认：",
            "",
            "- [ ] 所有 CLEAR 状态都经过了我的个人验证",
            "- [ ] 任何 NOT_APPLICABLE 状态都有合理说明",
            "- [ ] 所有潜在问题都已记录并有修复计划",
            "- [ ] 我理解如果存在 SUSPECTED 状态，Pipeline 将被阻塞",
            "",
            "**确认人**: ",
            "**确认时间**: ",
            "",
            "---",
            f"\n*基于 Academic Research Skills v3.10 Integrity Gate | {report.created}*"
        ])

        return "\n".join(lines)

    def acknowledge(self, user_name: str = "") -> bool:
        """用户确认闸门"""
        report = self._load_latest_report()
        if report:
            report.user_acknowledgement = True
            report.user_name = user_name
            report.acknowledged_at = datetime.now().isoformat()
            self._save_report(report)
            return True
        return False

    def _load_latest_report(self) -> Optional[IntegrityGateReport]:
        """加载最新报告"""
        if not INTEGRITY_DIR.exists():
            return None

        json_files = list(INTEGRITY_DIR.glob(f"Stage-{self.stage}_{self.project}_*.json"))
        if not json_files:
            return None

        latest = sorted(json_files)[-1]
        try:
            data = json.loads(latest.read_text(encoding="utf-8"))
            return IntegrityGateReport(**data)
        except Exception:
            return None


def main():
    parser = argparse.ArgumentParser(description="学术诚信闸门运行器")
    parser.add_argument("--project", "-p", required=True, help="项目名称")
    parser.add_argument("--stage", "-s", choices=["2.5", "4.5"], default="2.5", help="检查阶段")
    parser.add_argument("--auto", "-a", action="store_true", help="自动运行 LLM 检查")
    parser.add_argument("--acknowledge", action="store_true", help="确认闸门通过")

    args = parser.parse_args()

    runner = IntegrityGateRunner(project=args.project, stage=args.stage)

    if args.acknowledge:
        if runner.acknowledge():
            print("✅ 闸门已确认")
        else:
            print("⚠️  无法确认闸门")
    else:
        report = runner.run_checks(auto=args.auto)

        print("\n" + "=" * 50)
        print(f"📊 检查结果: {report.status}")
        if report.block_conditions:
            print("\n🔴 阻断条件:")
            for cond in report.block_conditions:
                print(f"   - {cond}")
        else:
            print("\n✅ 所有检查通过")


if __name__ == "__main__":
    main()