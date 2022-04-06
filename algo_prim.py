import random
import math 

def matrice_zero (length) :     #Matrice de length par length de 0 
    matrice = []
    for i in range(length):
        matrice.append([])
        for j in range(length):
            matrice[i].append(0)   
    return matrice

class Graphe:
    def __init__(self, nombre_sommet) : 
        self.nombre_sommet = nombre_sommet
        self.graphe = matrice_zero(nombre_sommet)
        
    def add_arete (self, sommet_i, sommet_f, valeur) : 
        self.graphe [sommet_i] [sommet_f] = valeur
        self.graphe [sommet_f] [sommet_i] = valeur
        return self
    
    def __str__(self) :
        affichage = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        
        for j in range (len(self.graphe) + 1):
            if j == 0:
                affichage  += "┏━"
            else:
                affichage  += "┳━"
        affichage += "┓\n┃ ┃"
        
        for i in range(len(self.graphe)):
            affichage += alphabet[i] + "┃"
        
        affichage += "\n"
            
        for j in range (len(self.graphe) + 1):
            if j == 0:
                affichage  += "┣━"
            else:
                affichage  += "╋━"
                
        affichage += "┫\n"
        for i in range (len(self.graphe)) :
            affichage += "┃" +  alphabet[i] + "┃"
            for j in range(len(self.graphe)) :
                affichage += "\033[3" + str(random.randint(1,6)) + "m" + str(self.graphe [i][j]) + "\033[0m┃"
            
            affichage += "\n"
            if i != len(self.graphe) - 1:
                for j in range (len(self.graphe) + 1):
                    if j == 0:
                        affichage  += "┣━"
                    else:
                        affichage  += "╋━"
                affichage += "┫\n"
            else :
                for j in range (len(self.graphe) + 1):
                    if j == 0:
                        affichage  += "┗━"
                    else:
                        affichage  += "┻━"
                affichage += "┛\n"
        return affichage
    
    def prim(self) : 
        
        grand_nombre = math.inf   #créa nombre infini qu'ils soit plus petit que la valeur du premier noeud
        
        liste_noeud_parcouru = []
        for i in range(self.nombre_sommet) :
            liste_noeud_parcouru.append(0)

        fin_boucle = 0

        liste_noeud_parcouru[0] = True
        
        prim = matrice_zero(self.nombre_sommet)
        
        while (fin_boucle < self.nombre_sommet - 1) : 
            
            min = grand_nombre
            sommet_i = 0
            sommet_f = 0
            
            for i in range(self.nombre_sommet):
                if liste_noeud_parcouru [i] :
                    for j in range(self.nombre_sommet) :
                        if (not liste_noeud_parcouru [j] and self.graphe [i] [j]):
                            if min > self.graphe [i] [j] :
                                min = self.graphe [i] [j]
                                sommet_i = i 
                                sommet_f = j 
                                
            liste_noeud_parcouru [sommet_f] = True
            fin_boucle += 1 
            prim [sommet_i] [sommet_f] = min 
            prim [sommet_f] [sommet_i] = prim [sommet_i] [sommet_f]  
                
        return prim 
				
