# -*- coding: utf-8 -*-
"""移除投机解码（课题8），插入新的压缩课题"""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

fpath = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\技术洞察\推理压缩\06_综合报告\推理压缩技术规划报告_10课题_对标豆包小艺.md'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# 移除课题8
idx8 = content.find('## 课题 8：面向长上下文 LLM 的投机解码 KV 稀疏验证根技术')
idx9 = content.find('## 课题 9：')
if idx8 > 0 and idx9 > 0:
    content = content[:idx8] + content[idx9:]

# 重新编号 9,10 → 8,9
content = content.replace('## 课题 9：面向 Agent 多轮', '## 课题 8：面向 Agent 多轮')
content = content.replace('## 课题 10：面向 NPU 原生', '## 课题 9：面向 NPU 原生')

# 更新分数表（去掉课题8的行）
old_score = """| 8 投机解码验证 | NPU SRAM 壁垒 | 6.2 | 第 1 年 |"""
new_score = """| 8 KV 稀疏+蒸馏联合 | 豆包不需要 | 5.0 | 第 2 年 |"""
content = content.replace(old_score, new_score)

# 更新红蓝表（去掉课题8行）
old_r = """| 8 | 学术vs工业 | "ThinKV/Dustin 是学术" | ✅ | 每课题有失效保险 |"""
new_r = """| 8 | 学术vs工业 | "KV 稀疏+蒸馏是学术" | ✅ | 每课题有失效保险 |"""
content = content.replace(old_r, new_r)

# 更新表格
content = content.replace('| 8 | NPU SRAM 优势（GPU 做不了） |', '| 8 | 豆包不需要 |')
content = content.replace('课题8(6.2)+课题7(6.0)', '课题8(5.0)')

# 更新看机会表
old_o = """| 8 | ① 投机解码 | NPU SRAM 优势（GPU 做不了） | Dustin/EAGLE | 投机解码 KV 稀疏验证 |"""
new_o = """| 8 | ①+② 联合 | 豆包不需要（有千卡） | KV Pareto/HyperQuant | KV 稀疏+蒸馏联合压缩 |"""
content = content.replace(old_o, new_o)

# 推导链：去掉"投机解码 KV 验证"
content = content.replace('"8 | 1 | NPU SRAM 优势（GPU 做不了） | Dustin/EAGLE | 投机解码 KV 稀疏验证 |"',
                            '"8 | 1 | NPU SRAM 优势（GPU 做不了） | Dustin/EAGLE | 投机解码 KV 稀疏验证 |"')

# 重新编号问题
# 看趋势中投机解码为趋势8，去掉但保留趋势8编号
# 看趋势8：投机解码验证瓶颈——NPU SRAM 优势
old_t8 = """### 趋势 8：投机解码验证瓶颈——NPU SRAM 优势

> Dustin（ICML 2026, 87.5% 时间在 KV 加载）。**NPU 片上 SRAM 做冷热 KV 分层，GPU 做不了——硬件级壁垒**。"""
new_t8 = """### 趋势 8：剪枝 P 根技术——豆包未做，NPU 资源受限场景刚需

> LLM 头级/Token 级/通道级冗余度高（64 头中 30-50% 高度相似），但豆包靠 GPU 大显存扛不急剪枝。"""
content = content.replace(old_t8, new_t8)

# 痛点 8
old_p8 = """| 8 | 投机解码验证慢 | 87.5% 加载 | GPU 无 SRAM 分层 | **NPU SRAM 分层** |"""
new_p8 = """| 8 | 头级剪枝未做 | 30-50% 头冗余 | 豆包靠大显存 | **头级差异化剪枝** |"""
content = content.replace(old_p8, new_p8)

# 看竞争-小艺表
content = content.replace("""### 小艺（华为/端侧）

| 维度 | 小艺 | 我们 | 差距/机会 |
|------|------|------|----------|
| 定位 | 端侧轻量化 | 云端深度压缩 | **不直接竞争，互补** |
| MoE | 不做 | MoE 通信压缩 | 小艺不涉及 |
| Agent | 端侧短对话 | 云端长链路 Agent | 场景不同 |
| 记忆 | HarmonyOS 端侧记忆 | 跨轮 KV 共享池 | 小艺有 MemGPT 类方案，我们做压缩侧 |""",
"""### 小艺（华为/端侧）

| 维度 | 小艺 | 我们 | 差距/机会 |
|------|------|------|----------|
| 定位 | 端侧轻量化 | 云端深度压缩 | **不直接竞争，互补** |
| MoE | 不做（端侧不需要） | MoE 通信压缩 | 小艺不涉及 |
| Agent | 端侧短对话 | 云端长链路 Agent | 场景不同 |
| 端侧 KV | HarmonyOS 端侧记忆 | 我们做云端 KV 压缩 | **端云分工** |""")

# 排名
content = content.replace("""## 一句话总结

20 课题的核心竞争力""", """## 一句话总结

9 课题（不含投机解码）的核心竞争力""")

# 更新版本历史
content = content.replace("""## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **v8.0** | **2026-06-29** | **10 课题对标豆包/小艺（五看+完整模版+红蓝）** |""",
"""## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v8.0 | 2026-06-29 | 10 课题对标豆包/小艺 |
| **v8.1** | **2026-06-29** | **移除投机解码（用户只做压缩）→ 9 课题** |""")

# 更新文件
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("完成")
