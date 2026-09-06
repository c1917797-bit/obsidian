import sys
sys.stdout.reconfigure(encoding='utf-8')
from layers.paper_analysis.paper_index import PaperIndex
from collections import Counter

print('='*70)
print('战略分析: Agent时代下AI推理的重点投入方向')
print('='*70)

index = PaperIndex()
index.load()
stats = index.get_stats()

print('\n【一、论文库规模】')
print(f'  总论文数: {stats["total_papers"]:,} 篇')

print('\n【二、Agent时代AI推理论文分布】')
agent_papers = index.search_by_problems(['Agent-Capability'], limit=200)
print(f'  Agent相关论文: {len(agent_papers)} 篇')

latency_papers = index.search_by_problems(['Latency'], limit=100)
print(f'  延迟优化论文: {len(latency_papers)} 篇')

memory_papers = index.search_by_problems(['Memory'], limit=100)
print(f'  内存优化论文: {len(memory_papers)} 篇')

scalability_papers = index.search_by_problems(['Scalability'], limit=100)
print(f'  扩展性论文: {len(scalability_papers)} 篇')

print('\n【三、核心技术分布】')
tech_dist = stats['tech_distribution']
for tech, count in sorted(tech_dist.items(), key=lambda x: -x[1])[:15]:
    print(f'  {tech}: {count} 篇')

print('\n【四、Agent推理交叉领域论文】')
agent_latency = index.search_by_problems(['Agent-Capability', 'Latency'], limit=50)
agent_memory = index.search_by_problems(['Agent-Capability', 'Memory'], limit=50)
agent_scalability = index.search_by_problems(['Agent-Capability', 'Scalability'], limit=50)

print(f'  Agent + 延迟优化: {len(agent_latency)} 篇')
print(f'  Agent + 内存优化: {len(agent_memory)} 篇')
print(f'  Agent + 扩展性: {len(agent_scalability)} 篇')

print('\n【五、高优先级论文（代表重点投入方向）】')
all_agent_papers = index.search_by_problems(['Agent-Capability', 'Latency', 'Memory', 'Scalability'], limit=30)
print('  Top Agent推理论文:')
for i, p in enumerate(all_agent_papers[:10], 1):
    techs = list(p.techs) if p.techs else []
    print(f'  {i}. {p.title[:60]}...')
    if techs:
        print(f'     技术栈: {techs}')

print('\n【六、问题标签分布（反映核心挑战）】')
problem_dist = stats['problem_distribution']
for prob, count in sorted(problem_dist.items(), key=lambda x: -x[1]):
    print(f'  {prob}: {count} 篇')
