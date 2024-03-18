import pygame
import sys

# Initialisation de Pygame
pygame.init()

# nb de cases

LONGUEUR = 10 
LARGEUR = 10

# Définition de la taille de la fenêtre

taille_case = 100

# Couleurs
blanc = (210, 180, 140)
noir = (139, 69, 19)

# Création de la fenêtre
fenetre = pygame.display.set_mode((taille_case*LONGUEUR, taille_case*LARGEUR))
pygame.display.set_caption("Échiquier Vierge")

# Boucle principale
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessin de l'échiquier
    fenetre.fill(blanc)
    for ligne in range(LONGUEUR):
        for colonne in range(LARGEUR):
            couleur_case = blanc if (ligne + colonne) % 2 == 0 else noir
            pygame.draw.rect(fenetre, couleur_case, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))

    # Rafraîchissement de l'affichage
    pygame.display.flip()

# Fin du programme
