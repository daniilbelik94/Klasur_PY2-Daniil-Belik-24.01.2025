# tkinter_app.py


# Aufgabe 8


import tkinter as tk

def update_label():
    text = entry.get()        # text aus dem Entry-Widget
    label.config(text=text)   # text im Label anzeigen

# Main Window
root = tk.Tk()
root.title("Tkinter App")
root.geometry("400x400")


# Entry-Widget für Eingaben
entry = tk.Entry(root)
entry.pack(pady=10, padx=10,)

# Knopf zum Aktualisieren des Labels
button = tk.Button(root, text="Text übernehmen", command=update_label)
button.pack(pady=5)

# Label zur Anzeige des Texts
label = tk.Label(root, text="Hier wird Ihr Text angezeigt")
label.pack(pady=10)

root.mainloop()