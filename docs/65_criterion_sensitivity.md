---
id: doc-65
number: 65
title: "Sensitivität der Kriterien: wie weit trägt numerische Evidenz wirklich?"
category: verification
status: reference
tags: [sensitivity, resolution, robin, baez-duarte, li-criterion, de-bruijn-newman, calibration]
source_file: 65_criterion_sensitivity.md
lang: de
---

# Sensitivität der Kriterien: wie weit trägt numerische Evidenz wirklich?

**Kategorie:** Verifikation / Kalibrierung
**Implementierung:** `kb/sensitivity.py` · Protokoll: `kb/research/results/sensitivity_report.json`
**Verwandt:** `docs/57` (U1, Ausgangspunkt) · `docs/59` (Ⓗ) · `docs/60` (T6) · `docs/63` (Experiment ②) · `docs/13`, `docs/14`, `docs/15`, `docs/23`

## Die Frage

`docs/58` zeigt: ein zur RH äquivalentes Kriterium ist **logisch** genau so
schwer wie die RH. Dieses Dokument zeigt die andere Hälfte:

> **Numerisch sind äquivalente Kriterien um viele Größenordnungen
> verschieden scharf.** „Das Kriterium wurde numerisch bestätigt" ist ohne die
> Angabe *bis zu welcher Höhe* eine leere Aussage.

Das ist Experiment ② aus `docs/63` — dort als bestes Aufwand-Nutzen-Verhältnis
eingestuft, weil **beide** Ausgänge informativ sind. Der Ausgang ist eingetreten:
alle geprüften Kriterien skalieren schlecht, aber auf drei ganz verschiedene
Arten, und einer der vier Fälle verhält sich völlig anders als erwartet.

## Der Gesamtvergleich

| Kriterium | Budget | Kostengesetz | Erreicht | Testobjekte komprimierbar? |
|---|---|---|---|:-:|
| **Direkte Nullstellenberechnung** (`docs/24`) | Höhe T | linear in T | γ ≈ 3·10¹² rigoros | nein |
| **Li-Koeffizienten λ_n** (`docs/14`) | Ordnung n | n ~ γ² | n ≤ 10⁹ trägt bis γ ≈ 2089 | nein |
| **Robins Ungleichung** (`docs/15`) | Größe n | Marge ~ K/(√log n · log log n) | Marge 2,5·10⁻⁴ bei log n ≈ 88 000 | **ja** |
| **Báez-Duarte d_N** (`docs/13`) | Dimension N | d_N² ~ C/log N | N = 32, d_N = 0,117 | nein |
| **de-Bruijn–Newman Λ** (`docs/23`) | — | *kein Rechenbudget* | 0 ≤ Λ ≤ 0,22 | — |

Reproduzierbar mit `python3 kb/sensitivity.py all --max-logn 600000`.

---

## 1 · Li-Koeffizienten — quadratisch in der Höhe

Aus `docs/57` U1, hier zur Einordnung wiederholt. Der Beitrag einer Nullstelle
ρ = β + iγ zu λ_n enthält −(1 − 1/ρ)ⁿ, und

```
|1 − 1/ρ| = 1 + (1 − 2β)/(2γ²) + O(γ⁻⁴)
```

Die Rate fällt **quadratisch mit der Höhe**, also wächst die nötige Ordnung wie
γ². Ein Budget von n ≤ 1000 — mehr als üblich gerechnet wird — reicht bis
γ ≈ 3,6, also nicht einmal bis zur ersten ζ-Nullstelle bei 14,13.

## 2 · Robins Ungleichung — gemessen, nicht geschätzt

Der einzige Fall, in dem sich die Sensitivität **direkt messen** lässt, ohne
irgendeine Asymptotik anzunehmen.

**Vorgehen.** Verletzt irgendein n Robins Ungleichung, dann auch eine
*kolossal abundante* Zahl. Diese sind der schärfste Testort — und sie lassen
sich konstruieren: zum Parameter ε ist der Exponent von p

