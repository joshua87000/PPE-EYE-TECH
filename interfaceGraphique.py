import pygame

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
width = 700
height = 700


ma_police = pygame.font.Font(None, 80)
# Définition du texte à afficher
mon_texte = ma_police.render("A", True, (255,255,255))

# Créer la fenêtre
screen = pygame.display.set_mode((width, height))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner le cercle
    center = (350,350)
    radius = 300
    color = (255, 0, 0) # Couleur rouge
    width = 2 # Epaisseur du contour
    pygame.draw.circle(screen, color, center, radius, width)
    screen.blit(mon_texte, (200, 200))


    pygame.draw.arc(screen, (0, 0, 255), (50, 50, 300, 200), 0, 6.14, 4)

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()
