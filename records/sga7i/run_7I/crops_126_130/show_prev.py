import json, glob, sys, os

# usage: show_prev.py <substring> [max per file]
needle = sys.argv[1]
maxn = int(sys.argv[2]) if len(sys.argv) > 2 else 1
root = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I'
for f in sorted(glob.glob(os.path.join(root, 'findings_*.json'))):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        print('ERR', f, e)
        continue
    n = 0
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if needle in s:
            sys.stdout.buffer.write((os.path.basename(f) + '\n').encode('utf-8'))
            sys.stdout.buffer.write((json.dumps(x, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
            n += 1
            if n >= maxn:
                break
