import pygame
from pygame.locals import *
import time
import random

#################
# @AntoSoulaire #
#################

# Initialisation de pygame, qui permettra l'affichage dans une fenêtre
pygame.init()

# Définition de la taille de la fenêtre
window = pygame.display.set_mode([640, 360])

# Définition du nom affiché au dessus de la fenêtre
pygame.display.set_caption('Loading')

# Génération du nombre aléatoire (définissant la vitesse de chargement
ran = random.randint(6, 10) * 10

# Initialisation de la largeur de la future barre de chargement, et du % de chargement
rec = 0
pourc = 0

# Définition des couleurs utilisées, en mode RGB
white2 = (250, 250, 250)
lgrey = (150, 150, 150)
dgrey = (58, 58, 58)

# Boucle du jeu
while True:
    
    # Si on clique sur la croix rouge, la fenêtre se ferme
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Le if est nécessaire pour ne pas créer une boucle infinie (sinon la barre de chargement reprend de 0 en boucle)
    if rec == 0:

        # Pour la durée du chargement
        for i in range(ran):

            # Calcul du % d'avancement
            pourc = int(((i + 1) / ran) * 100)

            # On note la valeur da la largeur précédente pour pouvoir ajouter une transition entre l'ancienne
            # Et la nouvelle valeur de rec (de pixel en pixel, au lieu d'ajouter 4 pixels à chaque nouveau %
            oldrec = rec

            # La barre fait 400 pixels de large, sa largeur sera donc de 4 pixels / pourcent
            rec = pourc * 4

            # La couleur du fond de la fenêtre sera gris foncé
            window.fill(dgrey)

            # Ici on dessine la barre donnant une idée de la distance qu'il reste à parcourir à la barre de chargement
            # Elle sera grise, et dessinée entre le background et la barre de chargement
            # Elle a les mêmes dimensions que la barre de chargement une fois cette dernière à 100%
            pygame.draw.rect(window, lgrey, Rect((120, 170), (400, 20)))

            # Cette boucle while sert à l'état de transition. Elle permet, comme expliqué plus haut, une transition
            # Plus fluide, pixel par pixel, et non pas % par % (ce qui ferait 4 pixels par 4 pixels)
            while oldrec < rec:

                # La manière dont le % au dessus de la barre sera affiché, on convertit le pourcentage en string
                # Et on lui ajouter le symbole '%' derrière
                text_display = str(pourc) + '%'

                # Définition de la police et de la taille du texte
                font = pygame.font.Font('freesansbold.ttf', 32)

                # Définition du contenu et de la couleur du texte
                text = font.render(text_display, True, white2, dgrey)

                # Définition du rectangle du text, et de la position de son centre
                textRect = text.get_rect()
                textRect.center = (320, 150)

                # Affichage du texte
                window.blit(text, textRect)

                # Pause d'un soixantième de seconde, permettant une transition fluide
                time.sleep(1/60)

                # Incrémentation de la valeur du oldrec, jusqu'à ce qu'il soit égal à rec (4 fois par boucle donc)
                oldrec += 1

                # Définition et affichage de la barre de chargement
                pygame.draw.rect(window, white2, Rect((120, 170), (oldrec, 20)))
                pygame.display.update()

    # Lorsque le chargement est terminé, on laisse la barre finale affichée, dans la pratique on continuerait
    # Vers la suite de notre programme
    pygame.draw.rect(window, white2, Rect((120, 170), (400, 20)))
    pygame.display.update()
