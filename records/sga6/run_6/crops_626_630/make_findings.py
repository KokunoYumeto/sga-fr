import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b626_630")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_626_630.json")
MAIN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")

F = []

F.append(dict(
    page=626,
    where="page start (first line under the running head '- 11 -')",
    scan="The page begins '< c_1(L_1)...c_1(L_s).Y > le nombre d'intersection, qui peut être calculé'.",
    tex=r"page_626.tex begins 'nombre d'intersection'; '\(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\) le' "
        r"is the end of page_625.tex ('Rappelons qu'on désigne par \(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\) le').",
    kind="marker", confidence="high", fix=None,
    note=r"Page 626 really begins at '\(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\) le'; page 625 ends "
         r"'Rappelons qu'on désigne par'. Exact fix: python -I move_marker.py 6 626 "
         r"'\(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\) le' --before (the marker then stands between "
         r"'désigne par' and '\(\langle'). The split falls inside a TeX line, so the 10 Nov script did not move it."))

F.append(dict(
    page=626,
    where="proof of Lemme 2.4, last formula",
    scan="'on aurait 0≥< c(L).c_1(H)^{r-1}> = < c_1(H)^{r-1}.Y> ≥1.': c without the index 1 (main scan and "
         "witness; the two c_1 on the same line have it).",
    tex=r"\langle c(L)\cdot",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\langle c_1(L)\cdot",
    note="d(L) is defined in 2.2 as <c_1(L).c_1(H)^{r-1}>; the print drops the index here. The TeX keeps the "
         "printed reading."))

F.append(dict(
    page=627,
    where="proof of Lemme 2.7, first sentence",
    scan="'Par 1.7 et 2.6, L_Y est un (0,a_2)-faisceau' (main scan and witness).",
    tex="Par 1.7 et 2.6,",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="Par 1.7 et 2.5,",
    note="Wrong reference number: the print has no 2.6 (Lemme 2.5 on p. 626 is followed by Lemme 2.7 on this page). "
         "The fact used, that L_Y is a (0,a_2)-faisceau because d(L_Y) <= 0, is Lemme 2.5, which the next pages cite "
         "as 2.5 for the same step (p. 628 'par 2.5', p. 629 'par 2.5', p. 630 'Par 2.5, L_Y est un "
         "(0,...,0,a_r)-faisceau'). The TeX keeps the printed reading."))

F.append(dict(
    page=628,
    where="first line",
    scan="'h^2(L(-a_1-2) = 0 par 1.4': only one closing parenthesis (main scan and witness).",
    tex="h^2(L(-a_1-2)=0",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="h^2(L(-a_1-2))=0",
    note="Unbalanced parenthesis in the print. The TeX keeps the printed reading."))

F.append(dict(
    page=628,
    where="Lemme 2.8, displayed inequality",
    scan="'a_o ≥ < c_1(L)^2 > +2e_o + Σ_{i=1}^2(2e_i-a_i)(δ-1+i over i) + β(β+1) .' (main scan and witness).",
    tex=r"+\beta(\beta+1)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"-\beta(\beta+1)",
    note="Sign of the last term. The proof on the same page gives a_o = 2α_2 + 2α_o - Σ_{i=1}^2 a_i(δ-1+i over i) - "
         "β_o with 2α_2 = <c_1(L)^2>, α_o = Σ_{i=0}^2 e_i(δ-1+i over i) and β_o ≤ β(β+1) by 2.7 (ii), hence "
         "a_o ≥ <c_1(L)^2> + 2e_o + Σ_{i=1}^2(2e_i-a_i)(δ-1+i over i) - β(β+1). Possibly the author's own slip. "
         "The TeX keeps the printed reading."))

F.append(dict(
    page=628,
    where="proof of Lemme 2.8, 'Donc a_o = ... - β_o et comme'",
    scan="'-β_o et comme d(L^{-1}(δ))≤0': no comma after β_o (main scan and witness).",
    tex=r"-\beta_0\), et comme",
    kind="punctuation", confidence="high",
    fix={"old": r"-\beta_0\), et comme", "new": r"-\beta_0\) et comme"},
    note="The TeX adds a comma the print does not have."))

F.append(dict(
    page=629,
    where="second paragraph, definition of ω",
    scan="'ω = Ext^{N-2}_{O_P} (O_X,Ω^N_{P/k} )' with the typed Ext underlined (sheaf Ext), main scan and witness.",
    tex=r"\mathcal E\!xt^{N-2}_{\mathcal O_P}",
    kind="underline", confidence="high",
    fix={"old": r"\mathcal E\!xt^{N-2}", "new": r"\underline{\Ext}^{N-2}"},
    note=r"The print has an underlined typed Ext, not a script E. \underline{\Ext} is the file's form (\Ext is "
         r"provided in the Exposé XIII local macros of main.tex; same fix as the p. 164 finding). This is the only "
         r"\mathcal E\!xt in main.tex."))