```
a_p(ε) = ⌊ log( (p^{1+ε} − 1)/(p^ε − 1) ) / log p ⌋ − 1
```

Aus dem Exponentenvektor folgen log n und σ(n)/n exakt. Gemessen wird

```
R(n) = σ(n) / ( e^γ · n · log log n ),     Marge := 1 − R(n)
```

Robins Ungleichung gilt für n > 5040 genau dann, wenn R(n) < 1.

**Ergebnis** (Auszug aus `kb/sensitivity.py robin`):

| ω(n) | größter Primfaktor | log n | Stellen von n | R(n) | Marge |
|---:|---:|---:|---:|---:|---:|
| 4 | 7 | 7,83 | 3,4 | 1,01321590 | **−0,0132** ⟵ *Robin verletzt (n = 2520)* |
| 42 | 181 | 192,3 | 84 | 0,98866703 | 0,01133 |
| 221 | 1 381 | 1 398 | 607 | 0,99683278 | 0,00317 |
| 1 311 | 10 753 | 10 834 | 4 705 | 0,99914201 | 0,000858 |
| 8 529 | 87 833 | 87 995 | 38 220 | 0,99975335 | **0,000247** |

Die erste Zeile ist die Selbstkontrolle: das Verfahren findet die bekannte
Ausnahme n = 2520 (eine der bekannten Ausnahmen unterhalb 5041) von selbst, ohne dass
man ihm sagt, wo sie liegt.

**Gemessenes Abklinggesetz.** Über drei Größenordnungen in log n (112 bis
88 000, 11 Messpunkte) ist

```
Marge  ≈  K / ( √(log n) · log log n ),      K = 0,839   (relative Streuung 14 %)
```

gleichbedeutend mit einer absoluten Lücke

```
e^γ · log log n  −  σ(n)/n   ≈   1,50 / √(log n)
```

*Hinweis zur Belastbarkeit:* Der Koeffizient 1,50 ist **hier gemessen**, nicht
aus der Literatur übernommen und nicht gegen sie abgeglichen. Die Form
1/√(log n) entspricht der bekannten Gestalt der Robin-Schranken; der konkrete
Zahlenwert ist als `T4-repo-numerik` einzustufen (`docs/64`).

**Reichweite:**

| Ziel-Marge | log n | Stellen von n | benötigte Primzahlen ω(n) |
|---|---|---|---|
| 10⁻³ | 8 600 | 10³⁷³⁴ | ≈ 950 |
| 10⁻⁴ | 4,2·10⁵ | 10¹⁸³ ⁰⁰⁰ | ≈ 3,2·10⁴ |
| 10⁻⁶ | 1,6·10⁹ | 10⁶·¹⁰⁸ | ≈ 7,4·10⁷ |
| 10⁻⁸ | 8,0·10¹² | 10³·¹⁰¹² | ≈ 2,7·10¹¹ |

**Der überraschende Teil.** Die Spalte „Stellen von n" sieht vernichtend aus —
eine Zahl mit 600 Millionen Stellen. Aber sie ist irreführend:

> **Robins Testobjekte sind komprimierbar.** Eine kolossal abundante Zahl wird
> nie ausgeschrieben, sondern als Exponentenvektor über den Primzahlen bis
> ≈ log n gespeichert. Die tatsächlichen Kosten wachsen daher nur wie
> π(log n) — die Zeile mit 38 220 Stellen wurde für dieses Dokument in
> **Sekunden** gerechnet.

Robin ist damit das einzige Kriterium der Sammlung, dessen praktische Reichweite
seine nominelle deutlich übersteigt. Marge 10⁻⁶ ist mit ~7,4·10⁷ Primzahlen
erreichbar — aufwendig, aber möglich.

