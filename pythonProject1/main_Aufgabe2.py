#main_Aufgabe2.py

# Aufgabe 2
def set_einkommen():
    pass

def set_notendurchschnitt():
    pass

def set_schulgeld():
    pass

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("A: Einkommen")
        print("B: Notendurchschnitt")
        print("C: Schulgeld")
        print("D: Exit")
        wahl = input("Ihre Wahl: ").upper()

        if wahl == 'A':
            set_einkommen()  # für Einkommen
        elif wahl == 'B':
            set_notendurchschnitt()  # für Notendurchschnitt
        elif wahl == 'C':
            set_schulgeld()  # Schulgeld
        elif wahl == 'D':
            break
        else:
            print("Ungültige Eingabe!")  # falscher Eingabe


if __name__ == '__main__':
    main()