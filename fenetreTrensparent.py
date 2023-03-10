from tkinter import *

root = Tk()
root.attributes("-alpha", 0.5)  # Règle la transparence de la fenêtre (0 = complètement transparent, 1 = complètement opaque)

def move_window():
    root.geometry("300x200+200+200")  # Déplace la fenêtre à la position x=200 et y=200

btn = Button(root, text="Déplacer la fenêtre", command=move_window)
btn.pack()

root.mainloop()



