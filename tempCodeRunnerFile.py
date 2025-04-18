platzbelegung = [True, False, True, False, False]

anzahlGesamt = len(platzbelegung)
i = 0
anzahlBelegt = 0

while i < anzahlGesamt:
    if platzbelegung[i] == True:
        anzahlBelegt = anzahlBelegt + 1
    i = i + 1

belegungProzent = (100 * anzahlBelegt) / anzahlGesamt
print(belegungProzent)