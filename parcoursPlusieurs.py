import random
from tkinter import *

LONGUEUR = 5
LARGEUR = 5

alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def graphe() :
	Tab = []
	for i in range(LARGEUR):
		ls = []
		for j in range(LONGUEUR):
			ls.append(i*LONGUEUR + j + 1)
		Tab.append(ls)

	# print(Tab)

	E = dict()
	for i in range(0,LARGEUR) :
		for j in range(0,LONGUEUR):

			E[i*LONGUEUR + j + 1] = [] # E[k]  : liste des voisins de la case k
			if 0 <= i-2 < LARGEUR and  0 <= j-1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-2][j-1])
			if 0 <= i-2 < LARGEUR and  0 <= j+1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-2][j+1])
			if 0 <= i+2 < LARGEUR and  0 <= j-1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+2][j-1])
			if 0 <= i+2 < LARGEUR and  0 <= j+1 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+2][j+1])
	
			if 0 <= i-1 < LARGEUR and  0 <= j-2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-1][j-2])
			if 0 <= i-1 < LARGEUR and  0 <= j+2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i-1][j+2])
			if 0 <= i+1 < LARGEUR and  0 <= j-2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+1][j-2])
			if 0 <= i+1 < LARGEUR and  0 <= j+2 < LONGUEUR : E[i*LONGUEUR + j + 1].append(Tab[i+1][j+2])
	
	return E

def parcours(case, chemin, graphe, chemins) :
	"""
		case : case actuelle du cavalier.
	"""
	if chemin is None:
		chemin=[]
	if chemins is None:
		chemins=[]

	chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également

	
	if len(chemin) == LONGUEUR*LARGEUR and chemin not in chemins:
		chemins.append(chemin.copy())

	else :
		voisins = []
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
		while cmpt < len(voisins):
			chemins = parcours(voisins[cmpt], chemin, graphe, chemins)
			cmpt+=1
			
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse
	return chemins


def affichage() :
	""" affichage simple de l'échiquier avec ordre de parcours des cellules indiqué."""

	case_dep = random.randint(1,LONGUEUR*LARGEUR)
	print('\nCase de départ: ', case_dep)
	chemins = parcours(case_dep, [], graphe(), [])
	print("Nb chemins:", len(chemins))

	if len(chemins) == 0: print("Aucune solution possible dans une grille de ", LONGUEUR, " x ", LARGEUR, " avec comme case de départ : ", case_dep)
	else:
		for chemin in chemins[:10]:

			Tab = [0 for i in range(LONGUEUR*LARGEUR)]


			for i in range(len(Tab)):
				Tab[chemin[i]-1] = i
			
			rg = 1
			for x in Tab :
				x +=1
				if x < 10:
					print("0", end="")
				print(x,end = " ")

				if rg >= LONGUEUR:
					print()
					rg = 1
				else : rg+=1

			print('\n\n')



affichage()
