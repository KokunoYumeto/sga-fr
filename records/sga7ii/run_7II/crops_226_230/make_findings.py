import json
import os
import sys

# Backslashes are written as the placeholder '§' in this file and restored at run time.
BS = chr(92)


def S(s):
    return None if s is None else s.replace('§', BS)


FOLDER = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b226_230'
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_226_230.json'

MP = 'misprint_in_print'
KEEP = 'The TeX keeps the printed reading.'

raw = [
    # ---------------- page 226 ----------------
    dict(page=226,
         where="Exemple 3.4, 'φ : X ⟶ P̌^r s'exprime, en coordonnés homogènes, par'",
         scan="coordonnés homogènes",
         tex="en coordonnés homogènes", kind=MP, confidence="high", fix=None,
         corrected="en coordonnées homogènes",
         note="Agreement slip (les coordonnées), as on pp. 216 and 222; again on p. 229. " + KEEP),
    dict(page=226,
         where="after (3.4.3), 'de sorte que X̌ est reduit à un point si p = 0'",
         scan="reduit: no accent on the first e (checked at 2x)",
         tex="est reduit à un point", kind=MP, confidence="high", fix=None,
         corrected="est réduit à un point",
         note="Missing acute accent. " + KEEP),
    # ---------------- page 227 ----------------
    dict(page=227,
         where="Proposition 3.5, 'Plus précisement, les trois ouverts suivants'",
         scan="précisement: acute on the first e only (checked at 2x)",
         tex="§underline{Plus précisement, les trois}", kind=MP, confidence="high", fix=None,
         corrected="§underline{Plus précisément, les trois}",
         note="Missing second acute accent. " + KEEP),
    dict(page=227,
         where="Proposition 3.5, 'les trois ouverts suivants de X sont identiques:'",
         scan="X with no check accent (no ink above the letter even at a light threshold)",
         tex="§underline{ouverts suivants de} $X$", kind=MP, confidence="medium", fix=None,
         corrected="§underline{ouverts suivants de} $§check{X}$",
         note="The three open sets a), b), c) are all open subsets of X̌ ('de X̌' in each item), so the statement needs X̌. "
              "Other checks on the page are fully typed; a check lost entirely to faint type cannot be fully excluded "
              "(half-printed checks occur on p. 228). " + KEEP),
    dict(page=227,
         where="Proposition 3.5, 'sont identiques:'",
         scan="underline stops before the colon",
         tex="§underline{sont identiques:}", kind="underline", confidence="high",
         fix={"old": "§underline{sont identiques:}", "new": "§underline{sont identiques}:"},
         note="Colon after an underlined phrase placed inside the underline (same pattern as the globally handled comma/full stop)."),
    dict(page=227,
         where="Corollaire 3.5.0, 'conditions est satisfaite: a)'",
         scan="underline stops before the colon",
         tex="§underline{conditions est satisfaite:}", kind="underline", confidence="high",
         fix={"old": "§underline{conditions est satisfaite:}", "new": "§underline{conditions est satisfaite}:"},
         note="As above."),
    # ---------------- page 228 ----------------
    dict(page=228,
         where="after (3.5.1.1), 'par la méthode naive de construire un inverse'",
         scan="naive: plain dotted i, no diaeresis or circumflex (checked at 2x)",
         tex="la méthode naive", kind=MP, confidence="medium", fix=None,
         corrected="la méthode naïve",
         note="Missing diaeresis; elsewhere the typescript writes î for ï. " + KEEP),
    dict(page=228,
         where="last line, 'Appliquons ceci a l'hypersurface X̌ dans P̌^r'",
         scan="a: no grave accent (checked at 2x)",
         tex="ceci a l'hypersurface", kind=MP, confidence="high", fix=None,
         corrected="ceci à l'hypersurface",
         note="Preposition à without its accent. " + KEEP),
    # ---------------- page 229 ----------------
    dict(page=229,
         where="after (3.5.3), 'Soit alors (x_o, H_o) un point fermé φ^{-1}(V') ;'",
         scan="un point fermé φ^{-1}(V') (no 'de'; checked at 2x)",
         tex="un point fermé $§varphi^{-1}(V')$", kind=MP, confidence="high", fix=None,
         corrected="un point fermé de $§varphi^{-1}(V')$",
         note="Missing word 'de' (compare 'un point fermé de P(N)' in Lemme 3.6). " + KEEP),
    dict(page=229,
         where="Lemme 3.6, 'un point fermé de P(N) , et désignons par'",
         scan="comma not underlined; only 'et' underlined",
         tex="§underline{, et}", kind="underline", confidence="high",
         fix={"old": "§underline{, et}", "new": ", §underline{et}"},
         note="The comma before the underlined 'et' sits outside the underline in the print."),
    dict(page=229,
         where="Démonstration of 3.6, 'Choisissons des coordonnés homogènes X_o,...,X_r'",
         scan="coordonnés homogènes",
         tex="des coordonnés homogènes", kind=MP, confidence="high", fix=None,
         corrected="des coordonnées homogènes",
         note="Agreement slip, as on p. 226. " + KEEP),
    # ---------------- page 230 ----------------
    dict(page=230,
         where="before (3.6.4), 'l'hyperplan à coefficients dans k[ε]/(ε²) d'équation (c.f. 3.1.1)'",
         scan="k[ε]/(ε²): epsilon inside the brackets (checked at 2x)",
         tex="$k[e]/(§epsilon^2)$", kind="symbol", confidence="high",
         fix={"old": "k[e]", "new": "k[§epsilon]"},
         note="The TeX has a Latin e for the print's ε, which the first line of the page transcribes correctly."),
]

findings = []
ok = True
cache = {}
for d in raw:
    f = {}
    for k in ('page', 'where', 'scan', 'tex', 'kind', 'confidence'):
        f[k] = S(d[k]) if isinstance(d[k], str) else d[k]
    fx = d['fix']
    f['fix'] = None if fx is None else {'old': S(fx['old']), 'new': S(fx['new'])}
    if d['kind'] == MP:
        f['corrected'] = S(d['corrected'])
    f['note'] = S(d['note'])
    findings.append(f)

    p = d['page']
    if p not in cache:
        with open(os.path.join(FOLDER, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
            cache[p] = fh.read()
    txt = cache[p]
    # every fix 'old' must occur exactly once and must not touch a marker line
    if f['fix'] is not None:
        n = txt.count(f['fix']['old'])
        if n != 1:
            ok = False
            print('FIX OLD COUNT', p, n, repr(f['fix']['old']))
        if '%%%%%%%%%%' in f['fix']['old']:
            ok = False
            print('MARKER IN OLD', p)
    # the quoted TeX reading of a misprint should be locatable too
    n = txt.count(f['tex'])
    if n != 1:
        print('NOTE: tex field count', p, n, repr(f['tex']))

if not ok:
    sys.exit(1)

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

from collections import Counter
c = Counter((f['page'], f['kind'] == MP) for f in findings)
for p in sorted({f['page'] for f in findings} | {226, 227, 228, 229, 230}):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
print('written', OUT, len(findings))
