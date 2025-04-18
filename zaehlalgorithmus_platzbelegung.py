
"""
Zählalgorithmus – Platzbelegung

Berechnung prozentualen Anteil belegter Plätze in einer Liste.
"""

plaetze = [1, 0, 1, 1, 0, 0, 1]  # 1 = belegt, 0 = frei

anzahl_belegt = 0
index = 0

while index < len(plaetze):
    if plaetze[index] == 1:
        anzahl_belegt += 1
    index += 1

anteil = (anzahl_belegt / len(plaetze)) * 100
print(f"Belegte Plätze: {anzahl_belegt} von {len(plaetze)} ({anteil:.2f}%)")
