# Li-Kriterium, Bombieri–Lagarias & Weil-Positivität

**Kategorie:** Äquivalentes Kriterium (Positivität)
**Autoren / Jahre:** André Weil (1952), Xian-Jin Li (1997), Enrico Bombieri & Jeffrey Lagarias (1999)
**Typ:** Zur RH äquivalente Positivitätsbedingungen
**Status:** Äquivalenzen bewiesen; Positivität allgemein unbewiesen

## Zusammenfassung
Eine Familie eng verwandter Kriterien formuliert die RH als **Positivitätsaussage**. Weils Kriterium nutzt die explizite Formel als quadratische Form; Lis Kriterium übersetzt die RH in die Nicht-Negativität einer expliziten Zahlenfolge λ_n; Bombieri–Lagarias zeigen, dass beide dasselbe bedeuten und geben eine arithmetische Formel.

## Li-Kriterium (1997)
- Definiere die **Li-Koeffizienten**:

```
λ_n = Σ_ρ [ 1 − (1 − 1/ρ)^n ]   (Summe über alle nicht-trivialen Nullstellen ρ)
```

- **Satz (Li):** Die RH ist äquivalent zu **λ_n ≥ 0 für alle n ≥ 1**.
- Die λ_n lassen sich auch über logarithmische Ableitungen der ξ-Funktion an ihren Nullstellen ausdrücken und sind numerisch berechenbar; alle bisher berechneten Werte sind positiv (konsistent mit RH), ein allgemeiner Beweis der Positivität fehlt.

## Bombieri–Lagarias (1999)
- Verallgemeinerten das Li-Kriterium auf beliebige Multimengen komplexer Zahlen mit gewissen Eigenschaften.
- Lieferten eine **arithmetische Formel** für die λ_n über die **Guinand–Weil-explizite Formel** und zeigten: Die Positivität der λ_n hat **dieselbe Bedeutung** wie Weils Positivitätskriterium.

## Weil-Positivität (Weils Kriterium, 1952)
- Weils explizite Formel verbindet eine Summe über Nullstellen mit einer Summe über Primzahlen plus archimedischen Termen.
- **Weils Kriterium:** Die RH gilt genau dann, wenn eine bestimmte zugehörige **quadratische Form positiv (semidefinit)** ist — die "Weil-Positivität".
- Diese Positivität ist der analytische Kern auch von **Connes' Spurformel-Programm** (Dok. 10): Connes' Reduktion der RH läuft letztlich auf den Nachweis genau dieser Positivität hinaus (vgl. Connes–Consani "Weil positivity and trace formula", 2021).

## Bedeutung / Einordnung
- Bündelt mehrere Programme (explizite Formel, Connes, de Branges) unter einem gemeinsamen **Positivitäts-Leitmotiv**.
- Macht die RH zu einer konkreten, prüfbaren (numerisch stark gestützten) Ungleichungsaussage.
- **Offen:** Der Nachweis der Positivität für *alle* n bzw. für die volle quadratische Form ist genauso schwer wie die RH selbst.

## Quellen
- [Complements to Li's Criterion for the Riemann Hypothesis — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022314X99923922)
- [On the explicit formula in the theory of prime numbers (World Scientific)](https://www.worldscientific.com/doi/10.1142/S1793042112500327)
- [An arithmetic interpretation of generalized Li's criterion (arXiv 1305.1421)](https://arxiv.org/pdf/1305.1421)
- [Li coefficients as norms of functions in a model space (arXiv 2301.05779)](https://arxiv.org/pdf/2301.05779)
