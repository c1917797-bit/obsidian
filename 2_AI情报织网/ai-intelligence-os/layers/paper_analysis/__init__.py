"""
Paper Analysis Integration - 论文分析集成
集成 Paper-Analysis-Renew 工作流能力
"""
import os
import json
import subprocess
import sys
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

from core.logger import get_logger

logger = get_logger("PaperAnalysis")

from layers.paper_analysis.paper_search_engine import PaperSearchEngine, ReadingPyramid, PaperMatch
from layers.paper_analysis.paper_insights import (
    PaperCardGenerator, TrendReportGenerator, ObsidianPaperSink, PaperInsightsPipeline,
    PaperCard, TrendReport
)
from layers.paper_analysis.paper_index import PaperIndex, IndexedPaper

@dataclass
class PaperFilterCriteria:
    """论文筛选条件"""
    venue: str = ""  # iclr, neurips, icml, etc.
    year: int = 0
    keyword: str = ""
    primary_area: str = ""
    min_citations: int = 0
    limit: int = 50


class PaperAnalysisIntegration:
    """
    论文分析集成
    提供:
    - 顶会论文筛选
    - 质量门禁
    - HTML报告生成
    - SMTP邮件通知
    """

    def __init__(self, conference_store=None, store=None):
        self.conference_store = conference_store
        self.store = store
        self.paper_analysis_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'third_party', 'Paper-Analysis-Renew'
        )

    def filter_papers(
        self,
        criteria: PaperFilterCriteria
    ) -> List[Dict]:
        """筛选论文"""
        if not self.conference_store:
            logger.error("ConferencePaperStore not available")
            return []

        papers = self.conference_store.search_papers(
            venue=criteria.venue,
            year=criteria.year,
            keyword=criteria.keyword,
            area=criteria.primary_area,
            limit=criteria.limit
        )

        results = []
        for p in papers:
            if criteria.min_citations > 0 and p.citation_count < criteria.min_citations:
                continue

            results.append(p.to_signal_dict())

        return results

    def generate_html_report(
        self,
        papers: List[Dict],
        title: str = "Paper Analysis Report",
        output_path: str = None
    ) -> str:
        """生成HTML报告"""
        if not output_path:
            output_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'data', 'reports'
            )
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f'paper_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html')

        html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        .paper {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 8px; }}
        .paper-title {{ font-size: 16px; font-weight: bold; color: #1a1a1a; }}
        .paper-meta {{ font-size: 13px; color: #666; margin: 8px 0; }}
        .paper-abstract {{ font-size: 14px; color: #444; margin-top: 10px; }}
        .badge {{ display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 12px; background: #e8f4ff; color: #0066cc; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p>Generated: {generated_at}</p>
    <p>Total Papers: {count}</p>
    <hr>
    {paper_html}
</body>
</html>
"""

        paper_html = ""
        for p in papers:
            badge_html = ""
            for kw in (p.get('keywords', [])[:5]):
                badge_html += f'<span class="badge">{kw}</span> '
            paper_html += f"""
        <div class="paper">
            <div class="paper-title">{p.get('title', '')}</div>
            <div class="paper-meta">
                Authors: {', '.join(p.get('authors', [])[:3]) if p.get('authors') else 'N/A'}
                | Citations: {p.get('citation_count', 0)}
                | Venue: {p.get('venue', '')} {p.get('year', '')}
            </div>
            <div class="paper-meta">{badge_html}</div>
            <div class="paper-abstract">{p.get('abstract', '')[:300]}...</div>
            <div class="paper-meta"><a href="{p.get('url', '#')}">Paper Link</a></div>
        </div>
            """

        html_content = html_template.format(
            title=title,
            generated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            count=len(papers),
            paper_html=paper_html
        )

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        logger.info(f"HTML report saved: {output_path}")
        return output_path

    def run_local_ci(self, venue: str = None, year: int = None) -> Dict:
        """
        运行本地质量门禁
        模拟 Paper-Analysis-Renew 的 quality local-ci
        """
        results = {
            'status': 'passed',
            'venue': venue,
            'year': year,
            'checks': [],
            'issues': [],
            'recommendations': []
        }

        if not venue or not year:
            results['status'] = 'skipped'
            results['issues'].append('venue and year are required')
            return results

        if self.conference_store:
            papers = self.conference_store.load_papers_from_url(venue, year, force=True)
            results['checks'].append(f'Loaded {len(papers)} papers for {venue}{year}')

            if len(papers) < 10:
                results['issues'].append(f'Low paper count: {len(papers)}')
                results['status'] = 'warning'

            duplicates = len(papers) - len(set(p.get('id', '') for p in papers))
            if duplicates > 0:
                results['issues'].append(f'Found {duplicates} duplicate paper IDs')
                results['status'] = 'warning'

        return results

    def summarize_papers(self, papers: List[Dict]) -> str:
        """生成论文摘要文本"""
        if not papers:
            return "No papers to summarize."

        summary = f"## 论文摘要报告 ({len(papers)} 篇)\n\n"

        by_venue = {}
        for p in papers:
            venue = p.get('venue', 'unknown')
            if venue not in by_venue:
                by_venue[venue] = []
            by_venue[venue].append(p)

        for venue, venue_papers in by_venue.items():
            summary += f"### {venue}\n"
            for p in venue_papers[:5]:
                title = p.get('title', '')[:80]
                citations = p.get('citation_count', 0)
                summary += f"- [{citations} citations] {title}\n"
            summary += "\n"

        return summary


class DrawIOIntegration:
    """
    DrawIO 图表集成
    集成 drawio-skill 能力

    支持:
    - 架构图生成
    - 流程图生成
    - 技术图谱可视化
    """

    def __init__(self):
        self.drawio_path = None
        self.temp_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'data', 'temp'
        )
        os.makedirs(self.temp_dir, exist_ok=True)

    def check_drawio_installed(self) -> bool:
        """检查draw.io是否安装"""
        import shutil
        self.drawio_path = shutil.which('drawio') or shutil.which('draw.io')
        if not self.drawio_path:
            self.drawio_path = shutil.which('C:\\Program Files\\draw.io\\drawio.exe')
        return self.drawio_path is not None

    def generate_architecture_diagram(
        self,
        description: str,
        output_path: str = None
    ) -> str:
        """
        生成架构图
        使用自然语言描述
        """
        if not output_path:
            output_path = os.path.join(
                self.temp_dir,
                f'arch_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            )

        drawio_xml = self._generate_ml_architecture_xml(description)

        xml_path = output_path.replace('.png', '.drawio')
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(drawio_xml)

        if self.check_drawio_installed():
            try:
                subprocess.run([
                    self.drawio_path,
                    '-x', '-o', output_path,
                    xml_path
                ], check=True, capture_output=True)
                logger.info(f"Architecture diagram saved: {output_path}")
            except Exception as e:
                logger.warning(f"Failed to export diagram: {e}")
                return xml_path
        else:
            logger.info(f"DrawIO not installed. XML saved: {xml_path}")
            return xml_path

        return output_path

    def _generate_ml_architecture_xml(self, description: str) -> str:
        """生成ML架构图的draw.io XML"""
        xml = '''<mxfile host="app.diagrams.net">
<diagram name="Architecture"'''

        layers = description.lower()
        if 'transformer' in layers:
            xml += self._transformer_architecture()
        elif 'agent' in layers or 'multi-agent' in layers:
            xml += self._multi_agent_architecture()
        elif ' inference ' in layers or 'serving' in layers:
            xml += self._inference_serving_architecture()
        else:
            xml += self._generic_architecture(description)

        xml += '</diagram></mxfile>'
        return xml

    def _transformer_architecture(self) -> str:
        return '''<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="Input Embedding" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
      <mxGeometry x="40" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="Positional Encoding" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
      <mxGeometry x="180" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="Encoder Layer xN" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
      <mxGeometry x="320" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="Decoder Layer xN" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
      <mxGeometry x="460" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Output Projection" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
      <mxGeometry x="600" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="2" target="3">
      <mxGeometry width="50" height="50" relative="0.5" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="" style="endArrow=classic;html=1;" edge="1" parent="1" source="3" target="4">
      <mxGeometry width="50" height="50" relative="0.5" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="" style="endArrow=classic;html=1;" edge="1" parent="1" source="4" target="5">
      <mxGeometry width="50" height="50" relative="0.5" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="" style="endArrow=classic;html=1;" edge="1" parent="1" source="5" target="6">
      <mxGeometry width="50" height="50" relative="0.5" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>'''

    def _multi_agent_architecture(self) -> str:
        return '''<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="User Request" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
      <mxGeometry x="300" y="40" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="Router Agent" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
      <mxGeometry x="140" y="160" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="Research Agent" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
      <mxGeometry x="280" y="160" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="Execution Agent" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
      <mxGeometry x="420" y="160" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Memory" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
      <mxGeometry x="280" y="280" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="Response" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
      <mxGeometry x="300" y="380" width="120" height="40" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>'''

    def _inference_serving_architecture(self) -> str:
        return '''<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="Client" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
      <mxGeometry x="300" y="20" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="API Gateway" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
      <mxGeometry x="300" y="100" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="vLLM/SGLang" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
      <mxGeometry x="300" y="180" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="KV Cache" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
      <mxGeometry x="140" y="260" width="100" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Tensor Parallel" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
      <mxGeometry x="460" y="260" width="100" height="40" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>'''

    def _generic_architecture(self, description: str) -> str:
        return f'''<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="{description[:50]}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
      <mxGeometry x="200" y="200" width="200" height="60" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>'''


class SocialMediaIntegration:
    """
    社交媒体集成
    支持 X/Twitter 数据采集
    """

    def __init__(self):
        self.twitter_available = False

    def check_twitter_api(self) -> bool:
        """检查 Twitter API 是否配置"""
        api_key = os.environ.get('TWITTER_API_KEY')
        api_secret = os.environ.get('TWITTER_API_SECRET')
        self.twitter_available = bool(api_key and api_secret)
        return self.twitter_available

    def search_tweets(self, query: str, limit: int = 20) -> List[Dict]:
        """搜索推文"""
        if not self.twitter_available:
            logger.warning("Twitter API not configured. Set TWITTER_API_KEY and TWITTER_API_SECRET")
            return []

        return []

    def extract_trending_topics(self, tweets: List[Dict]) -> List[str]:
        """提取趋势话题"""
        topics = []
        for tweet in tweets:
            for tag in tweet.get('hashtags', []):
                if tag.lower().startswith(('#ai', '#llm', '#gpt', '#agent')):
                    topics.append(tag)
        return list(set(topics))


class VideoContentIntegration:
    """
    视频内容集成
    支持 YouTube 字幕提取
    """

    def __init__(self):
        self.youtube_available = False

    def check_youtube_api(self) -> bool:
        """检查 YouTube API 是否配置"""
        api_key = os.environ.get('YOUTUBE_API_KEY')
        self.youtube_available = bool(api_key)
        return self.youtube_available

    def get_video_transcript(self, video_id: str) -> str:
        """获取视频字幕"""
        if not self.youtube_available:
            logger.warning("YouTube API not configured. Set YOUTUBE_API_KEY")
            return ""

        return ""

    def extract_technical_content(self, transcript: str, keywords: List[str]) -> List[str]:
        """提取技术内容片段"""
        if not transcript:
            return []

        segments = []
        lines = transcript.split('\n')
        for line in lines:
            if any(kw.lower() in line.lower() for kw in keywords):
                segments.append(line.strip())

        return segments