import random
from tkinter import *

LONGUEUR = 8
LARGEUR = 8
alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def graphe() :


	Tab = []
	for i in range(LONGUEUR):
		ls = []
		for j in range(LARGEUR):
			ls.append(i*LONGUEUR + j)
		Tab.append(ls)

	print(Tab)

	E = dict()
	for i in range(0,LONGUEUR) :
		for j in range(0,LARGEUR):

			E[i*LONGUEUR + j] = [] # E[k]  : liste des voisins de la case k
			if 0 <= i-2 < LONGUEUR and  0 <= j-1 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i-2][j-1])
			if 0 <= i-2 < LONGUEUR and  0 <= j+1 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i-2][j+1])
			if 0 <= i+2 < LONGUEUR and  0 <= j-1 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i+2][j-1])
			if 0 <= i+2 < LONGUEUR and  0 <= j+1 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i+2][j+1])
	
			if 0 <= i-1 < LONGUEUR and  0 <= j-2 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i-1][j-2])
			if 0 <= i-1 < LONGUEUR and  0 <= j+2 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i-1][j+2])
			if 0 <= i+1 < LONGUEUR and  0 <= j-2 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i+1][j-2])
			if 0 <= i+1 < LONGUEUR and  0 <= j+2 < LARGEUR : E[i*LONGUEUR + j].append(Tab[i+1][j+2])
	
	return E


def cavalierHamiltonHeuristique(graphe) :
	""" 
		recherche d'un chemin hamiltonien dans le graphe du cavalier.
	"""
	chemin = [] # contiendra les cases dans leur ordre de visite
	print(graphe)
	parcours(random.randint(0,LONGUEUR*LARGEUR-1), chemin, graphe)
	return chemin


def parcours(case, chemin, graphe) :
	"""
		case : case actuelle du cavalier.
	"""
	 
	chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également

	
	if len(chemin) == LONGUEUR*LARGEUR:
		gagne = True

	else :
		voisins = []
		gagne = False
		for u in graphe[case]:
			if u not in chemin:
				voisins.append(u)


		# --------Permet d'aller plus vite-------- 

		voisinsNbPossibles = []

		for u in voisins :
			nb = len( [v for v in graphe[u] if v not in chemin]) # nb de possibles à partir de u
			voisinsNbPossibles.append([u,nb])

		voisinsNbPossibles.sort(key= lambda x:x[1])# tri croissant suivant le nombre de possibles
		voisins = [ x[0] for x in voisinsNbPossibles ] # on récupère uniquement les voisins

		# ----------------------------------------- 

		cmpt = 0
		while cmpt < len(voisins) and gagne == False:
			gagne = parcours(voisins[cmpt], chemin, graphe)
			cmpt+=1

		if not gagne :
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse

	return gagne


def affichage() :
	""" affichage simple de l'échiquier avec ordre de parcours des cellules indiqué."""

	chemin = cavalierHamiltonHeuristique(graphe())

	print(chemin)

	Tab = [[0 for i in range(LONGUEUR)] for j in range(LARGEUR)]

	cmpt = 0
	for i in range(len(Tab)):
		for j in range(len(Tab[i])):
			Tab[i][j] = chemin[cmpt]
			cmpt +=1

	
	for x in Tab :
		for y in x:
			if y < 10:
				print("0", end="")
			print(y,end = " ")
		print()


affichage()
