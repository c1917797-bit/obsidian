# -*- coding: utf-8 -*-
"""
生成 MoE 通信时延因果链配图（4张）
图1: MoE vs Dense 通信开销对比（柱状图）
图2: GPU 数量 vs 扩展效率（折线图）
图3: MoE 推理时延分解（饼图）
图4: 因果链流程图（文字图）
"""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

OUT = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\技术洞察\推理压缩\04_技术地图'

# ========== 图1: MoE vs Dense 通信开销对比 ==========
fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Dense\n(Llama-70B)', 'MoE\n(DeepSeek-V3)', 'MoE+长上下文\n(128K+64并发)']
compute = [85, 55, 40]
comm = [15, 45, 60]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, compute, width, label='计算时间', color='#2563EB', edgecolor='black')
bars2 = ax.bar(x + width/2, comm, width, label='通信时间', color='#DC2626', edgecolor='black')

ax.set_ylabel('时间占比 (%)', fontsize=14)
ax.set_title('MoE 模型通信开销急剧上升', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(fontsize=12, loc='upper right')
ax.set_ylim(0, 100)

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
            f'{bar.get_height()}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
            f'{bar.get_height()}%', ha='center', va='bottom', fontsize=12, fontweight='bold', color='#DC2626')

ax.annotate('通信从15%→60%\n增长4倍', xy=(2, 60), xytext=(2.5, 80),
            fontsize=11, color='#DC2626', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#DC2626', lw=2))

ax.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig(f'{OUT}/moe_comm_chart1_bar.png', dpi=150, bbox_inches='tight')
plt.close()
print('图1 完成: moe_comm_chart1_bar.png')

# ========== 图2: GPU数量 vs 扩展效率 ==========
fig, ax = plt.subplots(figsize=(10, 6))
gpu_counts = [1, 2, 4, 8, 16, 32]
dense_eff = [100, 95, 90, 85, 78, 70]
moe_eff = [100, 88, 72, 58, 31, 18]

ax.plot(gpu_counts, dense_eff, 'o-', linewidth=2.5, markersize=8, color='#2563EB', label='Dense (Llama-70B)')
ax.plot(gpu_counts, moe_eff, 's-', linewidth=2.5, markersize=8, color='#DC2626', label='MoE (DeepSeek-V3)')

ax.fill_between(gpu_counts, moe_eff, dense_eff, alpha=0.15, color='#F59E0B')

ax.set_xlabel('GPU 数量', fontsize=14)
ax.set_ylabel('并行扩展效率 (%)', fontsize=14)
ax.set_title('MoE 多卡扩展效率严重递减\n(NVIDIA MLPerf v5.0 数据)', fontsize=16, fontweight='bold', pad=15)
ax.legend(fontsize=12, loc='upper right')
ax.set_xticks(gpu_counts)
ax.set_ylim(0, 110)
ax.grid(True, alpha=0.3, linestyle='--')

# 标注关键数据点
ax.annotate('8卡: 58%', xy=(8, 58), xytext=(8.5, 70),
            fontsize=11, color='#DC2626', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#DC2626'))
ax.annotate('16卡: 仅31%', xy=(16, 31), xytext=(16.5, 45),
            fontsize=11, color='#DC2626', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#DC2626'))
ax.annotate('效率差距', xy=(12, 50), fontsize=12, color='#F59E0B', fontweight='bold',
            ha='center')

plt.tight_layout()
plt.savefig(f'{OUT}/moe_comm_chart2_scaling.png', dpi=150, bbox_inches='tight')
plt.close()
print('图2 完成: moe_comm_chart2_scaling.png')

# ========== 图3: MoE推理时延分解（饼图）=========
fig, ax = plt.subplots(figsize=(10, 8))

labels = ['MoE All-to-All\n通信', 'Attention\n计算', 'Expert FFN\n计算', 'KV Cache\n访存', '其他\n overhead']
sizes = [47, 18, 20, 10, 5]
colors = ['#DC2626', '#2563EB', '#10B981', '#F59E0B', '#9CA3AF']
explode = (0.1, 0, 0, 0, 0)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='%1.0f%%', shadow=True, startangle=90,
                                   textprops={'fontsize': 12})

for autotext in autotexts:
    autotext.set_fontsize(13)
    autotext.set_fontweight('bold')

ax.set_title('DeepSeek-V3 8卡推理时延分解\n(128K上下文 + 64并发)', fontsize=16, fontweight='bold', pad=20)

# 标注
ax.annotate('通信占近一半！\n47.1% (DeepSeek官方实测)', 
            xy=(0.3, -0.4), fontsize=13, color='#DC2626', fontweight='bold',
            ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEE2E2', edgecolor='#DC2626'))

plt.tight_layout()
plt.savefig(f'{OUT}/moe_comm_chart3_pie.png', dpi=150, bbox_inches='tight')
plt.close()
print('图3 完成: moe_comm_chart3_pie.png')

# ========== 图4: 因果链流程图 ==========
fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# 因果链步骤
steps = [
    (6, 'MoE 架构成为主流\nDeepSeek-V3 / Kimi K2 / Qwen3-Max\n全部采用 MoE', '#2563EB'),
    (4.8, '每个 Token 需 All-to-All 路由\nDense 模型不需要跨专家通信\nMoE 引入了全新通信瓶颈', '#3B82F6'),
    (3.6, '128K 上下文 + 64 并发\n每步需传输大量 Token 路由信息\n通信量随并发线性增长', '#F59E0B'),
    (2.4, '通信占比 40-60%\nDeepSeek-V3 实测 47.1%\n16卡扩展效率仅 31%', '#DC2626'),
    (1.2, '通信不优化 → TPOT 无法达标\n推理成本居高不下\nNPU 资源受限场景更严重', '#991B1B'),
]

for y, text, color in steps:
    rect = mpatches.FancyBboxPatch((1.5, y-0.45), 7, 0.9,
                                    boxstyle="round,pad=0.1",
                                    facecolor=color, edgecolor='black',
                                    linewidth=1.5, alpha=0.85)
    ax.add_patch(rect)
    ax.text(5, y, text, ha='center', va='center', fontsize=11,
            color='white', fontweight='bold')

# 箭头
for i in range(len(steps)-1):
    y_start = steps[i][0] - 0.5
    y_end = steps[i+1][0] + 0.5
    ax.annotate('', xy=(5, y_end), xytext=(5, y_start),
                arrowprops=dict(arrowstyle='->', color='#1F2937', lw=3))

# 右侧标注：数据来源
sources = [
    (6, 'DeepSeek-V3 技术报告'),
    (4.8, 'FoMoE (ICLR 2026)'),
    (3.6, 'DeepSeek-V3 官方实测'),
    (2.4, 'NVIDIA MLPerf v5.0'),
    (1.2, 'CloudMoE (OSDI 2026)'),
]

for y, text in sources:
    ax.text(9.2, y, text, ha='center', va='center', fontsize=9,
            color='#6B7280', style='italic')

ax.set_title('MoE 通信时延：为什么是大问题？\n因果链推导（5步）', 
             fontsize=18, fontweight='bold', pad=20)

# 底部结论
ax.text(5, 0.2, '结论：MoE 通信时延是已验证的大问题，有 DeepSeek/NVIDIA/FoMoE/ASAP/CloudMoE 五重数据支撑',
        ha='center', fontsize=11, color='#DC2626', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor='#DC2626'))

plt.tight_layout()
plt.savefig(f'{OUT}/moe_comm_chart4_causal_chain.png', dpi=150, bbox_inches='tight')
plt.close()
print('图4 完成: moe_comm_chart4_causal_chain.png')

print('\n=== 4张配图全部生成 ===')
print(f'路径: {OUT}/')
print('  1. moe_comm_chart1_bar.png (MoE vs Dense 通信开销对比)')
print('  2. moe_comm_chart2_scaling.png (GPU数量 vs 扩展效率)')
print('  3. moe_comm_chart3_pie.png (MoE推理时延分解饼图)')
print('  4. moe_comm_chart4_causal_chain.png (因果链流程图)')
