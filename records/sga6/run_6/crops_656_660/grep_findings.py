"""Print findings (from the given findings files) whose JSON matches a regular expression.
usage: python -I grep_findings.py REGEX FILE [FILE ...]"""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(sys.argv[1], re.I)
for f in sys.argv[2:]:
    d = json.load(open(f, encoding="utf-8"))
    hits = [x for x in d if pat.search(json.dumps(x, ensure_ascii=False))]
    print("=====", f, len(d), "findings,", len(hits), "hits")
    for x in hits:
        print(json.dumps(x, ensure_ascii=False)[:1000])
        print()
