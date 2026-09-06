"""
文献语料库适配器 (Literature Corpus Adapter)
基于 Academic Research Skills v3.6.4 适配器协议

将 Obsidian vault 中的文献笔记转换为 Material Passport 格式的 literature_corpus[]
支持 Convention A (citekey in frontmatter)

用法:
    python corpus_adapter.py --project "my-research"
    python corpus_adapter.py --project "my-research" --dry-run
    python corpus_adapter.py --project "my-research" --format yaml

输出:
    passport.yaml - Material Passport literature_corpus[]
    rejection_log.yaml - 解析失败记录
"""
import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import frontmatter

# 确保模块路径正确
SCRIPT_DIR = Path(__file__).parent
OBSIDIAN_ROOT = Path("C:/Users/Huawei/Documents/code/Obsidian")
CORPUS_DIR = OBSIDIAN_ROOT / "4_AI情报洞察/论文洞察/_corpus"
PROJECT_DIR = OBSIDIAN_ROOT / "5_学术研究织网/研究项目"


class CorpusAdapter:
    """文献语料库适配器 - 将 Obsidian 文献笔记转换为 ARS 格式"""

    # ARS v3.6.4 适配器契约常量
    OBTAINED_VIA_OPTIONS = ["auto-discovered", "corpus-first", "search-fills-gap", "manual"]
    PRE_SCREENED_STATUS_OPTIONS = ["unprocessed", "Included", "Excluded", "Skipped"]

    # 污染信号 - Zhao et al. (2026) 发现
    PREPRINT_VENUES = [
        "arxiv", "bioRxiv", "SSRN", "PMC", "medRxiv", "chemRxiv"
    ]

    def __init__(self, project_name: str, dry_run: bool = False, verbose: bool = True):
        self.project_name = project_name
        self.dry_run = dry_run
        self.verbose = verbose
        self.entries: List[Dict[str, Any]] = []
        self.rejections: List[Dict[str, Any]] = []
        self.stats = {
            "total_scanned": 0,
            "total_accepted": 0,
            "total_rejected": 0,
            "by_rejection_reason": {}
        }

    def scan_corpus(self, corpus_dir: Path = None) -> List[Dict[str, Any]]:
        """扫描语料库目录，查找所有文献笔记"""
        if corpus_dir is None:
            corpus_dir = CORPUS_DIR

        if not corpus_dir.exists():
            self._log(f"⚠️  语料库目录不存在: {corpus_dir}")
            return []

        entries = []
        for md_file in corpus_dir.rglob("*.md"):
            self.stats["total_scanned"] += 1
            try:
                entry = self._parse_entry(md_file)
                if entry:
                    entry["_source_file"] = str(md_file.relative_to(OBSIDIAN_ROOT))
                    entries.append(entry)
                    self.stats["total_accepted"] += 1
                else:
                    self._record_rejection(str(md_file), "parse_failed", "无法解析文件")
            except Exception as e:
                self._record_rejection(str(md_file), "exception", str(e))
                self.stats["total_rejected"] += 1

        return entries

    def _parse_entry(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """解析单个文献笔记"""
        try:
            post = frontmatter.load(file_path)
        except Exception:
            # 尝试手动解析 frontmatter
            return self._manual_parse(file_path)

        # 提取 frontmatter
        fm = dict(post.metadata)

        # 验证必需字段
        if not fm.get("citekey") and not fm.get("title"):
            return None

        # 构建 entry
        entry = {
            "citekey": fm.get("citekey", ""),
            "title": fm.get("title", ""),
            "authors": fm.get("authors", ""),
            "year": fm.get("year", ""),
            "venue": fm.get("venue", ""),
            "venue_type": fm.get("venue_type", ""),
            "doi": fm.get("doi", ""),
            "url": fm.get("url", ""),
            "abstract": fm.get("abstract", ""),
            "obtained_via": fm.get("obtained_via", "auto-discovered"),
            "obtained_at": fm.get("date", datetime.now().isoformat()),
            "pre_screened_status": fm.get("pre_screened_status", "unprocessed"),
            "pre_screened_reason": fm.get("pre_screened_reason", ""),
            "pre_screened_date": fm.get("pre_screened_date", ""),
            "contamination_signals": {
                "preprint_post_llm_inflection": bool(fm.get("contamination_signals", {}).get("preprint_post_llm_inflection", False)),
                "semantic_scholar_unmatched": fm.get("contamination_signals", {}).get("semantic_scholar_unmatched"),
                "openalex_unmatched": fm.get("contamination_signals", {}).get("openalex_unmatched"),
                "crossref_unmatched": fm.get("contamination_signals", {}).get("crossref_unmatched"),
            },
            "project": fm.get("project", self.project_name),
            "source_note": fm.get("source_note", ""),
            "user_notes": fm.get("user_notes", ""),
            "created": fm.get("created", datetime.now().isoformat()),
        }

        # 计算污染信号
        entry["contamination_signals"] = self._compute_contamination_signals(entry, post.content)

        return entry

    def _manual_parse(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """手动解析 frontmatter (当 frontmatter 库失败时)"""
        try:
            content = file_path.read_text(encoding="utf-8")

            # 提取 frontmatter
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                return None

            fm_text = fm_match.group(1)
            fm = {}

            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    fm[key.strip()] = value.strip().strip('"\'')

            if not fm.get("citekey") and not fm.get("title"):
                return None

            return {
                "citekey": fm.get("citekey", ""),
                "title": fm.get("title", ""),
                "authors": fm.get("authors", ""),
                "year": fm.get("year", ""),
                "venue": fm.get("venue", ""),
                "venue_type": fm.get("venue_type", ""),
                "doi": fm.get("doi", ""),
                "url": fm.get("url", ""),
                "abstract": fm.get("abstract", ""),
                "obtained_via": fm.get("obtained_via", "auto-discovered"),
                "obtained_at": fm.get("date", datetime.now().isoformat()),
                "pre_screened_status": fm.get("pre_screened_status", "unprocessed"),
                "pre_screened_reason": fm.get("pre_screened_reason", ""),
                "pre_screened_date": fm.get("pre_screened_date", ""),
                "contamination_signals": {
                    "preprint_post_llm_inflection": False,
                    "semantic_scholar_unmatched": None,
                    "openalex_unmatched": None,
                    "crossref_unmatched": None,
                },
                "project": fm.get("project", self.project_name),
                "source_note": "",
                "user_notes": fm.get("user_notes", ""),
                "created": fm.get("created", datetime.now().isoformat()),
            }
        except Exception:
            return None

    def _compute_contamination_signals(self, entry: Dict, content: str) -> Dict[str, Any]:
        """计算污染信号 - 基于 Zhao et al. (2026)"""
        signals = entry.get("contamination_signals", {})

        # M1: 预印本后LLM拐点信号
        year = str(entry.get("year", ""))
        venue = str(entry.get("venue", "")).lower()

        if year and int(year) >= 2024:
            for preprint_venue in self.PREPRINT_VENUES:
                if preprint_venue in venue:
                    signals["preprint_post_llm_inflection"] = True
                    break

        return signals

    def _record_rejection(self, file_path: str, reason: str, detail: str):
        """记录解析失败"""
        self.rejections.append({
            "source_file": file_path,
            "rejection_reason": reason,
            "detail": detail,
            "timestamp": datetime.now().isoformat()
        })

        # 更新统计
        if reason not in self.stats["by_rejection_reason"]:
            self.stats["by_rejection_reason"][reason] = 0
        self.stats["by_rejection_reason"][reason] += 1

    def generate_passport(self, output_format: str = "yaml") -> Dict[str, Any]:
        """生成 Material Passport literature_corpus[]"""
        return {
            "version": "1.0",
            "project": self.project_name,
            "generated_at": datetime.now().isoformat(),
            "protocol": "ARS v3.6.4 corpus-first, search-fills-gap",
            "entries": self.entries,
            "rejection_log": self.rejections,
            "stats": self.stats
        }

    def export_yaml(self, passport: Dict, output_path: Path = None) -> str:
        """导出为 YAML 格式"""
        try:
            import yaml
            yaml_content = yaml.dump(passport, allow_unicode=True, sort_keys=False)
        except ImportError:
            yaml_content = self._dict_to_yaml(passport)

        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(yaml_content, encoding="utf-8")
            self._log(f"✅ 已导出: {output_path}")

        return yaml_content

    def _dict_to_yaml(self, d: Dict, indent: int = 0) -> str:
        """简单的 dict to YAML 转换"""
        lines = []
        for key, value in d.items():
            if isinstance(value, list):
                lines.append(f"{'  ' * indent}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        lines.append(self._dict_to_yaml(item, indent + 1))
                    else:
                        lines.append(f"{'  ' * (indent + 1)}- {item}")
            elif isinstance(value, dict):
                lines.append(f"{'  ' * indent}{key}:")
                lines.append(self._dict_to_yaml(value, indent + 1))
            else:
                lines.append(f"{'  ' * indent}{key}: {value}")
        return "\n".join(lines)

    def _log(self, msg: str):
        """日志输出"""
        if self.verbose:
            print(msg)

    def run(self, corpus_dir: Path = None, output_dir: Path = None) -> Dict[str, Any]:
        """运行完整适配流程"""
        self._log(f"\n📚 文献语料库适配器")
        self._log(f"   项目: {self.project_name}")
        self._log(f"   模式: {'DRY-RUN' if self.dry_run else 'LIVE'}")
        self._log("-" * 50)

        # Step 1: 扫描语料库
        self._log("\n🔍 Step 1: 扫描语料库...")
        self.entries = self.scan_corpus(corpus_dir)
        self._log(f"   扫描完成: {self.stats['total_scanned']} 文件")
        self._log(f"   接受: {self.stats['total_accepted']}, 拒绝: {self.stats['total_rejected']}")

        # Step 2: 生成 passport
        self._log("\n📋 Step 2: 生成 Material Passport...")
        passport = self.generate_passport()

        # Step 3: 输出
        if not self.dry_run and output_dir:
            self._log("\n💾 Step 3: 导出...")

            # 导出 passport.yaml
            passport_path = output_dir / f"{self.project_name}_passport.yaml"
            self.export_yaml(passport, passport_path)

            # 导出 rejection_log.yaml
            rejection_path = output_dir / f"{self.project_name}_rejection_log.yaml"
            rejection_data = {
                "generated_at": datetime.now().isoformat(),
                "rejections": self.rejections,
                "stats": self.stats
            }
            self.export_yaml(rejection_data, rejection_path)

        # 打印统计
        self._log("\n📊 统计:")
        self._log(f"   总扫描: {self.stats['total_scanned']}")
        self._log(f"   接受: {self.stats['total_accepted']}")
        self._log(f"   拒绝: {self.stats['total_rejected']}")
        if self.stats["by_rejection_reason"]:
            self._log("   拒绝原因分布:")
            for reason, count in self.stats["by_rejection_reason"].items():
                self._log(f"     {reason}: {count}")

        return passport


def main():
    parser = argparse.ArgumentParser(
        description="文献语料库适配器 - ARS v3.6.4 协议"
    )
    parser.add_argument("--project", "-p", required=True, help="项目名称")
    parser.add_argument("--dry-run", "-n", action="store_true", help="仅扫描不导出")
    parser.add_argument("--format", "-f", choices=["yaml", "json"], default="yaml", help="输出格式")
    parser.add_argument("--corpus-dir", help="语料库目录路径")
    parser.add_argument("--output-dir", help="输出目录路径")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")

    args = parser.parse_args()

    # 路径设置
    corpus_dir = Path(args.corpus_dir) if args.corpus_dir else CORPUS_DIR
    output_dir = Path(args.output_dir) if args.output_dir else PROJECT_DIR / args.project

    # 运行适配器
    adapter = CorpusAdapter(
        project_name=args.project,
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    result = adapter.run(corpus_dir=corpus_dir, output_dir=output_dir if not args.dry_run else None)

    if args.dry_run:
        print("\n📋 DRY-RUN 结果预览:")
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()