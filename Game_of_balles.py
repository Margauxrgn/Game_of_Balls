"""
Auteur: Margaux Rogeon
date : 7 octobre 2022

But du programme:
Projet 1 du cours de programmation à l'ULB - Jeu du sac de billes
Ce programme est un jeu qui se joue entre deux adversaires, le joueur humain,
et une Intelligence Artificielle dotée d'une stratégie. le joueur humain doit
indiqué un nombre de billes initiales déposées dans le sac, et chacun son tour,
il faut retirer entre 1, 2, 3 ou 4 billes. Le but du jeu est de ne pas retirer
la dernière bille, si c'est le cas, vous avez perdu.

Entrée: billes_res : le nombre de billes présentes dans le sac
Sorties: Fin du jeu quand le joueur humain a décidé d'arrêter le jeu.
"""

# importation des modules
import messages
from random import randint,seed

def init():
    # fonction de mise en condition du jeu, définition du nombre de billes initiales

    print(messages.message_2)
    inp = False
    while inp is False:
        billes_res = int(input(messages.entree_2))
        # implémentation dans la variable 'billes_res' le nombre de billes initiales
        if billes_res < 6 or billes_res > 40:
            print("Erreur, il faut choisir un nombre entre 6 et 40!")
        else:
            inp = True

    print(messages.message_3)
    return billes_res


def joueurH(billes_res):
    # fonction qui défini le jeu du joueur humain

    print(messages.message_4.format(billes_res))
    inp = False
    while inp is False:
        x = int(input(messages.entree_3))
        # implémentation dans la variable 'x' du nombre de billes retirées du sac de billes, choisi par le joueur
        if x != 1 and (x != 2) and (x != 3) and (x != 4):
            print("Erreur, il faut choisir un nombre entre 1 et 4!")
        else:
            inp= True
    billes_res = billes_res - x

    print(messages.message_5.format(billes_res))
    return billes_res


def joueurIA(billes_res):
    # fonction qui défini le jeu du joueur Intelligence Artificielle
    res = 0
    nbre_alea = randint(1, 100)
    # variable pour tirer un nombre aléatoire entre 1 et 100
    print(messages.message_6)

    # mise en place des stratégies
    if (billes_res - 1) % 5 == 0:
        # si le nombres de billes - 1 est égale à un multiple de 5
        if billes_res < 7:
            # 1er cas: le nombre de billes présentes dans le sac sont inférieur à 7
            billes_res = billes_res - 1
            res = 1
        elif billes_res >= 7 and nbre_alea <= 70:
            # 2ème cas: le nombre de billes présentes dans le sac sont supérieur ou égale à 7
            # et le nombre aléatoire tiré est inférieur ou égale à 70
            billes_res = billes_res - 1
            res = 1
        else:
            # 3ème cas : le nombre de billes présentes dans le sac sont supérieur ou égale à 7
            # et le nombre aléatoire tiré est supérieur à 70
            billes_res = billes_res - 2
            res = 2

    else:
        # si le nombre de billes - 1 n'est pas égale à un multiple de 5
        for i in range(1, 5):
            # test de toutes les possibilités entre 1, 2, 3 et 4 billes
            if (billes_res - i) % 5 == 1:
                res = i #variable qui retient la valeur de la ou les billes rétirées
        billes_res = billes_res - res

    print((messages.message_7.format(res)))
    return billes_res


def partie():
    # fonction qui défini le déroulement de la partie
    bills = init()
    final = False

    while final is False:
        # boucle pour introduire la fin du jeu, si il ne reste que une bille
        if (bills <= 1) and (final is False):
            # si il ne reste que 1 bille, fin du jeu
            print(messages.message_9)
            final = True
        elif final is False:
            # si il reste plus de 1 billes, c'est au tour du joueur humain de jouer
            bills = joueurH(bills)

        if (bills <= 1) and (final is False):
            # si il ne reste que 1 bille, fin du jeu
            print(messages.message_8)
            final = True
        elif final is False:
            # si il reste plus de 1 billes, c'est au tour du joueur IA de jouer
            bills = joueurIA(bills)

    y = (input(messages.entree_4))
    # variable 'y' pour relancer la partie
    if y == "oui":
        # si 'oui' relance de la fonction partie
        partie()
    else:
        # si non, fin du jeu
        print("La partie est terminée")

# mise en place de la variable graine
print(messages.message_1)
graine = int(input(messages.entree_1))
seed(graine)
# lancement de la première partie
partie()