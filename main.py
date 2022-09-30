"""
Programme fait par Adam Fillion
Groupe 023
Description: TP2 - Jeu de devinettes
"""

import random

start_jeu = True
nb_minimum = 0
nb_maximum = 100

def bornes():
    global nb_minimum, nb_maximum
    nb_minimum = int(input("Décidez le nombre minimum que je peux choisir:"))
    nb_maximum = int(input("Décider le nombre maximum que je peux choisir:"))

while start_jeu:
    print("Mon but est de vous faire deviner un nombre que j'ai choisi aléatoirement.")
    bornes()
    nombre_aleatoire = random.randint(nb_minimum, nb_maximum)
    print(f"Parfait, j'ai choisi un nombre entre {nb_minimum} et {nb_maximum}")
    print("Maintenant bonne chance pour le deviner !")
    nombre_essai = 1
    boucle_jeu = True
    while boucle_jeu == True:
        essai = int(input(f"Essai numéro {nombre_essai}, Entrez un nombre:"))
        nombre_essai += 1
        if essai < nombre_aleatoire:
            print("Pensez plus grand.")
        elif essai > nombre_aleatoire:
            print("Pensez plus petit.")
        elif essai == nombre_aleatoire:
            print("Bravo, vous m'avez eu !")
            rejouer = input("Voulez vous rejouez ?")
            if rejouer == "oui":
                boucle_jeu = False
            else:
                print("Merci et aurevoir")
                boucle_jeu = False
                start_jeu = False







