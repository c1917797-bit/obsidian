# -*- coding: utf-8 -*-
"""直接插入剪枝课题到课题9之前"""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

fpath = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\技术洞察\推理压缩\06_综合报告\推理压缩技术规划报告_10课题_对标豆包小艺.md'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

new_topic = """## 课题 9：面向 LLM 部署的注意力头差异化剪枝根技术

**课题名称**：面向 LLM 部署的注意力头差异化剪枝根技术

**关键挑战**：LLM-72B 有 64 个注意力头，但 30-50% 高度相似（冗余），浪费 20-30% FLOPS。GQA/MQA 减了 KV 头但 Query 头未减。豆包有千卡不在乎 20% FLOPS 浪费，但 NPU 资源受限场景**必须头级剪枝**。DoRA/LoRA 证明了低秩补偿的可行性。

**技术目标**：对 Qwen3/Llama 72B 模型，部署场景：头数减少 30-50%，精度≤1%，TPOT-20%。

**关键技术**：
①**注意力头冗余度画像**：头间余弦相似度聚类，>0.9 为冗余组。30-50% 头属于冗余组。
创新点：构建注意力头冗余度分析画像，量化每头贡献度。

②**组内代表头+LoRA 微调补偿**：冗余组保留 1 个代表头，LoRA 微调补偿精度损失。
创新点：组内代表头+LoRA 补偿联合，实现"剪枝但不损精度"。

③**部署后动态激活**：推理时按 query 复杂度激活不同头数——简单 query 激活 30% 头，复杂 query 激活 70%。
创新点：推理时动态头激活（训练时静态剪枝+推理时动态选择）。

**技术逻辑图**：
```
[64头Qwen-72B] → 头间余弦相似度聚类
                ↓
        冗余组(>0.9相似度)：保留1个代表头
        非冗余组：全部保留
                ↓
        LoRA微调补偿精度
                ↓
        推理时按query复杂度动态激活（30%-70%）
                ↓
        [头数↓30-50%，精度≤1%，TPOT-20%]
```

**课题规划**：注意力头剪枝课题（冗余画像+代表头+动态激活）：实现头数减少 30-50%，NPU 推理时按 query 复杂度动态选择头数。

**参考论文**：
- Wanda, NeurIPS 2024 — Weight×Activation magnitude 评估，本课题①冗余画像参考
- CompressKV, 2026 — Semantic Retrieval Heads 头级压缩，本课题③头级粒度参考
- BESA, NeurIPS 2024 — 结构化稀疏头级，本课题②剪枝参考
- DoRA, 2024 — LoRA 分解，本课题②LoRA 补偿参考
- GQA, 2023 — Grouped Query Attention 头级共享，本课题头级粒度基础

---

## 课题 10：面向 NPU 原生压缩的 CANN 算子库根技术"""

# 找到 "## 课题 9：面向 NPU 原生" 这个文本（投机解码移除后 CANN 现在是 9）
# 应该改成在它之前插入剪枝，然后 CANN 变 10
# 实际：现在 课题 9 = CANN 算子库，课题 10 = 之前的 10（已重编号）
# 需要：在 CANN 前面插入新的 课题 9（剪枝），然后 CANN 变 10

# 找 "## 课题 9：面向 NPU 原生压缩的 CANN 算子库根技术"
old_cann = "## 课题 9：面向 NPU 原生压缩的 CANN 算子库根技术"
if old_cann in content:
    content = content.replace(old_cann, new_topic, 1)
    print("插入成功")
else:
    print("未找到 CANN 文本")

# 更新分数表
old_score = """| 8 | KV 稀疏+蒸馏联合 | 豆包不需要 | 5.0 | 第 2 年 |"""
new_score = """| 8 | KV 稀疏+蒸馏联合 | 豆包不需要 | 5.0 | 第 2 年 |
| 9 | 注意力头差异化剪枝 | NPU 资源受限刚需 | 5.5 | 第 1 年 |"""
content = content.replace(old_score, new_score)

# 更新启动顺序
content = content.replace("""W5:  课题4(5.8)+课题5(5.5)+课题6(5.5)""", """W5:  课题4(5.8)+课题5(5.5)+课题6(5.5)+课题9(5.5)""")

# 更新一句话总结
content = content.replace('9 课题（不含投机解码）的核心竞争力', '10 课题（不含投机解码，专注压缩）的核心竞争力')

# 更新版本历史
content = content.replace(
    "| **v8.1** | **2026-06-29** | **移除投机解码（用户只做压缩）→ 9 课题** |",
    "| v8.1 | 2026-06-29 | 移除投机解码（用户只做压缩） |\n| **v8.2** | **2026-06-29** | **+注意力头剪枝（补全剪枝根技术）→ 10 课题压缩全覆盖** |"
)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("完成")
