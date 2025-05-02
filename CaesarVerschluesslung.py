def caesar_verschluesselung(text: str, verschiebung: int) -> str:
    """
    Verschlüsselt einen Text mithilfe des Caesar-Verschlüsselungsverfahrens.
    
    :param text: Der zu verschlüsselnde Text
    :param verschiebung: Anzahl der Stellen, um die jeder Buchstabe verschoben wird
    :return: Der verschlüsselte Text
    """
    verschluesselt = ''
    
    for zeichen in text:
        # Prüfen, ob das Zeichen ein Buchstabe ist
        if zeichen.isalpha():
            # ASCII-Wert des Zeichens um die Verschiebung erhöhen
            verschoben = ord(zeichen) + verschiebung

            # Verarbeitung für Kleinbuchstaben
            if zeichen.islower():
                if verschoben > ord('z'):
                    verschoben -= 26
                elif verschoben < ord('a'):
                    verschoben += 26

            # Verarbeitung für Großbuchstaben
            elif zeichen.isupper():
                if verschoben > ord('Z'):
                    verschoben -= 26
                elif verschoben < ord('A'):
                    verschoben += 26

            # In verschlüsselten Text hinzufügen
            verschluesselt += chr(verschoben)
        else:
            # Nicht-Buchstaben unverändert übernehmen
            verschluesselt += zeichen

    return verschluesselt


# Benutzereingaben
text = input("Gib einen Text ein: ")
verschiebung = int(input("Gib die Verschiebung ein (z. B. 3 oder -3): "))

# Verschlüsselung ausführen und Ergebnis ausgeben
verschluesselter_text = caesar_verschluesselung(text, verschiebung)
print("Verschlüsselter Text:", verschluesselter_text)
