# main_Aufgabe6.py

# Aufgabe 6

# Importierte Funktionen

# main_Aufgabe6.py
from classMod import SchoolFinance

def main():
    sf = SchoolFinance()
    while True:
        print("\nMenu:")
        print("A: Einkommen")
        print("B: Notendurchschnitt")
        print("C: Schulgeld berechnen")
        print("D: Exit")
        wahl = input("Ihre Wahl: ").upper()

        if wahl == 'A':
            sf.set_einkommen_console()  # methode für konsole
        elif wahl == 'B':
            sf.set_notendurchschnitt_console()  # nutze methode für konsole
        elif wahl == 'C':
            sf.set_schulgeld()
        elif wahl == 'D':
            break
        else:
            print("Ungültige Eingabe!")

if __name__ == '__main__':
    main()