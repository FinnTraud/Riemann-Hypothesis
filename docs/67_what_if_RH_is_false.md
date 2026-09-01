---
id: doc-67
number: 67
title: "Was wäre, wenn die RH falsch ist? Θ, Oszillationen & numerische Signaturen"
category: synthesis
status: meta
tags: [rh-false, supremum-theta, littlewood, skewes, robin, lehmer, falsification, de-bruijn-newman]
source_file: 67_what_if_RH_is_false.md
lang: de
---

# Was wäre, wenn die RH falsch ist?

**Kategorie:** Synthese / Falsifikations-Perspektive
**Autoren / Jahre:** Littlewood (1914); Skewes (1933/1955); Robin (1984); Odlyzko–te Riele (1985); Rodgers–Tao (2020); Ivić (2003, „reasons for doubting")
**Typ:** Systematische Gegenprobe — was folgte aus einer Ausnahmenullstelle, und was würde man sehen?
**Status:** Meta (alle Aussagen hier sind bewiesene bedingte Folgerungen)

## Zusammenfassung
Fast die gesamte Literatur fragt „Wie beweist man die RH?". Dieses Dokument fragt das Gegenteil: **Angenommen, es gäbe eine Nullstelle mit Re(ρ) ≠ 1/2 — was folgte daraus, und woran könnte man es merken?** Das ist aus drei Gründen wichtig: (1) es macht die RH falsifizierbar und damit wissenschaftlich sauber; (2) es zeigt, welche numerischen Experimente überhaupt informativ sind; (3) es kalibriert, wie viel man aus der bestehenden Numerik schließen darf — nämlich wenig.

## Mathematischer Kern

### Die Grundgröße Θ
```
Θ  :=  sup { Re(ρ) : ζ(ρ) = 0, 0 < Re ρ < 1 }   ∈ [1/2, 1].
RH  ⟺  Θ = 1/2.
```
Bekannt ist bisher nur `Θ ≤ 1` (Nichtverschwinden auf Re = 1, PNT) und `Θ ≥ 1/2` (trivial, wegen der Funktionalgleichung + unendlich vieler Nullstellen auf der Geraden, Dok. 03).

**Quadrupel-Struktur.** Wegen `ζ(\bar s) = \overline{ζ(s)}` und `Λ(s) = Λ(1−s)` kommen Nullstellen abseits der Geraden immer zu **viert**: `ρ, \barρ, 1−ρ, 1−\barρ`. Eine einzelne Ausnahme kann es nicht geben.

### Was sofort folgt (bewiesene bedingte Sätze)
| Konsequenz | Aussage bei Θ > 1/2 |
|---|---|
| Primzahlsatz-Fehlerterm | `ψ(x) − x = Ω_±( x^{Θ−ε} )` und `= O(x^{Θ+ε})` — der Fehler ist **beweisbar größer** als `√x` |
| π(x) vs. Li(x) | Littlewoods Oszillationssatz gilt unverändert; die Vorzeichenwechsel würden mit Amplitude `x^{Θ}/log x` auftreten |
| Mertens-Funktion | `M(x) = Ω(x^{Θ−ε})`, also **keine** Schranke `x^{1/2+ε}` (Dok. 16) |
| Robins Ungleichung | `σ(n) < e^γ n log log n` hätte **unendlich viele** Ausnahmen n > 5040 (Robin 1984) — die RH ist hier äquivalent, nicht nur implizierend (Dok. 15) |
| Li-Kriterium | mindestens ein `λ_n < 0` — und zwar (Bombieri–Lagarias) mit `λ_n ≈ −c·n·x^{...}`, exponentiell wachsend negativ (Dok. 14) |
| Nyman–Beurling | die Abstände `d_N` konvergierten **nicht** gegen 0 (Dok. 13, 45) |
| de-Bruijn–Newman | `Λ > 0`. Rodgers–Tao bewiesen `Λ ≥ 0`; `Λ > 0` **wäre äquivalent zu „RH falsch"** (Dok. 23) |
| Miller-Primzahltest | verlöre seine `O((log n)^4)`-Schranke; AKS bliebe unberührt (Dok. 36) |
| Kryptographie | **kein** praktischer Zusammenbruch — RSA/ECC hängen nicht an der RH (häufiges Missverständnis) |

### Wie eine Ausnahme aussähe — und warum man sie nicht sieht
1. **Die Höhe.** Verifiziert ist die RH für die ersten ~10^13 Nullstellen bzw. bis `T ≈ 3·10^{12}` (Platt, rigoros; Gourdon–Demichel heuristisch bis 10^{13}, Dok. 24). Eine Ausnahmenullstelle müsste oberhalb liegen. Zum Vergleich: **Skewes-Zahl** ~10^{316} und die Widerlegung der Mertens-Vermutung (erste Ausnahme vermutlich jenseits 10^{30}) zeigen, dass in dieser Theorie „endlich verifiziert" und „wahr" um viele Größenordnungen auseinanderliegen dürfen.
2. **Die Nähe.** Nullstellendichte-Sätze (Dok. 22, 49) erzwingen: Nullstellen mit `Re > 1/2 + δ` sind extrem selten (`N(σ,T) ≪ T^{...(1−σ)}`). Eine Ausnahme läge fast sicher **sehr nahe** an der Geraden — nicht sichtbar getrennt.
3. **Die Signatur.** Was man in Daten *tatsächlich* zuerst sähe:
   - **Lehmer-Paare** mit immer kleinerem Abstand (Dok. 23) — sie sind das numerische Vorbeben. `Λ ≥ 0` (Rodgers–Tao) heißt: solche Paare *müssen* asymptotisch beliebig eng werden, „die RH gilt gerade eben".
   - **Ausreißer in `S(T)`** (Argumentterm, Dok. 02): unter RH ist `S(T) = O(log T/log log T)`; anomale Sprünge wären ein Hinweis.
   - **Abweichung der Momente** von `a_k g_k` (Dok. 63) oder der Extremwerte von der FHK-Formel (Dok. 64).
   - **λ_n-Vorzeichen** (Dok. 14): ein negatives `λ_n` bei berechenbarem n wäre die direkteste Widerlegung — deshalb ist die λ_n-Berechnung ein sinnvolles Experiment, obwohl niemand ein negatives erwartet.

### Warum viele Fachleute trotzdem an die RH glauben — und die Gegenargumente
**Dafür:** GUE-Statistik über n Ebenen (Dok. 65); die RH ist im Funktionenkörperfall **bewiesen** (Dok. 18) und für Selberg-Zeta **bewiesen** (Dok. 19); >41 % der Nullstellen sind nachweislich auf der Geraden (Dok. 04); alle bekannten „Fast-Gegenbeispiele" (Davenport–Heilbronn) verletzen genau eine strukturelle Eigenschaft (Euler-Produkt).
**Dagegen (Ivić):** Die Mertens-Vermutung sah genauso gut aus und ist falsch; `S(T)` ist unbeschränkt; Lehmer-Paare zeigen keine Sicherheitsmarge; die Beispiele mit bewiesener RH haben alle eine Geometrie, die ℤ fehlt (Dok. 60, 61) — die Analogie könnte gerade dort brechen, wo sie zählt.

## Bedeutung / Einordnung
- **Regel für die Arbeit mit dieser Wissensbasis:** Jede numerische Aussage bekommt den Zusatz „bis Höhe T geprüft" — und die Skewes/Mertens-Kalibrierung, warum das wenig heißt (Dok. 35).
- Dieses Dokument liefert die **Falsifikationstests**, die im Experiment-Logbuch (Dok. 51) tatsächlich lohnen: λ_n-Vorzeichen, `d_N`-Konvergenz, Lehmer-Paar-Abstände, S(T)-Ausreißer, FHK-Maxima.
- Für die Beweisbewertung: Ein Ansatz, der **nicht sagen kann, wie er eine Ausnahmenullstelle ausschließt**, hat kein Argument — er hat eine Hoffnung.

## Quellen
- [A. Ivić, *On some reasons for doubting the Riemann hypothesis* (arXiv:math/0311162)](https://arxiv.org/abs/math/0311162)
- A. Odlyzko, H. te Riele, *Disproof of the Mertens conjecture*, J. reine angew. Math. 357 (1985).
- G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*, J. Math. Pures Appl. 63 (1984).
- [B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative* (arXiv:1801.05914)](https://arxiv.org/abs/1801.05914)
- [D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10^12* (arXiv:2004.09765)](https://arxiv.org/abs/2004.09765)

<!-- AUTO:VERNETZUNG START (kb/build_obsidian.py) -->
## 🔗 Vernetzung
> Automatisch erzeugt aus `kb/graph/*.json` durch `python3 kb/build_obsidian.py`. Inhaltliche Änderungen bitte in den Graph-Dateien vornehmen, nicht hier.

**Ausgehende Beziehungen**
- *modelliert* (`models`) → [[concept_RH|Riemann-Vermutung (RH)]] — Systematische Gegenprobe: Konsequenzen und numerische Signaturen von Θ>1/2.
- *benutzt* (`uses`) → [[23_de_Bruijn_Newman_constant_Polymath15|23 — De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]] — Λ>0 wäre äquivalent zu 'RH falsch'.
- *benutzt* (`uses`) → [[16_Mertens_function_Riesz_criterion|16 — Mertens-Funktion & Riesz-Kriterium (Möbius-basierte Kriterien)]] — Mertens-Widerlegung als Kalibrierung der Numerik.
- *ist Obstruktion für* (`obstruction_for`) → [[24_computational_verification|24 — Numerische Verifikation der Riemann-Vermutung]] — Verifikation bis 3·10^12 schließt eine Ausnahme nicht aus.
- *benutzt* (`uses`) → [[15_Robin_inequality|15 — Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)]] — Robin: RH falsch ⇒ unendlich viele Ausnahmen.

**Thematisch benachbart (gemeinsame Tags):** [[35_obstructions_barriers|Obstruktionen & Barrieren: Warum naive Ansätze scheitern MÜSSEN]] · [[23_de_Bruijn_Newman_constant_Polymath15|De-Bruijn–Newman-Konstante: Rodgers–Tao & Polymath15]] · [[15_Robin_inequality|Robins Ungleichung & Lagarias' elementares Kriterium (arithmetische Kriterien)]]

**Navigation:** [[00_INDEX|Index]] · [[MOC_00_Hub|Netzwerk-Hub]] · [[68_failure_anatomy|Fehler-Anatomie]] · [[69_comparison_matrix|Vergleichsmatrix]]
<!-- AUTO:VERNETZUNG END -->
