# main_Aufgabe5.py

# Aufgabe 5

from schulgeldMod import schulgeld

def set_schulgeld(einkommen=200000, notendurchschnitt=5.1):
    # berechnet und gibt das Schulgeld aus
    if einkommen is None or notendurchschnitt is None:
        print("Fehler: Einkommen oder Notendurchschnitt fehlt!")
        return

    # gleiches wie in set_schulgeld()
    betrag = schulgeld(einkommen, notendurchschnitt)
    print(f"Jährliches Schulgeld: {betrag:.1f} SFr")  # formatierte Ausgabe