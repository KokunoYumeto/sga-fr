"""A line that ends in an elided word (l', d', qu', jusqu' ...) followed by a line break prints a space after the
apostrophe ("L' anneau"). End such lines with % so that the next word follows at once (also across a page-marker line,
which is a comment). Both editions; each change is logged.
usage: python -I fix_elision_breaks.py VOL [--apply]"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import files  # noqa: E402

vol = sys.argv[1]
APPLY = "--apply" in sys.argv
# an elided word at the end of a line (not a prime in math: the letter must start a word, outside $...$ is not checked
# here, so a math prime is excluded by requiring a space, a line start or an opening bracket before the word)
END = re.compile(r"(?:(?<=\s)|(?<=^)|(?<=[(«~]))(?:[LlDdNnSsJjCcMmTt]|[Qq]u|[Jj]usqu|[Ll]orsqu|[Pp]uisqu|[Qq]uoiqu)['’]$")
for edition, log in (("diplomatic", f"FIXLOG_{vol}.jsonl"), ("current", f"FIXLOG_{vol}_CURRENT.jsonl")):
    for f in files(vol, edition):
        lines = f.read_text(encoding="utf-8").split("\n")
        hits = []
        for i, line in enumerate(lines[:-1]):
            if END.search(line) and not line.lstrip().startswith("%"):
                j = i + 1
                while j < len(lines) and lines[j].startswith("%%%%%%%%%%  scan idx"):
                    j += 1
                nxt = lines[j] if j < len(lines) else ""
                if nxt[:1].isalpha() or nxt[:1] in "\\$":
                    hits.append(i)
        print(edition, f.name, len(hits), "line-final elisions", [h + 1 for h in hits[:12]], "..." if len(hits) > 12 else "")
        if APPLY and hits:
            for i in hits:
                lines[i] = lines[i] + "%"
            f.write_text("\n".join(lines), encoding="utf-8", newline="")
            with open(pathlib.Path(__file__).parent / log, "a", encoding="utf-8") as g:
                for i in hits:
                    g.write(json.dumps({"vol": vol, "file": f.name, "page": None, "old": "elided word + line break",
                                        "new": "elided word + % (no space in the output)", "kind": "spacing",
                                        "source": "global (checker of SGA 5 batch 046-050)"}, ensure_ascii=False) + "\n")
