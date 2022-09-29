"""
Programme fait par Adam Fillion
Groupe 023
Description: TP2 - Jeu de devinettes
"""

boucle_jeu = True
import random

nombre_aleatoire = random.randint(0, 100)
print("J'ai choisi un nombre au hasard entre 0 et 100")
print("À vous de le deviner !")


def jeu():
    nombre_essai = 1
    essai = input(int(f"Essai numéro {nombre_essai}, Entrez un nombre:"))
    if essai == nombre_aleatoire:
        print("Bravo! Vous avez trouvé.")
        rejouer = input(str("Voulez-vous rejouez ?")
        if rejouer == "oui":
            jeu()
        else:
            boucle_jeu = False
    elif essai < nombre_aleatoire:
        print("Raté, pensez plus grand")
        nombre_essai = nombre_essai+1
        jeu()
    elif essai > nombre_aleatoire:
        print("Raté, pensez plus petit")
        nombre_essai = nombre_essai + 1
        jeu()
while boucle_jeu: