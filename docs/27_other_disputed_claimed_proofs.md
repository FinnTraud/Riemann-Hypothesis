# Weitere umstrittene, zurückgezogene & fehlerhafte Beweisbehauptungen

**Kategorie:** Gescheiterte / umstrittene Beweise (Sammeldokument)
**Zeitraum:** laufend (Schwerpunkt 2000er–2020er)
**Typ:** Übersicht über nicht akzeptierte Behauptungen
**Status:** ❌ Keine dieser Behauptungen ist von der Fachwelt anerkannt; RH bleibt offen

## Zusammenfassung
Die Riemann-Vermutung zieht eine außergewöhnlich große Zahl an Beweis- (und Widerlegungs-)Behauptungen an — vom ernsthaften Forschungsprogramm bis zur offensichtlich fehlerhaften Einzelarbeit. **Stand Juni 2026 ist keine als gültig akzeptiert; die RH ist formal offen.** Dieses Dokument sammelt Muster und konkrete Beispiele; die prominenten Einzelfälle de Branges (Dok. 20), Atiyah (Dok. 25) und Nash (Dok. 26) haben eigene Dokumente.

## Typische Fehlerquellen (wiederkehrende Muster)
- **Unbegründeter Vertauschungsschritt:** unzulässiges Vertauschen von Grenzwert/Integral/Summe.
- **Nicht etablierte Positivität:** eine Positivitätsbedingung (Li/Weil-Typ, Dok. 14) wird behauptet, aber nicht bewiesen.
- **Zirkelschluss:** die zu beweisende Aussage wird (verdeckt) vorausgesetzt.
- **Falsche Verallgemeinerung:** ein für Spezialfälle gültiges Argument wird unzulässig auf den allgemeinen Fall ausgedehnt.
- **Numerik statt Beweis:** endliche numerische Evidenz wird als Beweis ausgegeben (vgl. Mertens-Warnung, Dok. 16).

## Konkrete Beispiele (2010er–2020er)
- **Frank Vega, "New Criterion for the Riemann Hypothesis" (Cambridge Open Engage):** 2023 **zurückgezogen**, nachdem der Autor selbst einen Fehler im Beweis (S. 7) einräumte.
- **L. Agélas, behaupteter GRH-Beweis:** **Richard P. Brent** zeigte 2021 in einer Notiz, dass die Arbeit einen Fehler enthält.
- **Diverse arXiv-Behauptungen** (Pro und Contra), u. a. "The Riemann Hypothesis is false" (arXiv 2006.12546), "The Disproof of the Riemann Hypothesis" (arXiv 2102.08313), "Hypothesis of Riemann is rejected by definition" (arXiv 2110.03253) — keine von der Fachwelt akzeptiert.
- **Jin Gyu Lee, behaupteter Beweis:** in einer separaten Notiz (arXiv 1305.4614) als fehlerhaft analysiert.
- **"Pseudodifferential arithmetic and a failed attempt on the Riemann hypothesis" (arXiv 2202.11652):** bemerkenswert, weil der Autor selbst den **gescheiterten** Versuch dokumentiert — lehrreich, wo genau solche Ansätze brechen.

## KI-/Physik-nahe Behauptungen
- Diverse Preprints leiten die RH aus physikalischen "Kopplungskonstanten-Spektren" oder ML-Mustern ab (z. B. arXiv 2103.02223, 0803.1818). Diese sind heuristisch/spekulativ und liefern keinen formalen Beweis (vgl. Dok. 28 zur kritischen Einordnung von KI-Ansätzen).

## Bedeutung / Einordnung
- Die schiere Menge an Fehlversuchen unterstreicht: Die RH ist **resistent gegen "einfache" Ideen**; jede vorgeschlagene Abkürzung wurde geprüft und verworfen.
- **Peer Review funktioniert:** Behauptungen werden systematisch geprüft; Fehler werden gefunden (oft binnen Tagen/Wochen).
- Praktischer Hinweis: Clay Mathematics Institute erkennt einen Millennium-Preis-Beweis erst nach Publikation in einer angesehenen Zeitschrift und mehrjähriger Bewährung in der Fachwelt an — nicht auf bloße Preprint-Ankündigung hin.

