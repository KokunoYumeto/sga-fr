"""List earlier underline findings whose old text has a comma inside an underline span (precedent check)."""
import glob
import json
import re
import sys

root = sys.argv[1]
pat = re.compile(r"\\underline\{[^}]*,[^}]*\}")
for f in sorted(glob.glob(root + "/findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        fx = x.get("fix")
        if not isinstance(fx, dict):
            continue
        o = fx.get("old", "")
        if x.get("kind") == "underline" and pat.search(o):
            print(f.split("\\")[-1], x["page"], repr(o)[:110], "->", repr(fx.get("new", ""))[:110])
