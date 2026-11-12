"""Findings of SGA 5 pp. 476-480: build the JSON, check every fix's old (exactly once in its page file, in order,
and in the live diplomatic and current page regions), and simulate the four marker moves in memory (no file but the
findings JSON is written)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
S5 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
OUT = RUN / "findings_476_480.json"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = "\n"


def page_file(p):
    if p == 475:
        return RUN / "b471_475" / "page_475.tex"
    return RUN / "b476_480" / f"page_{p}.tex"


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 476 (and its first line, now in page_475.tex)
add(476, "beginning of the page",
    r"p. 476 begins 'φ = h'' et φ_0 = h'_{ν-1} ; nous obtenons l'existence de'; p. 475 ends 'Appliquons alors le deuxième lemme avec L = K'_ν ,'",
    r"page_475.tex ends '... lemme avec $L=K'_\nu$, $\varphi=h''_\nu$ et $\varphi_0=h'_{\nu-1}$;'; page_476.tex begins 'nous obtenons'",
    "marker", "high", None,
    r"Page 476 really begins at '$\varphi=h''_\nu$ et $\varphi_0=h'_{\nu-1}$;', the last line of page_475.tex. Exact fix: "
    r"python -I move_marker.py 5 476 '$\varphi=h' --before (bash single quotes: the anchor contains $ and a backslash; "
    r"the anchor matches before and after the h'' misprint fix filed under p. 475; simulated in memory on both layers: "
    r"'... deuxième lemme avec $L=K'_\nu$, ' / marker / '$\varphi=h''_\nu$ et $\varphi_0=h'_{\nu-1}$;' / 'nous obtenons "
    r"l'existence de ...'). Text not moved.")

add(475, "p. 476, line 1 (text under the folio-475 marker until the folio-476 marker is moved)",
    r"φ = h''  (no index ν; the next formula has it: φ_0 = h'_{ν-1})",
    r"$\varphi=h''_\nu$",
    "misprint_in_print", "high",
    {"old": r"$\varphi=h''_\nu$", "new": r"$\varphi=h''$"},
    r"Printed on p. 476. The print drops the index of h''_ν (p. 475: 'endomorphisme de complexe h''_ν : K'_ν → K'_ν'); "
    r"no trace of a subscript in the scan. The TeX silently corrects it; the fix restores the printed reading "
    r"(diplomatic layer only). Filed under p. 475 because the text stands in page_475.tex until the folio-476 marker is "
    r"moved (marker item of p. 476): apply before the move; the move's anchor '$\varphi=h' matches before and after "
    r"this edit.",
    corrected=r"$\varphi=h''_\nu$")

add(476, "Lemme 3 (i), line 1",
    "est projecfif",
    "est projecfif",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading (the corrected layer already reads 'projectif').",
    corrected="projectif")

E1_old = r"\item Soient $P$ et $Q$ des $A$-modules. Si $P$ est"
E1_new = r"\item \emph{Soient $P$ et $Q$ des $A$-modules}. \emph{Si $P$ est"
E2_old = (r", pour toute application $A_0$-linéaire $f_0:T(P)\to T(Q)$ il existe une application $A$-linéaire "
          r"$f:P\to Q$ telle que $T(f)")
E2_new = (r"}, \emph{pour toute application $A_0$-linéaire} $f_0:T(P)\to T(Q)$ \emph{il existe une application "
          r"$A$-linéaire} $f:P\to Q$ \emph{telle que} $T(f)")
UNDERLINE_XV = (r"The print underlines the statement word group by word group (letters and formulas not underlined); "
                r"Exposé XV's TeX has no underline markup. \emph is the file's command for underlining (Exposé XII "
                r"statements, XV's two \emph). ")
add(476, "Lemme 3 (i): 'Soient ... Si P est projecfif'",
    r"Soient P et Q des A-modules. Si P est projecfif,  (underlined: Soient / et / des / modules / Si / est projecfif)",
    r"\item Soient $P$ et $Q$ des $A$-modules. Si $P$ est projecfif, (no underline markup)",
    "underline", "high", {"old": E1_old, "new": E1_new},
    UNDERLINE_XV + r"This edit opens the group of 'Si $P$ est projecfif' and the next edit closes it: APPLY THE TWO "
    r"TOGETHER. The olds leave out the misprint 'projecfif', so both apply unchanged to the corrected layer "
    r"('projectif').")
add(476, "Lemme 3 (i): 'pour toute application ... telle que'",
    r"pour toute application A_0-linéaire f_0 : T(P) → T(Q) il existe une application A-linéaire f : P → Q telle que T(f) = f_0 .  (underlined: pour toute application / linéaire / il existe / une application / linéaire / telle que)",
    r", pour toute application $A_0$-linéaire $f_0:T(P)\to T(Q)$ il existe une application $A$-linéaire $f:P\to Q$ telle que $T(f)=f_0$. (no underline markup)",
    "underline", "high", {"old": E2_old, "new": E2_new},
    r"Closes the \emph group opened by the previous edit (after 'projecfif') and marks the remaining underlined runs: "
    r"APPLY TOGETHER WITH THE PREVIOUS EDIT.")
add(476, "Lemme 3 (ii), first two sentences",
    r"Supposons l'idéal I nilpotent. Pour tout A_0-module projectif P_0 il existe un A-module projectif P tel que T(P) ≃ P_0.  (underlined: Supposons l'idéal / nilpotent / Pour tout / module projectif / il existe un / module projectif / tel que)",
    r"\item Supposons l'idéal $I$ nilpotent. Pour tout $A_0$-module projectif $P_0$ il existe un $A$-module projectif $P$ tel que $T(P)\simeq P_0$. (no underline markup)",
    "underline", "high",
    {"old": r"\item Supposons l'idéal $I$ nilpotent. Pour tout $A_0$-module projectif $P_0$ il existe un $A$-module projectif $P$ tel que $T(P)",
     "new": r"\item \emph{Supposons l'idéal $I$ nilpotent}. \emph{Pour tout $A_0$-module projectif $P_0$ il existe un $A$-module projectif $P$ tel que} $T(P)"},
    UNDERLINE_XV + "Full stops left outside the groups.")
add(476, "Lemme 3 (ii), last sentence",
    r"Si de plus P' est un A-module plat tel que T(P') ≃ P_0 , alors on a P' ≃ P .  (underlined: Si de plus / est un / module plat tel que / alors / on a)",
    r"Si de plus $P'$ est un $A$-module plat tel que $T(P')\simeq P_0$, alors on a $P'\simeq P$. (no underline markup)",
    "underline", "high",
    {"old": r"Si de plus $P'$ est un $A$-module plat tel que $T(P')\simeq P_0$, alors on a $P'\simeq P$.",
     "new": r"\emph{Si de plus $P'$ est un $A$-module plat tel que} $T(P')\simeq P_0$, \emph{alors on a} $P'\simeq P$."},
    "As the rest of Lemme 3.")
add(476, "proof of (i), 'f_0∘u_P = u_Q∘f où f est'",
    "f_o∘u_P = u_Q∘f  où  f  est",
    r"$f_0\circ u_P=u_Q\circ f$, où $f$ est",
    "punctuation", "high",
    {"old": r"u_Q\circ f$, où", "new": r"u_Q\circ f$ où"},
    "The TeX adds a comma the print does not have.")
add(476, "last line: 'en introduisant un A_0-' / p. 477 'module libre'",
    r"un A_0-  (end of p. 476) | module libre (start of p. 477): 'A_0-module' divided at the page break",
    r"en introduisant un $A_0$-  (line end before the folio-477 marker) -> output 'A_0- module'",
    "other", "high",
    {"old": r"en introduisant un $A_0$-", "new": r"en introduisant un $A_0$-%"},
    r"The folio-477 marker is in the right place, but the line before it ends with '$A_0$-' and the marker line is a "
    r"comment, so the output reads 'A_0- module' with a space. The % joins the halves, as marker_split_word.py does; "
    r"the marker line is not touched.")

# ---------------------------------------------------------------- p. 477
add(477, "Bourbaki reference",
    "Alg. Comm., Chap. III, §4, n°6, lemme 2",
    r"Alg. comm., chap.~III, §4, n\textsuperscript{o}~6, lemme 2",
    "word", "high",
    {"old": r"Alg. comm., chap.~III", "new": r"Alg. Comm., Chap.~III"},
    "Capitals C as printed ('Comm.', 'Chap.').")
add(477, "Corollaire, first sentence and first clause",
    r"Supposons l'idéal I nilpotent. Pour tout complexe acyclique et borné à droite N_0 de A_0-modules projectifs,  (underlined: Supposons l'idéal / nilpotent / Pour tout complexe acyclique et borné à droite / de / modules projectifs)",
    r"Supposons l'idéal $I$ nilpotent. Pour tout complexe acyclique et borné à droite $N_0$ de $A_0$-modules projectifs, (no underline markup)",
    "underline", "high",
    {"old": r"Supposons l'idéal $I$ nilpotent. Pour tout complexe acyclique et borné à droite $N_0$ de $A_0$-modules projectifs,",
     "new": r"\emph{Supposons l'idéal $I$ nilpotent}. \emph{Pour tout complexe acyclique et borné à droite $N_0$ de $A_0$-modules projectifs},"},
    UNDERLINE_XV + "Punctuation left outside the groups.")
add(477, "Corollaire, second clause",
    r"il existe un complexe acyclique borné à droite N de A-modules projectifs tel que T(N) ≃ N_0 .  (underlined: il existe / un complexe acyclique borné à droite / de / modules projectifs / tel que)",
    r"il existe un complexe acyclique borné à droite $N$ de $A$-modules projectifs tel que $T(N)\simeq N_0$. (no underline markup)",
    "underline", "high",
    {"old": r"il existe un complexe acyclique borné à droite $N$ de $A$-modules projectifs tel que $T(N)",
     "new": r"\emph{il existe un complexe acyclique borné à droite $N$ de $A$-modules projectifs tel que} $T(N)"},
    "As the first part of the Corollaire.")
add(477, "display after 'suites exactes courtes'",
    "0 --> Z^i_0 --> N^i_0 --> Z^{i+1}_0 --> 0   (nothing after the last 0)",
    r"0\longrightarrow Z_0^i\longrightarrow N_0^i\longrightarrow Z_0^{i+1}\longrightarrow0,",
    "punctuation", "high",
    {"old": r"\longrightarrow0," + NL + r"\]", "new": r"\longrightarrow0" + NL + r"\]"},
    "The TeX adds a comma at the end of the display.")

# ---------------------------------------------------------------- p. 478
add(478, "beginning of the page",
    "p. 478 begins 'ces suites exactes de proche en proche'; p. 477 ends 'On relève N_0 en relevant toutes'",
    r"page_477.tex ends 'en relevant toutes ces'; page_478.tex begins 'suites exactes'",
    "marker", "high", None,
    r"Page 478 really begins at 'ces', the last word of page_477.tex. Exact fix: python -I move_marker.py 5 478 'ces' "
    r"--before (simulated in memory on both layers: '... On relève $N_0$ en relevant toutes ' / marker / 'ces' / "
    r"'suites exactes de proche en proche, ...'). Text not moved.")
add(478, "'puis Q_0 → R_0 en une application A-linéaire : Q → R'",
    "en une application A-linéaire : Q --> R par le lemme 3(i)",
    r"en une application $A$-linéaire $Q\to R$ par le lemme 3(i)",
    "punctuation", "high",
    {"old": r"$A$-linéaire $Q\to R$", "new": r"$A$-linéaire: $Q\to R$"},
    "The print has a colon before Q → R (no letter for the map); the TeX drops it.")
add(478, "'on pose P = Ker(Q → R)'",
    "P = Ker(Q --> R)",
    r"$P=\ker(Q\to R)$",
    "word", "high",
    {"old": r"\ker(Q\to R)", "new": r"\Ker(Q\to R)"},
    r"Capital K as printed; \Ker is the file's \operatorname{Ker}.")
add(478, "Démonstration du lemme 2: 'est homotope à φ_0'",
    "homotope (underlined) à φ_0",
    r"est homotope à $\varphi_0$",
    "underline", "high",
    {"old": r"homotope à $\varphi_0$", "new": r"\emph{homotope} à $\varphi_0$"},
    r"The word is underlined in the print; \emph as the file's command for underlining in Exposé XV.")
add(478, "Démonstration du lemme 1, line 1",
    "(quite à remplacer L par un complexe quasi-isomorphe)",
    "(quite à remplacer $L$ par un complexe",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading (the corrected layer already reads 'quitte').",
    corrected="quitte")

# ---------------------------------------------------------------- p. 479
add(479, "beginning of the page",
    "p. 479 begins 'est projectif en chaque degré'; p. 478 ends 'donc aussi T(L),'",
    r"page_478.tex ends 'donc aussi $T(L)$, est'; page_479.tex begins 'projectif en chaque degré'",
    "marker", "high", None,
    r"Page 479 really begins at 'est', the last word of page_478.tex. Exact fix: python -I move_marker.py 5 479 'est' "
    r"--before (simulated in memory on both layers: '... supposer que le complexe $L$, donc aussi $T(L)$, ' / marker / "
    r"'est' / 'projectif en chaque degré, ...'). Text not moved.")
add(479, "'remplacer L par L ⊕ N qui lui est quasi-isomorphe'",
    "remplacer L par L ⊕ N | qui lui est quasi-isomorphe  (no comma)",
    r"remplacer $L$ par $L\oplus N$, qui lui est",
    "punctuation", "high",
    {"old": r"$L\oplus N$, qui", "new": r"$L\oplus N$ qui"},
    "The TeX adds a comma the print does not have.")
add(479, "'car la suite exacte : 0 → R_0 → T(L) → M → 0 est scindée'",
    "car la suite exacte :  0 --> R_0 --> T(L) --> M --> 0  est",
    r"car la suite exacte \[ 0\longrightarrow R_0\longrightarrow T(L)\longrightarrow M\longrightarrow0 \] est",
    "punctuation", "high",
    {"old": r"car la suite exacte" + NL + r"\[", "new": r"car la suite exacte:" + NL + r"\["},
    "The print has a colon before the sequence; the TeX drops it.")
add(479, "display 'f_0 = h_0 d_{R_0} + d_{T(L)} h_0 où'",
    "f_0 = h_0d_{R_0}+d_{T(L)}h_0  où  h_0 = (h^i_0)_i  (no comma)",
    r"f_0=h_0d_{R_0}+d_{T(L)}h_0,",
    "punctuation", "high",
    {"old": r"d_{T(L)}h_0," + NL + r"\]", "new": r"d_{T(L)}h_0" + NL + r"\]"},
    "The TeX adds a comma at the end of the display.")

# ---------------------------------------------------------------- p. 480
add(480, "beginning of the page",
    "p. 480 begins 'et on voit que f = hd_R+d_Lh'; p. 479 ends 'avec h^i : R^i --> L^{i-1},'",
    r"page_479.tex ends 'avec $h^i:R^i\to L^{i-1}$, et on'; page_480.tex begins 'voit que'",
    "marker", "high", None,
    r"Page 480 really begins at 'et on', the end of page_479.tex. Exact fix: python -I move_marker.py 5 480 'et on' "
    r"--before (simulated in memory on both layers: '... avec $h^i:R^i\to L^{i-1}$, ' / marker / 'et on' / 'voit que' "
    r"...). Text not moved.")
add(480, "'Coker f = L''",
    "Coker f = L'",
    r"$\coker f=L'$",
    "word", "high",
    {"old": r"\coker f=L'", "new": r"\Coker f=L'"},
    r"The print has 'Coker'; \coker prints 'coker' in this file (the first \providecommand{\coker}{\operatorname{coker}} "
    r"wins over the later 'Coker' one). \Coker is the file's \operatorname{Coker}. These are the only uses of \coker "
    r"in s5.tex.")
add(480, "'T(L') ≃ Coker T(f) = Coker f_0 ≃ M'",
    "Coker T(f) = Coker f_0",
    r"\coker T(f)=\coker f_0",
    "word", "high",
    {"old": r"\coker T(f)=\coker f_0", "new": r"\Coker T(f)=\Coker f_0"},
    "As the previous item (twice).")

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for d in F:
    p = d["page"]
    texts.setdefault(p, page_file(p).read_text(encoding="utf-8"))
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    for ch in fx["old"] + fx["new"]:
        if ord(ch) < 32 and ch != "\n":
            print("CONTROL CHAR in", d["page"], repr(fx["old"][:40]))
            ok = False
    n = page_file(d["page"]).read_text(encoding="utf-8").count(fx["old"])
    if n != 1:
        print("NOT UNIQUE in original page file:", d["page"], n, repr(fx["old"]))
        ok = False
    if MARK.search(fx["old"]) or MARK.search(fx["new"]):
        print("touches a marker:", d["page"])
        ok = False
# apply in order (diplomatic page files)
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    t = texts[d["page"]]
    n = t.count(fx["old"])
    if n != 1:
        print("NOT UNIQUE when applied in order:", d["page"], n, repr(fx["old"]))
        ok = False
    texts[d["page"]] = t.replace(fx["old"], fx["new"], 1)
for p, t in texts.items():
    if t.count("{") != t.count("}"):
        print("BRACES UNBALANCED after the edits on page", p)
        ok = False
print("page-file checks:", "OK" if ok else "FAILED")


def regions(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


for layer in ("diplomatic", "current"):
    t = (S5 / layer / "s5.tex").read_text(encoding="utf-8")
    rg = regions(t)
    for d in F:
        fx = d["fix"]
        if not fx or (layer == "current" and d["kind"] == "misprint_in_print"):
            continue
        a, b = rg[d["page"]]
        n = t[a:b].count(fx["old"])
        if n != 1:
            print(layer, "live region of page", d["page"], "count", n, repr(fx["old"][:60]))


def move(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for layer in ("diplomatic", "current"):
    for fix_first in ((False, True) if layer == "diplomatic" else (False,)):
        t = (S5 / layer / "s5.tex").read_text(encoding="utf-8")
        if fix_first:
            old, new = r"$\varphi=h''_\nu$", r"$\varphi=h''$"
            assert t.count(old) == 1, t.count(old)
            t = t.replace(old, new, 1)
        for folio, anchor in ((476, r"$\varphi=h"), (478, "ces"), (479, "est"), (480, "et on")):
            t = move(t, folio, anchor)
            m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
            before = t[:m.start()].rstrip("\n").rsplit("\n", 1)[-1][-70:]
            after = t[m.end():].lstrip("\n").split("\n", 2)
            print(layer, "h''-fix first" if fix_first else "", folio, "|", repr(before), "/ MARK /", repr(after[0][:70]),
                  "/", repr(after[1][:50]))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT, len(F), "findings")
