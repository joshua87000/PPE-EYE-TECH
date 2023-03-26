from tkinter import *

def add_image(event):
    # Charger l'image depuis un fichier
    img = PhotoImage(file=r"C:\Users\Joshua\Downloads\youtubeLogo.png")

    # Ajouter l'image à la fenêtre
    label = Label(root, image=img)
    label.pack()

# Créer la fenêtre principale
root = Tk()

# Attacher l'événement à la touche 'v'
root.bind('<KeyPress-v>', add_image)

# Afficher la fenêtre
root.mainloop()


