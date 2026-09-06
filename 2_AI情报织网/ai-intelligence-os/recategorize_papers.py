# -*- coding: utf-8 -*-
"""
recategorize_papers.py
- 重新分类 943 篇未分类论文
- 策略：基于 title + abstract 关键词匹配到 42格
"""
import os
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

META_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\papers_meta.json'
OUTPUT_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文洞察\papers_meta_v2.json'

GRID_KEYWORDS = {
    'W×Q': {
        'weight_quant': ['quantization', 'quantize', 'quant', 'int4', 'int8', 'fp8', 'fp4', 'gptq', 'awq', 'smoothquant', 'bitsandbytes', 'bnb'],
        'weight_related': ['weight', 'linear', 'matmul', 'gemm'],
    },
    'W×P': {
        'keywords': ['pruning', 'prune', 'sparse', 'magnitude', 'movement', 'rigl', 'lottery', 'structured pruning'],
    },
    'W×D': {
        'keywords': ['distillation', 'distill', 'knowledge transfer', 'teacher-student', 'kd'],
    },
    'W×L': {
        'keywords': ['low-rank', 'low rank', 'lora', 'qlora', 'svd', 'tensor decomposition', 'cp decomposition', 'tucker'],
    },
    'W×S': {
        'keywords': ['2:4 sparsity', 'n:m sparsity', 'structured sparsity', 'semi-structured', 'ampere sparsity'],
    },
    'W×G': {
        'keywords': ['model compression', 'weight compression', 'parameter compression'],
    },
    'A×Q': {
        'keywords': ['activation quantization', 'activation quant', 'post-training quantization', 'ptq', 'qat'],
    },
    'A×G': {
        'keywords': ['flash attention', 'flashattention', 'kernel fusion', 'operator fusion', 'tensorrt', 'triton', 'cutlass', 'flashinfer', 'paged attention'],
    },
    'K×Q': {
        'keywords': ['kv cache quantization', 'kv quant', 'kv-cache compress', 'kvcache quant', 'kv low-bit', 'kivi', 'zipcache', 'kvquant'],
    },
    'K×P': {
        'keywords': ['kv cache pruning', 'kv pruning', 'kv sparsif', 'attention pruning', 'head pruning'],
    },
    'K×D': {
        'keywords': ['kv cache distillation', 'kv distill', 'cross-layer kv'],
    },
    'K×S': {
        'keywords': ['sliding window', 'streaming attention', 'sparse attention', 'longformer', 'bigbird', 'linear attention', 'linearattention', 'linformer', 'performer', 'reformer'],
    },
    'K×G': {
        'keywords': ['kv cache', 'key-value cache', 'pagedattention', 'vllm', 'sglang', 'mqa', 'gqa', 'multi-query', 'grouped-query', 'prefix cache', 'prefix-cache', 'prefix caching'],
    },
    'C×Q': {
        'keywords': ['allreduce quantiz', 'gradient quantiz', 'communication quant', 'terngrad', 'signsgd', '1-bit adam'],
    },
    'C×G': {
        'keywords': ['nccl', 'communication', 'collective', 'allreduce', 'all-gather', 'tensor parallel', 'pipeline parallel', 'expert parallel', 'topology', 'ring allreduce', 'tree allreduce', 'zero', 'zero-offload', 'fwdcomm', 'overlap'],
    },
    'C×S': {
        'keywords': ['gradient sparsif', 'communication sparse', 'powerSGD', 'deepspeed'],
    },
    'C×P': {
        'keywords': ['communication pruning', 'gradient pruning'],
    },
    'C×D': {
        'keywords': ['communication distillation'],
    },
    'C×L': {
        'keywords': ['low-rank gradient', 'gradient low-rank', 'atomo'],
    },
    'M×Q': {
        'keywords': ['vit quantiz', 'visual quantiz', 'image encoder quant', 'audio quantiz', 'speech quantiz', 'whisper quant'],
    },
    'M×L': {
        'keywords': ['vit low-rank', 'visual low-rank', 'image encoder low-rank'],
    },
    'M×S': {
        'keywords': ['vit sparse', 'token pruning', 'token merge', 'tome', 'tofu', 'visual sparse'],
    },
    'M×P': {
        'keywords': ['vit pruning', 'visual pruning', 'image encoder pruning', 'token pruning'],
    },
    'M×D': {
        'keywords': ['visual distill', 'multimodal distill', 'image encoder distill'],
    },
    'M×G': {
        'keywords': ['vit compression', 'visual encoder compression', 'multimodal compression', 'image encoder', 'audio encoder', 'speech encoder', 'modality encoder'],
    },
    'V×Q': {
        'keywords': ['vocoder quantiz', 'audio decoder quantiz', 'hifigan quant', 'tts quant'],
    },
    'V×L': {
        'keywords': ['vocoder low-rank', 'tts low-rank'],
    },
    'V×S': {
        'keywords': ['vocoder sparse', 'tts sparse'],
    },
    'V×P': {
        'keywords': ['vocoder pruning', 'tts pruning'],
    },
    'V×D': {
        'keywords': ['vocoder distill', 'tts distill'],
    },
    'V×G': {
        'keywords': ['vocoder', 'hifigan', 'tts decoder', 'tts compression', 'speech synthesis compression'],
    },
    'S×Q': {
        'keywords': ['beam search quant', 'state quantiz'],
    },
    'S×G': {
        'keywords': ['speculative decoding', 'speculative decoding', 'medusa', 'eagle', 'draft model', 'lookahead decoding', 'inference acceleration', 'decoding acceleration', 'agent memory', 'agent state', 'agent scheduling', 'mcp', 'a2a protocol', 'multi-agent'],
    },
    'S×L': {
        'keywords': ['state low-rank'],
    },
    'S×S': {
        'keywords': ['state sparse', 'beam sparse'],
    },
    'S×P': {
        'keywords': ['state pruning', 'beam pruning'],
    },
    'S×D': {
        'keywords': ['state distill'],
    },
}

