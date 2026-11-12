"""Read-only simulation of move_marker.py for volume 5 (both layers); prints the text around each moved marker."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = r'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
moves = [
    (128, "La différentielle", False),
    (129, "\\begin{equation}\n\\tag{6.8.7}", True),
]
for edition in ('diplomatic', 'current'):
    t = open(base + edition + '/s5.tex', encoding='utf-8').read()
    for folio, anchor, before in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        # count occurrences of the anchor in the search range (for uniqueness of the hit)
        rng = t2[:m.start()] if before else t2[m.start():]
        print('==', edition, 'folio', folio, 'anchor hits in search range:', rng.count(anchor), 'k=', k)
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        t = t2
        m2 = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio))
        print(repr(t[m2.start() - 160:m2.end() + 120]))
