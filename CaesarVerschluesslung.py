def caesar_verschluesselung(text, verschiebung):
    verschluesselt = ''
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
            verschluesselt += chr(verschoben)
        else:
            verschluesselt += zeichen
    return verschluesselt

text = input("Gib einen Text ein: ")
verschiebung = int(input("Gib die Verschiebung ein: "))
verschluesselter_text = caesar_verschluesselung(text, verschiebung)
print("Verschlüsselter Text:", verschluesselter_text)
