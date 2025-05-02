def caesar_verschluesselung(text: str, verschiebung: int) -> str:
    """
    Verschlüsselt einen Text mit dem Caesar-Verschlüsselungsverfahren.
    
    :param text: Der zu verarbeitende Text
    :param verschiebung: Die Anzahl der Buchstaben, um die verschoben wird
    :return: Der verschlüsselte (oder entschlüsselte) Text
    """
    ergebnis = ''

    for zeichen in text:
        if zeichen.isalpha():
            verschoben = ord(zeichen) + verschiebung

            if zeichen.islower():
                if verschoben > ord('z'):
                    verschoben -= 26
                elif verschoben < ord('a'):
                    verschoben += 26
            elif zeichen.isupper():
                if verschoben > ord('Z'):
                    verschoben -= 26
                elif verschoben < ord('A'):
                    verschoben += 26

            ergebnis += chr(verschoben)
        else:
            # Sonderzeichen, Zahlen und Leerzeichen bleiben gleich
            ergebnis += zeichen

    return ergebnis


# --- Hauptprogramm ---
def main():
    # Benutzerwahl: Verschlüsselung oder Entschlüsselung
    modus = input("Möchtest du (v)erschlüsseln oder (e)ntschlüsseln? ").lower()

    if modus not in ['v', 'e']:
        print("Ungültige Auswahl. Bitte 'v' oder 'e' eingeben.")
        return

    text = input("Gib den Text ein: ")
    verschiebung = int(input("Gib die Verschiebung ein (z. B. 3 oder -3): "))

    # Bei Entschlüsselung Verschiebung invertieren
    if modus == 'e':
        verschiebung = -verschiebung

    ergebnis_text = caesar_verschluesselung(text, verschiebung)
    print("Ergebnis:", ergebnis_text)


# Nur ausführen, wenn das Skript direkt gestartet wird
if __name__ == "__main__":
    main()
