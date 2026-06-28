# Connes–Moscovici: Prolate-Spheroidal-Operator und Zeta (2021–2022)

**Kategorie:** Spektraler Ansatz / nichtkommutative Geometrie (jüngste Entwicklung)
**Autoren / Jahr:** Alain Connes & Henri Moscovici (2021–2022); verwandt: Connes–Consani "Spectral triples and ζ-cycles" (2021)
**Typ:** Konkrete (approximative) Hilbert–Pólya-Operator-Realisierung
**Status:** Aktive Forschung; "annähernde" Operator-Lösung, kein vollständiger RH-Beweis

## Zusammenfassung
Connes und Moscovici untersuchten ab 2021 das Spektrum des **Prolate-Spheroidal-Wellenoperators** (ein klassischer Differentialoperator aus der Signalverarbeitung / Bandbegrenzung, ursprünglich von Slepian, Landau, Pollak an den Bell Labs studiert) und zeigten, dass dessen Spektrum eng mit den **Quadraten der Riemann-Nullstellen** zusammenhängt. Sie beschreiben dies als eine **konkrete, annähernde Realisierung der Hilbert–Pólya-Vermutung**.

## Kernidee
- Der **Prolate-Operator** ist ein expliziter, gut studierter selbstadjungierter Differentialoperator zweiter Ordnung.
- Schränkt man ihn auf das Komplement eines endlichen Intervalls ein, so besitzt er **negative Eigenwerte**, deren Ultraviolett-Verhalten (asymptotisches Wachstum) genau dem der **Quadrate der ζ-Nullstellen** entspricht.
- Auf einem größeren Definitionsbereich eindeutig selbstadjungiert fortgesetzt, sind die Eigenwerte asymptotisch ähnlich zu den Quadraten der Nullstellen; eine geeignete "Quadratwurzel" dieses Operators liefert damit einen Operator, der die Hilbert–Pólya-Vermutung **näherungsweise** löst.
- Eingebettet in das **semilokale Spurformel-Framework** von Connes (Dok. 10): ein semilokales Analogon des Prolate-Wellenoperators integriert zwei jüngere Entdeckungen zur spektralen Realisierung der Nullstellen.

## Bedeutung / Einordnung
- Erstmals ein **klassischer, explizit bekannter** Operator (kein ad-hoc konstruierter), dessen Spektrum strukturell die Nullstellen widerspiegelt — methodisch bemerkenswert.
- Verbindet Signalverarbeitung / Spektraltheorie / nichtkommutative Geometrie / Zahlentheorie.
- **Einschränkung:** Die Übereinstimmung ist asymptotisch/approximativ ("ultraviolettes Verhalten", "annähernde Lösung"). Eine *exakte* spektrale Realisierung *aller* Nullstellen samt Beweis der RH ist damit **nicht** erreicht.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Der Prolate-Wellenoperator
Klassischer Slepian–Landau–Pollak-Operator auf L²(−1,1), kommutierend mit der bandbegrenzten Fourier-Projektion:
```
(W_λ f)(x) = d/dx [ (1 − x²) df/dx ] + λ² x² f
```
W_λ ist selbstadjungiert mit diskretem Spektrum; seine Eigenfunktionen sind die **prolaten Sphäroidwellenfunktionen** (PSWF). Connes–Moscovici untersuchen die Einschränkung auf das **Komplement** eines Intervalls.

### Schlüsselresultat (asymptotisches Spektrum)
Für die selbstadjungierte Fortsetzung des auf das Außenintervall eingeschränkten Operators gilt: die negativen Eigenwerte −E_n erfüllen asymptotisch (Ultraviolett-Verhalten)
```
E_n  ~  (γ_n / 2)²   bzw.   die Zählfunktion der E_n  ≈  Zählfunktion der  γ_n²
```
wobei γ_n die Imaginärteile der nicht-trivialen Nullstellen sind. D. h.: das Spektrum reproduziert die **Quadrate der Riemann-Nullstellen**.

### Quadratwurzel ⇒ approximative Hilbert–Pólya-Lösung
Definiert man (heuristisch) den Operator √(Prolate) auf dem passenden Teilraum, so hat dieser Eigenwerte ≈ γ_n/2 — ein konkreter selbstadjungierter Operator, dessen Spektrum die γ_n *approximiert*. Wegen Selbstadjungiertheit sind diese reell (das war stets das Ziel, Dok. 05). Daher: „konkrete annähernde Realisierung der Hilbert–Pólya-Vermutung".

### Einbettung in die semilokale Spurformel
Connes setzt dies in das **semilokale** Framework (endlich viele Stellen S = {∞, p_1, …, p_k}): ein semilokaler Prolate-Operator W_S, dessen Spurformel die explizite Formel über S realisiert (vgl. Dok. 10). Die zu erreichende Aussage bleibt die globale Positivität.

### Warum nur approximativ
Die Übereinstimmung E_n ~ (γ_n/2)² ist **asymptotisch** (führende Ordnung im UV); die exakte Identität des Spektrums mit allen γ_n — und damit RH — ist nicht etabliert. Korrekturterme und die Niederenergie-Region sind nicht kontrolliert.

## Quellen
- [Prolate spheroidal operator and Zeta — Connes & Moscovici (arXiv 2112.05500)](https://arxiv.org/pdf/2112.05500)
- [Prolate operator and Riemann Zeta — Connes (PNAS)](https://alainconnes.org/wp-content/uploads/PNAS_030322.pdf)
- [Prolate spheroidal functions and zeta — Alain Connes (Blog)](https://alainconnes.org/2021/12/prolate-spheroidal-functions-and-zeta/)
- [Zeta cycles — Connes–Consani (arXiv 2106.01715)](https://alainconnes.org/wp-content/uploads/zeta-cycles-3.pdf)
- [The Hilbert-Pólya Conjecture and the Prolate Spheroidal Operator (TU Delft thesis)](https://repository.tudelft.nl/file/File_a03b023e-2ba7-45fb-bde9-6fcc7a53d306)
