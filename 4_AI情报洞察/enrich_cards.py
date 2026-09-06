"""
为重要论文批量补全关键创新/性能/代码字段
1. Top 100 核心论文: 用LLM生成key_innovation
2. 全部有arxiv_id的核心论文: regex提取code_url
3. 更新对应markdown文件
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, re, json, time, urllib.request
from collections import Counter
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============ 路径 ============
sys.path.insert(0, r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os')
META_ROOT = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文元数据'
CORE_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\core_papers_list.json'
V8_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_v8.json'
FULL_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_optimization_full_tagged.json'

# 加载Minimax客户端
try:
    from core.minimax_client import get_client
    llm = get_client()
    LLM_AVAILABLE = True
except Exception as e:
    print('LLM not available:', e)
    LLM_AVAILABLE = False

# ============ 加载核心论文清单 ============
with open(CORE_PATH, 'r', encoding='utf-8') as f:
    core_data = json.load(f)
core_papers = core_data['papers']
print('Core papers: {}'.format(len(core_papers)))

# 同时加载v8获取完整信息
with open(V8_PATH, 'r', encoding='utf-8-sig') as f:
    v8 = json.load(f)
with open(FULL_PATH, 'r', encoding='utf-8-sig') as f:
    full = json.load(f)

# 用v8补充abstracts
v8_index = {p.get('arxiv_id'): p for p in v8['papers'] if p.get('arxiv_id')}
for p in core_papers:
    aid = p.get('arxiv_id','')
    if aid and aid in v8_index:
        v8p = v8_index[aid]
        if not p.get('abstract') and v8p.get('abstract'):
            p['abstract'] = v8p['abstract']

# ============ 选Top核心 ============
# 排序: (matched_methods数) + (year)
def core_score(p):
    n_methods = len(p.get('matched_methods', []))
    year = p.get('year', 0)
    if not isinstance(year, int):
        year = 0
    return (n_methods * 100, year)

core_papers_sorted = sorted(core_papers, key=core_score, reverse=True)
TOP_N = 80
top_papers = core_papers_sorted[:TOP_N]
print('Top {} papers selected for LLM enhancement'.format(TOP_N))

# ============ LLM 增强 ============
import re

def llm_extract_keyinfo(title, abstract):
    """让LLM提取关键创新/性能/代码"""
    prompt = """分析以下AI论文，给出结构化信息。要求简洁。

论文标题: {title}

论文摘要: {abstract}

