import random
from tkinter import *

LONGUEUR = 8
LARGEUR = 8
alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

class Case:
	def __init__(self, numCase):
		self.numCase = numCase
		self.relCase = {}
		self.dejaVu = False     # si deja vu, la case est en rouge et on ne peut plus aller dessus
		self.estDessus = False  # si est dessus, on affiche le cavalier sur la case

class Plateau:
	def __init__(self, cavX, cavY, plateau = []):
		"""constructeur"""
		self.plateau = plateau
		if LONGUEUR > 26 or LARGEUR > 26:
			print("Taille trop grande !")
		else:
			for i in range(LONGUEUR):
				self.plateau.append([])
				for j in range(LARGEUR):
					self.plateau[i].append(Case(alph[i]+str(j+1)))
			self.initGraphe()
		self.plateau[cavX][cavY].estDessus = True
		self.plateau[cavX][cavY].dejaVu = True


		# création fenêtre et frames tkinter
		# Note aux collègues: d'ici jusqu'à la fin de maj_affichage c'est pour afficher la fenetre au lancement
		self.fenetre = Tk()
		self.fenetre.geometry('700x700')
		self.fenetre.title('Parcours Du Cavalier')
		self.fenetre['bg'] = '#F6B22F'
		self.fenetre.resizable(width=False, height=False)

		self.fenetre.update_idletasks()
		longueur_fenetre = self.fenetre.winfo_height()
		largeur_fenetre = self.fenetre.winfo_width()
		self.longueur_case = longueur_fenetre / LONGUEUR
		self.largeur_case = largeur_fenetre / LARGEUR

		self.image_cavalier = PhotoImage(file='cavalier.png')

		self.image_cavalier = self.image_cavalier.subsample(int(self.image_cavalier.width() / self.longueur_case)+1, int(self.image_cavalier.height() / self.largeur_case)+1)

		self.labels_cavalier = []

		for ligne in range(LARGEUR):
			for colonne in range(LONGUEUR):
				couleur_case = "#D2B48C" if (ligne + colonne) % 2 == 0 else "#8B4513"
				if (self.plateau[ligne][colonne].dejaVu):
					couleur_case = "red"

				case = Frame(self.fenetre, width=self.longueur_case, height=self.largeur_case, bg=couleur_case)
				case.grid(row=ligne, column=colonne)

				self.maj_affichage(ligne, colonne)

		self.fenetre.mainloop()

	def maj_affichage(self, ligne, colonne):
		# Met à jour l'affichage en fonction de l'état actuel de la case

		case = self.plateau[ligne][colonne]

		if case.estDessus:
			label_cavalier = Label(self.fenetre, image=self.image_cavalier, bg="red")
			label_cavalier.image = self.image_cavalier
			label_cavalier.grid(row=ligne, column=colonne)
			self.labels_cavalier.append(label_cavalier)
		else:
			# Supprime le label s'il existe
			for label in self.labels_cavalier:
				if label.grid_info()['row'] == ligne and label.grid_info()['column'] == colonne:
					label.grid_forget()
					self.labels_cavalier.remove(label)

		
	def initGraphe(self):
		for i in range(LONGUEUR):
			for j in range(LARGEUR):
				self.plateau[i][j].relCase = []
				if (i-2 >= 0):
					if (j-1 >= 0):
						self.plateau[i][j].relCase.append(self.plateau[i-2][j-1].numCase)
					if (j+1 < LONGUEUR):
						self.plateau[i][j].relCase.append(self.plateau[i-2][j+1].numCase)
				if (i+2 < LARGEUR):
					if (j-1 >= 0):
						self.plateau[i][j].relCase.append(self.plateau[i+2][j-1].numCase)
					if (j+1 < LONGUEUR):
						self.plateau[i][j].relCase.append(self.plateau[i+2][j+1].numCase)
				if (j-2 >= 0):
					if (i-1 >= 0):
						self.plateau[i][j].relCase.append(self.plateau[i-1][j-2].numCase)
					if (i+1 < LONGUEUR):
						self.plateau[i][j].relCase.append(self.plateau[i+1][j-2].numCase)

				if (j+2 < LONGUEUR):
					if (i-1 >= 0):
						self.plateau[i][j].relCase.append(self.plateau[i-1][j+2].numCase)
					if (i+1 < LONGUEUR):
						self.plateau[i][j].relCase.append(self.plateau[i+1][j+2].numCase)

	def afficherPlateau(self):
		print("\n")
		for i in range(LARGEUR):
			print("| ",end="")
			for j in range(LONGUEUR):
				print(self.plateau[i][j].numCase + ' | ',end="")
			print("\n")

jeu = Plateau(5, 5)





def graphe(n) :

	E = dict()
	for k in range(n*n) :
		i = k//n # ligne de la case k
		j = k%n # colonne de la case k

		E[k] = [] # E[k]  : liste des voisins de la case k
		if  0 <= i-2 < n and  0 <= j-1 < n : E[k].append((i-2)*n+(j-1))
		if  0 <= i-2 < n and  0 <= j+1 < n : E[k].append((i-2)*n+(j+1))
		if  0 <= i+2 < n and  0 <= j-1 < n : E[k].append((i+2)*n+(j-1))
		if  0 <= i+2 < n and  0 <= j+1 < n : E[k].append((i+2)*n+(j+1))

		if  0 <= i-1 < n and  0 <= j-2 < n : E[k].append((i-1)*n+(j-2))
		if  0 <= i-1 < n and  0 <= j+2 < n : E[k].append((i-1)*n+(j+2))
		if  0 <= i+1 < n and  0 <= j-2 < n : E[k].append((i+1)*n+(j-2))
		if  0 <= i+1 < n and  0 <= j+2 < n : E[k].append((i+1)*n+(j+2))
		
	return E


def cavalierHamiltonHeuristique(n) :
	""" recherche d'un chemin hamiltonien dans le graphe du cavalier."""
	chemin = [] # contiendra les cases dans leur ordre de visite
	parcours(random.randint(0,n*n-1), chemin)
	return chemin


def parcours(case, chemin) :
	"""
		case : case actuelle du cavalier.
	"""
	 
	chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également
	E = graphe(LONGUEUR)
	
	if len(chemin) == LONGUEUR*LARGEUR :
		gagne = True

	else :
		gagne = False
		voisins = [ u for u in E[case] if u not in chemin ] # voisins non visités de case
		voisinsNbPossibles = []

		for u in voisins :
			nb = len( [v for v in E[u] if v not in chemin]) # nb de possibles à partir de u
			voisinsNbPossibles.append([u,nb])

		voisinsNbPossibles.sort(key= lambda x:x[1])# tri croissant suivant le nombre de possibles
		voisins = [ x[0] for x in voisinsNbPossibles ] # on récupère uniquement les voisins

		cmpt = 0
		while cmpt < len(voisins) and gagne == False:
			gagne = parcours(voisins[cmpt], chemin)
			cmpt+=1

		if not gagne :
			chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse

	return gagne


def affichage(n) :
	""" affichage simple de l'échiquier avec ordre de parcours des cellules indiqué."""

	t = [[0 for j in range(n) ] for k in range(n)]
	chemin = cavalierHamiltonHeuristique(n)

	rg = 1
	for x in chemin :
		if rg > 9 : t[x//n][x%n] = str(rg)
		else : t[x//n][x%n] = '0'+str(rg)
		rg += 1


	for ligne in t :
		for c in ligne :
			print(c, end=" ")
		print()

affichage(8)