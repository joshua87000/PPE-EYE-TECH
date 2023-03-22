from tkinter import *
from tkinter.ttk import *
import time
import win32gui

def recherche_chaine(chaine1, chaine2):
    if chaine1 in chaine2:
        return 1
    else:
        return 0


# Créer une fenêtre
root = Tk()

# Changer le titre de la fenêtre
root.title("Ma fenêtre")

width = 300
height = 130
root.geometry("%dx%d" % (width, height))

# Définir le niveau de transparence de la fenêtre (50%)
root.attributes('-alpha', 0.5)

root.attributes("-topmost", True)

# Ouvrir l'image

LogoYoutube = PhotoImage(file=r"C:\Users\Joshua\Downloads\youtubeLogo.png")
LogoChrome = PhotoImage(file=r"C:\Users\Joshua\Downloads\logoChrome.png")

image = LogoChrome



# Afficher l'image dans un label
label = Label(root, image=image)
label.pack()

# Définir la durée de l'animation en millisecondes
duration = 250

# Définir une fonction pour détecter quand la souris entre dans la fenêtre
def enter(event):
    # Obtenir l'opacité actuelle de la fenêtre
    current_opacity = root.attributes('-alpha')
    
    # Définir la cible de l'opacité à 100%
    target_opacity = 1.0
    
    # Calculer la différence entre l'opacité actuelle et la cible
    opacity_difference = target_opacity - current_opacity
    
    # Définir le nombre de frames pour atteindre la cible d'opacité
    frames = int(duration / 20)
    
    # Calculer l'incrément d'opacité pour chaque frame
    opacity_increment = opacity_difference / frames
    
    # Créer une animation pour changer progressivement l'opacité
    for i in range(frames):
        opacity = current_opacity + opacity_increment * i
        root.attributes('-alpha', opacity)
        root.update_idletasks()
        time.sleep(duration / frames / 1000)

# Définir une fonction pour détecter quand la souris sort de la fenêtre
def leave(event):
    # Obtenir l'opacité actuelle de la fenêtre
    current_opacity = root.attributes('-alpha')
    
    # Définir la cible de l'opacité à 50%
    target_opacity = 0.5
    
    # Calculer la différence entre l'opacité actuelle et la cible
    opacity_difference = target_opacity - current_opacity
    
    # Définir le nombre de frames pour atteindre la cible d'opacité
    frames = int(duration / 20)
    
    # Calculer l'incrément d'opacité pour chaque frame
    opacity_increment = opacity_difference / frames
    
    # Créer une animation pour changer progressivement l'opacité
    for i in range(frames):
        opacity = current_opacity + opacity_increment * i
        root.attributes('-alpha', opacity)
        root.update_idletasks()
        time.sleep(duration / frames / 1000)

def update_App():
   
    global LogoYoutube
    global LogoChrome

    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
    print(window_title)

    if(recherche_chaine(window_title,"Youtube") == 1):
         label.configure(image=LogoYoutube)

   
   
    
    # Ajouter la fonction à la file d'attente des événements pour qu'elle soit exécutée toutes les 3 secondes
    root.after(3000, update_App)

# Appeler la fonction pour la première fois
update_App()

# Associer les fonctions aux événements de la souris sur la fenêtre
root.bind('<Enter>', enter)
root.bind('<Leave>', leave)

# Lancer la boucle d'événements
root.mainloop()
