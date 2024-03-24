import pygame
import sys
from parcoursPlusieurs import *

# nombre de cases

TAILLE_CASE = 101
TAILLE_ZONE_TEXT = 200

# Initialisation de Pygame
pygame.init()
clock = pygame.time.Clock()

# Enregitrement des résultats du parcours
tabParcours = []
nbChem = 0

# Variables de position du cavalier
estPose = False
estArrivee = False # Permet de stopper l'ajout des cases à "caseDejaParcouru"
x = 0
y = 0

# Tracé du parcours du cavalier
tabFl = []
caseDejaParcouru = []
indiceCurentCase = 0
aucunParcours = False

# Couleurs
blanc = (210, 180, 140)
noir = (139, 69, 19)
vert = (166, 231, 53)

# Textes
font = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 20)
text = ""


# Image
image = pygame.image.load("cavalier.png")
image = pygame.transform.scale(image, (TAILLE_CASE, TAILLE_CASE))

# ----------------- Fonctions---------------------
def getCoordCaseByIndice(caseIndice):
    coordx = int((caseIndice-1) % LONGUEUR * TAILLE_CASE)
    coordy = int((caseIndice-1) // LONGUEUR * TAILLE_CASE)
    return (coordx, coordy)

def getCaseIndiceByCoord(x,y):
    indiceCase = (x // TAILLE_CASE + 1) + (y // TAILLE_CASE) * LONGUEUR 
    return indiceCase

def centreCase(caseCoord):
    indicex = int(caseCoord[0] + TAILLE_CASE/2)
    indicey = int(caseCoord[1] + TAILLE_CASE/2)
    return (indicex, indicey)

# Création de la fenêtre
fenetre = pygame.display.set_mode((TAILLE_CASE*LONGUEUR+TAILLE_ZONE_TEXT, TAILLE_CASE*HAUTEUR))
pygame.display.set_caption("Problème : Le Parcours du Cavalier")

# Boucle principale de l'affichage
while True:

    fenetre.fill((200,150,100))

    # Dessin de l'échiquier
    for ligne in range(LONGUEUR):
        for colonne in range(HAUTEUR):
            couleur_case = blanc if (ligne + colonne) % 2 == 0 else noir
            if (colonne) * (LONGUEUR) + (ligne +1) in caseDejaParcouru:
                couleur_case_copy = []
                for i in couleur_case:
                    couleur_case_copy.append(i//2)
                couleur_case = tuple(couleur_case_copy)
            pygame.draw.rect(fenetre, couleur_case, (ligne * TAILLE_CASE, colonne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    # Gestion des events
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        # Vérifie si la case est valide et lance la recherche de parcours
        if event.type == pygame.MOUSEBUTTONDOWN and not estPose and event.button == 1:
            if event.pos[0] < TAILLE_CASE * LONGUEUR:
                estPose = True
                result = parcoursNonHeuristique(getCaseIndiceByCoord(event.pos[0], event.pos[1]), graphe())
                nbChem = len(result)
                if nbChem > 0:
                    tabParcours = result[0]
                    text = "Chemins trouvés : " + str(nbChem)
                else:
                    aucunParcours = True
                    tabParcours.append(getCaseIndiceByCoord(event.pos[0], event.pos[1]))


        if event.type == pygame.MOUSEMOTION and not estPose:
            x = event.pos[0]
            y = event.pos[1]
    
    # Affichage une fois que la case de départ a été choisie
    if estPose:
        # Texte
        textRenderer = font.render(text, True, (10,10,10))
        textRect = textRenderer.get_rect()
        textRect.center = (int(TAILLE_CASE*LONGUEUR+TAILLE_ZONE_TEXT/2), 40)
        fenetre.blit(textRenderer, textRect)

        if aucunParcours:
            # Texte si aucun chemin n'a été trouvé
            textRenderer2 = font2.render("Auncun chemin trouvés pour cette case", True, (10,10,10))
            textRect2 = textRenderer2.get_rect()
            textRect2.center = (int(TAILLE_CASE*LONGUEUR/2), int(TAILLE_CASE*HAUTEUR/2))
            fenetre.blit(textRenderer2, textRect2)

        # Affichage du cavalier
        fenetre.blit(image, getCoordCaseByIndice(tabParcours[indiceCurentCase]))

        # Calcul du chemin vert
        if not aucunParcours:
            if not estArrivee:
                caseDejaParcouru.append(tabParcours[indiceCurentCase])
            if indiceCurentCase < len(tabParcours) :
                    
                    if indiceCurentCase > 0:
                        pos1 = getCoordCaseByIndice(tabParcours[indiceCurentCase-1])
                        pos2 = getCoordCaseByIndice(tabParcours[indiceCurentCase])
                        tabFl.append((pos1, pos2))

                    if indiceCurentCase < len(tabParcours)-1:
                        indiceCurentCase+=1
            else:
                estArrivee = True
    
    # Affichage du contour de la case en vert
    elif x != 0 and y != 0 and x < LONGUEUR*TAILLE_CASE :
        pygame.draw.rect(fenetre, vert,(x//TAILLE_CASE*TAILLE_CASE,y//TAILLE_CASE*TAILLE_CASE, TAILLE_CASE,TAILLE_CASE), 5)
    
    # Dessin du chemin
    for fl in tabFl:
        pygame.draw.line(fenetre, vert, centreCase(fl[0]), centreCase(fl[1]), 3)
    
    
    # Rafraichissement de l'affichage
    pygame.display.flip()

    if estPose:
        clock.tick(3)
    else:
        clock.tick(60)