请回答（每行一项，不要前言）:
创新1: [核心创新1，一句话]
创新2: [可选，第二个创新点]
性能: [论文报告的具体数字,如"FPS↑1.5x 精度+0.2%"，无则填"未提具体数字"]
代码: [GitHub链接或项目名，无则填"未开源"]
类别: [参数/激活/KV/通信 之一]
方法: [量化/剪枝/稀疏/蒸馏/低秩/投机解码/注意力优化 之一]
""".format(title=title[:200], abstract=abstract[:1500] if abstract else '无摘要')
    
    try:
        resp = llm.chat([{'role':'user','content':prompt}], max_tokens=400)
        return parse_llm_response(resp)
    except Exception as e:
        return {'error': str(e)[:100]}

def parse_llm_response(resp):
    """解析LLM输出"""
    result = {
        'innovations': [],
        'performance': '',
        'code': '',
        'object': '',
        'method': '',
    }
    for line in resp.split('\n'):
        line = line.strip()
        if line.startswith('创新1'):
            result['innovations'].append(line[3:].lstrip(':：. ').strip())
        elif line.startswith('创新2'):
            result['innovations'].append(line[3:].lstrip(':：. ').strip())
        elif line.startswith('性能'):
            result['performance'] = line[2:].lstrip(':：. ').strip()
        elif line.startswith('代码'):
            result['code'] = line[2:].lstrip(':：. ').strip()
        elif line.startswith('类别'):
            result['object'] = line[2:].lstrip(':：. ').strip()
        elif line.startswith('方法'):
            result['method'] = line[2:].lstrip(':：. ').strip()
    return result

def regex_extract_code_and_performance(text):
    """正则提取GitHub链接和性能数字"""
    result = {'code_url': '', 'perf_hint': ''}
    if not text:
        return result
    
    # GitHub URL
    gh_match = re.search(r'github\.com/[\w\-]+/[\w\-]+', text, re.IGNORECASE)
    if gh_match:
        result['code_url'] = 'https://' + gh_match.group(0)
    
    # Hugging Face
    hf_match = re.search(r'huggingface\.co/[\w\-]+/[\w\-]+', text, re.IGNORECASE)
    if hf_match and not result['code_url']:
        result['code_url'] = 'https://' + hf_match.group(0)
    
    # Performance patterns
    perf_patterns = [
        r'(\d+\.?\d*)[\sx×\*]?\s*(?:speedup|faster|加速)',
        r'([\d\.]+%)\s*(?:accuracy|perplexity|precision)',
        r'(\d+\.?\d*-bit|\d+bit)',
        r'(INT\d|FP\d+)',
    ]
    perf_strings = []
    for pat in perf_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            perf_strings.append(m.group(0))
    if perf_strings:
        result['perf_hint'] = '; '.join(perf_strings[:3])
    
    return result

def find_md_file(aid, title, primary_cell):
    """根据arxiv_id找到对应的md文件"""
    safe_title = re.sub(r'[<>:"/\\|?*\n\r\t]', '', title or '')
    safe_title = re.sub(r'\s+', '_', safe_title.strip())[:50]
    fname = '{}_{}.md'.format(aid, safe_title) if aid else ''
    
    cell_dir = os.path.join(META_ROOT, primary_cell)
    fpath = os.path.join(cell_dir, fname)
    
    if os.path.exists(fpath):
        return fpath
    
    # 如果没找到，尝试hash filename
    if not aid:
        import hashlib
        h = hashlib.md5((title or '').encode('utf-8')).hexdigest()[:8]
        fname = '{}_{}.md'.format(h, safe_title)
        fpath = os.path.join(cell_dir, fname)
        if os.path.exists(fpath):
            return fpath
    
    return None

def update_md_file(fpath, key_innovation, performance, code_url, category=None, method=None):
    """更新md文件的关键字段"""
    if not fpath or not os.path.exists(fpath):
        return False
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 更新 key_innovation
    ki_escaped = key_innovation.replace('"', '\\"')
    content = re.sub(
        r'key_innovation: ".*?"',
        'key_innovation: "{}"'.format(ki_escaped),
        content
    )
    
    # 更新 performance
    perf_escaped = performance.replace('"', '\\"')
    content = re.sub(
        r'performance: ".*?"',
        'performance: "{}"'.format(perf_escaped),
        content
    )
    
    # 更新 code_url
    if code_url:
        content = re.sub(
            r'code_url: ".*?"',
            'code_url: "{}"'.format(code_url),
            content
        )
    
    # 更新 priority (升级为P1因为已被LLM分析)
    content = re.sub(
        r'priority: P\d',
        'priority: P1',
        content,
        count=1
    )
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 主流程
print('\n--- 步骤1: LLM提取Top {}篇关键创新 ---'.format(TOP_N))

enriched = {}
if LLM_AVAILABLE:
    for i, p in enumerate(top_papers):
        aid = p.get('arxiv_id','')
        title = p.get('title','')
        abstract = p.get('abstract','')[:1500]
        
        if not title:
            continue
        
        # 从full拿objects/methods
        f_p = next((fp for fp in full['papers'] if fp.get('arxiv_id')==aid), {})
        objects = f_p.get('objects', [])
        methods = f_p.get('methods', [])
        primary_obj = objects[0] if objects else '参数'
        primary_meth = methods[0] if methods else '量化'
        primary_cell = '{}×{}'.format(primary_obj, primary_meth)
        
        # 调LLM
        info = llm_extract_keyinfo(title, abstract)
        
        if 'error' in info:
            print('  [{}/{}] {} ERROR: {}'.format(i+1, TOP_N, aid, info['error'][:50]))
            time.sleep(2)
            continue
        
        innovations = info['innovations']
        key_innovation = ' | '.join([x for x in innovations if x and x != '未提具体数字' and len(x) > 3]) or '需精读后总结'
        performance = info['performance'] or '未提取到具体数字'
        code_url = info.get('code', '') or ''
        obj = info['object'] or primary_obj
        meth = info['method'] or primary_meth
        
        # 更新md文件
        fpath = find_md_file(aid, title, primary_cell)
        if fpath:
            updated = update_md_file(fpath, key_innovation, performance, code_url, obj, meth)
            if updated:
                enriched[aid] = {
                    'title': title[:80],
                    'primary_cell': primary_cell,
                    'innovations': innovations[:2],
                    'performance': performance[:80],
                    'code_url': code_url[:50],
                }
                print('  [{}/{}] {} {}'.format(i+1, TOP_N, aid, title[:50]))
        
        time.sleep(1.5)  # 避免API过频

print('LLM enriched: {}'.format(len(enriched)))

# 保存enrichment结果
enrich_path = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\enriched_top_papers.json'
with open(enrich_path, 'w', encoding='utf-8') as f:
    json.dump({
        'enriched_at': datetime.now().isoformat(),
        'count': len(enriched),
        'papers': enriched,
    }, f, ensure_ascii=False, indent=2)
print('Saved: {}'.format(enrich_path))

# ============ 步骤2: regex提取code_url (剩余核心论文) ============
print('\n--- 步骤2: Regex提取剩余核心论文的code_url ---')

regex_extracted = 0
for p in core_papers_sorted[TOP_N:]:
    aid = p.get('arxiv_id','')
    if aid in enriched:
        continue
    
    title = p.get('title','')
    abstract = p.get('abstract','')
    text = (title + ' ' + abstract).lower()
    
    if not aid:
        continue
    
    extracted = regex_extract_code_and_performance(text)
    if not extracted['code_url'] and not extracted['perf_hint']:
        continue
    
    # 找文件
    f_p = next((fp for fp in full['papers'] if fp.get('arxiv_id')==aid), {})
    objects = f_p.get('objects', [])
    methods = f_p.get('methods', [])
    primary_obj = objects[0] if objects else '参数'
    primary_meth = methods[0] if methods else '量化'
    primary_cell = '{}×{}'.format(primary_obj, primary_meth)
    
    fpath = find_md_file(aid, title, primary_cell)
    if fpath and extracted['code_url']:
        # 只更新code_url
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(
            r'code_url: ".*?"',
            'code_url: "{}"'.format(extracted['code_url']),
            content
        )
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            regex_extracted += 1

print('Regex extracted code_url: {}'.format(regex_extracted))

# ============ 总结 ============
print('\n=== Enrichment Summary ===')
print('Top {} papers enriched by LLM:'.format(TOP_N))
print('  Innovations: {}'.format(len(enriched)))
print('  Regex code URLs: {}'.format(regex_extracted))

# 实例
print('\n=== Sample enriched papers ===')
for aid, info in list(enriched.items())[:5]:
    print('  [{}]'.format(aid))
    print('    Title: {}'.format(info['title']))
    print('    Cell: {}'.format(info['primary_cell']))
    print('    Innov: {}'.format(' | '.join(info['innovations'])[:120]))
    if info['performance'] and info['performance'] != '未提取到具体数字':
        print('    Perf: {}'.format(info['performance']))
    if info['code_url']:
        print('    Code: {}'.format(info['code_url']))
