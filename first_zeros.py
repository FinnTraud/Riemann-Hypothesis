"""Berechnet die ersten 3 nicht-trivialen Nullstellen der Riemannschen ζ-Funktion."""
import mpmath as mp

mp.mp.dps = 30  # Dezimalstellen Präzision

for n in range(1, 4):
    print(n, mp.zetazero(n).imag)
