import json, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I"
F = []
def add(**k):
    F.append(k)

add(page=321,
    where="last sentence of the page: 'La suite de cet exposé est consacré à l'étude de ce schéma en groupes.'",
    scan="La suite de cet exposé est consacré à l'étude",
    tex="est consacré à l'étude",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="est consacrée à l'étude",
    note="Agreement slip of the print: the subject is 'La suite' (feminine). The TeX keeps the printed reading.")

add(page=322,
    where="last line, after (1.1.8): 'le groupe des composantes connexes de sa fibre spéciale A_o .'",
    scan="de sa fibre spéciale A_o . (A with subscript o, no prime; checked in a crop)",
    tex="de sa fibre spéciale $A_o$ .",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="de sa fibre spéciale $A'_o$ .",
    note="'sa' refers to A' (1.1.7); its special fibre is A'_o, as in (1.1.8) just above. The print drops the prime; the TeX keeps the printed reading.")

add(page=323,
    where="1.3.1, first sentence: 'aux changements de base formellements nets (VIII 7.3.5.3)'",
    scan="formellements nets",
    tex="formellements nets",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="formellement nets",
    note="Typing error for the adverb 'formellement'. The TeX keeps the printed reading.")

add(page=324,
    where="end of the paragraph continuing 1.3.1: 'sous la forme que lui a donné SERRE [27].'",
    scan="que lui a donné SERRE [27].",
    tex="que lui a donné SERRE",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected="que lui a donnée SERRE",
    note="Agreement slip of the print: the participle follows its direct object 'que' (= la forme). The TeX keeps the printed reading.")

add(page=324,
    where="display (1.4.2)",
    scan="Φ'_o = U_o/U_o^o ⊂ Φ_o , Ψ'_o = U'_o/U'_o^o ⊂ Ψ_o (the first Φ is typed over another character, the final shape is Φ with prime)",
    tex="\Phi'_o = U_o/U_o^{\,o} \subset \Phi_o \quad , \quad \Psi'_o = {U'}_o/{U'}_o^{\,o} \subset \Psi_o",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected="\Psi_o = U_o/U_o^{\,o} \subset \Phi_o \quad , \quad \Psi'_o = {U'}_o/{U'}_o^{\,o} \subset \Phi'_o",
    note="Notation slip of the print, taken over from VIII 7.3.2 (where Φ, Ψ are the component groups of P, Q): here Ψ_o, defined nowhere in IX, stands for the component group of A', which (1.1.8) calls Φ'_o, and Φ'_o is reused for the subgroup U_o/U_o^o of Φ_o. The corrected reading renames the two subgroups Ψ_o, Ψ'_o and puts Φ'_o for the component group of A'; it is an editorial suggestion and goes together with the next finding. The TeX keeps the printed reading.")

add(page=324,
    where="line after (1.4.2): 'de Φ_o et de Ψ_o définis par U et U'sont orthogonaux'",
    scan="de Φ_o et de Ψ_o définis par U et U'",
    tex="de $\Phi_o$ et de $\Psi_o$ définis",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected="de $\Phi_o$ et de $\Phi'_o$ définis",
    note="Same notation slip as in (1.4.2): the subgroup defined by U' lies in the component group of A', called Φ'_o in (1.1.8) and (1.2.1). Apply together with the corrected reading of (1.4.2). The TeX keeps the printed reading.")

add(page=324,
    where="line after (1.4.2): 'définis par U et U'sont orthogonaux l'un à l'autre pour'",
    scan="U'sont (no word space after U'; checked in a crop)",
    tex="$U'$sont",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="$U'$ sont",
    note="Missing word space in the print. The TeX keeps the printed reading.")

add(page=325,
    where="first sentence: 'ce prolongement (unique à isomorphe unique près) de W_K'",
    scan="(unique à isomorphe unique près)",
    tex="(unique à isomorphe unique près)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="(unique à isomorphisme unique près)",
    note="Typing error for 'isomorphisme'; the next sentence has 'à isomorphisme unique près'. The TeX keeps the printed reading.")

# checks
ok = True
for f in F:
    p = open(f"{base}/b321_325/page_{f['page']}.tex", encoding='utf-8', newline='').read()
    n = p.count(f['tex'])
    print(f['page'], repr(f['tex'][:50]), 'tex count', n)
    if f['fix'] is not None:
        m = p.count(f['fix']['old'])
        print('   fix old count', m)
        ok &= (m == 1)
    ok &= (n == 1)
print('ALL UNIQUE' if ok else 'PROBLEM')
out = f"{base}/findings_321_325_recheck.json"
with open(out, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
json.load(open(out, encoding='utf-8'))
print('written', out, len(F))
