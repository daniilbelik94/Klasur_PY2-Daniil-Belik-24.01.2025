#schulgeldMod.py

# Aufgabe 1a & 1b
def schulgeld(einkommen, notendurchschnitt):
    if einkommen < 100000:
        prozent = 10.0
    elif 100000 <= einkommen <= 200000:
        prozent = 9.0
    elif 200000 < einkommen <= 500000:
        prozent = 7.5
    else:
        prozent = 6.5

    # so berechу ich den Grundbetrag
    grundbetrag = einkommen * prozent / 100
    grundbetrag = min(grundbetrag, 100000)  # Maximalbetrag anwenden

    # reduziere den Betrag um den Prozentsatz des Notendurchschnitts
    reduktion = (notendurchschnitt * grundbetrag) / 100
    endbetrag = grundbetrag - reduktion

    # runde auf eine Nachkommastelle
    return round(endbetrag, 1)

 # Aufgabe 1b

if __name__ == '__main__':
    tests = [
        (80000, 9.1),   # Beispiel
        (1500000, 5.7), # Beispiel
        (250000, 8.5)   # zusätzliche Tests
    ]
    for e, n in tests:
        betrag = schulgeld(e, n)
        # hier formatiere ich die Ausgabe
        print(f"Einkommen: {e} SFr, Notendurchschnitt: {n} → Schulgeld: {betrag:.1f} SFr")