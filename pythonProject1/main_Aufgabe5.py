# main_Aufgabe5.py

# Aufgabe 5

from schulgeldMod import schulgeld

def set_schulgeld(einkommen=200000, notendurchschnitt=5.1):
    # Berechne das Schulgeld und gib es formatiert aus
    if einkommen is None or notendurchschnitt is None:
        print("Fehler: Einkommen oder Notendurchschnitt fehlt!")
        return

    # Berechne das Schulgeld und gib es formatiert aus
    betrag = schulgeld(einkommen, notendurchschnitt)
    print(f"Jährliches Schulgeld: {betrag:.1f} SFr")  # formatierte Ausgabe