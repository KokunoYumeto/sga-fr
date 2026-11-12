import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# usage: grep_findings.py <regex> <file> [<file> ...]
pat = re.compile(sys.argv[1])
for fn in sys.argv[2:]:
    d = json.load(open(fn, encoding='utf-8'))
    print('==', fn, len(d))
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            print(s[:900])
            print()
