"""Remove \\end{ENV} lines that have no opening \\begin{ENV} left (after a label pass turned the \\begin into the
print's run-in label), in both editions of a volume; each removal is logged.
usage: python -I fix_orphan_ends.py VOL ENV [--apply]"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import files  # noqa: E402

vol, env = sys.argv[1], sys.argv[2]
APPLY = "--apply" in sys.argv
TOK = re.compile(r"\\begin\{" + re.escape(env) + r"\}|\\end\{" + re.escape(env) + r"\}")
for edition, log in (("diplomatic", f"FIXLOG_{vol}.jsonl"), ("current", f"FIXLOG_{vol}_CURRENT.jsonl")):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        stack, orphans = [], []
        for m in TOK.finditer(t):
            if m.group(0).startswith("\\begin"):
                stack.append(m)
            elif stack:
                stack.pop()
            else:
                orphans.append(m)
        print(edition, f.name, "orphan \\end lines:", [t.count("\n", 0, m.start()) + 1 for m in orphans])
        if not APPLY or not orphans:
            continue
        for m in reversed(orphans):
            ls = t.rfind("\n", 0, m.start()) + 1
            le = t.find("\n", m.end())
            le = len(t) if le < 0 else le
            if t[ls:m.start()].strip() == "" and t[m.end():le].strip() == "":
                t = t[:ls] + t[le + 1:]
            else:
                t = t[:m.start()] + t[m.end():]
        f.write_text(t, encoding="utf-8", newline="")
        with open(pathlib.Path(__file__).parent / log, "a", encoding="utf-8") as g:
            for m in orphans:
                g.write(json.dumps({"vol": vol, "file": f.name, "page": None, "old": "\\end{" + env + "}", "new": "",
                                    "kind": "proof label", "source": "orphan end after a label fix"},
                                   ensure_ascii=False) + "\n")