SCENARIO_KEYWORDS = {
    'LLM': ['llm', 'large language model', 'language model', 'gpt', 'transformer', 'decoder', 'autoregressive', 'causal lm', 'bert', 'llama', 'mistral', 'qwen', 'deepseek', 'kimi'],
    'Agent': ['agent', 'multi-agent', 'tool use', 'function call', 'planning', 'react', 'autogpt', 'mcp', 'a2a'],
    '多模态': ['multimodal', 'multi-modal', 'vision-language', 'image-text', 'video-text', 'visual question', 'vqa', 'clip', 'llava', 'vision encoder'],
    'ASR': ['asr', 'speech recognition', 'whisper', 'audio recognition', 'automatic speech', 'transcription'],
    'TTS': ['tts', 'text-to-speech', 'speech synthesis', 'vocoder', 'hifigan', 'fastspeech'],
}

def classify_grid(title, abstract, existing_grid):
    """分类到 42格"""
    if existing_grid and existing_grid != 'Unclassified':
        return existing_grid

    text = (title + ' ' + abstract).lower()

    scores = defaultdict(int)
    for grid, config in GRID_KEYWORDS.items():
        if 'keywords' in config:
            for kw in config['keywords']:
                if kw in text:
                    scores[grid] += 2
        else:
            for cat, kws in config.items():
                for kw in kws:
                    if kw in text:
                        scores[grid] += 1

    if not scores:
        return None

    return max(scores, key=scores.get)

def classify_scenario(title, abstract, existing_scenario):
    """分类到场景"""
    if existing_scenario and existing_scenario != 'Unclassified':
        return existing_scenario

    text = (title + ' ' + abstract).lower()

    scores = defaultdict(int)
    for scenario, kws in SCENARIO_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                scores[scenario] += 1

    if not scores:
        return None

    return max(scores, key=scores.get)

def main():
    print(f"读取: {META_PATH}")
    with open(META_PATH, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    print(f"已加载: {len(papers)} 篇")

    grid_before = defaultdict(int)
    scenario_before = defaultdict(int)
    for p in papers:
        grid_before[p.get('grid') or 'None'] += 1
        scenario_before[p.get('scenario') or 'None'] += 1

    print("\n=== 重新分类前 ===")
    print(f"未分类 (grid): {grid_before.get('Unclassified', 0) + grid_before.get('None', 0)}")
    print(f"未分类 (scenario): {scenario_before.get('Unclassified', 0) + scenario_before.get('None', 0)}")

    recategorized_grid = 0
    recategorized_scenario = 0

    for p in papers:
        old_grid = p.get('grid')
        old_scenario = p.get('scenario')

        new_grid = classify_grid(p.get('title', ''), p.get('abstract', ''), old_grid)
        new_scenario = classify_scenario(p.get('title', ''), p.get('abstract', ''), old_scenario)

        if (not old_grid or old_grid == 'Unclassified') and new_grid:
            p['grid'] = new_grid
            recategorized_grid += 1
        elif old_grid:
            p['grid'] = old_grid

        if (not old_scenario or old_scenario == 'Unclassified') and new_scenario:
            p['scenario'] = new_scenario
            recategorized_scenario += 1
        elif old_scenario:
            p['scenario'] = old_scenario

    print(f"\n=== 重新分类后 ===")
    print(f"Grid 重新分类: {recategorized_grid} 篇")
    print(f"Scenario 重新分类: {recategorized_scenario} 篇")

    grid_after = defaultdict(int)
    scenario_after = defaultdict(int)
    for p in papers:
        g = p.get('grid') or 'Unclassified'
        grid_after[g] += 1
        s = p.get('scenario') or 'Unclassified'
        scenario_after[s] += 1

    print(f"\n未分类 (grid): {grid_after.get('Unclassified', 0)}")
    print(f"未分类 (scenario): {scenario_after.get('Unclassified', 0)}")

    print("\n=== 42格分布 (新) ===")
    for g, count in sorted(grid_after.items(), key=lambda x: -x[1])[:15]:
        print(f"  {g}: {count}")

    print("\n=== 场景分布 (新) ===")
    for s, count in sorted(scenario_after.items(), key=lambda x: -x[1]):
        print(f"  {s}: {count}")

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"\n输出: {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
