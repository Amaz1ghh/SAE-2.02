import random
from tkinter import *
import time

LONGUEUR = 5
HAUTEUR = 5


def graphe() :
	Tab = []
	for i in range(HAUTEUR):
		ls = []
		for j in range(LONGUEUR):
			ls.append(i*LONGUEUR + j + 1)
		Tab.append(ls)

	E = dict()
	for i in range(0,HAUTEUR):
		for j in range(0,LONGUEUR):

			E[i*LONGUEUR + j + 1] = [] # E[k]  : liste des voisins de la case k
			if 0 <= i-2 < HAUTEUR and  0 <= j-1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-2][j-1])
			if 0 <= i-2 < HAUTEUR and  0 <= j+1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-2][j+1])
			if 0 <= i+2 < HAUTEUR and  0 <= j-1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+2][j-1])
			if 0 <= i+2 < HAUTEUR and  0 <= j+1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+2][j+1])
	
			if 0 <= i-1 < HAUTEUR and  0 <= j-2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-1][j-2])
			if 0 <= i-1 < HAUTEUR and  0 <= j+2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-1][j+2])
			if 0 <= i+1 < HAUTEUR and  0 <= j-2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+1][j-2])
			if 0 <= i+1 < HAUTEUR and  0 <= j+2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+1][j+2])
	
	return E


def parcoursHeuristique(case, graphe, chemin = [], chemins = []) :
	"""
		case : case actuelle du cavalier.
	"""

	chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également

	
	if len(chemin) == LONGUEUR*HAUTEUR and chemin not in chemins:
		chemins.append(chemin.copy())

	else :
		voisins = []
		for u in graphe[case]:
			if u not in chemin:
				voisins.append(u)

		# --------Permet d'aller plus vite (partie heuristique)-------- 

		voisinsNbPossibles = []
		for u in voisins :
			nb = len( [v for v in graphe[u] if v not in chemin]) # nb de possibles à partir de u
			voisinsNbPossibles.append([u,nb])

		voisinsNbPossibles.sort(key= lambda x:x[1])# tri croissant suivant le nombre de possibles
		voisins = [ x[0] for x in voisinsNbPossibles ] # on récupère uniquement les voisins

		# ----------------------------------------- 

		cmpt = 0
		while cmpt < len(voisins):
			chemins = parcoursHeuristique(voisins[cmpt], graphe, chemin, chemins)
			cmpt+=1
			
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse
	return chemins

def parcoursNonHeuristique(case, graphe, chemin = [], chemins = []) :
	"""
		case : case actuelle du cavalier.
	"""

	chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également

	
	if len(chemin) == LONGUEUR*HAUTEUR and chemin not in chemins:
		chemins.append(chemin.copy())

	else:
		voisins = []
		for u in graphe[case]:
			if u not in chemin:
				voisins.append(u)
		cmpt = 0
		while cmpt < len(voisins):
			chemins = parcoursNonHeuristique(voisins[cmpt], graphe, chemin, chemins)
			cmpt+=1
			
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse
	return chemins


def affichageP(chemins, cpu, case_dep) :
	""" affichage simple de l'échiquier avec ordre de parcours des cellules indiqué."""
	if len(chemins) == 0: print("Aucune solution possible dans une grille de ", LONGUEUR, " x ", HAUTEUR, " avec comme case de départ : ", case_dep)
	else:
		for chemin in chemins[:1]:

			Tab = [0 for i in range(LONGUEUR*HAUTEUR)]


			for i in range(len(Tab)):
				Tab[chemin[i]-1] = i +1 
			
			rg = 1
			for x in Tab :
				if x < 10:
					print("0", end="")
				print(x,end = " ")

				if rg >= LONGUEUR:
					print()
					rg = 1
				else : rg+=1

			# print('\n\n')
		print('\nCPU: ', cpu, '\n\n')

