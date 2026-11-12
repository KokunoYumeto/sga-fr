"""In-memory simulation of move_marker.py for folios 249 and 251 on both layers (writes nothing)."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
MARK = re.compile(r'^%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%$', re.M)
root = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/'

def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == '\n' else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, None
    ls = t2.rfind('\n', 0, k) + 1
    if t2[ls:k].strip() == '':
        t2 = t2[:ls] + line + '\n' + t2[ls:]
    else:
        t2 = t2[:k] + '\n' + line + '\n' + t2[k:]
    return t2, k

for layer in ('diplomatic', 'current'):
    t = open(root + layer + '/main.tex', encoding='utf-8').read()
    t, k = move(t, 249, BS + '((S=' + BS + 'Spec(A))' + BS + ')', False)
    t, k2 = move(t, 251, "d'une", True)
    for folio in (249, 251):
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio))
        s = t.rfind('\n', 0, m.start() - 2)
        s = t.rfind('\n', 0, s)
        e = t.find('\n', m.end() + 1)
        e = t.find('\n', e + 1)
        print('==', layer, folio)
        print(t[s + 1:e][-700:] if len(t[s + 1:e]) > 700 else t[s + 1:e])
        print()
