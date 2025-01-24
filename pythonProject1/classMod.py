# classMod.py

# Aufgabe 7

# classMod.py
from schulgeldMod import schulgeld

class SchoolFinance:
    def __init__(self):
        self.einkommen = None
        self.notendurchschnitt = None

    # methods for GUI
    def set_einkommen(self, einkommen):
        self.einkommen = einkommen

    def set_notendurchschnitt(self, note):
        self.notendurchschnitt = note

    # method for console
    def set_einkommen_console(self):
        while True:
            eingabe = input("Einkommen (SFr) oder 'q' zum Beenden: ").strip()
            if eingabe.lower() == 'q':
                return
            try:
                einkommen = float(eingabe)
                if einkommen >= 50000:
                    self.einkommen = einkommen
                    print(f"Einkommen gespeichert: {einkommen} SFr")
                    return
                else:
                    print("Fehler: Einkommen muss ≥ 50.000 SFr!")
            except ValueError:
                print("Fehler: Ungültige Zahleneingabe!")

    def set_notendurchschnitt_console(self):
        while True:
            eingabe = input("Notendurchschnitt (1.0-10.0) oder 'q' zum Beenden: ").strip()
            if eingabe.lower() == 'q':
                return
            try:
                note = float(eingabe)
                if 1.0 <= note <= 10.0:
                    self.notendurchschnitt = note
                    print(f"Note gespeichert: {note}")
                    return
                else:
                    print("Fehler: Note muss zwischen 1.0 und 10.0 liegen!")
            except ValueError:
                print("Fehler: Ungültige Zahleneingabe!")

    def set_schulgeld(self):
        if self.einkommen is None or self.notendurchschnitt is None:
            print("Fehler: Einkommen oder Note fehlt!")
            return None
        betrag = schulgeld(self.einkommen, self.notendurchschnitt)
        print(f"Schulgeld: {betrag:.1f} SFr")
        return betrag