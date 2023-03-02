import pygame
import math

# Initialiser Pygame
pygame.init()

# Créer une fenêtre avec une taille de 400x400 pixels
screen = pygame.display.set_mode((400, 400))

# Initialiser les coordonnées du cercle
x, y = 100, 100

# Initialiser la destination du cercle
destination = (100, 100)

# Vitesse de déplacement du cercle (en pixels par frame)
speed = 1

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mettre à jour la destination avec les coordonnées de la souris
            destination = event.pos

    # Calculer la distance entre le cercle et sa destination
    distance = math.sqrt((destination[0] - x)**2 + (destination[1] - y)**2)

    # Si le cercle n'a pas atteint sa destination
    if distance > speed:
        # Calculer la direction vers laquelle se déplacer
        direction = math.atan2(destination[1] - y, destination[0] - x)

        # Mettre à jour les coordonnées du cercle en se déplaçant dans la direction déterminée
        x += speed * math.cos(direction)
        y += speed * math.sin(direction)

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Dessiner le cercle
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 50, 5)

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()
