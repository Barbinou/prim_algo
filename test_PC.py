from matrice import * 

partie = None 

while partie != "STOP" :

    partie = input("""Veuillez entrer la partie que vous voulez lancer :

    1 : Construction d'un graphe et de sa matrice adjacente 
    2 : Calcul de la puissance d'une matrice 
    3 : Calcul de la matrice transitive d'un graphe 
    STOP : Arrêt du programme 

    Votre saisie : """)

    print()

#---- première partie ----#

    if partie == "1" : 
        afficher_matrice(adjacence(saisie_graphe()))

#---- deuxième partie ----#

    elif partie == "2" :

        graphe_object = Graphe(3, [Arete(1, 1, 2), Arete(1, 2, 4), Arete(1, 3, 5), Arete(2, 1, 1), Arete(2, 2, 3), Arete(2, 3, 4), Arete(3, 1, 2), Arete(3, 2, 1), Arete(3, 3, 6)])
        graphe = adjacence(graphe_object)
        longueur_chemin = int(input("Veuillez entrer la longueur du chemin : "))
        sommet1 = int(input("Veuillez entrer le premier sommet : "))
        sommet2 = int(input("Veuillez entrer la second sommet : "))
        print()
        resultat = nombre_chemin(graphe, longueur_chemin, sommet1, sommet2)

        print(f"Le nombre de chemin entre le sommet {sommet1} et le sommet {sommet2} est de {resultat} chemins")
        print()

#---- Dernière partie ----#

    elif partie == "3" :
        
        graphe_object = Graphe(4, [Arete(1, 1, 2), Arete(1, 3, 4), Arete(2, 2, 5), Arete(2, 1, 1), Arete(3, 2, 4), Arete(3, 3, 2), Arete(4, 1, 1), Arete(4, 4, 3)])
        graphe = adjacence(graphe_object)
        matrice_transitive(graphe)
        print()

    elif partie == "STOP" :

        exit()

    else :
        
        print("Veuillez entrer une valeur correcte.")
        print()