LONGUEUR = 6
LARGEUR = 6

def grapheSeul() :
	Tab = []
	for i in range(LARGEUR):
		ls = []
		for j in range(LONGUEUR):
			ls.append(i*LONGUEUR + j + 1)
		Tab.append(ls)


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


def parcoursSeulHeuristique(case, chemin, graphe) :
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


		# --------Permet d'aller plus vite (partie heuristique)-------- 

		voisinsNbPossibles = []
		for u in voisins :
			nb = len( [v for v in graphe[u] if v not in chemin]) # nombre de voisins possibles à partir de u
			voisinsNbPossibles.append([u,nb])

		voisinsNbPossibles.sort(key= lambda x:x[1])# tri croissant suivant le nombre de voisins possibles
		voisins = [ x[0] for x in voisinsNbPossibles ] # on récupère uniquement les voisins

		# ----------------------------------------- 

		cmpt = 0
		while cmpt < len(voisins) and not gagne:
			gagne = parcoursSeulHeuristique(voisins[cmpt], chemin, graphe)
			cmpt+=1

		if not gagne :
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse

	return gagne

def parcoursSeulNonHeuristique(case, chemin, graphe) :
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
		cmpt = 0
		while cmpt < len(voisins) and not gagne:
			gagne = parcoursSeulNonHeuristique(voisins[cmpt], chemin, graphe)
			cmpt+=1

		if not gagne :
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse

	return gagne

def affichageS(chemin, cpu, case_dep) :
	""" affichage simple de l'échiquier avec ordre de parcours des cellules indiqué."""
	if len(chemin) < LONGUEUR*LARGEUR: print("Aucune solution possible dans une grille de ", LONGUEUR, " x ", LARGEUR, " avec comme case de départ : ", case_dep, "len: ", len(chemin))
	else:

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
		print('\nCPU: ', cpu, '\n\n')
