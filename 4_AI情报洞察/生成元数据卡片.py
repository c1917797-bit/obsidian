"""
批量生成14,407篇推理压缩论文的元数据卡片

路径: 4_AI情报洞察/论文元数据/{主分类}/{arxiv_id}_{短标题}.md
模板: 基于literature-corpus-entry扩展，增加4×5分类/性能/代码/个人追踪等字段
"""
import os
os.environ['PYTHONUTF8'] = '1'
import sys, io, re, json, time, hashlib
from collections import Counter, defaultdict
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============ 路径 ============
INSIGHT_DIR = r'C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察'
META_ROOT = os.path.join(INSIGHT_DIR, '论文元数据')
V8_PATH = os.path.join(INSIGHT_DIR, 'inference_compression_v8.json')
FULL_PATH = os.path.join(INSIGHT_DIR, 'inference_optimization_full_tagged.json')

# ============ 加载 ============
with open(V8_PATH, 'r', encoding='utf-8-sig') as f:
    v8 = json.load(f)
with open(FULL_PATH, 'r', encoding='utf-8-sig') as f:
    full = json.load(f)

# 用full的objects/methods标签（更完整）
aid_tags = {}
for p in full['papers']:
    aid = p.get('arxiv_id')
    if aid:
        aid_tags[aid] = {
            'objects': p.get('objects', []),
            'methods': p.get('methods', []),
            'cells': p.get('cells', []),
        }

# 标题关键词 -> 主分类（20格）
CELL_KEYWORDS = {
    '参数×量化': {'objects':['参数','weight','weights'], 'methods':['quantiz','quant','量化','int4','int8','fp8','gptq','awq']},
    '参数×剪枝': {'objects':['参数'], 'methods':['prun','sparse','wanda','sparsegpt','剪枝','稀疏']},
    '参数×稀疏': {'objects':['参数'], 'methods':['spars','稀疏']},
    '参数×蒸馏': {'objects':['参数'], 'methods':['distill','蒸馏']},
    '参数×低秩': {'objects':['参数'], 'methods':['low-rank','lora','svd','低秩','decomposition']},
    '激活×量化': {'objects':['激活','activation'], 'methods':['quantiz','quant','smoothquant','量化']},
    '激活×剪枝': {'objects':['激活'], 'methods':['prun','spars','token']},
    '激活×稀疏': {'objects':['激活'], 'methods':['spars']},
    '激活×蒸馏': {'objects':['激活'], 'methods':['distill']},
    '激活×低秩': {'objects':['激活'], 'methods':['low-rank','lora']},
    'KV×量化': {'objects':['KV','kv'], 'methods':['quantiz','量化']},
    'KV×剪枝': {'objects':['KV','kv'], 'methods':['prun','evict','eviction','稀疏','剪枝']},
    'KV×稀疏': {'objects':['KV','kv'], 'methods':['spars','稀疏']},
    'KV×蒸馏': {'objects':['KV','kv'], 'methods':['distill']},
    'KV×低秩': {'objects':['KV','kv'], 'methods':['low-rank','lora']},
    '通信×量化': {'objects':['通信'], 'methods':['quantiz']},
    '通信×剪枝': {'objects':['通信'], 'methods':['prun','spars']},
    '通信×稀疏': {'objects':['通信'], 'methods':['spars']},
    '通信×蒸馏': {'objects':['通信'], 'methods':['distill']},
    '通信×低秩': {'objects':['通信'], 'methods':['low-rank','lora']},
}

OBJECT_LABEL = {'参数':'参数', 'weight':'参数', 'weights':'参数', '激活':'激活', 'activation':'激活',
                'KV':'KV', 'kv':'KV', '通信':'通信'}