**Und trotzdem:** Die Marge nähert sich der Null nur wie 1/√(log n). Selbst am
äußersten machbaren Rand bliebe Robins Ungleichung um Größenordnungen von
einer Verletzung entfernt. **Jede Robin-Rechnung findet statt, wo die
Ungleichung bequem gilt.**

## 3 · Báez-Duarte d_N — das schlechteste Kriterium

Unter der BBLS-Vermutung (RH mit einfachen Nullstellen) gilt

```
d_N²  ~  C / log N,      C = Σ_ρ 1/|ρ|² = 2 + γ − log(4π) = 0,046191418…
```

Das eigene Experiment des Repos (`kb/research/results/dn_experiment_note.md`)
bestätigt die Konstante: gemessen (log N)·d_N² ≈ 0,048 bei N = 32 gegen
vorhergesagt 0,0462.

Daraus die Auflösungsgrenze — welches N braucht es, damit d_N unter δ fällt?

| Auflösung | log N | N |
|---|---|---|
| d_N < 0,1 | 4,62 | 10² |
| d_N < 0,05 | 18,5 | 10⁸ |
| d_N < 0,01 | 462 | **10²⁰¹** |
| d_N < 10⁻³ | 46 191 | 10²⁰ ⁰⁶¹ |
| d_N < 10⁻⁶ | 4,6·10¹⁰ | 10²·¹⁰¹⁰ |

**Warum das endgültig ist.** Anders als bei Robin gibt es hier keine
Kompression: N ist die **Dimension eines Least-Squares-Problems**, dessen
Konditionszahl mit N wächst (das Repo-Experiment misst cond(G) ≈ 2,7·10³
schon bei N = 32). Um d_N unter 0,01 zu drücken, bräuchte man eine Matrix mit
10²⁰¹ Zeilen. Das ist nicht „teuer", sondern in diesem Universum nicht
darstellbar.

> **d_N ist als numerisches Kriterium wertlos** — nicht weil zu wenig
> gerechnet wird, sondern weil die 1/log N-Konvergenz jede erreichbare
> Dimension vor der ersten signifikanten Stelle stoppt.

*Vorbehalt:* Die Asymptotik ist eine **Vermutung**, kein Satz. Die Tabelle ist
entsprechend bedingt — aber die Richtung ändert sich dadurch nicht, weil die
gemessenen d_N-Werte des Repo-Experiments genau diesem Gesetz folgen.

## 4 · Λ — die Ausnahme, und deshalb der interessanteste Fall

Die de-Bruijn–Newman-Konstante passt **nicht** in dieses Schema, und das ist
ein Ergebnis, kein Mangel.

Λ hat kein Rechenbudget, dessen Erhöhung die Auflösung verbessert. Bekannt ist
0 ≤ Λ ≤ 0,22 (Rodgers–Tao 2018 / Polymath15 2019), und die obere Schranke ist
von 1/2 (1950) auf 0,22 (2019) gefallen — sie bewegt sich also, aber nicht
durch mehr Rechenzeit.

Der Grund ist strukturell: Die Methode gewinnt ihre Kraft aus der **Glättung
der Wärmeleitungs-Deformation H_t bei t > 0**. Bei t → 0 verschwindet genau
diese Glättung — H_0 *ist* die ξ-Funktion. Es ist keine Wand aus Rechenzeit,
sondern eine Wand aus Methode.

> **Λ ist das einzige Kriterium der Sammlung, bei dem „mehr rechnen"
> grundsätzlich nicht hilft — und zugleich das einzige mit einer beweglichen
> Kennzahl.** Beides hängt zusammen: Λ bewegt sich, weil Menschen die Methode
> verbessern, nicht weil Maschinen länger laufen.

Genau deshalb steht Λ in `docs/58` an der Spitze des Near-Miss-Rankings und
gleichzeitig in `docs/63` nicht unter den lohnenden Experimenten.

---

## Was daraus folgt

