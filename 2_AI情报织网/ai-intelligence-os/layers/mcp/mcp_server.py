"""
MCP Server Integration
Model Context Protocol - 让AI Intelligence OS可以被Claude Code等工具调用
"""
import os
import json
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum

from core.logger import get_logger

logger = get_logger("MCPServer")

class MCPResource:
    """MCP资源"""

    def __init__(self, uri: str, name: str, description: str = "", mime_type: str = "text/markdown"):
        self.uri = uri
        self.name = name
        self.description = description
        self.mime_type = mime_type

    def to_dict(self) -> Dict:
        return {
            "uri": self.uri,
            "name": self.name,
            "description": self.description,
            "mimeType": self.mime_type
        }


class MCPTool:
    """MCP工具"""

    def __init__(self, name: str, description: str, input_schema: Dict):
        self.name = name
        self.description = description
        self.input_schema = input_schema

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.input_schema
        }


class MCPService:
    """
    MCP服务器实现
    让Intelligence OS可以作为MCP服务器被其他AI工具调用
    """

    def __init__(self, store=None, trend_engine=None, insight_agent=None):
        self.store = store
        self.trend_engine = trend_engine
        self.insight_agent = insight_agent
        self._resources = []
        self._tools = []
        self._initialize_resources()
        self._initialize_tools()

    def _initialize_resources(self):
        """初始化MCP资源"""
        self._resources = [
            MCPResource(
                uri="intelligence://daily-report",
                name="daily-report",
                description="Today's AI intelligence daily report"
            ),
            MCPResource(
                uri="intelligence://weekly-report",
                name="weekly-report",
                description="Current week's AI intelligence report"
            ),
            MCPResource(
                uri="intelligence://trending",
                name="trending-techs",
                description="Currently trending AI technologies"
            ),
            MCPResource(
                uri="intelligence://events",
                name="recent-events",
                description="Recent AI technology events"
            ),
            MCPResource(
                uri="intelligence://stats",
                name="system-stats",
                description="Intelligence OS system statistics"
            ),
        ]

    def _initialize_tools(self):
        """初始化MCP工具"""
        self._tools = [
            MCPTool(
                name="search_intelligence",
                description="Search AI intelligence events and reports",
                input_schema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"},
                        "days": {"type": "integer", "description": "Days to search back", "default": 7},
                        "limit": {"type": "integer", "description": "Max results", "default": 10}
                    },
                    "required": ["query"]
                }
            ),
            MCPTool(
                name="get_company_strategy",
                description="Get company AI strategy analysis",
                input_schema={
                    "type": "object",
                    "properties": {
                        "company": {"type": "string", "description": "Company name (OpenAI, Anthropic, DeepSeek, Google, Meta, Microsoft, NVIDIA)"}
                    },
                    "required": ["company"]
                }
            ),
            MCPTool(
                name="get_tech_roadmap",
                description="Get technology roadmap and evolution",
                input_schema={
                    "type": "object",
                    "properties": {
                        "tech_area": {"type": "string", "description": "Technology area (speculative decoding, kv cache, flash attention, etc.)"}
                    },
                    "required": ["tech_area"]
                }
            ),
            MCPTool(
                name="get_trend_summary",
                description="Get technology trend summary",
                input_schema={
                    "type": "object",
                    "properties": {
                        "days": {"type": "integer", "description": "Days to analyze", "default": 7}
                    }
                }
            ),
            MCPTool(
                name="get_convergence_report",
                description="Get technology convergence analysis",
                input_schema={
                    "type": "object",
                    "properties": {
                        "days": {"type": "integer", "description": "Days to analyze", "default": 30}
                    }
                }
            ),
            MCPTool(
                name="query_semantic",
                description="Semantic search using AI embeddings",
                input_schema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Natural language query"},
                        "top_k": {"type": "integer", "description": "Number of results", "default": 5}
                    },
                    "required": ["query"]
                }
            ),
            MCPTool(
                name="get_recent_papers",
                description="Get recent AI research papers",
                input_schema={
                    "type": "object",
                    "properties": {
                        "venue": {"type": "string", "description": "Conference venue (iclr, neurips, icml, cvpr, etc.)"},
                        "year": {"type": "integer", "description": "Publication year"},
                        "keyword": {"type": "string", "description": "Search keyword"}
                    }
                }
            ),
            MCPTool(
                name="generate_insight_report",
                description="Generate a structured insight report",
                input_schema={
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "description": "Topic to analyze"},
                        "depth": {"type": "string", "description": "Analysis depth (quick, medium, deep)", "default": "medium"}
                    },
                    "required": ["topic"]
                }
            )
        ]

    def get_resources(self) -> List[Dict]:
        """获取所有资源定义"""
        return [r.to_dict() for r in self._resources]

    def get_tools(self) -> List[Dict]:
        """获取所有工具定义"""
        return [t.to_dict() for t in self._tools]

    def handle_tool_call(self, tool_name: str, arguments: Dict) -> Any:
        """处理工具调用"""
        try:
            if tool_name == "search_intelligence":
                return self._search_intelligence(**arguments)
            elif tool_name == "get_company_strategy":
                return self._get_company_strategy(**arguments)
            elif tool_name == "get_tech_roadmap":
                return self._get_tech_roadmap(**arguments)
            elif tool_name == "get_trend_summary":
                return self._get_trend_summary(**arguments)
            elif tool_name == "get_convergence_report":
                return self._get_convergence_report(**arguments)
            elif tool_name == "query_semantic":
                return self._query_semantic(**arguments)
            elif tool_name == "get_recent_papers":
                return self._get_recent_papers(**arguments)
            elif tool_name == "generate_insight_report":
                return self._generate_insight_report(**arguments)
            else:
                return {"error": f"Unknown tool: {tool_name}"}
        except Exception as e:
            logger.error(f"Tool call failed: {tool_name}, {e}")
            return {"error": str(e)}

    def _search_intelligence(self, query: str, days: int = 7, limit: int = 10) -> Dict:
        """搜索情报"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        events = self.store.get_recent_events(days=days, limit=limit*2)

        query_lower = query.lower()
        filtered = [
            e for e in events
            if query_lower in (getattr(e, 'title', '') or '').lower()
            or query_lower in (getattr(e, 'summary', '') or '').lower()
            or query_lower in (getattr(e, 'entity', '') or '').lower()
        ]

        results = []
        for e in filtered[:limit]:
            results.append({
                "id": e.id,
                "title": getattr(e, 'title', ''),
                "entity": getattr(e, 'entity', ''),
                "time": getattr(e, 'time', ''),
                "importance": getattr(e, 'importance', 'P2'),
                "summary": getattr(e, 'summary', '')[:200],
                "url": getattr(e, 'url', '')
            })

        return {
            "query": query,
            "count": len(results),
            "results": results
        }

    def _get_company_strategy(self, company: str) -> Dict:
        """获取公司战略"""
        if not self.insight_agent:
            from layers.insight.insight_agent import InsightAgent
            from core.storage import UnifiedStore
            self.insight_agent = InsightAgent(store=UnifiedStore())

        report = self.insight_agent.generate_company_strategy_report(company)
        return {
            "company": company,
            "report_title": report.title,
            "content": report.content[:2000]
        }

    def _get_tech_roadmap(self, tech_area: str) -> Dict:
        """获取技术路线图"""
        if not self.insight_agent:
            from layers.insight.insight_agent import InsightAgent
            from core.storage import UnifiedStore
            self.insight_agent = InsightAgent(store=UnifiedStore())

        report = self.insight_agent.generate_tech_roadmap(tech_area)
        return {
            "tech_area": tech_area,
            "report_title": report.title,
            "content": report.content[:2000]
        }

    def _get_trend_summary(self, days: int = 7) -> Dict:
        """获取趋势摘要"""
        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            from core.storage import UnifiedStore
            self.trend_engine = TrendEngine(store=UnifiedStore())

        summary = self.trend_engine.get_trend_summary(days=days)
        return summary

    def _get_convergence_report(self, days: int = 30) -> Dict:
        """获取收敛报告"""
        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            from core.storage import UnifiedStore
            self.trend_engine = TrendEngine(store=UnifiedStore())

        converging = self.trend_engine.get_converging_techs(days=days)
        production_ready = self.trend_engine.get_production_ready(days=days)

        return {
            "converging_techs": converging[:10],
            "production_ready": production_ready[:10],
            "analyzed_days": days
        }

    def _query_semantic(self, query: str, top_k: int = 5) -> Dict:
        """语义查询"""
        try:
            from layers.rag.semantic_search import create_semantic_search, create_query_engine

            semantic_search = create_semantic_search(store=self.store)
            semantic_search.load_index()
            semantic_search.build_index_from_store(days=30)

            query_engine = create_query_engine(semantic_search, store=self.store)
            answer = query_engine.ask(query)

            return {
                "query": query,
                "answer": answer
            }
        except Exception as e:
            logger.error(f"Semantic query failed: {e}")
            return {"error": f"Semantic query failed: {e}"}

    def _get_recent_papers(self, venue: str = None, year: int = None, keyword: str = None) -> Dict:
        """获取最近论文"""
        try:
            from layers.paper_analysis.conference_papers import ConferencePaperStore

            store = ConferencePaperStore()
            papers = store.search_papers(venue=venue, year=year, keyword=keyword, limit=20)

            return {
                "venue": venue,
                "year": year,
                "keyword": keyword,
                "count": len(papers),
                "papers": [
                    {
                        "title": p.title,
                        "authors": p.authors[:3] if hasattr(p, 'authors') else [],
                        "citation_count": getattr(p, 'citation_count', 0),
                        "url": p.url if hasattr(p, 'url') else ''
                    }
                    for p in papers[:10]
                ]
            }
        except Exception as e:
            logger.error(f"Get papers failed: {e}")
            return {"error": str(e)}

    def _generate_insight_report(self, topic: str, depth: str = "medium") -> Dict:
        """生成洞察报告"""
        try:
            from layers.paper_analysis.deep_research import DeepResearchPipeline, ResearchQuery

            if not self.store:
                from core.storage import UnifiedStore
                self.store = UnifiedStore()

            pipeline = DeepResearchPipeline(store=self.store)
            scope = "technical" if depth == "deep" else "overview"
            query = ResearchQuery(topic=topic, scope=scope, depth=depth)

            finding = pipeline.run_research(query)

            return {
                "topic": topic,
                "depth": depth,
                "key_points": finding.key_points[:10] if hasattr(finding, 'key_points') else [],
                "summary": finding.summary[:500] if hasattr(finding, 'summary') else ''
            }
        except Exception as e:
            logger.error(f"Generate report failed: {e}")
            return {"error": str(e)}

    def read_resource(self, uri: str) -> Dict:
        """读取资源内容"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        if "daily-report" in uri:
            events = self.store.get_recent_events(days=1, limit=20)
            return self._format_events_as_markdown(events, "今日AI情报")
        elif "weekly-report" in uri:
            events = self.store.get_recent_events(days=7, limit=50)
            return self._format_events_as_markdown(events, "本周AI情报")
        elif "trending" in uri:
            return self._get_trending_markdown()
        elif "events" in uri:
            events = self.store.get_recent_events(days=7, limit=30)
            return self._format_events_as_markdown(events, "近期事件")
        elif "stats" in uri:
            return self._get_stats_markdown()
        else:
            return {"error": f"Unknown resource: {uri}"}

    def _format_events_as_markdown(self, events: List, title: str) -> Dict:
        """将事件格式化为Markdown"""
        lines = [f"# {title}\n"]
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        lines.append(f"**事件数量**: {len(events)}\n\n")

        for e in events[:15]:
            lines.append(f"## {getattr(e, 'title', 'Unknown')}\n")
            lines.append(f"- **实体**: {getattr(e, 'entity', 'Unknown')}")
            lines.append(f"- **时间**: {getattr(e, 'time', '')}")
            lines.append(f"- **重要性**: {getattr(e, 'importance', 'P2')}")
            lines.append(f"- **摘要**: {getattr(e, 'summary', '')[:200]}...\n")

        return {
            "contents": [{
                "uri": f"intelligence://{title}",
                "mimeType": "text/markdown",
                "text": '\n'.join(lines)
            }]
        }

    def _get_trending_markdown(self) -> Dict:
        """获取趋势Markdown"""
        if not self.trend_engine:
            from layers.trends.trend_engine import TrendEngine
            from core.storage import UnifiedStore
            self.trend_engine = TrendEngine(store=UnifiedStore())

        summary = self.trend_engine.get_trend_summary(days=7)

        lines = ["# 热门技术趋势\n"]
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        lines.append("## 热门技术\n")
        for tech in summary.get('trending_techs', [])[:5]:
            lines.append(f"- {tech}")

        lines.append("\n## 收敛中的技术\n")
        for tech in summary.get('converging_techs', [])[:5]:
            lines.append(f"- {tech}")

        lines.append("\n## 生产就绪\n")
        for proj in summary.get('production_ready', [])[:5]:
            lines.append(f"- {proj}")

        return {
            "contents": [{
                "uri": "intelligence://trending",
                "mimeType": "text/markdown",
                "text": '\n'.join(lines)
            }]
        }

    def _get_stats_markdown(self) -> Dict:
        """获取统计Markdown"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        stats = self.store.get_stats()

        lines = ["# Intelligence OS 统计\n"]
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        lines.append(f"- 总信号数: {stats.get('total_signals', 0)}")
        lines.append(f"- 本周信号: {stats.get('signals_this_week', 0)}")
        lines.append(f"- 总事件数: {stats.get('total_events', 0)}")
        lines.append(f"- 本周事件: {stats.get('events_this_week', 0)}")
        lines.append(f"- 启用信源: {stats.get('enabled_sources', 0)}\n")

        lines.append("## 事件类型分布\n")
        for et, count in stats.get('events_by_type', {}).items():
            lines.append(f"- {et}: {count}")

        return {
            "contents": [{
                "uri": "intelligence://stats",
                "mimeType": "text/markdown",
                "text": '\n'.join(lines)
            }]
        }

    def start_server(self, host: str = "localhost", port: int = 8765):
        """启动MCP服务器"""
        try:
            from mcp.server import Server
            from mcp.server.stdio import stdio_server
            import asyncio

            server = Server(name="IntelligenceOS-MCP")

            @server.list_resources()
            async def list_resources():
                return self.get_resources()

            @server.read_resource()
            async def read_resource(uri: str):
                return self.read_resource(uri)

            @server.list_tools()
            async def list_tools():
                return self.get_tools()

            @server.call_tool()
            async def call_tool(name: str, arguments: Dict):
                return self.handle_tool_call(name, arguments)

            async def run():
                async with stdio_server() as (read_stream, write_stream):
                    await server.run(read_stream, write_stream, server.create_initialization_options())

            asyncio.run(run())

        except ImportError:
            logger.error("mcp package not installed. Run: pip install mcp")
            logger.info("Alternative: Use HTTP server mode")
            self._start_http_server(host, port)

    def _start_http_server(self, host: str, port: int):
        """启动HTTP服务器模式"""
        try:
            from flask import Flask, request, jsonify

            app = Flask(__name__)

            @app.route('/resources', methods=['GET'])
            def list_resources():
                return jsonify(self.get_resources())

            @app.route('/resources/<path:uri>', methods=['GET'])
            def get_resource(uri):
                result = self.read_resource(f"intelligence://{uri}")
                return jsonify(result)

            @app.route('/tools', methods=['GET'])
            def list_tools():
                return jsonify(self.get_tools())

            @app.route('/tools/call', methods=['POST'])
            def call_tool():
                data = request.json
                result = self.handle_tool_call(data.get('name'), data.get('arguments', {}))
                return jsonify(result)

            logger.info(f"Starting HTTP MCP server on {host}:{port}")
            app.run(host=host, port=port)

        except ImportError:
            logger.error("flask not installed. Run: pip install flask")


class MCPClient:
    """
    MCP客户端
    用于连接其他MCP服务器
    """

    def __init__(self, server_url: str = None):
        self.server_url = server_url or os.environ.get('MCP_SERVER_URL', 'http://localhost:8765')

    def call_tool(self, tool_name: str, arguments: Dict = None) -> Any:
        """调用远程工具"""
        import requests

        try:
            response = requests.post(
                f"{self.server_url}/tools/call",
                json={"name": tool_name, "arguments": arguments or {}},
                timeout=30
            )
            return response.json()
        except Exception as e:
            logger.error(f"MCP call failed: {e}")
            return {"error": str(e)}

    def list_tools(self) -> List[Dict]:
        """列出远程工具"""
        import requests

        try:
            response = requests.get(f"{self.server_url}/tools", timeout=10)
            return response.json()
        except Exception as e:
            logger.error(f"MCP list failed: {e}")
            return []


def create_mcp_service(store=None, trend_engine=None, insight_agent=None) -> MCPService:
    """创建MCP服务实例"""
    return MCPService(store=store, trend_engine=trend_engine, insight_agent=insight_agent)


def setup_mcp_server():
    """设置MCP服务器并生成配置文件"""
    config = {
        "mcpServers": {
            "intelligence-os": {
                "command": "python",
                "args": ["-m", "layers.mcp.server"],
                "env": {
                    "OBSIDIAN_VAULT_PATH": os.environ.get('OBSIDIAN_VAULT_PATH', ''),
                    "MINIMAX_API_KEY": os.environ.get('MINIMAX_API_KEY', '')
                }
            }
        }
    }

    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'mcp_config.json')
    os.makedirs(os.path.dirname(config_path), exist_ok=True)

    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    logger.info(f"MCP config saved to: {config_path}")
    return config_path