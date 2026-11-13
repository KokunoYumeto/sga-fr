import json, io, glob, os
base = r'C:/Users/user/Documents/sga_scan_check_20261105'
out = io.open(os.path.join(base, 'run_6', 'crops_416_420', 'prev_underline.txt'), 'w', encoding='utf-8')
files = sorted(glob.glob(os.path.join(base, 'MANUAL_6_findings_3[6-9]*.json'))) + \
        sorted(glob.glob(os.path.join(base, 'MANUAL_6_findings_40*.json')))
for fn in files:
    d = json.load(open(fn, encoding='utf-8'))
    n_u = 0
    for x in d:
        if x.get('kind') == 'underline':
            n_u += 1
            out.write(os.path.basename(fn) + ' ' + json.dumps(x, ensure_ascii=False)[:600] + '\n\n')
    out.write('## %s: %d findings, %d underline\n\n' % (os.path.basename(fn), len(d), n_u))
out.close()
