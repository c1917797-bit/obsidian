"""
处理剩余55篇核心论文
- 通过arxiv_id前缀查找文件（不再依赖title）
- 补建缺失的2篇
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, re, json, time
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, r'C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os')
from core.minimax_client import get_client
llm = get_client()

META_ROOT = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\论文元数据'
CORE_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\core_papers_list.json'
V8_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_v8.json'
FULL_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_optimization_full_tagged.json'
PROGRESS_PATH = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\enriched_papers_progress.json'

# 加载
with open(CORE_PATH, 'r', encoding='utf-8') as f:
    core_data = json.load(f)
core_papers = core_data['papers']

with open(V8_PATH, 'r', encoding='utf-8-sig') as f:
    v8 = json.load(f)
v8_index = {p.get('arxiv_id'): p for p in v8['papers'] if p.get('arxiv_id')}

with open(FULL_PATH, 'r', encoding='utf-8-sig') as f:
    full = json.load(f)
full_index = {p.get('arxiv_id'): p for p in full['papers'] if p.get('arxiv_id')}

with open(PROGRESS_PATH, 'r', encoding='utf-8') as f:
    progress = json.load(f)
already_done = set(progress.get('done', []))
enriched_results = progress.get('results', {})

print('Already done:', len(already_done))
print('Total core papers:', len(core_papers))

# ============ 通过arxiv_id找文件 ============
def find_md_by_aid(aid):
    """通过arxiv_id前缀找文件"""
    for cell_dir in os.listdir(META_ROOT):
        cell_path = os.path.join(META_ROOT, cell_dir)
        if not os.path.isdir(cell_path):
            continue
        for f in os.listdir(cell_path):
            if f.startswith(aid + '_') or f == aid + '.md':
                return os.path.join(cell_path, f), cell_dir
    return None, None

# ============ 收集待处理 ============
to_process = []
for p in core_papers:
    aid = p.get('arxiv_id','')
    if not aid or aid in already_done:
        continue
    title = p.get('title','')
    if not title:
        continue
    
    # 找文件
    fpath, cell_dir = find_md_by_aid(aid)
    if not fpath:
        # 文件不存在 - 创建
        if not p.get('abstract'):
            v8p = v8_index.get(aid)
            if v8p:
                p['abstract'] = v8p.get('abstract', '')
        
        # 确定primary cell
        f_p = full_index.get(aid, {})
        objects = f_p.get('objects', [])
        methods = f_p.get('methods', [])
        primary_obj = objects[0] if objects else '参数'
        primary_meth = methods[0] if methods else '量化'
        primary_cell = '{}×{}'.format(primary_obj, primary_meth)
        
        # 生成文件名
        safe_title = re.sub(r'[<>:"/\\|?*\n\r\t]', '', title)
        safe_title = re.sub(r'\s+', '_', safe_title.strip())[:50]
        fname = '{}_{}.md'.format(aid, safe_title)
        cell_path = os.path.join(META_ROOT, primary_cell)
        fpath_new = os.path.join(cell_path, fname)
        
        to_process.append({
            'p': p,
            'aid': aid,
            'title': title,
            'abstract': p.get('abstract', ''),
            'primary_cell': primary_cell,
            'fpath': fpath_new,  # 需要创建
            'is_new': True,
        })
    else:
        # 文件存在
        # 确定primary cell
        f_p = full_index.get(aid, {})
        objects = f_p.get('objects', [])
        methods = f_p.get('methods', [])
        primary_obj = objects[0] if objects else '参数'
        primary_meth = methods[0] if methods else '量化'
        primary_cell = '{}×{}'.format(primary_obj, primary_meth)
        
        if not p.get('abstract'):
            v8p = v8_index.get(aid)
            if v8p:
                p['abstract'] = v8p.get('abstract', '')
        
        to_process.append({
            'p': p,
            'aid': aid,
            'title': title,
            'abstract': p.get('abstract', ''),
            'primary_cell': primary_cell,
            'fpath': fpath,
            'is_new': False,
        })

print('To process: {}'.format(len(to_process)))
for item in to_process[:5]:
    print('  -', item['aid'], item['title'][:50], '(new)' if item['is_new'] else '')

# ============ 创建缺失的MD文件 ============
NEW_CARD_TEMPLATE = '''---
type: literature-corpus-entry
citekey: {citekey}
title: "{title}"
authors: []
year: {year}
venue: {venue}
venue_type: conference
arxiv_id: "{aid}"
doi: ""
url: "https://arxiv.org/abs/{aid}"
pdf_url: "https://arxiv.org/pdf/{aid}"
object: {obj}
method: {meth}
cell: "{cell}"
all_objects: []
all_methods: []
abstract: |
{abstract_indented}
key_innovation: "待精读后填写"
performance: "待精读后填写"
code_url: ""
hf_model: ""
status: unread
priority: P2
date_added: 2026-07-06
obtained_via: "core_paper_backfill"
obtained_at: 2026-07-06
tags:
  - inference-compression
  - {obj}
  - {meth}
---

# {title}

## 基本信息

| 字段 | 值 |
|------|------|
| **Citekey** | `{citekey}` |
| **年份** | {year} |
| **会议/期刊** | {venue} |
| **arXiv** | [{aid}](https://arxiv.org/abs/{aid}) |
| **4×5分类** | {cell} |
| **来源** | core_paper_backfill |

## 摘要

{abstract}

## 关键创新

*待精读后在此填写 1-3 个方法核心创新点*

## 性能数据

| 模型/场景 | 压缩率 | 精度 | 加速比 | 显存 |
|-----------|--------|------|--------|------|
| 待填 | | | | |

## 代码与资源

- **PDF**: https://arxiv.org/pdf/{aid}
- **代码**: （精读时查找GitHub链接）

## 我的笔记

## 相关论文

---

*基于 ARS v3.6.4 literature_corpus_entry schema*
'''

def citekey(authors_str, year, title):
    parts = []
    if authors_str:
        words = authors_str.split()
        lastname = words[-1].lower() if words else 'anon'
        parts.append(re.sub(r'[^a-z]', '', lastname))
    else:
        parts.append('anon')
    parts.append(str(year) if year else 'nd')
    if title:
        en_words = re.findall(r'[A-Za-z]+', title)
        if en_words:
            parts.append(en_words[0].lower())
    return ''.join(parts)[:50]

for item in to_process:
    if item['is_new']:
        # 创建文件
        p = item['p']
        year = p.get('year','')
        if not year:
            pub = p.get('published','')
            if pub and len(pub) >= 4:
                try: year = int(pub[:4])
                except: year = ''
        venue = p.get('venue','')
        authors_str = ''
        if p.get('authors'):
            a = p['authors']
            if isinstance(a, list): authors_str = str(a[0]) if a else ''
            else: authors_str = str(a)
        abstract = p.get('abstract', '暂无摘要')
        abstract_indented = '\n  '.join(abstract.split('\n')[:20])
        
        # Safely escape
        title_safe = item['title'].replace('"', '\\"')
        abstract_safe = abstract.replace('"', '\\"')
        
        content = NEW_CARD_TEMPLATE.format(
            citekey=citekey(authors_str, year, item['title']),
            title=title_safe,
            year=year or '""',
            venue=venue.replace('"','') if venue else 'arXiv',
            aid=item['aid'],
            obj=item['primary_cell'].split('×')[0],
            meth=item['primary_cell'].split('×')[1],
            cell=item['primary_cell'],
            abstract=abstract_safe,
            abstract_indented=abstract_indented,
        )
        with open(item['fpath'], 'w', encoding='utf-8') as f:
            f.write(content)
        print('  Created: {}'.format(item['fpath']))

print('File creation done')

# ============ LLM处理 ============
def llm_extract(title, abstract, max_retries=3):
    prompt = '''分析以下AI论文，给出关键创新点。要求简洁。

标题: {title}

摘要: {abstract}

回答格式（每行一项）:
创新1: [核心创新点1，一句话]
性能: [具体数字如"加速1.5x"，无则填"未提数字"]
代码: [GitHub链接或"未开源"]
'''.format(title=title[:200], abstract=(abstract or '无摘要')[:1200])
    
    for attempt in range(max_retries):
        try:
            resp = llm.chat([{'role':'user','content':prompt}], max_tokens=200)
            return parse_response(resp), None
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            return None, str(e)[:60]

def parse_response(resp):
    innovations = []
    performance = ''
    code = ''
    for line in resp.split('\n'):
        line = line.strip()
        if line.startswith('创新1') or line.startswith('创新2'):
            v = re.sub(r'^\S+:', '', line).strip()
            if v and len(v) > 3:
                innovations.append(v)
        elif line.startswith('性能'):
            performance = re.sub(r'^\S+:', '', line).strip()
        elif line.startswith('代码'):
            code = re.sub(r'^\S+:', '', line).strip()
    return {
        'innovations': innovations[:2],
        'performance': performance,
        'code': code,
    }

def update_md_safe(fpath, info):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    innovations_text = ' | '.join(info['innovations']) if info['innovations'] else '需精读总结'
    performance = info['performance'] or '未提数字'
    code = info['code'] or ''
    
    new_content = re.sub(
        r'key_innovation: ".*?"',
        lambda m, t=innovations_text: 'key_innovation: "{}"'.format(t.replace('"', '\\"').replace('\\', '\\\\')),
        content
    )
    new_content = re.sub(
        r'performance: ".*?"',
        lambda m, t=performance: 'performance: "{}"'.format(t.replace('"', '\\"').replace('\\', '\\\\')),
        new_content
    )
    if code and code != '未开源':
        new_content = re.sub(
            r'code_url: ".*?"',
            lambda m, t=code: 'code_url: "{}"'.format(t.replace('"', '\\"').replace('\\', '\\\\')),
            new_content
        )
    new_content = re.sub(r'priority: P\d', 'priority: P1', new_content, count=1)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

print('\n=== Processing {} papers ==='.format(len(to_process)))
enriched_this_run = 0
failures_this_run = []

for i, item in enumerate(to_process):
    info, err = llm_extract(item['title'], item['abstract'])
    if err:
        failures_this_run.append({'aid': item['aid'], 'err': err})
        already_done.add(item['aid'])
        print('  [{}/{}] {} FAILED: {}'.format(i+1, len(to_process), item['aid'], err[:40]))
        time.sleep(2)
        continue
    
    if info:
        update_md_safe(item['fpath'], info)
        enriched_results[item['aid']] = {
            'title': item['title'][:80],
            'primary_cell': item['primary_cell'],
            'innovations': info['innovations'][:2],
            'performance': info['performance'][:50],
            'code': info['code'][:60],
            'is_new_file': item['is_new'],
        }
        enriched_this_run += 1
        already_done.add(item['aid'])
        if (i+1) % 5 == 0:
            print('  [{}/{}] done={}'.format(i+1, len(to_process), enriched_this_run))
    time.sleep(1.5)

# 保存进度
with open(PROGRESS_PATH, 'w', encoding='utf-8') as f:
    json.dump({
        'last_update': datetime.now().isoformat(),
        'done': list(already_done),
        'results': enriched_results,
        'failures': failures_this_run,
    }, f, ensure_ascii=False, indent=2)

print('\n=== Final ===')
print('This run enriched: {}'.format(enriched_this_run))
print('Failures: {}'.format(len(failures_this_run)))
print('Total in v2: {}'.format(len(enriched_results)))
print()
print('Sample (this run):')
new_done = [aid for aid in already_done if aid in enriched_results and enriched_results[aid].get('is_new_file')]
for aid in list(enriched_results.keys())[:5]:
    info = enriched_results[aid]
    print('  [{}] {}'.format(aid, info['title'][:50]))
    print('    Innov: {}'.format(' | '.join(info['innovations'])[:100]))
    if info['performance'] != '未提数字':
        print('    Perf: {}'.format(info['performance']))
    if info['code'] and info['code'] != '未开源':
        print('    Code: {}'.format(info['code']))