**1. Die Rangfolge ist eindeutig.** Direkte Nullstellenberechnung ≫
Li-Kriterium ≫ Robin ≫ d_N. Zwischen dem Referenzmaßstab (γ ≈ 3·10¹²) und dem
schlechtesten Kriterium (d_N) liegen so viele Größenordnungen, dass ein
Vergleich fast sinnlos wird.

**2. Numerische Kriterienprüfung ist als RH-Evidenz systematisch wertlos.**
Der Ausgang A aus `docs/63` ② ist eingetreten. Das korrigiert die
Evidenzbewertung in `docs/13`, `docs/14`, `docs/15` und `docs/45`: Was dort
als „numerische Bestätigung" firmiert, findet ausnahmslos in Regimen statt, in
denen das jeweilige Kriterium blind ist.

**3. Es gibt trotzdem einen Grund, diese Kriterien zu rechnen — nur einen
anderen.** Sie taugen zur *Validierung von Implementierungen* (das
d_N-Experiment traf die BBLS-Konstante auf 4 % genau und bewies damit die
Korrektheit der selbst hergeleiteten Formulierung), zur *Selbstkontrolle*
(die Robin-Rechnung fand die Ausnahme n = 2520 selbständig) und zur
*Anschauung*. Als Evidenz für die RH taugen sie nicht.

**4. Die Kompressionsfrage ist eine eigene Achse.** Sie war vor dieser
Rechnung nicht sichtbar und trennt Robin scharf von d_N: gleich schlechte
Skalierung, völlig verschiedene Erreichbarkeit. Wer Kriterien nach
numerischer Brauchbarkeit sortiert, muss beides fragen — Kostengesetz **und**
Darstellbarkeit der Testobjekte.

**5. Für den Vorwurf „Numerik beweist nichts" gibt es jetzt Zahlen.**
`docs/35` und `docs/59` Ⓗ sagen das qualitativ (Mertens, Skewes). Dieses
Dokument sagt für vier konkrete Kriterien, *wie weit* die Numerik trägt — und
die Antwort ist bei dreien: praktisch gar nicht.

## Offen geblieben

- **Der gemessene Koeffizient 1,50 in der Robin-Lücke** ist nicht gegen die
  Literatur abgeglichen. Es gibt Arbeiten zu genau dieser Asymptotik; findet
  sich der Wert dort, ist das eine unabhängige Bestätigung der Rechnung —
  findet er sich nicht, gehört die Diskrepanz geprüft.
- **Volchkov, Sekatskii, Redheffer** (`docs/45`) wurden nicht analysiert.
  Redheffer ist ein Determinantenkriterium und dürfte ein drittes,
  wieder anderes Kostenprofil haben.
- **Die Alternative Hypothese** (`docs/53`) verlangt Abstandsstatistik bei
  großer Höhe — dort ist die Sensitivitätsfrage anders gestellt (Stichprobe
  statt Auflösung) und noch offen.

