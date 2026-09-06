"""
推理优化论文查询工具 v2（支持20格查询）
用法：
  python query_papers.py --cell "KVx量化"        # 查KV×量化格
  python query_papers.py --cell "通信x蒸馏"       # 查通信×蒸馏格
  python query_papers.py --obj "KV"               # 查KV相关所有格
  python query_papers.py --method "量化"           # 查量化相关所有格
  python query_papers.py "keyword" --limit 20     # 按关键词搜
  python query_papers.py --stats                   # 看20格统计
"""
import json, sys, os, argparse
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FULL_DB = r"C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_optimization_full_tagged.json"
V9_DB = r"C:\Users\Huawei\Documents\code\Obsidian\4_AI情报洞察\inference_compression_v9.json"

OBJ_LIST = ['参数', '激活', 'KV', '通信']
MTH_LIST = ['量化', '剪枝', '稀疏化', '蒸馏', '低秩']

def load_db():
    with open(FULL_DB, 'r', encoding='utf-8') as f:
        return json.load(f)

def query_cell(cell_name, min_cite=0, limit=50):
    db = load_db()
    results = []
    for p in db['papers']:
        if cell_name in p.get('cells', []):
            cite = p.get('gs_citation', 0)
            if not isinstance(cite, int): cite = 0
            if cite >= min_cite:
                results.append((cite, p))
    results.sort(key=lambda x: -x[0])
    return results[:limit]

def query_obj(obj, limit=50):
    db = load_db()
    results = []
    for p in db['papers']:
        cells = p.get('cells', [])
        if any(c.startswith(obj + 'x') for c in cells):
            cite = p.get('gs_citation', 0)
            if not isinstance(cite, int): cite = 0
            results.append((cite, p))
    results.sort(key=lambda x: -x[0])
    return results[:limit]

def query_method(mth, limit=50):
    db = load_db()
    results = []
    for p in db['papers']:
        cells = p.get('cells', [])
        if any(c.endswith('x' + mth) for c in cells):
            cite = p.get('gs_citation', 0)
            if not isinstance(cite, int): cite = 0
            results.append((cite, p))
    results.sort(key=lambda x: -x[0])
    return results[:limit]

def show_stats():
    db = load_db()
    cell_c = Counter()
    for p in db['papers']:
        for c in p.get('cells', []):
            cell_c[c] += 1
    
    print("=" * 60)
    print("20格统计（full数据库 {}篇）".format(len(db['papers'])))
    print("=" * 60)
    print("\n{:8s}".format(""), end="")
    for mth in MTH_LIST:
        print("{:>10s}".format(mth), end="")
    print()
    print("-" * 58)
    for obj in OBJ_LIST:
        print("{:8s}".format(obj), end="")
        for mth in MTH_LIST:
            c = cell_c.get(obj + 'x' + mth, 0)
            tag = ""
            if c == 0: tag = " DIAMOND"
            elif c < 15: tag = " LOW"
            elif c > 100: tag = " RED"
            print("{:>10d}{}".format(c, tag), end="")
        print()

def main():
    parser = argparse.ArgumentParser(description='20格论文查询')
    parser.add_argument('--cell', help='查询某格(如 KVx量化)')
    parser.add_argument('--obj', help='查询某对象所有格(如 KV)')
    parser.add_argument('--method', help='查询某方法所有格(如 量化)')
    parser.add_argument('--min-cite', type=int, default=0)
    parser.add_argument('--limit', type=int, default=30)
    parser.add_argument('--stats', action='store_true')
    args = parser.parse_args()
    
    if args.stats:
        show_stats()
        return
    
    if args.cell:
        results = query_cell(args.cell, args.min_cite, args.limit)
        print("\n格 {} : {} 篇".format(args.cell, len(results)))
        for i, (cite, p) in enumerate(results):
            print("  {}. [{}ref] [{}] {}".format(i+1, cite, p['venue'][:10], p['title'][:55]))
    
    elif args.obj:
        results = query_obj(args.obj, args.limit)
        print("\n对象 {} : {} 篇".format(args.obj, len(results)))
        for i, (cite, p) in enumerate(results):
            print("  {}. [{}ref] [{}] {} | cells={}".format(
                i+1, cite, p['venue'][:10], p['title'][:45], p.get('cells',[])))
    
    elif args.method:
        results = query_method(args.method, args.limit)
        print("\n方法 {} : {} 篇".format(args.method, len(results)))
        for i, (cite, p) in enumerate(results):
            print("  {}. [{}ref] [{}] {} | cells={}".format(
                i+1, cite, p['venue'][:10], p['title'][:45], p.get('cells',[])))

if __name__ == '__main__':
    main()
