from tkinter import *

# Créer une fenêtre
root = Tk()

# Changer le titre de la fenêtre
root.title("Mon application")

width = 300
height = 130
root.geometry("%dx%d" % (width, height))

root.attributes('-alpha', 0.5)

# Ouvrir l'image
image = PhotoImage(file=r"C:\Users\Joshua\Downloads\youtubeLogo.png")

# Afficher l'image dans un label
label = Label(root, image=image)
label.pack()

# Définir une fonction pour détecter quand la souris entre dans la fenêtre
def enter(event):
    root.attributes('-alpha', 1.0)

# Définir une fonction pour détecter quand la souris sort de la fenêtre
def leave(event):
    root.attributes('-alpha', 0.5)

# Associer les fonctions aux événements de la souris sur la fenêtre
root.bind('<Enter>', enter)
root.bind('<Leave>', leave)

# Lancer la boucle d'événements
root.mainloop()

