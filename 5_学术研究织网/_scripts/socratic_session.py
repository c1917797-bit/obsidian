"""
苏格拉底对话会话管理器 (Socratic Dialogue Session Manager)
基于 Academic Research Skills v3.10 Socratic Mentoring System

功能:
- 5层对话结构追踪
- 意图检测 (exploratory vs goal-oriented)
- 对话健康监测 (每5轮)
- 承诺门 (Commitment Gate) 追踪
- 洞察提取

用法:
    python socratic_session.py --topic "研究主题" --project "项目名"
    python socratic_session.py --project "项目名" --continue-session
"""
import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict

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
DIALOGUE_DIR = OBSIDIAN_ROOT / "5_学术研究织网/对话日志"
PROJECT_DIR = OBSIDIAN_ROOT / "5_学术研究织网/研究项目"


@dataclass
class DialogueTurn:
    """单轮对话记录"""
    turn_id: int
    user_input: str
    ai_response: str
    intent_detected: str  # exploratory / goal-oriented
    layer: int
    layer_name: str
    key_insights: List[str] = field(default_factory=list)
    health_alerts: List[str] = field(default_factory=list)


@dataclass
class CommitmentGate:
    """承诺门记录"""
    layer: int
    question: str
    user_commitment: str
    passed: bool
    timestamp: str


@dataclass
class SocraticSession:
    """苏格拉底对话会话"""
    session_id: str
    project: str
    topic: str
    current_layer: int = 1
    layer_names: List[str] = field(default_factory=lambda: [
        "问题定义", "方法反思", "证据视角", "启示探索", "综合"
    ])
    intent: str = "exploratory"
    status: str = "in-progress"
    dialogue_turn_count: int = 0
    turns: List[DialogueTurn] = field(default_factory=list)
    commitment_gates: List[CommitmentGate] = field(default_factory=list)
    insights: List[str] = field(default_factory=list)
    health_alerts: List[str] = field(default_factory=list)
    dialogue_health: str = "healthy"
    created: str = ""
    last_updated: str = ""

    def __post_init__(self):
        if not self.created:
            self.created = datetime.now().isoformat()
        self.last_updated = datetime.now().isoformat()


