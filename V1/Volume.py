import cv2

# Ouvrir la webcam (index 0 pour la webcam par défaut)
cap = cv2.VideoCapture(1)

# Nommer la fenêtre d'affichage
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

# Boucle infinie pour lire les images de la webcam
while True:
    # Lire une image de la webcam
    ret, frame = cap.read()

    # Afficher l'image dans la fenêtre nommée
    cv2.imshow("Webcam", frame)

    # Définir la propriété de la fenêtre pour permettre la modification de la taille
    cv2.setWindowProperty("Webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

    # Déplacer la fenêtre en dehors de l'écran
    cv2.moveWindow("Webcam", -10000, -10000)

    # Attendre 1 milliseconde pour permettre l'affichage de l'image
    # Appuyer sur la touche 'q' pour quitter la boucle
    if cv2.waitKey(1) == ord('q'):
        break

# Libérer la ressource de la webcam et fermer les fenêtres d'affichage
cap.release()
cv2.destroyAllWindows()



