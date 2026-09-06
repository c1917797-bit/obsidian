"""
MiniMax API 调用模块
支持对话补全、JSON模式输出
"""
import os
import json
import re
import requests
from typing import Optional, List, Dict, Any

class MiniMaxClient:
    def __init__(self, api_key: Optional[str] = None, group_id: Optional[str] = None):
        self.api_key = api_key or os.environ.get("MINIMAX_API_KEY") or "sk-cp-kPLl6HgnfToI4iu6hiLLzKtLoeOHlKO9czMW2IIgHTOhBPcLQ1czDnk2NnroVEs_jZh38L4akjtF_UOwhjMIeZpUFoBym772vtjm0hvQgAaM-5-tL5QNYok"
        self.group_id = group_id or os.environ.get("MINIMAX_GROUP_ID") or "1747208907339094016"
        self.base_url = "https://api.minimax.chat/v1"
        self.model = "MiniMax-Text-01"

    def chat(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096
    ) -> str:
        """发送对话请求"""
        if not self.api_key:
            raise ValueError("MINIMAX_API_KEY未设置")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        full_messages = []
        if system_prompt:
            full_messages.append({"role": "system", "content": system_prompt})
        full_messages.extend(messages)

        payload = {
            "model": self.model,
            "messages": full_messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "group_id": self.group_id
        }

        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=300
        )
        response.raise_for_status()

        # ── FIX: Force UTF-8 decoding before JSON parsing ──
        # requests defaults to ISO-8859-1/Windows-1252 when the server sends no
        # explicit charset, corrupting Chinese text. Set encoding first.
        response.encoding = 'utf-8'

        try:
            raw_content = response.json()["choices"][0]["message"]["content"]
        except (json.JSONDecodeError, UnicodeDecodeError):
            # Fallback: decode raw bytes as UTF-8 directly
            raw_content = response.content.decode('utf-8', errors='replace')
        content = raw_content.strip()

        # Remove thinking tags and content between them
        content = re.sub(r'<\|startofthink\|>.*?<\|endofthink\|>', '', content, flags=re.DOTALL)
        content = re.sub(r'<\|endofthink\|>.*?', '', content, flags=re.DOTALL)
        content = re.sub(r'<think>.*?', '', content, flags=re.DOTALL)

        # Try to find the actual formatted response after markers
        markers = [
            '[热点',
            '[AI-',
            '[一句话总结]',
            '# AI',
            '```\n['
        ]
        for marker in markers:
            idx = content.find(marker)
            if idx != -1:
                content = content[idx:]
                break

        # If still has prompt residue, try to find closing brackets
        if content.startswith('The user') or content.startswith('You are'):
            first_bracket = content.find('[')
            first_code = content.find('```')
            valid_starts = [x for x in [first_bracket, first_code] if x != -1]
            if valid_starts:
                start = min(valid_starts)
                content = content[start:]

        # Truncate if still contains multiple report-like blocks (take first block only)
        if content.count('[热点') > 1 or content.count('```\n[') > 1:
            # Keep only first complete block
            match = re.search(r'(\[热点[^\[]+\])', content)
            if match:
                content = content[:match.end()]

        # Final cleanup - remove any remaining prompt residue
        lines = content.split('\n')
        clean_lines = []
        for line in lines:
            if line.startswith('The user') or line.startswith('You are'):
                continue
            clean_lines.append(line)
        content = '\n'.join(clean_lines).strip()

        return content if content else raw_content.strip()

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        temperature: float = 0.3
    ) -> Dict[str, Any]:
        """发送请求并强制返回JSON格式"""
        if system_prompt and "json" not in system_prompt.lower():
            system_prompt += "\n\n必须返回有效的JSON，不要包含任何解释或markdown格式。"
        else:
            system_prompt = "你必须返回有效的JSON，不要包含任何解释或markdown格式。"

        result = self.chat(messages, system_prompt, temperature)
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            json_str = result.strip()
            for start in range(len(json_str)):
                if json_str[start] == '{' or json_str[start] == '[':
                    break
            for end in range(len(json_str), start, -1):
                if json_str[end-1] == '}' or json_str[end-1] == ']':
                    break
            return json.loads(json_str[start:end])

    def structured_extract(
        self,
        content: str,
        schema: Dict[str, Any],
        system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """根据schema提取结构化信息"""
        default_system = f"""你是一个信息提取专家。根据用户提供的原始内容，按照以下schema提取信息：

{json.dumps(schema, ensure_ascii=False, indent=2)}

要求：
1. 只返回符合schema的JSON
2. 不要添加任何解释
3. 如果原始内容中没有对应字段，使用null
4. 严格遵循字段类型"""
        if system_prompt:
            default_system = system_prompt

        messages = [{"role": "user", "content": content}]
        return self.chat_json(messages, default_system)

def get_client() -> MiniMaxClient:
    return MiniMaxClient()