class SocraticSessionManager:
    """苏格拉底对话会话管理器"""

    # 5层对话的问题模板
    LAYER_QUESTIONS = {
        1: [  # 问题定义
            "你为什么对这个话题感兴趣？",
            "你已经知道了什么？",
            "你想回答什么问题？",
            "这个问题为什么重要？",
            "谁会关心这个问题的答案？"
        ],
        2: [  # 方法反思
            "你打算用什么方法研究这个问题？",
            "你需要什么样的证据？",
            "什么样的数据能回答你的问题？",
            "你的研究设计能否真的验证你的假设？",
            "有哪些替代方法？"
        ],
        3: [  # 证据视角
            "你找到了什么证据？",
            "这些证据来自哪里？",
            "证据的质量如何？",
            "是否有相反的证据？",
            "你如何评估这些证据的可信度？"
        ],
        4: [  # 启示探索
            "从这些发现能得出什么结论？",
            "这些结论对现有知识有何贡献？",
            "审稿人会挑战什么？",
            "你的发现有何局限性？",
            "下一步应该做什么？"
        ],
        5: [  # 综合
            "经过这番对话，你学到了什么？",
            "你的研究问题是否需要调整？",
            "你接下来要做什么？"
        ]
    }

    # 高置信度词汇 (触发反恶魔代言人)
    HIGH_CONFIDENCE_WORDS = ["显然", "毫无疑问", "每个人都知道", "显然地", "毫无疑问地", "obviously", "clearly", "undoubtedly"]

    # 对话健康指标检测模式
    HEALTH_PATTERNS = {
        "persistent_agreement": ["同意", "是的", "没错", "对的", "I agree", "yes", "that's right"],
        "conflict_avoidance": ["但是", "不过", "然而", "虽然", "but", "however", "although"],
        "premature_convergence": ["那就这样", "结论是", "总结一下", "in conclusion", "to sum up"]
    }

    def __init__(self, project: str, topic: str = "", session_id: str = None):
        self.project = project
        self.topic = topic
        self.session_id = session_id or self._generate_session_id()
        self.client = get_client() if MINIMAX_AVAILABLE else None

        # 尝试加载已有会话
        self.session = self._load_session()

        if not self.session:
            self.session = SocraticSession(
                session_id=self.session_id,
                project=project,
                topic=topic,
                created=datetime.now().isoformat(),
                last_updated=datetime.now().isoformat()
            )

    def _generate_session_id(self) -> str:
        """生成会话ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_topic = self.topic[:20].replace(" ", "_") if self.topic else "session"
        return f"socratic_{safe_topic}_{timestamp}"

    def _load_session(self) -> Optional[SocraticSession]:
        """从 Obsidian 加载会话"""
        session_file = DIALOGUE_DIR / f"{self.session_id}.json"
        if session_file.exists():
            try:
                data = json.loads(session_file.read_text(encoding="utf-8"))
                return SocraticSession(**data)
            except Exception:
                return None
        return None

    def _save_session(self):
        """保存会话到 Obsidian"""
        DIALOGUE_DIR.mkdir(parents=True, exist_ok=True)
        session_file = DIALOGUE_DIR / f"{self.session_id}.json"
        session_file.write_text(json.dumps(asdict(self.session), ensure_ascii=False, indent=2), encoding="utf-8")

    def _generate_note_content(self) -> str:
        """生成 Obsidian 笔记内容"""
        session = self.session
        lines = [
            "---",
            f"type: socratic-dialogue",
            f'stage: "{self._get_stage_from_layer(session.current_layer)}"',
            f"intent: {session.intent}",
            f"dialogue_turn_count: {session.dialogue_turn_count}",
            f'layer: {session.current_layer}',
            f'layer_name: "{session.layer_names[session.current_layer - 1]}"',
            f"status: {session.status}",
            f"project: {session.project}",
            f"commitment_gate_passed: {str(self._check_commitment_gate_passed()).lower()}",
            f"dialogue_health: {session.dialogue_health}",
            f"health_alerts: {json.dumps(session.health_alerts, ensure_ascii=False)}",
            f"insights_gathered: {json.dumps(session.insights, ensure_ascii=False)}",
            f"created: {session.created}",
            f"last_updated: {session.last_updated}",
            "---",
            "",
            f"# 苏格拉底对话: {session.topic}",
            "",
            f"**会话ID**: {session.session_id}",
            f"**项目**: {session.project}",
            f"**当前层**: L{session.current_layer} - {session.layer_names[session.current_layer - 1]}",
            f"**意图状态**: {session.intent}",
            f"**对话轮次**: {session.dialogue_turn_count}",
            f"**健康状态**: {session.dialogue_health}",
            "",
            "## 对话记录",
            ""
        ]

        # 添加每轮对话
        for turn in session.turns:
            lines.extend([
                f"### 轮次 {turn.turn_id} (L{turn.layer} - {turn.layer_name})",
                "",
                f"**用户**: {turn.user_input}",
                "",
                f"**AI**: {turn.ai_response}",
                "",
            })
            if turn.key_insights:
                lines.append(f"**洞察**: {', '.join(turn.key_insights)}")
            if turn.health_alerts:
                lines.append(f"**健康警报**: {', '.join(turn.health_alerts)}")
            lines.append("")

        # 添加承诺门
        if session.commitment_gates:
            lines.extend(["", "## 承诺门 (Commitment Gates)", ""])
            for gate in session.commitment_gates:
                status = "✅" if gate.passed else "⏳"
                lines.extend([
                    f"### L{gate.layer} {status}",
                    f"**问题**: {gate.question}",
                    f"**用户承诺**: {gate.user_commitment}",
                    ""
                ])

        # 添加洞察收集
        if session.insights:
            lines.extend(["", "## 洞察收集 (INSIGHT Collection)", ""])
            for i, insight in enumerate(session.insights, 1):
                lines.append(f"{i}. [INSIGHT] {insight}")

        return "\n".join(lines)

    def _get_stage_from_layer(self, layer: int) -> str:
        """从层号获取阶段名"""
        stages = {
            1: "1-RESEARCH",
            2: "1-RESEARCH",
            3: "1-RESEARCH",
            4: "1-RESEARCH",
            5: "1-RESEARCH"
        }
        return stages.get(layer, "1-RESEARCH")

    def _check_commitment_gate_passed(self) -> bool:
        """检查当前层承诺门是否通过"""
        layer = self.session.current_layer
        for gate in self.session.commitment_gates:
            if gate.layer == layer and not gate.passed:
                return False
        return True

    def detect_intent(self, user_input: str) -> str:
        """意图检测 - 判断用户是探索型还是目标型"""
        # 探索型关键词
        exploratory_keywords = ["我想了解", "我在探索", "不确定", "也许", "可能", "怎么", "为什么", "什么", "探讨", "研究"]
        # 目标型关键词
        goal_keywords = ["我要", "我需要", "目标是", "完成", "得出结论", "写论文", "写报告"]

        user_lower = user_input.lower()
        for kw in goal_keywords:
            if kw in user_lower:
                return "goal-oriented"

        for kw in exploratory_keywords:
            if kw in user_lower:
                return "exploratory"

        return self.session.intent  # 保持之前的意图

    def check_dialogue_health(self) -> Tuple[str, List[str]]:
        """检查对话健康状态"""
        recent_turns = self.session.turns[-5:] if len(self.session.turns) >= 5 else self.session.turns

        if not recent_turns:
            return "healthy", []

        alerts = []
        health = "healthy"

        # 检查持续同意模式
        if len(recent_turns) >= 3:
            agreement_count = sum(1 for t in recent_turns if any(p in t.user_input for p in self.HEALTH_PATTERNS["persistent_agreement"]))
            if agreement_count >= len(recent_turns) * 0.7:
                alerts.append("persistent_agreement: 检测到持续同意模式")
                health = "warning"

        # 检查冲突回避
        if len(recent_turns) >= 3:
            avoidance_count = sum(1 for t in recent_turns if any(p in t.user_input for p in self.HEALTH_PATTERNS["conflict_avoidance"]))
            if avoidance_count == 0 and len(recent_turns) >= 3:
                alerts.append("conflict_avoidance: 未检测到分歧讨论")
                health = "warning"

        # 检查过早收敛
        last_input = recent_turns[-1].user_input if recent_turns else ""
        if any(p in last_input for p in self.HEALTH_PATTERNS["premature_convergence"]):
            alerts.append("premature_convergence: 检测到过早收敛")
            health = "critical"

        # 检查高置信度词汇 (反恶魔代言人触发)
        if any(w in last_input for w in self.HIGH_CONFIDENCE_WORDS):
            alerts.append(f"high_confidence_word_detected: 包含高置信度词汇")

        return health, alerts

    def generate_layer_question(self, layer: int) -> str:
        """生成当前层的问题"""
        questions = self.LAYER_QUESTIONS.get(layer, [])
        if questions:
            import random
            return random.choice(questions)
        return "请继续你的研究思考..."

    def process_user_input(self, user_input: str) -> Dict[str, Any]:
        """处理用户输入，生成 AI 响应"""
        session = self.session
        session.dialogue_turn_count += 1
        turn_id = session.dialogue_turn_count

        # 1. 意图检测
        intent = self.detect_intent(user_input)
        session.intent = intent

        # 2. 检查承诺门
        commitment_passed = self._check_commitment_gate_passed()

        # 3. 如果是探索型意图且当前轮次 % 5 == 0，重新评估意图
        if session.dialogue_turn_count % 5 == 0 and intent == "exploratory":
            session.intent = "exploratory"  # 保持探索模式

        # 4. 生成 AI 响应
        ai_response = self._generate_response(user_input, turn_id, intent)

        # 5. 检查对话健康
        health, alerts = self.check_dialogue_health()
        session.dialogue_health = health
        session.health_alerts.extend(alerts)

        # 6. 提取洞察
        insights = self._extract_insights(user_input, ai_response)
        session.insights.extend(insights)

        # 7. 记录对话轮次
        turn = DialogueTurn(
            turn_id=turn_id,
            user_input=user_input,
            ai_response=ai_response,
            intent_detected=intent,
            layer=session.current_layer,
            layer_name=session.layer_names[session.current_layer - 1],
            key_insights=insights,
            health_alerts=alerts
        )
        session.turns.append(turn)
        session.last_updated = datetime.now().isoformat()

        # 8. 如果是第5轮，检查是否需要升级层
        if session.dialogue_turn_count % 5 == 0:
            self._check_layer_transition()

        # 9. 保存会话
        self._save_session()

        # 10. 生成 Obsidian 笔记
        self._save_to_obsidian()

        return {
            "turn_id": turn_id,
            "ai_response": ai_response,
            "current_layer": session.current_layer,
            "layer_name": session.layer_names[session.current_layer - 1],
            "intent": intent,
            "dialogue_health": health,
            "health_alerts": alerts,
            "commitment_gate_passed": commitment_passed,
            "new_insights": insights,
            "total_turns": session.dialogue_turn_count
        }

    def _generate_response(self, user_input: str, turn_id: int, intent: str) -> str:
        """生成 AI 响应"""
        if self.client:
            try:
                # 构建 prompt
                layer_prompt = self._get_layer_prompt(session.current_layer)
                prompt = f"""你是一个苏格拉底式导师，正在帮助用户进行学术研究思考。

