"""Simulate move_marker.py / marker_split_word.py on both layers in memory (same logic as the scripts, nothing written)."""
import sys

sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)


def move_marker(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


def pull(t, folio, piece):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    if not t[:prev_end].endswith(piece):
        return None
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]


def show(t, folio):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    return repr(t[m.start() - 90:m.start()]) + ' || ' + repr(t[m.end():m.end() + 70])


CMDS = [
    ('move', 306, BS + '((1+X^{(j)}t)', True),
    ('move', 308, 'sa', True),
    ('move', 309, 'la série', True),
    ('pull', 310, BS + '(K' + BS + ')-', None),
    ('move', 311, BS + '(1+X' + BS + ') de', True),
]
for edition in ('diplomatic', 'current'):
    t = files('6', edition)[0].read_text(encoding='utf-8')
    for kind, folio, arg, before in CMDS:
        t2 = move_marker(t, folio, arg, before) if kind == 'move' else pull(t, folio, arg)
        if t2 is None:
            print(edition, folio, 'FAILED')
            continue
        print(edition, folio, kind, repr(arg))
        print('   ', show(t2, folio))
        t = t2
