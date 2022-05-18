from algo_prim import * 

graph = Graphe(7)      # création d'un graphe
graph.add_arete(0, 1, 7)
graph.add_arete(1, 2, 8)
graph.add_arete(2, 4, 5)
graph.add_arete(4, 6, 9)
graph.add_arete(6, 5, 11)
graph.add_arete(5, 3, 6)
graph.add_arete(3, 0, 5)
graph.add_arete(1, 3, 9)
graph.add_arete(1, 4, 7)
graph.add_arete(3, 4, 15)
graph.add_arete(5, 4, 8)
        
print(tabToString(graph.prim())) # affichage de la matrice adjacente après le passage dans l'algorithme de Prim 

print(tabToString(graph.graphe)) # affichage de la matrice adjacente avant le passage dans l'algorithme de Prim 

PC_chemin(graph.prim()) # plus court chemin 