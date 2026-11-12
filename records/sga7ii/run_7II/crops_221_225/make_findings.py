import json
import os
import sys

# Backslashes are written as the placeholder '§' in this file and restored at run time.
BS = chr(92)


def S(s):
    return None if s is None else s.replace('§', BS)


FOLDER = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b221_225'
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_221_225.json'

MP = 'misprint_in_print'
KEEP = 'The TeX keeps the printed reading.'

raw = [
    # ---------------- page 221 ----------------
    dict(page=221,
         where="after the first diagram, 'Les droites la-dedans passant par un point de F y forment un fermé'",
         scan="la-dedans: no accent on the a (checked at 2.5x)",
         tex="la-dedans", kind=MP, confidence="high", fix=None,
         corrected="là-dedans",
         note="Spelling slip; the typescript has the accented à on the same page ('Il reste à prouver'). " + KEEP),
    dict(page=221,
         where="Proposition 3.3, 'le sous-ensemble de P(N) formé des points (x, H) tel que x soit une singularité quadratique'",
         scan="tel que (underlined)",
         tex="§underline{tel que}", kind=MP, confidence="low", fix=None,
         corrected="§underline{tels que}",
         note="Agreement with 'des points (x, H)', as in Proposition 3.2 ('des hyperplans H tel que', p. 218). " + KEEP),
    # ---------------- page 222 ----------------
    dict(page=222,
         where="proof of 3.3, 'indépendantes du choix particulier des coordonnés, on peut les expliciter'",
         scan="coordonnés,",
         tex="particulier des coordonnés", kind=MP, confidence="high", fix=None,
         corrected="particulier des coordonnées",
         note="Agreement slip (les coordonnées; 'choisies' follows in the same sentence), as on p. 216. " + KEEP),
    dict(page=222,
         where="same sentence, 'à l'aide de coordonnés choisies d'une façon très particulière'",
         scan="coordonnés choisies",
         tex="coordonnés choisies", kind=MP, confidence="high", fix=None,
         corrected="coordonnées choisies",
         note="Agreement slip. " + KEEP),
    dict(page=222,
         where="'on peut choisir des coordonnés homogènes X_o,...,X_r dans P^r'",
         scan="coordonnés homogènes",
         tex="coordonnés homogènes", kind=MP, confidence="high", fix=None,
         corrected="coordonnées homogènes",
         note="Agreement slip. " + KEEP),
    dict(page=222,
         where="3.3.3, 'l'hyperplan H provient, via (3.1.1) de g_{n-r}'",
         scan="g_{n-r} (checked at 3x)",
         tex="g_{n-r}", kind=MP, confidence="high", fix=None,
         corrected="g_{r-n}",
         note="The generators are g_1,...,g_{r-n} (3.3.2) with n < r, so n-r is no index; (3.3.5) and (3.3.9) take "
              "g_{r-n} as the generator giving H, and (3.3.10)-(3.3.16) work with h_{r-n}. " + KEEP),
    dict(page=222,
         where="(3.3.4), the trivialization '(λ_1,...,λ_{r-n}) ↦ Σ_1^{n-r} λ_i g_{n+i}'",
         scan="(λ_1,...,λ_{r-n}) ↦ Σ_1^{n-r} λ_i g_{n+i}: small lambdas, upper limit n-r, index n+i on g (checked at 3x)",
         tex="(§lambda_1,§dots,§lambda_{r-n}) §longmapsto §sum_1^{n-r} §lambda_i g_{n+i}",
         kind=MP, confidence="medium", fix=None,
         corrected="(§Lambda_1,§dots,§Lambda_{r-n}) §longmapsto §sum_1^{r-n} §Lambda_i g_i",
         note="Three slips in one formula. The upper limit n-r for r-n is certain (the tuple has r-n entries, n < r). "
              "g_{n+i} for g_i: the generators are g_1,...,g_{r-n}, and (3.3.5) writes Σ λ_i g_i. Small λ for the "
              "homogeneous coordinates is the least certain: the line after (3.3.5) sets λ_i = Λ_i/Λ_{r-n}, and Λ "
              "occurs nowhere else; without that part read Σ_1^{r-n} λ_i g_i. " + KEEP),
    # ---------------- page 223 ----------------
    dict(page=223,
         where="(3.3.5), right side '(v,(g_{r-n}+ Σ_1^{n-r-1} λ_i g_i)'",
         scan="upper limit n-r-1 (checked at 2.5x)",
         tex="§sum_1^{n-r-1}", kind=MP, confidence="high", fix=None,
         corrected="§sum_1^{r-n-1}",
         note="The coordinates are λ_1,...,λ_{r-n-1} (left side of (3.3.5); (3.3.9) and (3.3.10) have the limit r-n-1). " + KEEP),
    dict(page=223,
         where="(3.3.5), right side '(v,(g_{r-n}+ Σ λ_i g_i)∈ P(I/I^2)|V'",
         scan="two parentheses opened, one closed after g_i (checked at 2.5x)",
         tex="§lambda_i g_i) §in", kind=MP, confidence="high", fix=None,
         corrected="§lambda_i g_i)) §in",
         note="The parenthesis opened before v is not closed. " + KEEP),
    dict(page=223,
         where="after (3.3.5), '(où l'on pose λ_i = Λ_i/Λ_{n-r} ).'",
         scan="Λ_i / Λ_{n-r}: the typed capital Lambda (inverted V, heavier right leg, no crossbar), distinct from the small λ on the left (checked at 5x)",
         tex="§wedge_i / §wedge_{n-r}", kind="symbol", confidence="high",
         fix={"old": "§wedge_i / §wedge_{n-r}", "new": "§Lambda_i / §Lambda_{n-r}"},
         note="Capital Lambda: the homogeneous coordinates of the fibre of P(I/I^2), whose quotients are the λ_i of "
              "(3.3.5); a wedge has no meaning here. Apply before the next finding, which concerns the same expression."),
    dict(page=223,
         where="same line, 'λ_i = Λ_i/Λ_{n-r}'",
         scan="Λ_{n-r} (checked at 5x)",
         tex="§Lambda_{n-r} (after the symbol fix above; at present §wedge_{n-r})", kind=MP, confidence="high", fix=None,
         corrected="§Lambda_{r-n}",
         note="The affine coordinates λ_1,...,λ_{r-n-1} of (3.3.5) come from dividing by the coordinate of g_{r-n}; "
              "n-r is no index (n < r). After the symbol fix the TeX keeps the printed reading."),
    dict(page=223,
         where="'le complété Ô_{P(Ň),(x,H)} de l'anneau local de P(N) en (x, H)'",
         scan="P(Ň): a check over the N (checked at 2.5x)",
         tex="§mathbb{P}(§check{N})", kind=MP, confidence="medium", fix=None,
         corrected="§mathbb{P}(N)",
         note="The same sentence speaks of the local ring of P(N), and (3.3.8), (3.3.9) and p. 224 write "
              "Ô_{P(N),(x_o,H)}; P(N) is the bundle of lines in Ň (3.1). " + KEEP),
    dict(page=223,
         where="'Exprimons maintenant φ en termes de ces coordonnés'",
         scan="ces coordonnés",
         tex="ces coordonnés", kind=MP, confidence="high", fix=None,
         corrected="ces coordonnées",
         note="Agreement slip. " + KEEP),
    dict(page=223,
         where="(3.3.6), second line 'l'hyperplan d'équation Σ_{i=0}^{n+r} φ_i(x,λ)T_i = 0'",
         scan="upper limit n+r (checked at 2.5x)",
         tex="§sum_{i=0}^{n+r}", kind=MP, confidence="high", fix=None,
         corrected="§sum_{i=0}^{r}",
         note="A hyperplane of P^r has the r+1 coefficients φ_0,...,φ_r: (3.3.8) and (3.3.12) use φ_o, φ_i, "
              "φ_{n+i} (i ≤ r-n) and φ_r. " + KEEP + " The corrected layer has Σ_{i=0}^{r} but leaves out the "
              "middle member '= φ (x_1,...,x_n,λ_1,...,λ_{r-n-1})' of (3.3.6), which the print and the diplomatic TeX have."),
    dict(page=223,
         where="before (3.3.7), 'point qui s'écrit en coordonnés homogènes'",
         scan="coordonnés homogènes",
         tex="coordonnés homogènes", kind=MP, confidence="high", fix=None,
         corrected="coordonnées homogènes",
         note="Agreement slip. " + KEEP),
    dict(page=223,
         where="(3.3.7), '(x) = (1,x_1,...,x_n, h_1(x),...,h_{r-n}(x) ,'",
         scan="the parenthesis opened before 1 is not closed; the comma follows h_{r-n}(x) (checked at 1.8x)",
         tex="h_{r-n}(x) §quad ,", kind=MP, confidence="high", fix=None,
         corrected="h_{r-n}(x)) §quad ,",
         note="Missing closing parenthesis. " + KEEP),
    dict(page=223,
         where="(3.3.9), 'dans Ô_{P(N),(x_o H)}'",
         scan="(x_o H): no comma between the subscript o and H (checked at 3.5x)",
         tex="(x_o H)", kind=MP, confidence="medium", fix=None,
         corrected="(x_o,H)",
         note="As after (3.3.8) on this page and on p. 224: Ô_{P(N),(x_o,H)}. " + KEEP),
    # ---------------- page 224 ----------------
    dict(page=224,
         where="first line, 'Rappellant g_i = x_{n+i} - h_i(x_1,...,x_n)'",
         scan="Rappellant (double l)",
         tex="Rappellant", kind=MP, confidence="high", fix=None,
         corrected="Rappelant",
         note="Spelling slip, as 'Rappellons' on p. 216. " + KEEP),
    dict(page=224,
         where="(3.3.11), 'φ_i(x,λ) = λ_i pour 1 ≤ i ≤ n ,'",
         scan="φ_i(x,λ) = λ_i pour 1 ≤ i ≤ n (checked at 2x)",
         tex="§varphi_i(x,§lambda) = §lambda_i §qquad §mbox{pour} §quad 1 §leq i §leq n",
         kind=MP, confidence="medium", fix=None,
         corrected="§varphi_{n+i}(x,§lambda) = §lambda_i §qquad §mbox{pour} §quad 1 §leq i §leq r-n-1",
         note="(3.3.10) already gives φ_i for 1 ≤ i ≤ n. With g_j = x_{n+j} - h_j, (3.3.9) gives "
              "D_{n+i}(g_{r-n} + Σ λ_j g_j) = λ_i for 1 ≤ i ≤ r-n-1 (and φ_r = 1, (3.3.12)); the matrix (3.3.15) "
              "has the matching identity block of size r-n-1. Both the index and the range are misprinted. " + KEEP),
]

