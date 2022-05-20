# ----- Création des graphes et affichage en matrice -----#

class Arete:
    def __init__(self, sommet_initial, sommet_final, valeur):
        self.sommet_initial = sommet_initial
        self.sommet_final = sommet_final
        self.valeur = valeur


class Graphe:
    def __init__(self, nombre_sommet, liste_aretes):
        self.nombre_sommet = nombre_sommet
        self.liste_aretes = liste_aretes


def saisie_arete():
    sommet_i = int(input("Entrer le sommet initial en chiffre : "))
    sommet_f = int(input("Entrer le sommet final en chiffre : "))
    sommet_v = int(input("Entrer la valeur de l'arête : "))
    arete = Arete(sommet_i, sommet_f, sommet_v)
    return arete


def saisie_graphe():
    nombre_s = int(input("Entrer le nombre de sommet : "))
    n = int(input("Veuillez entrer le nombre d'arêtes : "))
    liste = []
    for i in range(n):
        liste.append(saisie_arete())
    graphe = Graphe(nombre_s, liste)
    return graphe


def matrice_zero(length):  # Matrice de length par length de 0
    matrice = []
    for i in range(length):
        matrice.append([])
        for j in range(length):
            matrice[i].append(0)
    return matrice


def adjacence(graphe):
    adjacente = matrice_zero(graphe.nombre_sommet)

    arete = graphe.liste_aretes

    for k in range(len(arete)):  # remplace les 0 de ma grille par les valeurs des aretes
        arete_data = arete[k]
        position_ligne = arete_data.sommet_initial - 1
        position_colonne = arete_data.sommet_final - 1
        valeur = arete_data.valeur
        adjacente[position_ligne][position_colonne] = valeur

    return adjacente


def afficher_matrice(adjacente):
    for inner_list in adjacente:
        for adjacente in inner_list:
            print(adjacente, end=" ")  # end =" " pour ne pas sauter une ligne
        print()


# ----- Section sur les manipulations de matrice -----#


def produit(matrice1, matrice2):
    def produit_inter(matrice1, matrice2, ligne_M1, colonne_M2):
        total = 0
        for i in range(len(matrice1)):
            total += matrice1[ligne_M1][i] * matrice2[i][colonne_M2]
        return total

    matrice3 = matrice_zero(len(matrice1))

    for i in range(len(matrice1)):
        for j in range(len(matrice1)):
            matrice3[i][j] = produit_inter(matrice1, matrice2, i, j)
    return matrice3


def addition(matrice1, matrice2):
    m3 = matrice_zero(len(matrice1))
    for i in range(len(matrice1)):
        for j in range(len(matrice1)):
            m3[i][j] = matrice1[i][j] + matrice2[i][j]
    return m3


def puissance(matrice, n):
    matrice_final = matrice_zero(len(matrice))
    matrice_final = addition(matrice, matrice_final)
    for i in range(n - 1):
        matrice_final = produit(matrice_final, matrice)
    return matrice_final


def nombre_chemin(matrice, longueur_chemin, sommet1, sommet2):
    if sommet1 != sommet2:
        matrice_nc = puissance(matrice, longueur_chemin)
        nombreChemin = (matrice_nc[sommet1 - 1][sommet2 - 1]) + (matrice_nc[sommet2 - 1][sommet1 - 1])
        return nombreChemin
    else:
        matrice_nc = puissance(matrice, longueur_chemin)
        nombreChemin = (matrice_nc[sommet1 - 1][sommet2 - 1])
        return nombreChemin


# ----- Section sur les matrices booléennes -----#


def conversion_matrice_bool(matrice):
    matrice_final = matrice_zero(len(matrice))
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != 0:
                matrice_final[i][j] = 1
    return matrice_final


def produit_bool(matrice1, matrice2):
    return conversion_matrice_bool(produit(matrice1, matrice2))


def addition_bool(matrice1, matrice2):
    return conversion_matrice_bool(addition(matrice1, matrice2))


def matrice_identique(matrice1, matrice2):
    return matrice1 == matrice2


def matrice_identite(matrice):
    matrice_i = matrice_zero(len(matrice))
    for i in range(len(matrice)):
        matrice_i[i][i] = 1
    return matrice_i


def puissance_bool(matrice, n):
    return conversion_matrice_bool(puissance(matrice, n))


def matrice_transitive(matrice):
    matriceT = matrice_identite(matrice)
    matriceTback = None
    tour = 1
    while matriceT != matriceTback:
        matrice_add = puissance_bool(matrice, tour)
        matriceTback = matriceT
        matriceT = addition_bool(matriceT, matrice_add)
        tour += 1
    return afficher_matrice(matriceT)
