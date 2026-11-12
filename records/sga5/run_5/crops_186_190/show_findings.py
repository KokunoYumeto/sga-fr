"""Print findings of earlier batches filtered by kind or substring (read-only helper)."""
import json
import sys

path, key = sys.argv[1], sys.argv[2]
val = sys.argv[3] if len(sys.argv) > 3 else None
d = json.load(open(path, encoding="utf-8"))
out = []
for f in d:
    if val is None:
        if key in json.dumps(f, ensure_ascii=False):
            out.append(f)
    elif f.get(key) == val:
        out.append(f)
sys.stdout.reconfigure(encoding="utf-8")
for f in out[:40]:
    print(json.dumps(f, ensure_ascii=False)[:700])
    print()
print(len(out), "of", len(d))