findings = []
for r in raw:
    f = dict(page=r['page'], where=r['where'], scan=r['scan'], tex=S(r['tex']), kind=r['kind'],
             confidence=r['confidence'],
             fix=None if r['fix'] is None else {"old": S(r['fix']['old']), "new": S(r['fix']['new'])})
    if r['kind'] == MP:
        f['corrected'] = S(r['corrected'])
    f['note'] = r['note']
    findings.append(f)

# ---- checks ----
ok = True
pages = {}
for p in sorted({f['page'] for f in findings}):
    with open(os.path.join(FOLDER, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        pages[p] = fh.read()
for f in findings:
    t = pages[f['page']]
    if f['fix'] is not None:
        n = t.count(f['fix']['old'])
        if n != 1:
            ok = False
            print('FIX OLD COUNT', n, f['page'], repr(f['fix']['old']))
        if '%%%%%%%%%%' in f['fix']['old']:
            ok = False
            print('FIX TOUCHES MARKER', f['page'])
    tex = f['tex']
    if ' (after the' in tex:
        continue
    n = t.count(tex)
    if n != 1:
        ok = False
        print('TEX COUNT', n, f['page'], repr(tex))
# the post-fix misprint: check against the page after applying the fix
t223 = pages[223]
for f in findings:
    if f['page'] == 223 and f['fix'] is not None:
        t223 = t223.replace(f['fix']['old'], f['fix']['new'])
post = BS + 'Lambda_{n-r}'
if t223.count(post) != 1:
    ok = False
    print('POST-FIX TEX COUNT', t223.count(post))

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

sys.stdout.reconfigure(encoding='utf-8')
counts = {}
for f in findings:
    c = counts.setdefault(f['page'], [0, 0])
    c[1 if f['kind'] == MP else 0] += 1
print('checks ok' if ok else 'CHECKS FAILED')
print({p: '%d/%d' % tuple(v) for p, v in sorted(counts.items())})
