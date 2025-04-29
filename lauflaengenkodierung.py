# Lauflängenkodierung
# ist ein Komprimierungsalgorithmus
# welches die Menge Digitaler Daten reduziert

""" Zählt gleiche, aufeinanderfolgende Zeichen.
    Speichert die Anzahl + das Zeichen.
    Arbeitet effizient ohne zusätzliche Libraries.
    Ergebnis: eine kürzere Darstellung des ursprünglichen Textes.
"""

def run_length_encoding(text):
    encoded_text = ""
    i = 0
    while i < len(text):
        count = 1
        c = text[i]
        j = i
        while j < len(text) - 1:
            if text[j] == text[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_text = encoded_text + str(count) + c
        i = j + 1
    return encoded_text

text = "aaaaabbbbbccccddddffff"
encoded_text = run_length_encoding(text)
print(encoded_text)
