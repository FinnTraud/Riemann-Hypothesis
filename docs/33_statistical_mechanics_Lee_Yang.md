# Statistische Mechanik & Lee–Yang-Analogie (Newman)

**Kategorie:** Lösungsrelevante Analogie (mathematische Physik)
**Autoren / Jahre:** Lee & Yang (1952); Pólya; Charles Newman (1976, 2016er Mini-Kurs); de Bruijn
**Typ:** Physikalisch motivierter Reellwurzeligkeits-Ansatz
**Status:** Strukturelle Analogie; trägt Werkzeuge bei, kein Beweis

## Zusammenfassung
Es gibt eine tiefe Analogie zwischen der RH (Reellwurzeligkeit der ξ-Funktion) und dem **Lee–Yang-Theorem** der statistischen Mechanik (Nullstellen von Zustandssummen liegen auf einem Kreis/einer Geraden). Charles Newman entwickelte daraus einen statistisch-mechanischen Blick, der direkt zur **de-Bruijn–Newman-Konstante** (Dok. 23) führte und Werkzeuge zur Kontrolle reeller Nullstellen liefert.

## Die Analogie
- **Lee–Yang (1952):** Für bestimmte ferromagnetische Spin-Modelle liegen die Nullstellen der Zustandssumme (als Funktion der Fugazität/des Magnetfelds) exakt auf dem Einheitskreis bzw. der imaginären Achse — eine *erzwungene* Lage der Nullstellen aufgrund von Positivität/Korrelationsungleichungen.
- **RH-Parallele:** Die RH verlangt, dass die Nullstellen von ξ alle auf der reellen Achse (nach Drehung: kritische Gerade) liegen. ξ ist die Fourier-Transformierte einer **positiven, geraden** Funktion Φ.
- **Pólyas Programm:** Pólya untersuchte hinreichende Bedingungen dafür, dass Fourier-Transformierte positiver gerader Funktionen *nur reelle* Nullstellen haben — exakt die Lee–Yang-artige Frage, angewandt auf ξ.

## Newmans Beitrag & die Deformationsidee
- Newman (1976) führte die **Wärmeleitungs-Deformation** H_t der ξ-Funktion ein (Faltung von Φ mit einem Gauß-Kern) und bewies die Existenz der **de-Bruijn–Newman-Konstante Λ**: H_t hat genau dann nur reelle Nullstellen, wenn t ≥ Λ. RH ⟺ Λ ≤ 0 (Dok. 23).
- Werkzeuge aus der statistischen Mechanik (Korrelationsungleichungen, GHS-Ungleichung, Monotonie der Nullstellen unter dem Wärmefluss) liefern Kontrolle über die Nullstellenbewegung.
- **Lehmer-Paare** (extrem nahe beieinanderliegende Nullstellen) sind die "kritischen Konfigurationen", die zeigen, wie knapp die Reellwurzeligkeit erhalten bleibt — sie lieferten Rodgers–Tao (Dok. 23) den Hebel für Λ ≥ 0.

## Bedeutung / Einordnung
- Bringt **Positivitäts-/Korrelationswerkzeuge** der mathematischen Physik in die RH-Forschung ein — methodisch fruchtbar (de-Bruijn–Newman, Polymath15).
- Verbindet drei Stränge: Pólya/Laguerre–Pólya (Dok. 29), de-Bruijn–Newman (Dok. 23) und Random-Matrix/Quantenchaos (Dok. 06–08).
- **Grenze:** Liefert ein quantitatives "wie knapp" und starke Heuristik, aber keinen Mechanismus, der Λ ≤ 0 erzwingt — also keinen Beweis.

## Mathematischer Kern (Formeln, Sätze, Beweisskizzen)

