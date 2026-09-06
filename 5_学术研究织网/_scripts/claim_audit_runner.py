"""
Claim-Faithfulness 审计运行器
基于 Academic Research Skills v3.8 L3 Claim-Faithfulness System

验证每条引用是否真正支撑论文中的声明
5类 HIGH-WARN 类别:
- HW01: claim-not-supported (引用不支持声明)
- HW02: negative-constraint-violation (引用否定声明)
- HW03: fabricated-reference (引用不存在)
- HW04: anchorless (无锚点)
- HW05: constraint-violation-uncited (约束违反但无引用)

用法:
    python claim_audit_runner.py --project "my-research" --paper "paper.md"
    python claim_audit_runner.py --project "my-research" --audit-all
    python claim_audit_runner.py --project "my-research" --show-pending
"""
import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict, field
import hashlib

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
CLAIM_AUDIT_DIR = OBSIDIAN_ROOT / "5_学术研究织网/claim_audit"
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"


@dataclass
class ClaimEntry:
    """单条声明"""
    claim_id: str
    claim_text: str
    source_citekey: str
    anchor_type: str  # quote / page / section / paragraph / none
    anchor_value: str
    audit_status: str = "pending"  # pending / verified / failed / high_warn
    high_warn_category: str = ""
    notes: str = ""


@dataclass
class ClaimAuditReport:
    """完整审计报告"""
    project: str
    paper_section: str
    created: str
    updated: str
    audit_status: str  # pending / in_progress / verified / failed / high_warn
    claims: List[Dict] = field(default_factory=list)
    high_warn_count: int = 0
    claims_total: int = 0
    claims_verified: int = 0
    claims_failed: int = 0
    claims_pending: int = 0
    uncited_assertions: List[Dict] = field(default_factory=list)
    constraint_violations: List[Dict] = field(default_factory=list)