F.append(dict(
    page=629,
    where="end of the proof of (i) for r >= 3",
    scan="'Mais, pour n >> 0, h^1(L(n)) = 0 (voir FGA 149 § 6) ; d'où (i).' No minus sign (main scan and witness).",
    tex=r"h^1(L(n))=0\) (voir FGA",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"h^1(L(-n))=0\) (voir FGA",
    note="The argument needs h^1(L(-n)) = 0 for n >> 0 (X normal; the vanishing cited from FGA 149 § 6, as in the "
         "case r = 2 above): with h^1(L(-n-1)) = h^1(L(-n)) for n >= 2+h_2 it gives (i). h^1(L(n)) = 0 for n >> 0 "
         "(Serre) would prove nothing here. The TeX keeps the printed reading."))

F.append(dict(
    page=630,
    where="page start (first line under the running head '- 15 -')",
    scan="The page begins 'déjà prouvé, on en conclut que quelque soit m ≥ -2,'.",
    tex="page_630.tex begins 'prouvé, on en conclut'; 'déjà' ends page_629.tex ('... grâce à 2.9.1. Donc par (i) "
        "déjà').",
    kind="marker", confidence="high", fix=None,
    note="Page 630 really begins at 'déjà'; page 629 ends 'Donc par (i)'. Exact fix: python -I move_marker.py 6 630 "
         "'déjà' --before (the marker then stands between 'Donc par (i)' and 'déjà')."))

F.append(dict(
    page=630,
    where="page end",
    scan="The page ends with the display 'Σ_{i=0}^r a_i^{(m)}(n+i over i) = Σ_{j=0}^r a_j(mn+j over j)' (foot of "
         "p. 630 in both scans); p. 631 begins 'on ait : a_i^{(m)} = P_i^{(m,r)} (a_r,...,a_i).' (witness).",
    tex=r"page_630.tex ends '... tel que dans l'égalité suivante :'; the display (\[ \sum_{i=0}^{r}a_i^{(m)}"
        r"\binom{n+i}{i} = \sum_{j=0}^{r}a_j\binom{mn+j}{j}, \]) stands below the "
        r"folio 631 marker.",
    kind="marker", confidence="high", fix=None,
    note="The folio 631 marker must stand below the display, before 'on ait :'. Exact fix: python -I move_marker.py "
         "6 631 'on ait :'. The display's comma: next finding."))

F.append(dict(
    page=630,
    where="last display (in the TeX under the folio 631 marker)",
    scan="'... = Σ_{j=0}^r a_j(mn+j over j)' with nothing after it; p. 631 begins 'on ait :' (both scans).",
    tex=r"\sum_{j=0}^{r}a_j\binom{mn+j}{j},",
    kind="punctuation", confidence="high", fix=None,
    note=r"The TeX adds a comma at the end of the display. The text sits under the folio 631 marker, so there is "
         r"no fix in page_630.tex; edit for main.tex (the string occurs once there): old "
         r"'\binom{mn+j}{j},' new '\binom{mn+j}{j}' (with or after the marker move)."))

F.append(dict(
    page=630,
    where="first line",
    scan="'on en conclut que quelque soit m ≥ -2,' (main scan and witness).",
    tex="quelque soit",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="quel que soit",
    note="Spelling slip: the concessive form before a noun or variable is 'quel que soit'. The TeX keeps the printed reading."))

F.append(dict(
    page=630,
    where="Remarque 2.10, second display",
    scan="'a_{m,i} = Σ_{j=0}^{r-i} a_{j+i} (m-1+i over j)' (main scan and witness).",
    tex=r"\binom{m-1+i}{j}",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\binom{m-1+j}{j}",
    note="Wrong index in the binomial. From Σ a_{m,i}(n+i over i) = Σ a_j(m+n+j over j), n = -1 gives "
         "a_{m,0} = Σ_j a_j(m-1+j over j), and the recursion gives a_{m,i} = Σ_{j=0}^{r-i} a_{j+i}(m-1+j over j) "
         "(r = 1: a_{m,0} = a_0 + m a_1, the printed form gives a_0 + (m-1) a_1). The TeX keeps the printed reading."))

# checks
ok = True
main = MAIN.read_text(encoding="utf-8")
for x in F:
    t = (B / ("page_%d.tex" % x["page"])).read_text(encoding="utf-8")
    if x.get("fix"):
        n = t.count(x["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, x["page"], x["fix"]["old"])
    if x["kind"] == "misprint_in_print":
        n = t.count(x["tex"])
        if n != 1:
            ok = False
            print("MISPRINT TEX COUNT", n, x["page"], x["tex"])
    for k, v in x.items():
        if isinstance(v, str) and ("\r" in v or "\t" in v):
            ok = False
            print("CONTROL CHAR", x["page"], k)
for s in (r"\binom{mn+j}{j},", r"\(\langle c_1(L_1)\cdots c_1(L_s)\cdot Y\rangle\) le", "on ait :"):
    print("main.tex count", main.count(s), s)
print("Donc par (i) déjà count", main.count("Donc par (i) déjà"))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok" if ok else "PROBLEM", len(F))
