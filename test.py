from algo_prim import * 
graph = Graphe(9)
graph.add_arete(0, 1, 4)
graph.add_arete(0, 2, 7)
graph.add_arete(1, 2, 1)
graph.add_arete(1, 3, 9)
graph.add_arete(1, 5, 2)
graph.add_arete(2, 5, 1)
graph.add_arete(3, 6, 6)
graph.add_arete(3, 4, 2)
graph.add_arete(4, 6, 0)
graph.add_arete(4, 8, 5)
graph.add_arete(4, 7, 5)
graph.add_arete(4, 5, 1)
graph.add_arete(5, 7, 3)
graph.add_arete(6, 8, 5)
graph.add_arete(7, 8, 2)

def afficher_matrice (adjacente) :     
    for inner_list in adjacente :
        for adjacente in inner_list :
            print(adjacente, end=" ") #end =" " pour ne pas sauter une ligne 
        print()

afficher_matrice(graph.prim())
print(tabToString(graph.prim()))
print(str(graph))