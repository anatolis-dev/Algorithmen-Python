# Bubblesort
# Der größte Wert "wandert" bei jedem Durchlauf nach hinten.
# Es wird so oft verglichen und getauscht, bis die Liste vollständig sortiert ist.

def bubble_sort(liste):
    n = len(liste)
    # Durchlaufe alle Elemente der Liste
    for i in range(n):
        # Letzte i Elemente sind schon an der richtigen Stelle
        for j in range(0, n-i-1):
            # Tausche, falls das aktuelle Element größer ist als das nächste
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Beispiel:
zahlen = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(zahlen)
print("Sortierte Liste:", zahlen)
