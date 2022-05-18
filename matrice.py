#----- Création des graphes et affichage en matrice -----#

class Arete:  
    def __init__(self, sommet_initial, sommet_final, valeur) : 
        self.sommet_initial = sommet_initial 
        self.sommet_final = sommet_final
        self.valeur = valeur

class Graphe:
    def __init__(self, nombre_sommet, liste_aretes) : 
        self.nombre_sommet = nombre_sommet
        self.liste_aretes = liste_aretes 
        
def saisie_arete () :  # création de l'arête 
    sommet_i = int(input("Entrer le sommet initial en chiffre : "))
    sommet_f = int(input("Entrer le sommet final en chiffre : "))
    sommet_v = int(input("Entrer la valeur de l'arête : "))
    arete = Arete(sommet_i, sommet_f, sommet_v)
    return arete 

def saisie_graphe () : # création du graphe
    nombre_s = int(input("Entrer le nombre de sommet : "))
    n = int(input("Veuillez entrer le nombre d'arêtes : "))
    liste = []
    for i in range(n) : # création liste arête 
        liste.append(saisie_arete())
    graphe = Graphe(nombre_s, liste)
    return graphe


def matrice_zero (length) :     #Matrice de length x length de 0  
    matrice = []
    for i in range(length):
        matrice.append([])
        for j in range(length):
            matrice[i].append(0)   
    return matrice

def adjacence(graphe) :
    
    adjacente = matrice_zero(graphe.nombre_sommet)
    
    arete = graphe.liste_aretes 
             
    for k in range (len(arete)) : #remplace les 0 de ma grille par les valeurs des aretes 
        arete_data = arete [k]
        position_ligne = arete_data.sommet_initial - 1
        position_colonne = arete_data.sommet_final - 1 
        valeur = arete_data.valeur
        adjacente [position_ligne] [position_colonne] = valeur 
        adjacente [position_colonne] [position_ligne] = valeur 
        
    return adjacente
      
def afficher_matrice (adjacente) :    #parcours de la matrice pour l'afficher 
    for inner_list in adjacente :
        for adjacente in inner_list :
            print(adjacente, end=" ") #end =" " pour ne pas sauter une ligne 
        print()


#----- Section sur les manipulations de matrice -----#


def produit (matrice1, matrice2) : 
    
    def produit_inter (matrice1, matrice2, ligne_M1, colonne_M2) :    #le produit d'une ligne de la matrice 1 par la colonne de la matrice 2
        total = 0
        for i in range(len(matrice1)) :
            total += matrice1 [ligne_M1] [i] * matrice2[i][colonne_M2]
        return total
    
    matrice3 = matrice_zero(len(matrice1)) #création du resultat
    
    for i in range(len(matrice1)):
        for j in range(len(matrice1)) : 
            matrice3 [i] [j] = produit_inter(matrice1, matrice2, i, j)  #remplace le 0 de la matrice 3 par le résultat de produit d'une ligne et colonne spécifique 
    return matrice3
        
def addition(matrice1, matrice2):
    m3 = matrice_zero(len(matrice1))
    for i in range(len(matrice1)):
        for j in range(len(matrice1)):
            m3[i][j] = matrice1[i][j] + matrice2[i][j]
    return m3

def puissance(matrice, n):
    matrice_final = matrice_zero(len(matrice)) 
    matrice_final = addition(matrice, matrice_final) #additionne matrice 0 avec matrice en paramètre pour avoir une copie 
    for i in range(n - 1):
        matrice_final = produit(matrice_final, matrice)
    return matrice_final 

def nombre_chemin (matrice, longueur_chemin, sommet1, sommet2) : 
    if sommet1 != sommet2 : # premier condition de A vers B et de B vers A 
        matrice_nc = puissance(matrice, longueur_chemin)
        nombreChemin = (matrice_nc [sommet1 - 1] [sommet2 - 1]) + (matrice_nc [sommet2 - 1][sommet1 - 1])
        return nombreChemin
    else : # condition si A vers A 
        matrice_nc = puissance(matrice, longueur_chemin)
        nombreChemin = (matrice_nc [sommet1 - 1] [sommet2 - 1])
        return nombreChemin


#----- Section sur les matrices booléennes -----#


def conversion_matrice_bool (matrice) :    # on prend une matrice quelconque en paramètre 
    matrice_final = matrice_zero(len(matrice))
    for i in range (len(matrice)) :
        for j in range (len(matrice)) : # si il y a une valeur autre que 0 je mets 1 à la place pour la convertir en matrice booléenne 
            if matrice [i] [j] != 0 :   
                matrice_final [i] [j] = 1 
    return matrice_final 

def produit_bool (matrice1, matrice2) :   # convertion toutes les fonctions pour les bools 
    return conversion_matrice_bool(produit(matrice1, matrice2))

def addition_bool (matrice1, matrice2) : 
    return conversion_matrice_bool(addition(matrice1, matrice2))

def matrice_identique (matrice1, matrice2) : # ne sert à rien juste pour l'exercice 
    return matrice1 == matrice2 # car les matrices sont des listes 2D 
       
def matrice_identite (matrice) : # création matrice identité
    matrice_i = matrice_zero(len(matrice)) 
    for i in range (len(matrice)) :
        matrice_i [i] [i] = 1  # 1 sur les diagonales 
    return matrice_i 

def puissance_bool (matrice, n) :
    return conversion_matrice_bool(puissance(matrice, n))

def matrice_transitive (matrice) :
    matriceT = matrice_identite(matrice) # initialisation des matrice T et matrice T-1
    matriceTback = None 
    tour = 1 # nous permet de faire la puissance à chaque tour 
    while matriceT != matriceTback :
        matrice_add = puissance_bool(matrice, tour) 
        matriceTback = matriceT # matrice T-1 devient T  
        matriceT = addition_bool(matriceT, matrice_add) # matrice T devient T+1
        tour += 1 
    return afficher_matrice(matriceT)