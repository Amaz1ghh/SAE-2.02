import random
from tkinter import *

LONGUEUR = 5
LARGEUR = 7

class Case:
    def __init__(self, coorX, coorY):
        self.numCase = (coorX, coorY)  #indice de la case -> couple de coordonnées
        self.relCase = []
        
        self.dejaVu = False     # si deja vu, la case est en rouge et on ne peut plus aller dessus
        self.estDessus = False  # si est dessus, on affiche le cavalier sur la case

class Plateau:

    # Constructeur
    def __init__(self, cavX, cavY, anim = False):
        """constructeur"""
        self.plateau = []
        self.cavX = cavX    #coordonnées de base du cavalier
        self.cavY = cavY
        self.animation = anim
        for i in range(LARGEUR):
            self.plateau.append([])
            for j in range(LONGUEUR):
                self.plateau[i].append(Case(i, j))
        self.initGraphe()
        self.plateau[self.cavX][self.cavY].estDessus = True
        self.plateau[self.cavX][self.cavY].dejaVu = True
        chemin = self.backtracking(self.cavX, self.cavY)

        if self.animation:
            # création fenêtre et frames tkinter
            self.fenetre = Tk()
            self.fenetre.geometry('700x700')
            self.fenetre.title('Parcours Du Cavalier')
            self.fenetre['bg'] = '#F6B22F'
            self.fenetre.resizable(width=False, height=False)

            self.fenetre.update_idletasks()
            largeur_fenetre = self.fenetre.winfo_height()
            longueur_fenetre = self.fenetre.winfo_width()
            self.longueur_case = longueur_fenetre / LONGUEUR
            self.largeur_case = largeur_fenetre / LARGEUR

            self.image_cavalier = PhotoImage(file='cavalier.png')

            self.image_cavalier = self.image_cavalier.subsample(int(self.image_cavalier.width() / self.longueur_case)+1, int(self.image_cavalier.height() / self.largeur_case)+1)

            self.labels_cavalier = []

            for ligne in range(LARGEUR):
                for colonne in range(LONGUEUR):
                        couleur_case = "#D2B48C" if (ligne + colonne) % 2 == 0 else "#8B4513"
                        
                        case = Frame(self.fenetre, width=self.longueur_case, height=self.largeur_case, bg=couleur_case)
                        
                        case.grid(row=ligne, column=colonne)
            
            self.deplacer_cavalier(chemin, 0)
            self.fenetre.mainloop()

    def maj_affichage(self, ligne, colonne):
        # Met à jour l'affichage en fonction de l'état actuel de la case

        case = self.plateau[ligne][colonne]

        if case.estDessus:
            case = Frame(self.fenetre, width=self.longueur_case, height=self.largeur_case, bg='red')
            case.grid(row=ligne, column=colonne)
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
    
    def deplacer_cavalier(self, chemin, index):
            # Déplace le cavalier à l'index spécifié dans le chemin
            if index < len(chemin):
                pre_ligne, pre_colonne = chemin[index-1]
                ligne, colonne = chemin[index]
                self.plateau[pre_ligne][pre_colonne].estDessus = False
                self.maj_affichage(pre_ligne, pre_colonne)

                # Met à jour les coordonnées du cavalier sur le plateau
                self.cavX, self.cavY = ligne, colonne
                self.plateau[self.cavX][self.cavY].estDessus = True

                # Met à jour l'affichage
                self.maj_affichage(ligne, colonne)

                # Appel récursif avec un délai de 500 millisecondes
                self.fenetre.after(500, lambda: self.deplacer_cavalier(chemin, index + 1))
                


    def initGraphe(self):
        for i in range(LARGEUR):
            for j in range(LONGUEUR):
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
                    if (i+1 < LARGEUR):
                        self.plateau[i][j].relCase.append(self.plateau[i+1][j-2].numCase)
                if (j+2 < LONGUEUR):
                    if (i-1 >= 0):
                        self.plateau[i][j].relCase.append(self.plateau[i-1][j+2].numCase)
                    if (i+1 < LARGEUR):
                        self.plateau[i][j].relCase.append(self.plateau[i+1][j+2].numCase)
             
    
    
    def backtracking(self, x, y, chain=None):
        if chain is None:
            chain = []

        chain.append(self.plateau[x][y].numCase)
        self.plateau[x][y].dejaVu = True

        if len(chain) == LONGUEUR * LARGEUR:
            return chain

        for relation in self.plateau[x][y].relCase:
            next_x, next_y = relation
            if not self.plateau[next_x][next_y].dejaVu:
                ext_chain = self.backtracking(next_x, next_y, chain)
                if ext_chain:
                    return ext_chain

        self.plateau[x][y].dejaVu = False
        chain.pop()

        return None
          

jeu = Plateau(0, 0, True)






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
	E = graphe(n)
	chemin = [] # contiendra les cases dans leur ordre de visite


	def parcours( case ) :
		"""
			case : case actuelle du cavalier.
		"""
		chemin.append(case) # case est ajoutée au chemin, ce qui la marque comme visitée également

		if len(chemin) == n*n :
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

			for v in voisins :
				if gagne : break
				else : gagne = parcours( v )
			if not gagne :
				chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse


		return gagne


	parcours(  random.randint(0,n*n-1)  )
	return chemin


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