# SGA en français

Ce dépôt contient les textes français du Séminaire de géométrie algébrique du Bois Marie (SGA) d’Alexander Grothendieck et de ses collaborateurs, en LaTeX, vérifiés par IA page par page sur les scans de l’imprimé. Il commence par les livres de lecture de SGA 7 I et II (*Groupes de monodromie en géométrie algébrique*), sous trois formes : texte diplomatique, texte corrigé avec apparat critique, texte de lecture, en LaTeX et en PDF.

## Contenu

- [`raw/pro_returns/SGA7_READERS_20261112/`](raw/pro_returns/SGA7_READERS_20261112/) : les livres de lecture de SGA 7 I et II, construction du 12 novembre 2026, telle qu’elle a été livrée, avec ses enregistrements. Pas encore relue.
- [`volumes/`](volumes/) : les textes de référence de SGA 4, SGA 5, SGA 6, SGA 7 I et SGA 7 II, chacun en deux couches (voir ci-dessous).
- [`records/`](records/) : par volume, les journaux de corrections, les registres des coquilles de l’imprimé, les rejeux, les rapports des vérificateurs et leurs consignes.
- [`method/`](method/) : la méthode de la vérification (`METHODOLOGY.md`, en anglais), la consigne des vérificateurs, les questions réglées pour tout un volume (`GLOBAL_ISSUES_SGA.md`) et les scripts.

## Les textes de référence

Chaque volume a deux couches :

- `diplomatic` (texte diplomatique) : le texte tel qu’il est imprimé, coquilles de l’imprimé comprises ;
- `current` (texte corrigé) : le même texte, coquilles corrigées.

Les coquilles de l’imprimé sont relevées dans `records/<volume>/MISPRINTS_<volume>.json` ; chaque correction de transcription est journalisée dans `FIXLOG_<volume>.jsonl` (couche diplomatique) et rejouée dans `FIXLOG_<volume>_CURRENT.jsonl` (couche corrigée).

**SGA 5, SGA 7 I, SGA 7 II.** Transcriptions par IA (OpenAI Codex, juin–août 2026), chacune en une couche diplomatique et une couche corrigée. Elles ont été vérifiées page par page sur les scans par Claude Opus 5.5 (Anthropic), par lots de cinq pages imprimées : SGA 5 (Lecture Notes in Mathematics 589, 1977) sur le scan à plat à 300 dpi, 97 lots ; SGA 7 I (LNM 288, 1972) sur l’exemplaire de l’Internet Archive (environ 360 ppi), 106 lots ; SGA 7 II (LNM 340, 1973) sur le scan de l’IAS (300 dpi), 88 lots. Des copies DjVu indépendantes à 300 dpi servent de second témoin pour les traits fins. Les pages d’abord vérifiées par l’API (SGA 7 I p. 251–270 et 401–530 ; SGA 7 II p. 266–285 et 396–430) ont été revérifiées par des sous-agents. Les coquilles de SGA 7 ont fait l’objet d’un passage commun par GPT-6.1 Sol (OpenAI API). Pour SGA 5, la couche corrigée avait deux versions divergentes (c4, c5) : c5 est la base, et ce que seule c4 contient a été repris après comparaison (`records/sga5/ref_c4/`) ; les corrections antérieures de Codex ont été rapprochées (`RECONCILE_CODEX_5.json`). Les corrections sont produites par IA.