## Mathematischer Kern (typische Fehlermechanismen, an Formeln gezeigt)

### Fehlertyp 1 — unzulässige Vertauschung von Limes/Summe/Integral
Häufig wird die explizite Formel (Dok. 02) manipuliert, etwa
```
"ψ(x) − x = −Σ_ρ x^ρ/ρ"   →   (falsch) Σ_ρ x^ρ/ρ = O(x^{1/2}) "weil jeder Term ≤ x^{1/2}/|ρ|".
```
Der Fehler: Die Summe über ρ ist nur **bedingt** konvergent und nicht absolut; gliedweises Abschätzen ist ungültig. Ohne Kontrolle von Σ 1/|ρ| (divergent) kollabiert das Argument.

### Fehlertyp 2 — Positivität wird angenommen statt bewiesen
Bei Li/Weil-artigen Beweisen (Dok. 14) wird λ_n = Σ_ρ[1−(1−1/ρ)^n] ≥ 0 „gezeigt", indem die zu beweisende Lage Re(ρ)=1/2 in einem Zwischenschritt schon benutzt wird:
```
"(1 − 1/ρ) hat Betrag ≤ 1, also λ_n ≥ 0" — gilt nur, wenn Re(ρ) ≤ 1/2, also zirkulär.
```

### Fehlertyp 3 — falsche Verallgemeinerung
Ein für Re(s) > 1 (Eulerprodukt-Bereich, ζ ≠ 0) gültiges Argument wird unzulässig in den kritischen Streifen 0 < Re(s) < 1 fortgesetzt, wo das Eulerprodukt divergiert.

### Konkrete dokumentierte Fälle
- **Vega, „New Criterion for the RH"** (Cambridge Open Engage, 2023): vom Autor selbst zurückgezogen — fehlerhafter Schritt auf S. 7 (eine behauptete Ungleichung gilt nicht).
- **Agélas (GRH-Beweis):** Brent (arXiv 2103.09418) lokalisiert den Fehler in einer unzulässigen Abschätzung einer L-Funktions-Summe.
- **„The Riemann Hypothesis is false" (arXiv 2006.12546), „Disproof…" (2102.08313):** numerische/definitorische Missverständnisse; keine valide Konstruktion einer Off-Line-Nullstelle.
- **Jin Gyu Lee:** in arXiv 1305.4614 als fehlerhaft analysiert (Fehler in einer Konturverschiebung).
- **arXiv 2202.11652 (selbst-dokumentierter Fehlversuch):** zeigt explizit, an welcher Stelle ein pseudodifferentieller Operatoransatz die nötige Selbstadjungiertheit *nicht* liefert — lehrreich.

### Meta-Regel (Clay-Institut)
Ein Millennium-Beweis wird erst nach Publikation in einer angesehenen Zeitschrift **und** ~2 Jahren Bewährung in der Fachwelt anerkannt — nie auf bloße Preprint-Ankündigung.

## Quellen
- [Retracted: New Criterion for the Riemann Hypothesis — Cambridge Open Engage](https://www.cambridge.org/engage/coe/article-details/647ff4fe4f8b1884b7f34706)
- [On some results of Agelas concerning the GRH ... (Brent, arXiv 2103.09418)](https://arxiv.org/pdf/2103.09418)
- [Note on a proposed proof of the Riemann Hypothesis by Jin Gyu Lee (arXiv 1305.4614)](https://arxiv.org/pdf/1305.4614)
- [Pseudodifferential arithmetic and a failed attempt on the Riemann hypothesis (arXiv 2202.11652)](https://arxiv.org/pdf/2202.11652)
- [Millennium Prize Problems — Wikipedia](https://en.wikipedia.org/wiki/Millennium_Prize_Problems)