当前对话信息：
- 轮次：{turn_id}
- 当前层：L{session.current_layer} - {session.layer_names[session.current_layer - 1]}
- 用户意图：{intent}
- 主题：{session.topic}

{layer_prompt}

用户输入：「{user_input}」

请以苏格拉底式对话风格回应：
1. 不要直接给出答案，而是通过提问引导
2. 如果检测到用户表达高置信度观点，引入反面观点
3. 鼓励用户深入思考
4. 每次回应控制在100字以内

苏格拉底式回应："""

                messages = [{"role": "user", "content": prompt}]
                response = self.client.chat(messages, temperature=0.7)
                return response[:500] if response else self._fallback_response(user_input, turn_id)
            except Exception as e:
                print(f"⚠️  LLM 调用失败: {e}")
                return self._fallback_response(user_input, turn_id)
        else:
            return self._fallback_response(user_input, turn_id)

    def _get_layer_prompt(self, layer: int) -> str:
        """获取各层的导师提示"""
        prompts = {
            1: "【问题定义层】你的目标是帮助用户明确真正想研究的问题。使用探询性问题澄清模糊之处。",
            2: "【方法反思层】你的目标是帮助用户反思研究方法。讨论方法的可行性和局限性。",
            3: "【证据视角层】你的目标是帮助用户评估证据。引出对证据来源和质量的思考。",
            4: "【启示探索层】你的目标是帮助用户探索研究发现的意义和局限。引入反驳观点。",
            5: "【综合层】你的目标是帮助用户整合所学，形成清晰的研究计划。"
        }
        return prompts.get(layer, "")

    def _fallback_response(self, user_input: str, turn_id: int) -> str:
        """备用响应 (当 LLM 不可用时)"""
        layer = self.session.current_layer
        responses = {
            1: "你提到这一点很有意思。能否更详细地说明你对这个问题的理解？具体来说，你期望找到什么答案？",
            2: "这是一个很好的研究方法思路。你认为这种方法的最大优势是什么？有没有考虑过其他替代方案？",
            3: "你引用的这个证据很有价值。你如何评估这个证据的可信度？是否有其他相反的证据？",
            4: "这个发现有重要意义。你认为审稿人会如何评估这个结论？有什么潜在的局限性吗？",
            5: "经过这番讨论，你对研究问题有什么新的理解？接下来你打算如何推进研究？"
        }
        return responses.get(layer, "请继续分享你的研究思考。")

    def _extract_insights(self, user_input: str, ai_response: str) -> List[str]:
        """从对话中提取洞察"""
        insights = []

        # 检测 [INSIGHT] 标签
        if "[INSIGHT]" in user_input.upper() or "[INSIGHT]" in ai_response.upper():
            import re
            matches = re.findall(r'\[INSIGHT\]\s*(.+?)(?:\n|$)', user_input + " " + ai_response, re.IGNORECASE)
            insights.extend(matches)

        return insights[:3]  # 最多3个洞察

    def _check_layer_transition(self):
        """检查是否需要切换到下一层"""
        session = self.session

        # 检查当前层承诺门是否通过
        current_layer_gates = [g for g in session.commitment_gates if g.layer == session.current_layer]
        all_passed = all(g.passed for g in current_layer_gates) if current_layer_gates else True

        # 如果当前层有足够的对话轮次且承诺门通过，可以考虑升级
        layer_turn_counts = [len([t for t in session.turns if t.layer == l]) for l in range(1, 6)]
        current_layer_turns = layer_turn_counts[session.current_layer - 1] if session.current_layer <= len(layer_turn_counts) else 0

        # 每层至少5轮，且承诺门通过，才允许升级
        if current_layer_turns >= 5 and all_passed and session.current_layer < 5:
            session.current_layer += 1
            print(f"📍 升级到 L{session.current_layer}: {session.layer_names[session.current_layer - 1]}")

    def trigger_commitment_gate(self) -> Dict[str, Any]:
        """触发承诺门"""
        layer = self.session.current_layer
        gate_questions = {
            1: "我对这个问题有三个初步假设：1) ... 2) ... 3) ...",
            2: "我计划用 [方法] 来验证 [假设]，因为 [理由]",
            3: "我预期会发现 [预期结果]，因为 [证据/理由]",
            4: "审稿人可能会挑战 [弱点]，我会用 [方法] 回应",
            5: "最终研究发现将是 [总结]"
        }

        gate = CommitmentGate(
            layer=layer,
            question=gate_questions.get(layer, "请分享你的研究承诺"),
            user_commitment="",
            passed=False,
            timestamp=datetime.now().isoformat()
        )
        self.session.commitment_gates.append(gate)
        self._save_session()

        return asdict(gate)

    def pass_commitment_gate(self, gate_id: int, commitment: str):
        """通过承诺门"""
        if 0 <= gate_id < len(self.session.commitment_gates):
            gate = self.session.commitment_gates[gate_id]
            gate.user_commitment = commitment
            gate.passed = True
            gate.timestamp = datetime.now().isoformat()
            self.session.commitment_gate_passed = True
            self._save_session()

    def _save_to_obsidian(self):
        """保存到 Obsidian"""
        content = self._generate_note_content()
        note_file = DIALOGUE_DIR / f"{self.session_id}.md"
        note_file.write_text(content, encoding="utf-8")

    def get_status(self) -> Dict[str, Any]:
        """获取会话状态"""
        return {
            "session_id": self.session.session_id,
            "project": self.session.project,
            "topic": self.session.topic,
            "current_layer": self.session.current_layer,
            "layer_name": self.session.layer_names[self.session.current_layer - 1],
            "intent": self.session.intent,
            "dialogue_turn_count": self.session.dialogue_turn_count,
            "dialogue_health": self.session.dialogue_health,
            "status": self.session.status,
            "commitment_gates_passed": sum(1 for g in self.session.commitment_gates if g.passed),
            "commitment_gates_total": len(self.session.commitment_gates),
            "insights_count": len(self.session.insights)
        }


def main():
    parser = argparse.ArgumentParser(description="苏格拉底对话会话管理器")
    parser.add_argument("--topic", "-t", help="研究主题")
    parser.add_argument("--project", "-p", required=True, help="项目名称")
    parser.add_argument("--session-id", "-s", help="会话ID (继续已有会话)")
    parser.add_argument("--continue-session", "-c", action="store_true", help="继续最近会话")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互模式")

    args = parser.parse_args()

    # 确定会话ID
    session_id = args.session_id
    if args.continue_session:
        # 查找最近的会话
        if DIALOGUE_DIR.exists():
            sessions = list(DIALOGUE_DIR.glob("socratic_*.json"))
            if sessions:
                session_id = sessions[-1].stem

    # 创建管理器
    manager = SocraticSessionManager(
        project=args.project,
        topic=args.topic or "",
        session_id=session_id
    )

    if args.interactive:
        print(f"\n🗣️  苏格拉底对话会话")
        print(f"   项目: {manager.project}")
        print(f"   主题: {manager.topic}")
        print(f"   会话ID: {manager.session_id}")
        print(f"   当前层: L{manager.session.current_layer} - {manager.session.layer_names[manager.session.current_layer - 1]}")
        print("\n输入 'quit' 退出，输入 'status' 查看状态，输入 'gate' 触发承诺门\n")

        while True:
            user_input = input("\n你: ").strip()
            if user_input.lower() in ["quit", "exit", "退出"]:
                print("👋 再见!")
                break
            elif user_input.lower() == "status":
                status = manager.get_status()
                print(f"\n📊 状态: {json.dumps(status, ensure_ascii=False, indent=2)}")
            elif user_input.lower() == "gate":
                gate = manager.trigger_commitment_gate()
                print(f"\n⚠️  承诺门已触发: {gate['question']}")
                commitment = input("你的承诺: ").strip()
                manager.pass_commitment_gate(len(manager.session.commitment_gates) - 1, commitment)
            else:
                result = manager.process_user_input(user_input)
                print(f"\n🤖 AI: {result['ai_response']}")
                print(f"\n📍 L{result['current_layer']} - {result['layer_name']} | 轮次: {result['total_turns']} | 健康: {result['dialogue_health']}")
                if result['new_insights']:
                    print(f"💡 新洞察: {', '.join(result['new_insights'])}")
                if result['health_alerts']:
                    print(f"⚠️  健康警报: {', '.join(result['health_alerts'])}")
    else:
        # 打印状态
        status = manager.get_status()
        print(f"\n📊 会话状态:")
        print(json.dumps(status, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()