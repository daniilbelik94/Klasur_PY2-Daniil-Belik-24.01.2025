# main_Aufgabe3.py

# Aufgabe 3

def set_einkommen():
    while True:

        eingabe = input("Einkommen (SFr) oder 'q' zum Beenden: ").strip()
        if eingabe.lower() == 'q':
            return None  # Beenden der Funktion

        try:
            einkommen = float(eingabe)  # konvertiere in float und prüfen auf Gültigkeit
            if einkommen >= 50000:
                return einkommen
            else:
                print("Fehler: Einkommen muss mindestens 50.000 SFr betragen!")
        except ValueError:
            print("Fehler: Ungültige Zahleneingabe!")  # hier wird die falsche Eingabe gefangen