### Lee–Yang-Theorem (1952)
Für ein ferromagnetisches Ising-Modell mit Zustandssumme als Polynom in der Fugazität z = e^{−2βh} (h = Magnetfeld):
```
Z_N(z) = Σ_{config} ... = c ∏_{k=1}^{N} (z − z_k).
```
**Satz (Lee–Yang).** Alle Nullstellen z_k liegen auf dem Einheitskreis |z_k| = 1 (äquivalent: rein imaginäres Feld h). Beweis nutzt Positivität der Kopplungen (Korrelationsungleichungen) — die Nullstellen werden durch Positivität auf eine Kurve gezwungen.

### Analogie zur ξ-Funktion
ξ ist die Fourier-(Laplace-)Transformierte der **positiven, geraden** Dichte Φ (Dok. 23):
```
ξ(1/2 + iz) = ∫_{−∞}^∞ Φ(u) e^{izu} du,   Φ(u) > 0, Φ(−u) = Φ(u).
```
RH = „alle Nullstellen z reell" ist die **exakte Entsprechung** des Lee–Yang-Phänomens (Nullstellen auf einer Geraden/Kurve, erzwungen durch Positivität von Φ).

### Pólyas Kriterium (hinreichende Bedingung)
**Satz (Pólya).** Ist Φ(u) > 0 gerade und erfüllt gewisse Konvexitäts-/log-Konkavitätsbedingungen (Φ ∈ geeignete Klasse), so hat ∫ Φ(u)e^{izu}du nur reelle Nullstellen. Das tatsächliche Φ für ξ erfüllt diese hinreichenden Bedingungen *nicht* nachweislich — genau hier klafft die Lücke.

### Wärmefluss und Newmans Λ (Verbindung zu Dok. 23)
Falte Φ mit Gauß-Kern (Wärmeleitung): Φ_t(u) = e^{t u²}-Gewichtung ⇒ H_t(z) = ∫ e^{tu²}Φ(u)e^{izu}du. Die Nullstellen z_k(t) erfüllen eine Gradientenfluss-ODE
```
dz_k/dt = − Σ_{j≠k} 2/(z_k − z_j)   (Calogero-artige Dynamik / „Coulomb-Gas" auf der Geraden).
```
Reelle Nullstellen sind ein Fixpunkt dieser Dynamik für t ≥ Λ. **GHS-Ungleichung** und Monotonie liefern Kontrolle ⇒ Newmans Λ existiert, Λ ≤ 0 ⟺ RH.

### Lehmer-Paare als kritische Konfigurationen
Zwei Nullstellen γ_n, γ_{n+1} mit Abstand ≪ Mittelwert bilden ein **Lehmer-Paar**; im Coulomb-Gas-Bild sind sie „fast kollidierende" Teilchen. Ihre Existenz (z. B. bei γ ≈ 7005,06) zeigt, dass die Reellheit nur knapp gehalten wird — der Hebel für Rodgers–Tao Λ ≥ 0 (Dok. 23).

## Quellen
- [2016 Mini-Course by Chuck Newman — Statistical Mechanics and the Riemann Hypothesis (NYU Shanghai)](https://research.shanghai.nyu.edu/centers-and-institutes/math/2016-mini-course-chuck-newman-statistical-mechanics-and-riemann)
- [Constants of de Bruijn-Newman type in analytic number theory and statistical physics (arXiv 1901.06596)](https://arxiv.org/pdf/1901.06596)
- [Schoenberg's Theory of Totally Positive Functions and the Riemann Zeta Function (arXiv 2007.12889)](https://arxiv.org/pdf/2007.12889)
- [Lehmer pairs of zeros, the de Bruijn-Newman constant Λ, and the Riemann Hypothesis (ResearchGate)](https://www.researchgate.net/publication/226697760_Lehmer_pairs_of_zeros_the_de_Bruijn-Newman_constant_L_and_the_Riemann_Hypothesis)
- [The early historical roots of Lee-Yang theorem (arXiv 1410.6450)](https://arxiv.org/pdf/1410.6450)
