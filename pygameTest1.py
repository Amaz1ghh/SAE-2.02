import pygame
import sys

# Initialisation de Pygame
pygame.init()

# nb de cases
LONGUEUR = 5
LARGEUR = 5

# Définition de la taille de la fenêtre
TAILLE_CASE = 101

#variable de positionnement du cavalier
estPose = False
x = 0
y = 0

# Couleurs
blanc = (210, 180, 140)
noir = (139, 69, 19)
vert = (0, 255, 0)

#image
image = pygame.image.load("cavalier.png")
image = pygame.transform.scale(image, (TAILLE_CASE, TAILLE_CASE))


# fonction qui place le cavalier

def initPoseCavalier(x,y):
    casex = x // TAILLE_CASE
    casey = y // TAILLE_CASE
    return (casex*TAILLE_CASE,casey*TAILLE_CASE)


# Création de la fenêtre
fenetre = pygame.display.set_mode((TAILLE_CASE*LONGUEUR, TAILLE_CASE*LARGEUR))
pygame.display.set_caption("Échiquier Vierge")

# Boucle principale
while True:

    # Dessin de l'échiquier
    fenetre.fill(blanc)
    for ligne in range(LONGUEUR):
        for colonne in range(LARGEUR):
            couleur_case = blanc if (ligne + colonne) % 2 == 0 else noir
            pygame.draw.rect(fenetre, couleur_case, (colonne * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not estPose and event.button == 1:
            x,y = initPoseCavalier(event.pos[0], event.pos[1])
            estPose = True

        if event.type == pygame.MOUSEMOTION and not estPose:
            x = event.pos[0]
            y = event.pos[1]
            
    if estPose:
        fenetre.blit(image, (x,y))
    elif x != 0 and y != 0:
        pygame.draw.rect(fenetre, vert,(x//TAILLE_CASE*TAILLE_CASE,y//TAILLE_CASE*TAILLE_CASE, TAILLE_CASE,TAILLE_CASE), 5)

        

    # Rafraîchissement de l'affichage
    pygame.display.flip()
        

# Fin du programme