**SGA 4.** Le texte est l’édition LaTeX française de SGA 4, tomes 1–3 (Lecture Notes in Mathematics 269, 270, 305), diffusée par Fabrice Orgogozo (https://www.normalesup.org/~forgogozo/SGA4/ ; instantané au commit git `71766d9`), avec ses fichiers de configuration TeX et ses notes éditoriales « N.D.E. », plus les retouches de conservation de la source faites par OpenAI Codex en août–septembre 2026. Première vérification (11 novembre 2026) : chaque page imprimée qui a du TeX (1 557 pages) a été vérifiée sur les scans par deux modèles, Claude Opus 5.5 et GPT-6.1 Sol ; les 898 corrections données à l’identique par les deux sont appliquées à la couche diplomatique, dont 774 rejouées dans la couche corrigée ; 930 coquilles de l’imprimé sont relevées et non appliquées ; les 443 pages où les deux modèles divergent ou signalent un doute attendent une seconde vérification (`records/sga4/api_pass_20261111/PAGES_FOR_APP_CHECK.json`). Les corrections sont produites par IA.

**SGA 4½.** Seuls les enregistrements d’une vérification par sondage (`records/sga4_5/`) sont ici ; le texte est la composition LaTeX de Daniel Miller (https://github.com/dkmiller/sga4.5).

**SGA 6.** Transcription par IA (OpenAI Codex, juin–août 2026 ; base : la division du 5 août), en deux couches, avec repères de pages ajoutés. Vérification en cours, de la même manière que SGA 5 et SGA 7, sur l’exemplaire de l’Internet Archive (environ 360 ppi) de SGA 6 (Lecture Notes in Mathematics 225, 1971) : 78 lots de cinq pages sur 140 faits au 12 novembre 2026. Les corrections de Codex du 23 août sont dans `records/sga6/ref_hold/` et ne sont pas encore dans les couches vérifiées : chacune est vérifiée sur le scan avant d’y entrer (`records/sga6/HOLD_VS_CORR.md`, 119 différences).

Les chemins locaux des enregistrements ont été anonymisés (« user »).

## Auteurs et crédits

Alexander Grothendieck, avec M. Raynaud et D. S. Rim, Groupes de monodromie en géométrie algébrique I, Séminaire de géométrie algébrique du Bois-Marie 1967–1969 (SGA 7 I), Lecture Notes in Mathematics 288, Springer, 1972 : exposés I, II, VI–IX. Pierre Deligne et Nicholas Katz, Groupes de monodromie en géométrie algébrique II (SGA 7 II), Lecture Notes in Mathematics 340, Springer, 1973 : exposés X–XXII. Les attributions détaillées des exposés sont conservées. L’exposé VI de D. S. Rim a été publié en anglais et reste en anglais dans les deux éditions linguistiques.

M. Artin, A. Grothendieck et J.-L. Verdier, avec la collaboration de N. Bourbaki, P. Deligne et B. Saint-Donat, Théorie des topos et cohomologie étale des schémas, Séminaire de géométrie algébrique du Bois-Marie 1963–1964 (SGA 4), Lecture Notes in Mathematics 269, 270 (1972) et 305 (1973), Springer. A. Grothendieck, avec la collaboration de I. Bucur, C. Houzel, L. Illusie, J.-P. Jouanolou et J.-P. Serre, Cohomologie l-adique et fonctions L, Séminaire de géométrie algébrique du Bois-Marie 1965–1966 (SGA 5), édité par L. Illusie, Lecture Notes in Mathematics 589, Springer, 1977.

Les textes français de SGA 5 et SGA 7 sont transcrits par IA ; celui de SGA 4 est l’édition LaTeX de Fabrice Orgogozo (voir ci-dessous) ; les corrections sont produites par IA. La construction des livres de lecture de SGA 7 est due à GPT-6 Astra (OpenAI, mode Pro de ChatGPT). Ces désignations n’attribuent à l’intelligence artificielle aucune contribution humaine.

Crédits humains hérités, tels que les livres de lecture les portent (en anglais dans l’original) :

> Sources and authorship
>
> The original SGA volumes retain their authors, seminar contributors and editors, named in the corresponding texts. The collection includes work of Alexander Grothendieck, Michèle Raynaud, Michel Raynaud, Pierre Deligne, Nicholas Katz, Michel Demazure, Michael Artin, Jean-Louis Verdier, Luc Illusie and their collaborators; this list does not replace the detailed credits in each volume.
>
> SGA 1 retains the French retypesetting associated with Bas Edixhoven’s volunteer project, the Société mathématique de France and Michel Raynaud’s notes, from arXiv math/0206203v2 (https://arxiv.org/abs/math/0206203v2).
>
> SGA 2 is AI-translated from the corrected French TeX of the re-edition edited by Yves Laszlo, Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2), Documents Mathématiques 4, Société mathématique de France, 2005 (arXiv math/0511279v1 (https://arxiv.org/abs/math/0511279v1)), and follows its numbering and labels. Most of the initial French typesetting was done by volunteers of Bas Edixhoven’s project (L. Bayle, N. Borne, O. Brinon, J. Buresi, M. Chardin, F. Ducrot, P. Graftiaux, F. Han, P. Karwasz, L. Koelblen, D. Madore, S. Morel, D. Naie, B. Osserman, J. Riou and V. Sécherre); C. Sabbah adapted it to the SMF format.
>
> The SGA 2 and SGA 3 English sources acknowledge Jacob C. Reinhold’s English translation (https://github.com/jcreinhold/sga/tree/e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e), snapshot e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e, used for comparison and drafting. His stated CC BY 4.0 notice applies to that contribution and is preserved; it does not license the underlying French works or every contribution here. Inherited English wording remains attributed to its human source. In SGA 3, lemmas, proofs and corrections added in the Philippe Gille–Patrick Polo re-edition are given in Translator's notes and Additions that cite it.
>
> SGA 4 is AI-translated from the French LaTeX edition of SGA 4, Tomes 1–3, distributed by Fabrice Orgogozo (normalesup.org/~forgogozo/SGA4 (https://www.normalesup.org/~forgogozo/SGA4/); source snapshot at git commit 71766d9), and uses its TeX configuration files. Its footnotes headed “N.D.E.” are that edition's editorial notes, translated.
>
> SGA 4½ preserves Daniel Miller’s LaTeX typesetting (https://github.com/dkmiller/sga4.5) and its original typesetter’s note. It is not attributed to AI.
>
> Additional English translation is AI-translated; subsequent corrections, editing, reconstruction and typesetting are AI-produced. The source-specific human credits and genuine third-party notices remain applicable; attribution does not establish permission or endorsement.

## Autres langues

- Anglais : https://github.com/KokunoYumeto/sga-en
- Espagnol : https://github.com/KokunoYumeto/sga-es
- Index des éditions EGA, FGA et SGA : https://github.com/KokunoYumeto/ega-fga-sga

## Droits

Les droits sur l’œuvre originale appartiennent à son auteur ou aux représentants ou héritiers de celui-ci. Dans la mesure où nous détenons des droits sur la transcription, la traduction, les corrections et la composition produites par l’intelligence artificielle, nous les dédions au domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir un ticket GitHub et nous la retirerons.

https://github.com/KokunoYumeto/sga-fr/issues

https://creativecommons.org/publicdomain/zero/1.0/
