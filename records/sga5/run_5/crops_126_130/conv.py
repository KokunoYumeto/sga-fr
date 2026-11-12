import json, sys, glob, os
sys.stdout.reconfigure(encoding='utf-8')
run = r'C:/Users/user/Documents/sga_scan_check_20261105/run_5/'
keys = sys.argv[1:]
for fn in sorted(glob.glob(run + 'findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception as e:
        print('ERR', fn, e)
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if all(k in s for k in keys):
            print(os.path.basename(fn), s[:900])
            print()
