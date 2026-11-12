import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
F = []
def add(**k): F.append(k)

add(page=401, where="title",
    scan="UNE FORMULE DE CONGRUENCE POUR LA FONCTION ζ, double underline ending under the N of FONCTION; the handwritten ζ is not underlined (checked at 2x)",
    tex=r"\underline{\underline{UNE FORMULE DE CONGRUENCE POUR LA FONCTION $\zeta$}}",
    kind="underline", confidence="high",
    fix={"old": r"LA FONCTION $\zeta$}}", "new": r"LA FONCTION}} $\zeta$"},
    note="")
add(page=401, where="0. Introduction, par. 'Soit X un schéma propre', line 2",
    scan="peut-être réduite modulo p",
    tex=r"peut-être réduite modulo $p$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="peut être réduite",
    note="The adverb 'peut-être' (perhaps) where 'peut être' (can be) is meant. The TeX keeps the printed reading.")
add(page=402, where="first paragraph, last line",
    scan="WARNING-CHEVALLEY [8] (typed hyphen)",
    tex=r"WARNING--CHEVALLEY [8]",
    kind="punctuation", confidence="medium",
    fix={"old": r"WARNING--CHEVALLEY", "new": r"WARNING-CHEVALLEY"},
    note="The TeX's -- gives an en dash; the typescript has its ordinary hyphen. The same en dash for a typed hyphen stands at 413 Euler--Poincaré and 428 Chevalley--Warning (prints checked: hyphen) and 416 Artin--Hasse.")
add(page=402, where="par. 'Une autre méthode', line 2",
    scan="\"coefficient tordus\"",
    tex=r"``coefficient tordus''",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"``coefficients tordus''",
    note="The TeX keeps the printed reading.")
add(page=402, where="heading of section 1",
    scan="1. Un rappel sur les opérations \"p-linéaires\": only 'Un rappel sur les opérations' and 'linéaires' are underlined; the two quotation marks and 'p-' are not (checked at 2x)",
    tex=r"1. \underline{Un rappel sur les opérations ``$p$-linéaires''}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{Un rappel sur les opérations ``$p$-linéaires''}",
         "new": r"\underline{Un rappel sur les opérations} ``$p$-\underline{linéaires}''"},
    note=r"Cf. the file's own '$q$-\underline{linéaire}' after (1.0.1). If block underlines through inner math letters are kept, the minimal change is to move the closing quotation marks out of the underline.")
add(page=402, where="1.0, last sentence",
    scan="Una application",
    tex=r"Una application",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="Une application",
    note="The TeX keeps the printed reading.")
add(page=402, where="line after (1.0.1)",
    scan="s'appelle q-linéaire si elle additive et si elle vérifie",
    tex=r"si elle additive et si elle vérifie",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="si elle est additive",
    note="'est' is missing in the print. The TeX keeps the printed reading.")
add(page=403, where="line before (1.0.7)",
    scan="On définit des k-sous-espace stables par φ",
    tex=r"On définit des $k$-sous-espace stables par $\varphi$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"des $k$-sous-espaces stables",
    note="The TeX keeps the printed reading.")
add(page=403, where="Proposition 1.1, display defining V^{1-φ}",
    scan="V^{1-φ} = les 𝔽_q-vectoriel formé des points fixes de φ",
    tex=r"\underline{les $\mathbb F_q$-vectoriel formé des points fixes de}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"le $\mathbb F_q$-vectoriel",
    note="Singular noun and participle (vectoriel formé). The TeX keeps the printed reading.")
add(page=404, where="Corollaire 1.1.2, label",
    scan="Corollaire 1.1.2. with only the word 'Corollaire' underlined (checked at 2x)",
    tex=r"\underline{Corollaire 1.1.2.}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{Corollaire 1.1.2.}", "new": r"\underline{Corollaire} 1.1.2."},
    note=r"As on p. 403, where the TeX already has \underline{Proposition} 1.1.")
add(page=404, where="(1.1.8), first row",
    scan="Gl(n,k̄) ⟶ Gl(n,k̄) (small l, twice)",
    tex=r"\mathrm{Gl}(n,\bar k)&\longrightarrow\mathrm{Gl}(n,\bar k)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\mathrm{GL}(n,\bar k)&\longrightarrow\mathrm{GL}(n,\bar k)",
    note="GL everywhere else, including the parallel row of (1.1.9). The TeX keeps the printed reading.")
add(page=405, where="Corollaire 1.1.10, label",
    scan="Corollaire 1.1.10. with only the word 'Corollaire' underlined (checked)",
    tex=r"\underline{Corollaire 1.1.10.}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{Corollaire 1.1.10.}", "new": r"\underline{Corollaire} 1.1.10."},
    note="")
add(page=405, where="Proposition 1.2, label",
    scan="Proposition 1.2. with only the word 'Proposition' underlined (checked)",
    tex=r"\underline{Proposition 1.2.}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{Proposition 1.2.}", "new": r"\underline{Proposition} 1.2."},
    note="")
add(page=405, where="Proposition 1.2, statement",
    scan="d'un espace vectoriel / de dimension finie sur un corps séparablement clos k (no V)",
    tex=r"d'un espace vectoriel de dimension finie sur un corps",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"d'un espace vectoriel $V$ de dimension finie",
    note="V is used in the conclusion (1-φ : V → V) but not introduced; 1.1 and 1.1.10 read 'd'un espace vectoriel V de dimension finie'. The TeX keeps the printed reading.")

# order keys
keys = ["page","where","scan","tex","kind","confidence","fix","corrected","note"]
out = []
for f in F:
    d = {}
    for k in keys:
        if k == "corrected" and f["kind"] != "misprint_in_print":
            continue
        d[k] = f.get(k)
    out.append(d)

# checks
ok = True
for d in out:
    p = os.path.join(base, "b401_405", "page_%03d.tex" % d["page"])
    txt = open(p, encoding="utf-8", newline="").read()
    if "\r" in txt:
        print("CR in", p)
    if d["fix"]:
        n = txt.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", d["page"], repr(d["fix"]["old"]), n)
        if "%%%%%%%%%%" in d["fix"]["old"]:
            ok = False; print("marker in old")
    # tex excerpt presence (check without newlines)
    flat = txt.replace("\n", " ")
    if d["tex"] not in flat and d["tex"] not in txt:
        print("tex excerpt not verbatim on page", d["page"], repr(d["tex"]))
print("ok" if ok else "FAIL", len(out))
outp = os.path.join(base, "findings_401_405_recheck.json")
with open(outp, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
# re-load to validate
json.load(open(outp, encoding="utf-8"))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in out)
for pg in range(401, 406):
    print(pg, c[(pg, False)], c[(pg, True)])
