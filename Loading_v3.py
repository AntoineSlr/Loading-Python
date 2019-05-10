import pygame
from pygame.locals import *

# Initialisation de pygame, qui permettra l'affichage dans une fenêtre
pygame.init()

# Définition de la taille de la fenêtre
window = pygame.display.set_mode([640, 360])

# Définition du nom affiché au dessus de la fenêtre
pygame.display.set_caption('Loading')

# Définition des voyelles en minuscule et consonnes en majuscule
# Les mots de passe générés dans cet exemple sont composés d'une consonne en majuscule suivie de 4 voyelles en minuscule
maj = "BCDFGHJKLMNPQRSTVWXZ"
mina = "aeiouy"

# Définition du nombre total de mots de passe à écrire (20 * 6 * 6 * 6 * 6)
total = 25920

# Ouverture du fichier txt dans lequel seront écrits les mots de passe
fo = open("passwords.txt", "w+")

# Initialisation de la largeur de la future barre de chargement
rec = 0

# Initialisation du % de chargement
pourc = 0

# Initialisation du nombre de mots de passe déjà écrits dans le fichier
av = 0

# Définition des couleurs utilisées, en mode RGB
white2 = (250, 250, 250)  # Presque du blanc
lgrey = (150, 150, 150)  # Gris clair
dgrey = (58, 58, 58)  # Gris foncé

# Boucle du 'jeu'
while True:

    # Si on clique sur la croix rouge, la fenêtre se ferme
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Ce if est nécessaire pour ne pas créer une boucle infinie (sinon la barre de chargement reprend de 0 en boucle)
    if rec == 0:
        # Pour la durée de la création des mots de passe
        for a in range(len(maj)):
            for b in range(len(mina)):
                for c in range(len(mina)):
                    for d in range(len(mina)):
                        for e in range(len(mina)):

                            # Incrémentation du nombre de mots de passe calculés
                            av += 1
                            
                            # Calcul du % d'avancement
                            pourc = float((av / total) * 100)

                            password = []
                            mdp = ""
                            for i in range(5):
                                password.append('-')
                            password[0] = maj[a]
                            password[1] = mina[b]
                            password[2] = mina[c]
                            password[3] = mina[d]
                            password[4] = mina[e]
                            for i in range(5):
                                mdp += password[i]

                            fo.write("{}\n".format(mdp))

                            # La barre fait 400 pixels de large, sa largeur sera donc de 4 pixels / pourcent
                            rec = pourc * 4

                            # La couleur du fond de la fenêtre sera gris foncé
                            window.fill(dgrey)

                            # Ici on dessine la barre donnant une idée de la distance qu'il reste à
                            # parcourir à la barre de chargement elle sera grise, et dessinée entre le
                            # background et la barre de chargement. Elle a les mêmes dimensions que la barre
                            # de chargement une fois cette dernière à 100%

                            pygame.draw.rect(window, lgrey, Rect((120, 170), (400, 20)))

                            # La manière dont le % au dessus de la barre sera affiché, on convertit
                            # le pourcentage en string et on lui ajoute le symbole '%' derrière
                            text_display = str(int(pourc)) + '%'
                            display3 = str(av) + " / " + str(total)

                            # Définition de la police et de la taille du texte
                            font = pygame.font.SysFont('opensans.ttf', 24)

                            # Définition du contenu et de la couleur du texte
                            text = font.render(text_display, True, white2, dgrey)
                            text2 = font.render(mdp, True, white2, dgrey)
                            text3 = font.render(display3, True, white2, dgrey)

                            # Définition du rectangle du texte, et de la position de son centre
                            textRect = text.get_rect()
                            textRect.center = (320, 150)

                            textRect2 = text2.get_rect()
                            textRect2.center = (320, 210)

                            textRect3 = text3.get_rect()
                            textRect3.center = (320, 250)

                            # Affichage du texte
                            window.blit(text, textRect)
                            window.blit(text2, textRect2)
                            window.blit(text3, textRect3)

                            # time.sleep(1)

                            # Définition et affichage de la barre de chargement
                            pygame.draw.rect(window, white2, Rect((120, 170), (rec, 20)))
                            pygame.display.update()

    # Lorsque le chargement est terminé, on laisse la barre finale affichée, dans la pratique on continuerait
    # Vers la suite de notre programme
    pygame.draw.rect(window, white2, Rect((120, 170), (400, 20)))

    # Définition du contenu et de la couleur du texte
    end = "Chargement terminé !"
    endtext = font.render(end, True, dgrey, white2)
    # Définition du rectangle du texte, et de la position de son centre
    textRect4 = endtext.get_rect()
    textRect4.center = (320, 180)

    # Affichage du texte
    window.blit(endtext, textRect4)

    pygame.display.update()
