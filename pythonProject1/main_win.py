# main_win.py

# aufgabe 7
# tkinter GUI
import tkinter as tk
from classMod import SchoolFinance

class App:
    def __init__(self, root):
        self.sf = SchoolFinance()
        self.root = root
        self.root.geometry("400x300")

        # widgets für Eingabe
        self.entry_einkommen = tk.Entry(root)
        self.entry_einkommen.pack(pady=5)

        self.entry_note = tk.Entry(root)
        self.entry_note.pack(pady=5)

        # widgets für Ausgabe
        self.label_einkommen = tk.Label(root, text="Einkommen: -")
        self.label_einkommen.pack(pady=5)

        self.label_note = tk.Label(root, text="Notendurchschnitt: -")
        self.label_note.pack(pady=5)

        self.label_schulgeld = tk.Label(root, text="Schulgeld: -")
        self.label_schulgeld.pack(pady=5)

        # knöpfe
        btn_einkommen = tk.Button(root, text="Einkommen speichern", command=self.save_einkommen)
        btn_einkommen.pack(pady=5)

        btn_note = tk.Button(root, text="Note speichern", command=self.save_note)
        btn_note.pack(pady=5)

        btn_schulgeld = tk.Button(root, text="Schulgeld berechnen", command=self.calculate_schulgeld)
        btn_schulgeld.pack(pady=5)

    def save_einkommen(self):
        try:
            einkommen = float(self.entry_einkommen.get())
            if einkommen >= 50000:
                self.sf.set_einkommen(einkommen)
                self.label_einkommen.config(text=f"Einkommen: {einkommen} SFr", fg="black")
                print(f"Einkommen gespeichert: {einkommen} SFr")
            else:
                error_msg = "Einkommen muss ≥ 50.000 SFr!"
                print(error_msg)
                self.label_einkommen.config(text=error_msg, fg="red")
        except ValueError:
            error_msg = "Ungültige Eingabe!"
            print(error_msg)
            self.label_einkommen.config(text=error_msg, fg="red")

    def save_note(self):
        try:
            note = float(self.entry_note.get())
            if 1.0 <= note <= 10.0:
                self.sf.set_notendurchschnitt(note)
                self.label_note.config(text=f"Notendurchschnitt: {note}", fg="black")
                print(f"Note gespeichert: {note}")
            else:
                error_msg = "Note muss zwischen 1.0 und 10.0 liegen!"
                print(error_msg)
                self.label_note.config(text=error_msg, fg="red")
        except ValueError:
            error_msg = "Ungültige Eingabe!"
            print(error_msg)
            self.label_note.config(text=error_msg, fg="red")

    def calculate_schulgeld(self):
        betrag = self.sf.set_schulgeld()
        if betrag is None:
            error_msg = "Fehler: Einkommen oder Note fehlt!"
            print(error_msg)
            self.label_schulgeld.config(text=error_msg, fg="red")
        else:
            self.label_schulgeld.config(text=f"Schulgeld: {betrag:.1f} SFr", fg="black")
            print(f"Berechnetes Schulgeld: {betrag:.1f} SFr")

root = tk.Tk()
app = App(root)
root.mainloop()