## Quellen
Die Rechnungen in Abschnitt 2 sind **in diesem Repo durchgeführt**
(`kb/sensitivity.py`, Protokoll `kb/research/results/sensitivity_report.json`)
und als `T4-repo-numerik` einzustufen (`docs/64`). Die zugrunde liegenden
Sätze und Vermutungen sind in den Einzeldokumenten belegt: `docs/13`
(Nyman–Beurling/Báez-Duarte, BBLS-Asymptotik), `docs/14` (Li-Kriterium),
`docs/15` (Robin), `docs/23` (de-Bruijn–Newman), `docs/24` (Verifikationsstand).
Primärbelege:
- [Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann* (J. Math. Pures Appl. 63, 1984)](https://zbmath.org/?q=an%3A0530.10034)
- [Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis* (arXiv math/0202141)](https://arxiv.org/abs/math/0202141)
- [Rodgers & Tao, *The de Bruijn–Newman constant is non-negative* (arXiv 1801.05914)](https://arxiv.org/abs/1801.05914)
- [Polymath15, *Effective approximation of heat flow evolution of the Riemann ξ function* (arXiv 1904.12438)](https://arxiv.org/abs/1904.12438)

## Verknüpfungen (auto)

<!-- OBSIDIAN-LINKS:BEGIN (generiert von kb/obsidian.py) -->

> [!warning]- Blocker — woran dieser Ansatz hängt (2)
> - **Äquivalenz-Falle** *(Tier 2)* — Ein Kriterium ist zur RH äquivalent und damit exakt gleich schwer — die Umformulierung erzeugt den Anschein von Fortschritt, ohne die Beweislast zu senken.
>   *Fluchtbedingung:* Eine der beiden Richtungen muss in STRIKT SCHWÄCHERER Form unbedingt bewiesen werden, oder es muss eine quantitative Größe geben, die sich unabhängig von der RH bewegen lässt (Λ ≤ 0.22, Anteil > 41 %, d_N-Raten). Nur solche Bewegungen zählen als Fortschritt — siehe docs/58.
> - **Numerische Extrapolation** *(Tier 3)* — Aus endlicher Rechnung wird auf asymptotisches Verhalten geschlossen — die RH-Landschaft hat dafür berüchtigte Gegenbeispiele.
>   *Fluchtbedingung:* Nicht überwindbar, nur vermeidbar: Numerik darf Hypothesen erzeugen und widerlegen, aber nie stützen. Ein rigoroses Intervall-Zertifikat (doc-54) ist etwas anderes als eine Stichprobe.
> 
> Vollständige Matrix: [[55_failure_taxonomy]]

> [!abstract]- Graph-Nachbarn (8)
> - *ist Evidenz für* → [[13_Nyman_Beurling_Baez_Duarte|13 · Nyman–Beurling-Kriterium & Báez-Duarte-Verschärfung]] — Miss die numerische Reichweite der Baez-Duarte-Distanz d_N.
> - *ist Evidenz für* → [[15_Robin_inequality|15 · Robins Ungleichung & Lagarias' elementares Kriterium]] — Miss die Robin-Marge entlang kolossal abundanter Zahlen.
> - *ist Evidenz für* → [[14_Li_criterion_Bombieri_Lagarias_Weil_positivity|14 · Li-Kriterium, Bombieri–Lagarias & Weil-Positivität]] — Ordnet die Li-Sensitivitaet in den Kriterienvergleich ein.
> - *benutzt* → [[57_untried_directions|57 · Noch nicht Versuchtes]] — Fuehrt die in U1 angekuendigte Sensitivitaetsanalyse aus.
> - *benutzt* → [[63_experiment_decision_value|63 · Entscheidungswert von Experimenten]] — Ist Experiment (2) der Entscheidungswert-Rangliste.
> - *benutzt* → [[23_de_Bruijn_Newman_constant_Polymath15|23 · De-Bruijn–Newman-Konstante]] — Lambda als Ausnahme: methodische statt rechnerische Wand.
> - *benutzt* → [[24_computational_verification|24 · Numerische Verifikation der Riemann-Vermutung]] — Direkte Nullstellenberechnung als Referenzmassstab.
> - ← *wird benutzt von* [[59_invariants_test_vectors|59 · Invarianten & Testvektoren]] — Ueberschuss-Test H stuetzt sich auf die gemessenen Reichweiten.

**Meta-Ebene:** [[55_failure_taxonomy|55 · Muster im Scheitern]] · [[56_failure_autopsies|56 · Autopsien]] · [[57_untried_directions|57 · Noch nicht versucht]] · [[58_gap_registry_near_miss|58 · Lücken]] · [[59_invariants_test_vectors|59 · Invarianten]] · [[60_counterexample_oracle|60 · Orakel]] · [[_Statusboard|Statusboard]]

<!-- OBSIDIAN-LINKS:END -->