METHOD_LABEL = {'quantiz':'量化', 'quant':'量化', '量化':'量化', 'int4':'量化',
                'prun':'剪枝/稀疏', 'sparse':'剪枝/稀疏', 'spars':'剪枝/稀疏', '剪枝':'剪枝/稀疏', '稀疏':'剪枝/稀疏',
                'wanda':'剪枝/稀疏', 'sparsegpt':'剪枝/稀疏', 'smoothquant':'量化',
                'distill':'蒸馏', '蒸馏':'蒸馏',
                'low-rank':'低秩', 'lora':'低秩', 'svd':'低秩', '低秩':'低秩', 'decomposition':'低秩'}

def sanitize_filename(name, max_len=80):
    """去除Windows非法字符，限制长度"""
    name = re.sub(r'[<>:"/\\|?*\n\r\t]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    if len(name) > max_len:
        name = name[:max_len]
    return name

def parse_authors(authors_field):
    """解析authors字段 - 可能是字符串'X;Y;Z'或列表[dict]"""
    if isinstance(authors_field, list):
        result = []
        for a in authors_field[:5]:
            if isinstance(a, dict):
                a = a.get('name') or a.get('value') or ''
            a = str(a).strip()
            if a:
                result.append(a)
        return result
    elif isinstance(authors_field, str):
        # 分号/逗号分隔
        parts = re.split(r'[;,]', authors_field)
        return [p.strip() for p in parts if p.strip()][:5]
    return []

def extract_year(paper):
    """提取年份"""
    # 优先用year字段
    y = paper.get('year')
    if y:
        try:
            return int(y)
        except:
            pass
    # 其次用published字段
    pub = paper.get('published','')
    if pub and len(pub) >= 4:
        try:
            return int(pub[:4])
        except:
            pass
    # 最后用arxiv_id
    aid = paper.get('arxiv_id','')
    if len(aid) >= 2:
        try:
            yr = int('20' + aid[:2])
            if 2010 <= yr <= 2030:
                return yr
        except:
            pass
    return None

def make_citekey(authors, year, title):
    """生成citekey: firstauthorYEARfirstword"""
    parts = []
    
    # 作者 - 取第一个作者的姓
    if authors and authors[0]:
        a = str(authors[0]).strip()
        # 取最后一个单词作为姓
        words = a.split()
        lastname = words[-1].lower() if words else 'anon'
        parts.append(re.sub(r'[^a-z]', '', lastname))
    else:
        parts.append('anon')
    
    # 年份
    if year:
        parts.append(str(year))
    else:
        parts.append('nd')
    
    # 标题首词
    if title:
        # 优先英文首词
        en_words = re.findall(r'[A-Za-z]+', title)
        if en_words:
            parts.append(en_words[0].lower())
        else:
            parts.append('paper')
    
    return ''.join(parts)[:50]  

def determine_primary_cell(objects, methods, title='', abstract=''):
    """根据objects/methods和标题摘要确定主分类格"""
    if not objects or not methods:
        # 从文本推断
        text = (title + ' ' + abstract).lower()
        
        # 检测对象
        obj = None
        if any(kw in text for kw in ['kv cache', 'kv-cache', 'key-value cache', 'prefill', 'paged attention']):
            obj = 'KV'
        elif any(kw in text for kw in ['tensor parallel', 'pipeline parallel', 'expert parallel', 'communication']):
            obj = '通信'
        elif any(kw in text for kw in ['token compression', 'token pruning', 'token merging', 'prompt compression', 'activation', 'visual token']):
            obj = '激活'
        else:
            obj = '参数'
        
        # 检测方法
        meth = None
        if any(kw in text for kw in ['quantiz', ' int4', ' int8', ' fp8', 'gptq', 'awq', 'smoothquant']):
            meth = '量化'
        elif any(kw in text for kw in ['low-rank', 'lora', 'svd', 'decomposition']):
            meth = '低秩'
        elif any(kw in text for kw in ['distill', 'teacher-student']):
            meth = '蒸馏'
        elif any(kw in text for kw in ['sparse attention', 'pruning', 'sparsity', 'wanda', 'sparsegpt', 'token prune', 'sparse']):
            meth = '剪枝/稀疏'
        else:
            meth = '量化'  # 默认
        
        return obj, meth
    
    # 优先用第一个object + 第一个method
    obj = objects[0]
    meth = methods[0]
    
    # 标准化
    obj = OBJECT_LABEL.get(obj, obj if obj in ['参数','激活','KV','通信'] else '参数')
    meth = METHOD_LABEL.get(meth, meth if meth in ['量化','剪枝/稀疏','蒸馏','低秩'] else '量化')
    
    return obj, meth

def make_card(paper, idx):
    """生成单篇论文的卡片内容"""
    aid = paper.get('arxiv_id','')
    title = paper.get('title','')
    authors_parsed = parse_authors(paper.get('authors', []))
    year = extract_year(paper)
    venue = paper.get('venue','')
    abstract = paper.get('abstract','')
    url = paper.get('url', f'https://arxiv.org/abs/{aid}' if aid else '')
    
    # 从full拿objects/methods
    tags = aid_tags.get(aid, {})
    objects = tags.get('objects', [])
    methods = tags.get('methods', [])
    cells = tags.get('cells', [])
    
    # 主分类格
    primary_obj, primary_meth = determine_primary_cell(objects, methods, title, abstract)
    primary_cell = '{}×{}'.format(primary_obj, primary_meth)
    
    # citekey
    citekey = make_citekey(authors_parsed, year, title)
    
    # 处理特殊字符
    safe_title = title.replace('"', '\\"')
    
    # 生成YAML
    yaml_lines = [
        '---',
        'type: literature-corpus-entry',
        'citekey: {}'.format(citekey),
        'title: "{}"'.format(safe_title),
    ]
    
    if authors_parsed:
        yaml_lines.append('authors:')
        for a in authors_parsed:
            yaml_lines.append('  - "{}"'.format(str(a).replace('"','').strip()))
    else:
        yaml_lines.append('authors: []')
    
    yaml_lines.extend([
        'year: {}'.format(year if year else '""'),
        'venue: {}'.format(str(venue).replace('"','').strip()),
        'venue_type: conference',
        'arxiv_id: "{}"'.format(aid),
        'doi: ""',
        'url: "{}"'.format(url),
        ('pdf_url: "https://arxiv.org/pdf/{}"'.format(aid) if aid else 'pdf_url: ""'),
    ])
    
    # 推理压缩特定字段
    yaml_lines.append('object: {}'.format(primary_obj))
    yaml_lines.append('method: {}'.format(primary_meth))
    yaml_lines.append('cell: "{}"'.format(primary_cell))
    if objects:
        yaml_lines.append('all_objects:')
        for o in objects:
            yaml_lines.append('  - "{}"'.format(o))
    else:
        yaml_lines.append('all_objects: []')
    if methods:
        yaml_lines.append('all_methods:')
        for m in methods:
            yaml_lines.append('  - "{}"'.format(m))
    else:
        yaml_lines.append('all_methods: []')
    
    # 摘要
    yaml_lines.append('abstract: |')
    for line in (abstract or '暂无摘要').split('\n')[:20]:
        yaml_lines.append('  ' + line.strip())
    
    # 关键创新 (placeholder)
    yaml_lines.extend([
        'key_innovation: "待精读后填写"',
        'performance: "待精读后填写"',
    ])
    
    # 代码资源
    yaml_lines.extend([
        'code_url: ""',
        'hf_model: ""',
    ])
    
    # 个人追踪
    yaml_lines.extend([
        'status: unread',
        'priority: P2',
        'date_added: {}'.format(datetime.now().strftime('%Y-%m-%d')),
    ])
    
    # 来源
    src = paper.get('source','')
    yaml_lines.append('obtained_via: "{}"'.format(src if src else 'arxiv'))
    yaml_lines.append('obtained_at: {}'.format(datetime.now().strftime('%Y-%m-%d')))
    
    # 标签
    yaml_lines.append('tags:')
    yaml_lines.append('  - inference-compression')
    yaml_lines.append('  - {}'.format(primary_obj))
    yaml_lines.append('  - {}'.format(primary_meth))
    if authors_parsed:
        a = authors_parsed[0]
        words = a.split()
        lastname = words[-1].lower() if words else ''
        if lastname:
            yy = str(year)[-2:] if year else ''
            yaml_lines.append('  - {}{}'.format(lastname, yy))
    
    yaml_lines.append('---')
    
    # Body
    body = [
        '',
        '# {}'.format(title),
        '',
        '## 基本信息',
        '',
        '| 字段 | 值 |',
        '|------|------|',
        '| **Citekey** | `{}` |'.format(citekey),
        '| **年份** | {} |'.format(year or 'N/A'),
        '| **会议/期刊** | {} |'.format(venue or 'arXiv preprint'),
        ('| **arXiv** | [{}]({}) |'.format(aid, url) if aid else '| **arXiv** | N/A |'),
        '| **4×5分类** | {} |'.format(primary_cell),
        '| **来源** | {} |'.format(paper.get('source','') or 'arXiv'),
        '| **作者** | {} |'.format(', '.join(authors_parsed[:3]) or 'N/A'),
        '',
        '## 摘要',
        '',
        abstract or '*暂无摘要*',
        '',
        '## 关键创新',
        '',
        '*待精读后在此填写 1-3 个方法核心创新点*',
        '',
        '> 提示：',
        '> - 这个方法解决什么问题？',
        '> - 相比已有方法的本质区别？',
        '> - 实验中验证了什么关键指标？',
        '',
        '## 性能数据',
        '',
        '| 模型/场景 | 压缩率 | 精度 | 加速比 | 显存 |',
        '|-----------|--------|------|--------|------|',
        '| 待填 | | | | |',
        '',
        '> 精读时把论文表格中的关键数字搬过来',
        '',
        '## 代码与资源',
        '',
        '- **PDF**: https://arxiv.org/pdf/{}'.format(aid) if aid else '',
        '- **代码**: （精读时查找GitHub链接）',
        '- **HuggingFace模型**: （如适用）',
        '',
        '## 我的笔记',
        '',
        '*精读笔记在此写，或链接到 [[专题笔记名]]*',
        '',
        '## 相关论文',
        '',
        '*精读时用Obsidian双链 `[[arxiv_id]]` 连接相关工作*',
        '',
        '---',
        '',
        '*基于 ARS v3.6.4 literature_corpus_entry schema*  ',
        '*生成日期: {} | 来源: {}*'.format(datetime.now().strftime('%Y-%m-%d'), src or 'arXiv'),
    ]
    
    content = '\n'.join(yaml_lines) + '\n' + '\n'.join(body)
    return content, primary_cell

# ============ 批量生成 ============
print('Total papers: {}'.format(len(v8['papers'])))
print('Output root: {}'.format(META_ROOT))

# 创建目录骨架
os.makedirs(META_ROOT, exist_ok=True)
cells_to_create = set()
for p in v8['papers']:
    aid = p.get('arxiv_id','')
    tags = aid_tags.get(aid, {})
    primary_obj, primary_meth = determine_primary_cell(
        tags.get('objects',[]), tags.get('methods',[]),
        p.get('title',''), p.get('abstract',''))
    primary_cell = '{}×{}'.format(primary_obj, primary_meth)
    cells_to_create.add(primary_cell)

# 添加"未分类"格子
cells_to_create.add('未分类')

for cell in sorted(cells_to_create):
    cell_dir = os.path.join(META_ROOT, cell)
    os.makedirs(cell_dir, exist_ok=True)
    # 加.gitkeep
    gitkeep = os.path.join(cell_dir, '.gitkeep')
    if not os.path.exists(gitkeep):
        open(gitkeep, 'w').close()
print('Cell dirs created: {}'.format(len(cells_to_create)))

# ============ 生成文件 ============
BATCH_SIZE = 100
papers = v8['papers']
total = len(papers)
written = 0
skipped = 0
errors = []
FORCE_OVERWRITE = True   # 强制覆盖现有卡片
cell_counter = Counter()

start = time.time()
for i, p in enumerate(papers):
    try:
        aid = p.get('arxiv_id','')
        title = p.get('title','')
        
        if not title:
            skipped += 1
            continue
        
        # 决定主分类
        tags = aid_tags.get(aid, {})
        primary_obj, primary_meth = determine_primary_cell(
            tags.get('objects',[]), tags.get('methods',[]),
            title, p.get('abstract',''))
        primary_cell = '{}×{}'.format(primary_obj, primary_meth)
        
        # 生成文件名
        if aid:
            short_title = sanitize_filename(title)[:50]
            fname = '{}_{}.md'.format(aid, short_title)
        else:
            # 用title hash
            h = hashlib.md5(title.encode('utf-8')).hexdigest()[:8]
            short_title = sanitize_filename(title)[:50]
            fname = '{}_{}.md'.format(h, short_title)
        
        fpath = os.path.join(META_ROOT, primary_cell, fname)
        
        # 检查是否已存在 (force=True 时覆盖)
        if os.path.exists(fpath) and not FORCE_OVERWRITE:
            skipped += 1
            continue
        
        # 生成内容
        content, _ = make_card(p, i)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        written += 1
        cell_counter[primary_cell] += 1
        
    except Exception as e:
        errors.append((i, str(e)[:80]))
    
    if (i+1) % 500 == 0:
        elapsed = time.time() - start
        rate = (i+1) / elapsed
        eta = (total - i - 1) / rate if rate > 0 else 0
        print('  [{}/{}] written={}, skipped={}, eta={:.0f}s'.format(
            i+1, total, written, skipped, eta))

print('\n=== Generation complete ===')
print('Total papers: {}'.format(total))
print('Written: {}'.format(written))
print('Skipped (already exist or no title): {}'.format(skipped))
print('Errors: {}'.format(len(errors)))
print('Elapsed: {:.1f}s'.format(time.time() - start))

# 按cell分布
print('\nBy cell:')
for cell, c in cell_counter.most_common():
    print('  {}: {}'.format(cell, c))

# ============ 生成索引文件 ============
print('\nGenerating index files...')

# 1. 全部论文索引（按cell）
index_path = os.path.join(META_ROOT, '_索引_全部论文.md')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write('---\ntags: [inference-compression, index]\n---\n\n')
    f.write('# 推理压缩论文索引 - 共 {} 篇\n\n'.format(written))
    f.write('> 基于 ARS v3.6.4 模板生成。每行为一篇论文的链接。\n\n')
    
    # 按cell分组
    cell_groups = defaultdict(list)
    for p in v8['papers']:
        aid = p.get('arxiv_id','')
        title = p.get('title','')
        if not title:
            continue
        tags = aid_tags.get(aid, {})
        primary_obj, primary_meth = determine_primary_cell(
            tags.get('objects',[]), tags.get('methods',[]),
            title, p.get('abstract',''))
        primary_cell = '{}×{}'.format(primary_obj, primary_meth)
        cell_groups[primary_cell].append((aid, title, p.get('year','')))
    
    for cell in sorted(cell_groups.keys()):
        c_papers = cell_groups[cell]
        f.write('\n## {} ({})\n\n'.format(cell, len(c_papers)))
        for aid, title, year in sorted(c_papers, key=lambda x: (str(x[2]), x[1]))[:500]:
            short_title = sanitize_filename(title)[:80]
            fname = '{}_{}.md'.format(aid, short_title) if aid else 'unknown.md'
            f.write('- **[{}]({})** [{}] {}\n'.format(
                aid or '?', 
                os.path.join(cell, fname).replace('\\', '/'),
                year or '?', 
                title[:80]))

print('  Index: {}'.format(index_path))

# 2. 未读清单
unread_path = os.path.join(META_ROOT, '_未读清单.md')
with open(unread_path, 'w', encoding='utf-8') as f:
    f.write('---\ntags: [inference-compression, unread]\n---\n\n')
    f.write('# 未读论文清单 - 共 {} 篇\n\n'.format(written))
    f.write('> 使用方法：在卡片里将 status: unread 改成 status: reading 或 status: read\n\n')
    
    by_cell = Counter()
    for p in v8['papers']:
        aid = p.get('arxiv_id','')
        title = p.get('title','')
        if not title: continue
        tags = aid_tags.get(aid, {})
        primary_obj, primary_meth = determine_primary_cell(
            tags.get('objects',[]), tags.get('methods',[]),
            title, p.get('abstract',''))
        by_cell['{}×{}'.format(primary_obj, primary_meth)] += 1
    
    f.write('按20格分布:\n\n')
    for cell, c in sorted(by_cell.items()):
        f.write('- {}: {}篇\n'.format(cell, c))

print('  Unread: {}'.format(unread_path))

# 3. 主入口
home_path = os.path.join(META_ROOT, '_主页.md')
with open(home_path, 'w', encoding='utf-8') as f:
    f.write('---\ntags: [inference-compression, home]\n---\n\n')
    f.write('# 推理压缩论文元数据系统\n\n')
    f.write('## 系统说明\n\n')
    f.write('- 总论文数: **{}**\n'.format(written))
    f.write('- 模板: 基于 ARS v3.6.4 literature_corpus_entry\n')
    f.write('- 字段: 包含三态阅读追踪、性能数据、个人笔记\n')
    f.write('- 数据源: arXiv (48组短语查询) + OpenReview + Papercopilot\n\n')
    f.write('## 文件结构\n\n')
    f.write('```\n')
    f.write('论文元数据/\n')
    f.write('  _主页.md (本文件)\n')
    f.write('  _索引_全部论文.md\n')
    f.write('  _未读清单.md\n')
    f.write('  参数×量化/        # {} 篇\n'.format(cell_counter.get('参数×量化',0)))
    f.write('  参数×剪枝/        # {} 篇\n'.format(cell_counter.get('参数×剪枝/稀疏',0)))
    f.write('  ...\n')
    f.write('```\n\n')
    f.write('## 使用方式\n\n')
    f.write('1. **打开 `_主页.md`** - 看系统说明\n')
    f.write('2. **打开 `_索引_全部论文.md`** - 浏览所有论文\n')
    f.write('3. **打开 `_未读清单.md`** - 看待读清单\n')
    f.write('4. **进入 4×5 子目录** - 按主题精读\n\n')
    f.write('## 精读工作流\n\n')
    f.write('```\n')
    f.write('unread -> reading -> read\n')
    f.write('  ↓        ↓        ↓\n')
    f.write('首次浏览  正在读    精读完成\n')
    f.write('  ↓        ↓        ↓\n')
    f.write('           填关键创新 + 性能 + 笔记\n')
    f.write('```\n\n')
    f.write('## Dataview 查询示例\n\n')
    f.write('在主页里可加：\n\n')
    f.write('```dataview\n')
    f.write('TABLE cell, priority, status, year\n')
    f.write('FROM "4_AI情报洞察/论文元数据"\n')
    f.write('WHERE status = "unread"\n')
    f.write('SORT priority ASC\n')
    f.write('LIMIT 50\n')
    f.write('```\n')

print('  Home: {}'.format(home_path))

print('\n=== Done ===')
print('Total files in {}/: {}'.format(META_ROOT, written))
