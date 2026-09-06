import sys, os
sys.stdout.reconfigure(encoding='utf-8')
BASE = r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os'
main = open(os.path.join(BASE, 'main.py'), encoding='utf-8').read()
# Find all function definitions
for i, line in enumerate(main.split('\n')):
    if line.startswith('def ') and 'main' in line:
        print(f'Line {i+1}: {line}')

# Also show the argparse block
for i, line in enumerate(main.split('\n')):
    if 'argparse' in line or 'add_argument' in line or '--mode' in line or '--api-key' in line:
        print(f'Line {i+1}: {line}')