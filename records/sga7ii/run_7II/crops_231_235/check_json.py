import json
import sys

folder = sys.argv[1]
path = sys.argv[2]
with open(path, encoding="utf-8") as f:
    data = json.load(f)
for i, d in enumerate(data):
    with open(f"{folder}/page_{d['page']}.tex", encoding="utf-8", newline="") as f:
        text = f.read()
    tex_count = text.count(d["tex"]) if d.get("tex") else None
    fix = d.get("fix")
    old_count = text.count(fix["old"]) if fix else None
    print(i, d["page"], d["kind"], "tex_count=", tex_count, "old_count=", old_count)
print("entries:", len(data))
