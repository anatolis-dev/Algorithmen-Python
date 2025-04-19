
# Funktion zur Umwandlung einer Dezimalzahl in eine Binärzahl (rekursiv)

def dez_to_bin(number):
    if number < 0:
        return "Zahl muss positiv sein"
    n = number // 2
    r = number % 2
    if n == 0:
        return str(r)
    else:
        return dez_to_bin(n) + str(r)
    
number = int(input("Positive Zahl eingeben: "))
print(dez_to_bin(number))
    
"""
# Code beschreibung

def dez_to_bin(number):

    # Überprüfen, ob die Eingabe negativ ist
    if number < 0:
        return "Zahl muss positiv sein"

    # Ganzzahlige Division durch 2 → ergibt den nächsten Wert für den rekursiven Aufruf
    n = number // 2

    # Modulo 2 → ergibt den aktuellen Binärstellenwert (0 oder 1)
    r = number % 2

    # Rekursionsabbruch: Wenn n == 0, dann ist das die letzte Ziffer (r)
    if n == 0:
        return str(r)
    else:
        # Rekursiver Aufruf für n, hänge r als letzte Binärstelle an
        return dez_to_bin(n) + str(r)

# Nutzereingabe: positive Zahl einlesen
number = int(input("Positive Zahl eingeben: "))

# Ausgabe der Binärdarstellung
print(dez_to_bin(number))
"""