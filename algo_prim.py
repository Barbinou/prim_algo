import random
import math


def matrice_zero(length):  # Matrice de length par length de 0
    matrice = []
    for i in range(length):
        matrice.append([])
        for j in range(length):
            matrice[i].append(0)
    return matrice


class Graphe:
    def __init__(self, nombre_sommet):  # constructeur
        self.nombre_sommet = nombre_sommet  # défini la variable sommet de l'objet
        self.graphe = matrice_zero(nombre_sommet)  # créé la matrice du graphe remplie de 0 au taille : nombre_sommet x nombre_sommet

    def add_arete(self, sommet_i, sommet_f, valeur):  # fonction pour ajouter une arète
        self.graphe[sommet_i][sommet_f] = valeur  # defini la valeur pour aller du 1er sommet au 2eme
        self.graphe[sommet_f][sommet_i] = valeur  # defini la valeur pour aller du 2eme sommet au 1er
        return self

    def __str__(self):
        affichage = ""  # valeur a retourner
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # pour mettre un nom aux cases

        for j in range(len(self.graphe) + 1):  # crée le haut du quadrillage
            if j == 0:
                affichage += "┏━"  # début du 1er angle
            else:
                affichage += "┳━"  # séparateur
        affichage += "┓\n┃ ┃"  # ferme la 1ere ligne du quadruillage et fait un retour a la ligne en ajoutant une case vide

        for i in range(len(self.graphe)):  # pour créer la seconde ligne
            affichage += alphabet[i] + "┃"  # met les lettres entre des cases

        affichage += "\n"  # retour a la ligne

        for j in range(len(self.graphe) + 1):  # ajoute un séparateur
            if j == 0:
                affichage += "┣━"  # début du 1er angle
            else:
                affichage += "╋━"  # séparateur

        affichage += "┫\n"  # ferme la dernière case et ajoute une ligne
        for i in range(len(self.graphe)):
            affichage += "┃" + alphabet[i] + "┃"  # met la lettre de la ligne dans une case
            for j in range(len(self.graphe)):
                affichage += "\033[3" + str(random.randint(1, 6)) + "m" + str(self.graphe[i][j]) + "\033[0m┃"  # ajoute la valeure avec une couleur aléatoire et ferme la case

            affichage += "\n"
            if i != len(self.graphe) - 1:  # vérifie s'il sagit de la dernière ligne
                for j in range(len(self.graphe) + 1):  # ajoute un séparateur
                    if j == 0:
                        affichage += "┣━"  # début du 1er angle
                    else:
                        affichage += "╋━"  # séparateur
                affichage += "┫\n"  # ferme la dernière case et ajoute une ligne
            else:
                for j in range(len(self.graphe) + 1):
                    if j == 0:
                        affichage += "┗━"  # début du 1er angle
                    else:
                        affichage += "┻━"  # séparateur
                affichage += "┛\n"  # ferme la dernière case et ajoute une ligne
        return affichage

    def prim(self):

        grand_nombre = math.inf  # créa nombre infini qu'ils soit plus petit que la valeur du premier noeud

        liste_noeud_parcouru = []
        for i in range(self.nombre_sommet):
            liste_noeud_parcouru.append(0)

        fin_boucle = 0

        liste_noeud_parcouru[0] = True

        prim = matrice_zero(self.nombre_sommet)

        while (fin_boucle < self.nombre_sommet - 1):

            min = grand_nombre
            sommet_i = 0
            sommet_f = 0

            for i in range(self.nombre_sommet):
                if liste_noeud_parcouru[i]:
                    for j in range(self.nombre_sommet):
                        if (not liste_noeud_parcouru[j] and self.graphe[i][j]):
                            if min > self.graphe[i][j]:
                                min = self.graphe[i][j]
                                sommet_i = i
                                sommet_f = j

            liste_noeud_parcouru[sommet_f] = True
            fin_boucle += 1
            prim[sommet_i][sommet_f] = min
            prim[sommet_f][sommet_i] = prim[sommet_i][sommet_f]

        return prim
