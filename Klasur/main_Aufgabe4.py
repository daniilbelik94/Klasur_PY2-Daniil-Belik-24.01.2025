#main_Aufgabe4.py

# Aufgabe 4

def set_notendurchschnitt():
    while True:

        eingabe = input("Notendurchschnitt (1.0-10.0) oder 'q' zum Beenden: ").strip()
        if eingabe.lower() == 'q':
            return None

        try:
            note = float(eingabe)  # konvertiere eingabe zu Float
            # pruefe ob die Note im Bereich 1.0 bis 10.0 liegt
            if 1.0 <= note <= 10.0:
                return note
            else:
                print("Fehler: Note muss zwischen 1.0 und 10.0 liegen!")
        except ValueError:
            print("Fehler: Ungültige Zahleneingabe!")  # fange falsche Eingaben ab