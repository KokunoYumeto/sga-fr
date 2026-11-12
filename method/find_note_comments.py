"""List editorial note comments that stand after text on a line (% ... FIX ..., restauré, dpi, a date), with what follows
the note, so that a note which swallows the rest of its line (the text after it is lost in the output) can be seen.
usage: python -I find_note_comments.py VOL [VOL ...]"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import files  # noqa: E402

NOTE = re.compile(r"(?<!\\)%(?!%%%%%%%%%)(.*(FIX|restaur|dpi|confirm|\d{4}-\d{2}-\d{2}).*)$")
for vol in sys.argv[1:]:
    for f in files(vol, "diplomatic"):
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            m = NOTE.search(line)
            if not m or not line[:m.start()].strip():
                continue
            note = m.group(1)
            # what follows the last date or FIX number in the note
            ends = [x.end() for x in re.finditer(r"\d{4}-\d{2}-\d{2}\.?|FIX ?#?\d+\.?|\)\.", note)]
            tail = note[ends[-1]:].strip() if ends else note.strip()
            print(f"{vol} {f.name}:{i}: ...{line[max(0, m.start() - 30):m.start()]!r} %{note[:70]!r} || after: {tail[:90]!r}")
