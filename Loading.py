import time
import random
from os import system, name

#################
# @AntoSoulaire #
#################

# Initialisation du tableau qui se mettra à jour en fonction du chargement
bar = []

# Remplissage du tableau par 20 valeurs vides (qui se rempliront donc tous les 5%)
for i in range(20):
    bar.append('')

# Choix d'un nombre aléatoire qui servira de référence pour la barre de chargement
ran = random.randint(4, 10) * 10

# Boucle de chargement (en fonction de la valeur aléatoire ci-dessus)
for i in range(ran):

    # On met à jour le % d'avancement 4 fois par seconde
    time.sleep(0.25)
    pourc = ((i+1)/ran) * 100

    # On regarde la valeur 'pourc', tous les 5% on met à jour l'une des cases vides du tableau 'bar'
    for x in range(len(bar)):
        if ((x + 1) * 5) <= pourc:
            # (On remplace '' par '█'
            bar[x] = '█'

    # La valeur 'load' servira à afficher la tableau 'bar' sous forme de string
    load = ""
    for x in range(len(bar)):
        load += bar[x]

    # Clear le terminal afin de n'avoir qu'une seule barre de chargement, au lieu de 4 / seconde
    # Note : Fonctionne dans l'invite de commandes, mais pas dans la console de certains IDE
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    # [Esthétique] Permet de toujours avoir 4 chiffres affichés (par exemple 1.250 ou 15.00 ou 100.0)
    pourc = str(float(int(pourc * 100))/100)
    if len(pourc) < 5:
        if pourc[1] == '.':
            pourc = "0" + pourc
        else:
            pourc += "0"
        if len(pourc) < 5:
            pourc = "0" + pourc

    # Affichage final
    print(pourc + "% " + load)
