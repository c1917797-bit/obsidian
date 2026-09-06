"""
Semantic Search Layer - RAG Implementation
Learned from Khoj: https://github.com/khoj-ai/khoj
"""
import os
import json
import numpy as np
from typing import List, Dict, Optional, Tuple
from datetime import datetime

from core.logger import get_logger

logger = get_logger("SemanticSearch")

class SemanticSearch:
    """
    语义搜索引擎
    基于向量相似度的知识检索
    支持多种embedding模型
    """

    def __init__(self, store=None, embedder=None):
        self.store = store
        self.embedder = embedder
        self._index_cache = {}
        self._similarity_threshold = 0.7

    def initialize_embedder(self, model_type: str = "minimax"):
        """初始化embedding模型"""
        if model_type == "minimax":
            from core.minimax_client import get_client
            self.embedder = MinimaxEmbedder(client=get_client())
        elif model_type == "local":
            try:
                from sentence_transformers import SentenceTransformer
                self.embedder = LocalEmbedder(model_name="all-MiniLM-L6-v2")
            except ImportError:
                logger.warning("sentence-transformers not installed, falling back to minimax")
                from core.minimax_client import get_client
                self.embedder = MinimaxEmbedder(client=get_client())
        else:
            from core.minimax_client import get_client
            self.embedder = MinimaxEmbedder(client=get_client())

    def index_events(self, events: List) -> int:
        """为事件建立向量索引"""
        if not self.embedder:
            self.initialize_embedder()

        indexed_count = 0
        for event in events:
            try:
                text = self._event_to_text(event)
                embedding = self.embedder.embed(text)

                if not hasattr(event, 'embedding'):
                    event.embedding = embedding.tolist() if isinstance(embedding, np.ndarray) else embedding

                self._index_cache[event.id] = {
                    'event_id': event.id,
                    'embedding': event.embedding,
                    'text': text[:500],
                    'title': getattr(event, 'title', ''),
                    'entity': getattr(event, 'entity', ''),
                    'time': getattr(event, 'time', ''),
                    'importance': getattr(event, 'importance', 'P2'),
                    'indexed_at': datetime.now().isoformat()
                }
                indexed_count += 1
            except Exception as e:
                logger.error(f"Failed to index event {event.id}: {e}")

        return indexed_count

    def _event_to_text(self, event) -> str:
        """将事件转换为文本用于embedding"""
        parts = []
        if hasattr(event, 'title') and event.title:
            parts.append(event.title)
        if hasattr(event, 'summary') and event.summary:
            parts.append(event.summary)
        if hasattr(event, 'entity') and event.entity:
            parts.append(event.entity)
        if hasattr(event, 'tech_categories') and event.tech_categories:
            parts.append(', '.join(event.tech_categories))
        if hasattr(event, 'innovation') and event.innovation:
            parts.append(event.innovation)
        return ' | '.join(parts)

    def search(self, query: str, top_k: int = 5, filters: Dict = None) -> List[Dict]:
        """
        语义搜索
        返回与query最相关的事件
        """
        if not self._index_cache:
            logger.warning("Index is empty, no search results")
            return []

        if not self.embedder:
            self.initialize_embedder()

        try:
            query_embedding = self.embedder.embed(query)

            results = []
            for event_id, event_data in self._index_cache.items():
                if filters:
                    if not self._passes_filters(event_data, filters):
                        continue

                similarity = self._cosine_similarity(
                    query_embedding,
                    np.array(event_data['embedding'])
                )

                if similarity >= self._similarity_threshold:
                    results.append({
                        'event_id': event_id,
                        'similarity': float(similarity),
                        'title': event_data['title'],
                        'entity': event_data['entity'],
                        'text': event_data['text'][:300],
                        'time': event_data['time'],
                        'importance': event_data['importance']
                    })

            results.sort(key=lambda x: x['similarity'], reverse=True)
            return results[:top_k]

        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    def _passes_filters(self, event_data: Dict, filters: Dict) -> bool:
        """检查事件是否通过过滤条件"""
        if 'importance' in filters:
            if event_data.get('importance') not in filters['importance']:
                return False
        if 'entity' in filters:
            if filters['entity'].lower() not in event_data.get('entity', '').lower():
                return False
        if 'days' in filters:
            event_time = datetime.fromisoformat(event_data.get('time', '2020-01-01'))
            days_ago = (datetime.now() - event_time).days
            if days_ago > filters['days']:
                return False
        return True

    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """计算余弦相似度"""
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot_product / (norm1 * norm2)

    def get_related_events(self, event_id: str, top_k: int = 3) -> List[Dict]:
        """获取与指定事件相关的其他事件"""
        if event_id not in self._index_cache:
            return []

        source_event = self._index_cache[event_id]
        source_embedding = np.array(source_event['embedding'])

        results = []
        for other_id, other_data in self._index_cache.items():
            if other_id == event_id:
                continue

            similarity = self._cosine_similarity(
                source_embedding,
                np.array(other_data['embedding'])
            )

            if similarity > 0.5:
                results.append({
                    'event_id': other_id,
                    'similarity': float(similarity),
                    'title': other_data['title'],
                    'entity': other_data['entity']
                })

        results.sort(key=lambda x: x['similarity'], reverse=True)
        return results[:top_k]

    def build_index_from_store(self, days: int = 30) -> int:
        """从存储构建索引"""
        if not self.store:
            from core.storage import UnifiedStore
            self.store = UnifiedStore()

        events = self.store.get_recent_events(days=days, limit=500)
        return self.index_events(events)

    def save_index(self, filepath: str = None) -> str:
        """保存索引到文件"""
        if not filepath:
            data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
            os.makedirs(data_dir, exist_ok=True)
            filepath = os.path.join(data_dir, 'semantic_index.json')

        index_data = {
            'events': list(self._index_cache.values()),
            'saved_at': datetime.now().isoformat(),
            'count': len(self._index_cache)
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

        logger.info(f"Saved semantic index: {filepath}")
        return filepath

    def load_index(self, filepath: str = None) -> int:
        """从文件加载索引"""
        if not filepath:
            data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
            filepath = os.path.join(data_dir, 'semantic_index.json')

        if not os.path.exists(filepath):
            logger.warning(f"Index file not found: {filepath}")
            return 0

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                index_data = json.load(f)

            self._index_cache = {}
            for event_data in index_data.get('events', []):
                self._index_cache[event_data['event_id']] = event_data

            logger.info(f"Loaded {len(self._index_cache)} events into semantic index")
            return len(self._index_cache)
        except Exception as e:
            logger.error(f"Failed to load index: {e}")
            return 0


class MinimaxEmbedder:
    """MiniMax embedding封装"""

    def __init__(self, client):
        self.client = client

    def embed(self, text: str) -> np.ndarray:
        """使用MiniMax API生成embedding"""
        try:
            response = self.client.chat([
                {"role": "user", "content": f"Generate a dense embedding for the following text. Return ONLY a JSON array of numbers, no explanation: {text[:1000]}"}
            ], temperature=0.0, max_tokens=1024)

            embedding = self._parse_response(response)
            return np.array(embedding)
        except Exception as e:
            logger.error(f"Embedding failed: {e}")
            return np.zeros(256)

    def _parse_response(self, response: str) -> List[float]:
        """解析embedding响应"""
        try:
            import re
            numbers = re.findall(r'-?\d+\.?\d*', response)
            return [float(n) for n in numbers[:256]]
        except:
            return [0.0] * 256


class LocalEmbedder:
    """本地embedding模型封装"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name)
        self.dimension = 384

    def embed(self, text: str) -> np.ndarray:
        """使用本地模型生成embedding"""
        embedding = self.model.encode(text[:1000])
        return embedding


class QueryEngine:
    """
    自然语言查询引擎
    整合语义搜索和知识图谱
    """

    def __init__(self, semantic_search: SemanticSearch, store=None):
        self.semantic_search = semantic_search
        self.store = store

    def ask(self, question: str, context: str = None) -> str:
        """
        回答自然语言问题
        结合语义搜索和LLM生成
        """
        relevant_events = self.semantic_search.search(question, top_k=5)

        if not relevant_events:
            return "暂无相关信息"

        context_text = self._build_context(relevant_events, context)

        prompt = f"""基于以下技术事件信息，回答用户问题。

用户问题: {question}

相关事件信息:
{context_text}

请简洁准确地回答。如果信息不足，请说明。
直接输出回答内容，不要解释。"""

        from core.minimax_client import get_client
        client = get_client()

        try:
            answer = client.chat([{"role": "user", "content": prompt}])
            return answer
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return f"查询失败: {e}"

    def _build_context(self, events: List[Dict], extra_context: str = None) -> str:
        """构建上下文文本"""
        context_parts = []

        if extra_context:
            context_parts.append(f"背景信息: {extra_context}")

        context_parts.append("相关事件:")
        for i, event in enumerate(events, 1):
            context_parts.append(f"{i}. [{event['title']}] @ {event['entity']}")
            context_parts.append(f"   相关度: {event['similarity']:.2f}")
            context_parts.append(f"   摘要: {event.get('text', 'N/A')[:200]}")

        return '\n'.join(context_parts)

    def expand_query(self, query: str) -> List[str]:
        """扩展查询，生成相关查询变体"""
        prompt = f"""为以下查询生成3个相关的查询变体，用于信息检索。
原查询: {query}
要求: 直接输出3个变体，每个一行，不要解释。"""

        from core.minimax_client import get_client
        client = get_client()

        try:
            response = client.chat([{"role": "user", "content": prompt}])
            variants = [line.strip() for line in response.split('\n') if line.strip()]
            return variants[:3] if variants else [query]
        except:
            return [query]

    def get_concept_graph(self, concept: str, depth: int = 2) -> Dict:
        """
        获取概念图谱
        返回与概念相关的其他概念及其关系
        """
        search_results = self.semantic_search.search(concept, top_k=20)

        concepts = {concept: {'related': [], 'mentions': 1}}

        for result in search_results:
            text = result.get('text', '')
            if concept.lower() in text.lower():
                concepts[concept]['mentions'] += 1

            words = text.split()
            for word in words:
                if len(word) > 5 and word not in concepts:
                    concepts[word] = {'related': [concept], 'mentions': 1}
                elif word in concepts and concept not in concepts[word]['related']:
                    concepts[word]['related'].append(concept)

        return {
            'central_concept': concept,
            'related_concepts': [
                {'name': k, 'mentions': v['mentions'], 'related_to': v['related']}
                for k, v in concepts.items() if k != concept
            ],
            'depth': depth
        }


def create_semantic_search(store=None) -> SemanticSearch:
    """创建语义搜索实例"""
    return SemanticSearch(store=store)


def create_query_engine(semantic_search: SemanticSearch, store=None) -> QueryEngine:
    """创建查询引擎实例"""
    return QueryEngine(semantic_search=semantic_search, store=store)