class ClaimAuditRunner:
    """Claim-Faithfulness 审计运行器"""

    # HIGH-WARN 类别
    HIGH_WARN_CATEGORIES = {
        "HW01": "claim-not-supported",
        "HW02": "negative-constraint-violation",
        "HW03": "fabricated-reference",
        "HW04": "anchorless",
        "HW05": "constraint-violation-uncited"
    }

    # 三层引用锚点格式
    REF_PATTERN = re.compile(r'<!--ref:([^>]+)-->(?:<!--anchor:([^:]+):([^>]+)-->)?')

    def __init__(self, project: str, paper_path: str = ""):
        self.project = project
        self.paper_path = paper_path
        self.client = get_client() if MINIMAX_AVAILABLE else None
        self.claims: List[ClaimEntry] = []
        self.report: Optional[ClaimAuditReport] = None

    def extract_claims_from_paper(self, paper_path: str = "") -> List[ClaimEntry]:
        """从论文中提取声明"""
        if not paper_path:
            paper_path = self.paper_path

        if not paper_path:
            return []

        path = Path(paper_path)
        if not path.exists():
            return []

        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            return []

        claims = []
        claim_id = 0

        # 查找所有引用
        for match in self.REF_PATTERN.finditer(content):
            claim_id += 1
            citekey = match.group(1)
            anchor_kind = match.group(2) or "none"
            anchor_value = match.group(3) or ""

            # 提取该引用附近的文本作为 claim
            start = max(0, match.start() - 200)
            end = min(len(content), match.end() + 200)
            context = content[start:end].strip()

            claim = ClaimEntry(
                claim_id=f"C{claim_id:02d}",
                claim_text=context[:200],  # 截取200字符
                source_citekey=citekey,
                anchor_type=anchor_kind,
                anchor_value=anchor_value
            )
            claims.append(claim)

        self.claims = claims
        return claims

    def audit_claims(self, auto: bool = True) -> ClaimAuditReport:
        """审计所有声明"""
        if not self.claims:
            return ClaimAuditReport(
                project=self.project,
                paper_section=self.paper_path,
                created=datetime.now().isoformat(),
                updated=datetime.now().isoformat(),
                audit_status="pending"
            )

        print(f"\n🔍 Claim-Faithfulness 审计")
        print(f"   项目: {self.project}")
        print(f"   声明总数: {len(self.claims)}")
        print("-" * 50)

        verified_count = 0
        failed_count = 0
        pending_count = 0
        high_warn_count = 0

        for i, claim in enumerate(self.claims, 1):
            print(f"\n🔍 [{i}/{len(self.claims)}] 审计 {claim.claim_id}: {claim.claim_text[:50]}...")

            if auto and self.client:
                result = self._audit_single_claim_llm(claim)
            else:
                result = self._audit_single_claim_manual(claim)

            claim.audit_status = result["status"]
            claim.high_warn_category = result.get("high_warn_category", "")
            claim.notes = result.get("notes", "")

            if result["status"] == "verified":
                verified_count += 1
            elif result["status"] in ["failed", "high_warn"]:
                failed_count += 1
                if result["status"] == "high_warn":
                    high_warn_count += 1
            else:
                pending_count += 1

        # 创建报告
        self.report = ClaimAuditReport(
            project=self.project,
            paper_section=self.paper_path,
            created=datetime.now().isoformat(),
            updated=datetime.now().isoformat(),
            audit_status="high_warn" if high_warn_count > 0 else "verified" if verified_count > 0 else "pending",
            claims=[asdict(c) for c in self.claims],
            high_warn_count=high_warn_count,
            claims_total=len(self.claims),
            claims_verified=verified_count,
            claims_failed=failed_count,
            claims_pending=pending_count
        )

        # 保存报告
        self._save_report()

        return self.report

    def _audit_single_claim_llm(self, claim: ClaimEntry) -> Dict[str, Any]:
        """使用 LLM 审计单条声明"""
        if not self.client:
            return {"status": "pending", "notes": "LLM 不可用"}

        # 查找引用原文
        ref_content = self._fetch_reference_content(claim.source_citekey)

        prompt = f"""你是学术诚信审计员，负责验证引用是否真正支撑声明。

声明: {claim.claim_text}

引用 ({claim.source_citekey}):
锚点类型: {claim.anchor_type}
锚点值: {claim.anchor_value}

引用原文:
{ref_content[:500] if ref_content else '[无法获取引用内容]'}

请判断：
1. 该引用是否真正支撑上述声明？
2. 是否存在断章取义或过度推广？
3. 是否有相反的证据？

返回 JSON 格式：
{{
    "status": "verified / failed / high_warn / pending",
    "high_warn_category": "claim-not-supported / negative-constraint-violation / fabricated-reference / anchorless / constraint-violation-uncited / (空)",
    "notes": "详细说明"
}}

只返回 JSON，不要有其他内容。"""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat(messages, temperature=0.3)
            result = json.loads(response)
            return result
        except Exception as e:
            return {"status": "pending", "notes": f"LLM 调用失败: {str(e)}"}

    def _audit_single_claim_manual(self, claim: ClaimEntry) -> Dict[str, Any]:
        """手动审计单条声明"""
        # 无锚点的是 anchorless
        if claim.anchor_type == "none" or not claim.anchor_value:
            return {
                "status": "high_warn",
                "high_warn_category": "anchorless",
                "notes": "声明有引用但无锚点"
            }

        # 默认 pending
        return {
            "status": "pending",
            "notes": "需手动验证"
        }

    def _fetch_reference_content(self, citekey: str) -> str:
        """获取引用内容"""
        # 查找 corpus 中的文献
        for md_file in CORPUS_DIR.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm = self._parse_frontmatter(fm_match.group(1))
                    if fm.get("citekey") == citekey or fm.get("title", "").lower() in citekey.lower():
                        # 返回摘要部分
                        if "abstract" in fm:
                            return fm.get("abstract", "")
                        # 或返回文件内容的一部分
                        return content[fm_match.end():fm_match.end()+500]
            except Exception:
                continue
        return ""

    def _parse_frontmatter(self, fm_text: str) -> Dict[str, Any]:
        """简单解析 frontmatter"""
        fm = {}
        for line in fm_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm[key.strip()] = value.strip().strip('"\'')
        return fm

    def find_uncited_assertions(self, paper_path: str = "") -> List[Dict[str, str]]:
        """查找未声明的断言"""
        if not paper_path:
            paper_path = self.paper_path

        if not paper_path:
            return []

        path = Path(paper_path)
        if not path.exists():
            return []

        content = path.read_text(encoding="utf-8")
        uncited = []

        # 查找可能是声明但没有引用的句子
        sentences = re.split(r'[.。]+', content)
        for i, sent in enumerate(sentences):
            # 如果句子超过一定长度且不包含引用
            if len(sent) > 50 and '<!--ref:' not in sent and '[[' not in sent:
                # 检查是否像声明
                if any(kw in sent for kw in ["表明", "显示", "证明", "认为", "发现", "suggests", "shows", "demonstrates", "found"]):
                    uncited.append({
                        "position": f"句子 {i+1}",
                        "text": sent.strip()[:100],
                        "suggestion": "添加引用或标记为背景知识"
                    })

        return uncited[:10]  # 最多10条

    def _save_report(self):
        """保存报告到 Obsidian"""
        if not self.report:
            return

        CLAIM_AUDIT_DIR.mkdir(parents=True, exist_ok=True)

        date_str = datetime.now().strftime("%Y-%m-%d")
        safe_project = self.project.replace(" ", "_")
        safe_paper = Path(self.report.paper_section).stem[:30] if self.report.paper_section else "unknown"

        filename = f"ClaimAudit_{safe_project}_{safe_paper}_{date_str}.md"
        filepath = CLAIM_AUDIT_DIR / filename

        content = self._generate_markdown()

        filepath.write_text(content, encoding="utf-8")
        print(f"\n✅ 审计报告已保存: {filepath}")

        # 同时保存 JSON
        json_path = filepath.with_suffix(".json")
        json_path.write_text(json.dumps(asdict(self.report), ensure_ascii=False, indent=2), encoding="utf-8")

    def _generate_markdown(self) -> str:
        """生成 Markdown 报告"""
        report = self.report
        if not report:
            return ""

        status_icon = {
            "pending": "⏳",
            "in_progress": "🔄",
            "verified": "✅",
            "failed": "❌",
            "high_warn": "🔴"
        }

        lines = [
            "---",
            "type: claim-tracking",
            f'project: "{report.project}"',
            f"paper_section: TODO",
            f"audit_status: {report.audit_status}",
            f"claims_total: {report.claims_total}",
            f"claims_verified: {report.claims_verified}",
            f"claims_failed: {report.claims_failed}",
            f"claims_pending: {report.claims_pending}",
            f"high_warn_count: {report.high_warn_count}",
            f"created: {report.created}",
            f"updated: {report.updated}",
            "---",
            "",
            f"# Claim-Faithfulness 审计报告",
            "",
            f"**项目**: {report.project}",
            f"**状态**: {status_icon.get(report.audit_status, '⏳')} {report.audit_status}",
            "",
            "## 审计概览",
            "",
            "| 指标 | 数值 |",
            "|------|------|",
            f"| 总声明数 | {report.claims_total} |",
            f"| 已验证 | {report.claims_verified} |",
            f"| 失败 | {report.claims_failed} |",
            f"| 待处理 | {report.claims_pending} |",
            f"| HIGH-WARN | {report.high_warn_count} |",
            "",
        ]

        # HIGH-WARN 详情
        if report.high_warn_count > 0:
            lines.extend([
                "## 🔴 HIGH-WARN 声明",
                "",
                "| Claim ID | 声明文本 | 类别 | 状态 |",
                "|----------|----------|------|------|"
            ])
            for claim in report.claims:
                if claim.get("high_warn_category"):
                    lines.append(f"| {claim['claim_id']} | {claim['claim_text'][:50]}... | {claim['high_warn_category']} | {claim['audit_status']} |")

        # 所有声明列表
        lines.extend([
            "",
            "## 所有声明 (Claim Manifest)",
            "",
            "| ID | 声明文本 | 来源 | 锚点类型 | 状态 |",
            "|----|----------|------|----------|------|"
        ])

        for claim in report.claims:
            lines.append(f"| {claim['claim_id']} | {claim['claim_text'][:40]}... | {claim['source_citekey']} | {claim['anchor_type']} | {claim['audit_status']} |")

        lines.extend([
            "",
            "---",
            f"\n*Claim-Faithfulness Audit | ARS v3.8 | {report.updated}*"
        ])

        return "\n".join(lines)

    def show_pending(self) -> List[Dict]:
        """显示待处理的声明"""
        pending = []
        for claim in self.claims:
            if claim.audit_status == "pending":
                pending.append(asdict(claim))
        return pending


