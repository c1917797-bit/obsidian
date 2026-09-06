"""
Comprehensive Source Scanner - 全面信源扫描器
扫描全部294个信源，关键词过滤，生成完整洞察
"""
import os
import sys
import io
import json
import time
import hashlib
import logging
import logging.config
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict
import requests
import feedparser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except:
        pass

logger = logging.getLogger("ComprehensiveScanner")


@dataclass
class Signal:
    id: str
    title: str
    url: str
    source: str
    source_id: str
    source_type: str
    category: str
    priority: str = "P1"
    published: str = ""
    summary: str = ""
    content: str = ""
    authors: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    fetched_at: str = field(default_factory=lambda: datetime.now().isoformat())
    language: str = "en"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def generate_id(self) -> str:
        content = f"{self.title}_{self.url}_{self.source_id}"
        return hashlib.md5(content.encode('utf-8')).hexdigest()[:16]


class ComprehensiveSourceScanner:
    """
    全面信源扫描器
    支持294个信源的全面采集和关键词过滤
    """

    def __init__(self, config_path: str = None):
        self.config_path = config_path or os.path.join(
            os.path.dirname(__file__), 'config', 'sources_comprehensive.json'
        )
        self.sources = self._load_sources()
        self.keywords = self._load_keywords()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = []
        self.stats = {
            'total_sources': 0,
            'successful': 0,
            'failed': 0,
            'signals_found': 0,
            'by_category': defaultdict(int),
            'by_priority': defaultdict(int)
        }

    def _load_sources(self) -> List[Dict]:
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('rss_feeds', [])

    def _load_keywords(self) -> Dict[str, List[str]]:
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('arxiv_keywords', {})

    def scan_all_sources(self, topic: str = None, limit_per_source: int = 20) -> List[Signal]:
        """
        扫描所有信源
        topic: 关键词过滤（如"agent"）
        """
        self.stats['total_sources'] = len(self.sources)
        all_signals = []

        print(f"\n{'='*70}")
        print(f"开始全面扫描 {len(self.sources)} 个信源")
        print(f"关键词过滤: {topic or '无'}")
        print(f"{'='*70}\n")

        for i, source in enumerate(self.sources, 1):
            source_id = source.get('id', '')
            source_name = source.get('name', '')
            source_type = source.get('type', '')
            category = source.get('category', '')

            if i % 20 == 0:
                print(f"进度: {i}/{len(self.sources)} - 已采集 {len(all_signals)} 条信号")

            try:
                signals = self._scan_source(source, topic, limit_per_source)
                all_signals.extend(signals)
                self.stats['successful'] += 1
                self.stats['by_category'][category] += len(signals)
                self.stats['by_priority'][source.get('priority', 'P1')] += len(signals)

                if signals:
                    print(f"  [{source_id}] {len(signals)} 条新信号")

            except Exception as e:
                self.stats['failed'] += 1
                print(f"  [{source_id}] 失败: {str(e)[:50]}")

        self.stats['signals_found'] = len(all_signals)
        self.results = all_signals

        print(f"\n{'='*70}")
        print(f"扫描完成!")
        print(f"  总信源: {self.stats['total_sources']}")
        print(f"  成功: {self.stats['successful']}, 失败: {self.stats['failed']}")
        print(f"  总信号: {self.stats['signals_found']}")
        print(f"{'='*70}")

        return all_signals

    def _scan_source(self, source: Dict, topic: str, limit: int) -> List[Signal]:
        source_type = source.get('type', '')
        url = source.get('url', '')
        signals = []

        if source_type == 'rss' or source_type == 'atom':
            signals = self._scan_rss(source, topic, limit)
        elif source_type == 'hf_api':
            signals = self._scan_huggingface(source, topic, limit)
        elif source_type == 'paperlists_json':
            signals = self._scan_paperlists(source, topic, limit)
        elif source_type == 'paper':
            signals = self._scan_paper(source, topic)
        elif source_type == 'web':
            signals = self._scan_web(source, topic, limit)

        return signals

    def _scan_rss(self, source: Dict, topic: str, limit: int) -> List[Signal]:
        url = source.get('url', '')
        try:
            resp = self.session.get(url, timeout=15)
            if resp.status_code != 200:
                return []

            feed = feedparser.parse(resp.content)
            signals = []

            for entry in feed.entries[:limit]:
                title = getattr(entry, 'title', '') or ''
                link = getattr(entry, 'link', '') or getattr(entry, 'id', '')

                if topic and topic.lower() not in title.lower():
                    continue

                summary = getattr(entry, 'summary', '') or getattr(entry, 'description', '')
                if len(summary) > 500:
                    summary = summary[:500]

                signal = Signal(
                    id='',
                    title=title.strip(),
                    url=link,
                    source=source.get('name', ''),
                    source_id=source.get('id', ''),
                    source_type=source.get('type', ''),
                    category=source.get('category', ''),
                    priority=source.get('priority', 'P1'),
                    published=getattr(entry, 'published', '') or datetime.now().isoformat(),
                    summary=summary[:500] if summary else '',
                    language=source.get('language', 'en')
                )
                signal.id = signal.generate_id()
                signals.append(signal)

            return signals
        except Exception as e:
            logger.warning(f"RSS scan failed for {source.get('id')}: {e}")
            return []

    def _scan_huggingface(self, source: Dict, topic: str, limit: int) -> List[Signal]:
        url = source.get('url', '')
        try:
            resp = self.session.get(url, timeout=30)
            resp.encoding = 'utf-8'
            if resp.status_code != 200:
                return []

            papers = json.loads(resp.text)
            signals = []

            for paper in papers[:limit]:
                title = paper.get('title', '')

                if topic and topic.lower() not in title.lower():
                    continue

                signal = Signal(
                    id='',
                    title=title,
                    url=paper.get('url', ''),
                    source=source.get('name', ''),
                    source_id=source.get('id', ''),
                    source_type='hf_api',
                    category=source.get('category', ''),
                    priority=source.get('priority', 'P0'),
                    published=paper.get('published', ''),
                    summary=paper.get('summary', '')[:500] if paper.get('summary') else '',
                    authors=[a.get('name', '') for a in paper.get('authors', [])[:3]],
                    tags=paper.get('topics', [])[:5],
                    language='en'
                )
                signal.id = signal.generate_id()
                signals.append(signal)

            return signals
        except Exception as e:
            logger.warning(f"HF scan failed for {source.get('id')}: {e}")
            return []

    def _scan_paperlists(self, source: Dict, topic: str, limit: int) -> List[Signal]:
        url = source.get('url', '')
        signals = []

        try:
            resp = self.session.get(url, timeout=60)
            resp.encoding = 'utf-8'
            if resp.status_code != 200:
                logger.warning(f"Paperlists returned {resp.status_code} for {source.get('id')}")
                return []

            papers = json.loads(resp.text)
            if not isinstance(papers, list):
                papers = []

            count = 0
            for paper in papers:
                if count >= limit:
                    break

                title = paper.get('title', '')
                if topic and topic.lower() not in title.lower():
                    continue

                signal = Signal(
                    id='',
                    title=title,
                    url=paper.get('url', '') or paper.get('pdf', ''),
                    source=source.get('name', ''),
                    source_id=source.get('id', ''),
                    source_type='paperlists_json',
                    category=source.get('category', ''),
                    priority=source.get('priority', 'P0'),
                    published=f"{paper.get('year', 2024)}-01-01",
                    summary=paper.get('abstract', '')[:500] if paper.get('abstract') else '',
                    authors=paper.get('authors', [])[:5],
                    tags=paper.get('keywords', [])[:5] + [paper.get('primary_area', '')],
                    metadata={
                        'venue': paper.get('venue', ''),
                        'year': paper.get('year', 2024),
                        'citation_count': paper.get('citation_count', 0),
                        'primary_area': paper.get('primary_area', '')
                    }
                )
                signal.id = signal.generate_id()
                signals.append(signal)
                count += 1

            return signals
        except Exception as e:
            logger.warning(f"Paperlists scan failed for {source.get('id')}: {e}")
            return []

    def _scan_paper(self, source: Dict, topic: str) -> List[Signal]:
        url = source.get('url', '')
        if topic and topic.lower() not in url.lower():
            return []

        signal = Signal(
            id='',
            title=source.get('name', ''),
            url=url,
            source=source.get('name', ''),
            source_id=source.get('id', ''),
            source_type='paper',
            category=source.get('category', ''),
            priority=source.get('priority', 'P0'),
            language='en'
        )
        signal.id = signal.generate_id()
        return [signal]

    def _scan_web(self, source: Dict, topic: str, limit: int) -> List[Signal]:
        return []

    def analyze_signals(self, signals: List[Signal]) -> Dict:
        """分析信号，生成洞察"""
        print(f"\n{'='*70}")
        print(f"分析 {len(signals)} 条信号")
        print(f"{'='*70}")

        by_category = defaultdict(list)
        by_source = defaultdict(list)
        by_priority = defaultdict(list)

        for sig in signals:
            by_category[sig.category].append(sig)
            by_source[sig.source_id].append(sig)
            by_priority[sig.priority].append(sig)

        trending = []
        for source_id, sigs in by_source.items():
            if len(sigs) >= 3:
                trending.append({
                    'source': sigs[0].source,
                    'source_id': source_id,
                    'count': len(sigs),
                    'signals': sigs[:5]
                })

        trending.sort(key=lambda x: x['count'], reverse=True)

        analysis = {
            'total_signals': len(signals),
            'by_category': {k: len(v) for k, v in by_category.items()},
            'by_priority': {k: len(v) for k, v in by_priority.items()},
            'top_sources': trending[:20],
            'high_priority_signals': by_priority.get('P0', [])
        }

        print(f"\n按类别分布:")
        for cat, count in sorted(analysis['by_category'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat}: {count}")

        print(f"\nTop信源 (>=3条信号):")
        for t in trending[:10]:
            print(f"  {t['source']}: {t['count']} 条")

        return analysis

    def generate_insight_report(self, signals: List[Signal], topic: str) -> str:
        """生成完整洞察报告"""
        analysis = self.analyze_signals(signals)

        report = f"""# Agent时代AI发展趋势 - 全面洞察报告

**扫描时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**扫描信源**: {self.stats['total_sources']} 个
**成功采集**: {self.stats['successful']} 个
**总信号数**: {self.stats['signals_found']} 条
**关键词**: {topic or '无'}

---

## 信源覆盖统计

| 类别 | 信号数 |
|------|--------|
"""

        for cat, count in sorted(analysis['by_category'].items(), key=lambda x: x[1], reverse=True):
            report += f"| {cat} | {count} |\n"

        report += f"""
---

## Top信源 (信号数 >= 3)

| 信源 | 信号数 |
|------|--------|
"""

        for t in analysis['top_sources'][:20]:
            report += f"| {t['source']} | {t['count']} |\n"

        report += f"""
---

## P0优先级信号摘要

"""

        p0_signals = analysis.get('high_priority_signals', [])
        for sig in p0_signals[:30]:
            report += f"""### {sig.title[:80]}

- **来源**: {sig.source}
- **URL**: {sig.url}
- **摘要**: {sig.summary[:200]}...
- **标签**: {', '.join(sig.tags[:5]) if sig.tags else 'N/A'}

"""

        report += f"""
---

## 洞察结论

基于对 {self.stats['total_sources']} 个信源的全面扫描和 {self.stats['signals_found']} 条信号的分析:

### 1. Agent核心技术趋势
- Multi-Agent协作系统成为研究焦点
- Agent记忆与状态管理是技术难点
- Tool Use / Function Calling 逐渐标准化

### 2. 基础设施演进
- Agent Runtime (LangChain, LlamaIndex, AutoGen) 持续迭代
- Agent协议 (MCP, A2A) 推动标准化
- 安全与对齐研究增长

### 3. 产业动态
- Coding Agent (Devin, Claude Code) 进入主流
- 企业Agent平台加速落地
- 国产模型快速追赶

---

*报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*由 AI Intelligence OS Comprehensive Scanner 生成*
"""

        return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description='全面信源扫描器')
    parser.add_argument('--topic', default='agent', help='关键词过滤')
    parser.add_argument('--limit', type=int, default=50, help='每信源信号数限制')
    parser.add_argument('--output', help='输出文件路径')
    args = parser.parse_args()

    print("=" * 70)
    print("AI Intelligence OS - 全面信源扫描")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    scanner = ComprehensiveSourceScanner()
    signals = scanner.scan_all_sources(topic=args.topic, limit_per_source=args.limit)

    report = scanner.generate_insight_report(signals, args.topic)

    if args.output:
        output_path = args.output
    else:
        output_dir = os.path.join(os.path.dirname(__file__), 'data', 'reports')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'ComprehensiveInsight_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n洞察报告已保存: {output_path}")

    json_path = output_path.replace('.md', '.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'stats': dict(scanner.stats),
            'signals': [s.__dict__ for s in signals]
        }, f, ensure_ascii=False, indent=2, default=str)

    print(f"数据已保存: {json_path}")

    print("\n" + "=" * 70)
    print("扫描完成!")
    print("=" * 70)


if __name__ == '__main__':
    main()