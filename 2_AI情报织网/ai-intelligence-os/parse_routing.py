import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

# Read BOTH template files
tpls_dir = r'C:\Users\Huawei\Documents\code\Obsidian\3_AI情报日历\templates'
routing_path = os.path.join(tpls_dir, '信源路由配置.md')
routing = open(routing_path, encoding='utf-8').read()

print('=== 全部内容长度 ===', len(routing))
print()

# Print all non-empty, non-header lines that contain keywords
keywords = ['机器之心', '量子位', 'a16z', 'Twitter', 'langchain', 'vllm', 'sglang',
           'arxiv', 'openai', 'anthropic', 'huggingface', 'nvidia', 'google',
           'deepseek', 'mooncake', 'flash', 'tensorrt', 'llama.cpp', 'llamaindex',
           'autogen', 'mcp', 'openai', 'batch', 'andrewn', 'IEEE', 'USENIX',
           'lesswrong', 'arxiv.org', 'github.com', 'blog.', 'docs.', 'release']

lines = routing.split('\n')
print('=== 含关键词的行 ===')
for i, line in enumerate(lines):
    lower = line.lower()
    for kw in keywords:
        if kw.lower() in lower:
            print(f'  [{i+1}] {line[:120]}')
            break

print()
print('=== 全部行（前80行）===')
for i, line in enumerate(lines[:80]):
    if line.strip():
        print(f'  [{i+1:3d}] {line[:120]}')