def main():
    parser = argparse.ArgumentParser(description="Claim-Faithfulness 审计运行器")
    parser.add_argument("--project", "-p", required=True, help="项目名称")
    parser.add_argument("--paper", help="论文文件路径")
    parser.add_argument("--audit-all", "-a", action="store_true", help="审计所有声明")
    parser.add_argument("--show-pending", action="store_true", help="显示待处理声明")
    parser.add_argument("--find-uncited", "-u", action="store_true", help="查找未声明断言")

    args = parser.parse_args()

    runner = ClaimAuditRunner(project=args.project, paper_path=args.paper or "")

    if args.find_uncited and args.paper:
        print("\n🔍 查找未声明断言...")
        uncited = runner.find_uncited_assertions(args.paper)
        if uncited:
            print(f"\n找到 {len(uncited)} 条未声明断言:")
            for item in uncited:
                print(f"  - {item['position']}: {item['text'][:50]}...")
        else:
            print("未发现未声明断言")
        return

    if args.show_pending:
        claims = runner.extract_claims_from_paper()
        pending = runner.show_pending()
        print(f"\n⏳ 待处理声明: {len(pending)}/{len(claims)}")
        for c in pending:
            print(f"  {c['claim_id']}: {c['claim_text'][:50]}...")
        return

    if args.audit_all:
        if not args.paper:
            print("⚠️  需要指定 --paper 参数")
            return

        claims = runner.extract_claims_from_paper(args.paper)
        print(f"\n📋 从论文中提取了 {len(claims)} 条声明")

        report = runner.audit_claims(auto=True)

        print("\n" + "=" * 50)
        print(f"📊 审计结果:")
        print(f"   总声明: {report.claims_total}")
        print(f"   已验证: {report.claims_verified}")
        print(f"   失败: {report.claims_failed}")
        print(f"   HIGH-WARN: {report.high_warn_count}")


if __name__ == "__main__":
    main()