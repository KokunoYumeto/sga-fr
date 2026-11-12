import json, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\\'
for f in sys.argv[1:]:
    try:
        d = json.load(open(base + f, encoding='utf-8'))
    except Exception as e:
        print(f, e)
        continue
    n = 0
    for x in d:
        if x.get('kind') == 'underline' and x.get('fix'):
            print(f, x['page'], '|', x['where'][:100])
            print('  OLD:', x['fix']['old'][:600])
            print('  NEW:', x['fix']['new'][:800])
            print('  NOTE:', x.get('note', '')[:400])
            n += 1
            if n >= 4:
                break
