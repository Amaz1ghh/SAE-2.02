import pygame
import sys

# Initialisation de Pygame
pygame.init()
clock = pygame.time.Clock()

# variable temp
tabtemp = [30, 34, 26, 13, 2, 10, 6, 17, 4, 12, 23, 36, 28, 32, 19, 8, 21, 25, 33, 29, 18, 5, 9, 1, 14, 22, 35, 24, 11, 15, 7, 3, 16, 27, 31, 20]
nbChemTemp = 153

# nb de cases
LONGUEUR = 6
HAUTEUR = 6

# Définition de la taille de la fenêtre
TAILLE_CASE = 101

# Variable de positionnement du cavalier
estPose = False
estArrivee = False # Permet de stoper l'ajout des case à "caseDejaParcouru"
x = 0
y = 0

# Tableau des flèches pour le parcours du cavalier
tabFl = []
caseDejaParcouru = []
indiceCurentCase = 0

# Couleurs
blanc = (210, 180, 140)
noir = (139, 69, 19)
vert = (166, 231, 53)

# Texte
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Nombre de Chemins trouvés : ' + str(nbChemTemp), True, (10,10,10))

# Image
image = pygame.image.load("cavalier.png")
image = pygame.transform.scale(image, (TAILLE_CASE, TAILLE_CASE))


# fonction qui place le cavalier

def deplacerCavalier(caseIndice):
    indicex = int((caseIndice-1) % LONGUEUR * TAILLE_CASE)
    indicey = int((caseIndice-1) // LONGUEUR * TAILLE_CASE)
    return (indicex, indicey)

def centreCase(caseCoord):
    indicex = int(caseCoord[0] + TAILLE_CASE/2)
    indicey = int(caseCoord[1] + TAILLE_CASE/2)
    return (indicex, indicey)



# Création de la fenêtre
fenetre = pygame.display.set_mode((TAILLE_CASE*LONGUEUR+200, TAILLE_CASE*HAUTEUR))
pygame.display.set_caption("Problème : Le Parcours du Cavalier")

# Boucle principale
while True:

    # Dessin de l'échiquier
    fenetre.fill((200,150,100))
    for ligne in range(LONGUEUR):
        for colonne in range(HAUTEUR):
            couleur_case = blanc if (ligne + colonne) % 2 == 0 else noir
            if (colonne) * (LONGUEUR) + (ligne +1) in caseDejaParcouru:
                couleur_case_copy = []
                for i in couleur_case:
                    couleur_case_copy.append(i//2)
                couleur_case = tuple(couleur_case_copy)
            pygame.draw.rect(fenetre, couleur_case, (ligne * TAILLE_CASE, colonne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not estPose and event.button == 1:
            estPose = True

        if event.type == pygame.MOUSEMOTION and not estPose:
            x = event.pos[0]
            y = event.pos[1]
            
    if estPose:
        fenetre.blit(image, deplacerCavalier(tabtemp[indiceCurentCase]))

        if not estArrivee:
            caseDejaParcouru.append(tabtemp[indiceCurentCase])

        if indiceCurentCase < len(tabtemp) :
                
                if indiceCurentCase > 0:
                    pos1 = deplacerCavalier(tabtemp[indiceCurentCase-1])
                    pos2 = deplacerCavalier(tabtemp[indiceCurentCase])
                    tabFl.append((pos1, pos2))
                if indiceCurentCase < len(tabtemp)-1:
                    indiceCurentCase+=1
                
        else:
            estArrivee = True
        

        

    elif x != 0 and y != 0:
        pygame.draw.rect(fenetre, vert,(x//TAILLE_CASE*TAILLE_CASE,y//TAILLE_CASE*TAILLE_CASE, TAILLE_CASE,TAILLE_CASE), 5)
    
    # Dessin du chemin
    for fl in tabFl:
        pygame.draw.line(fenetre, vert, centreCase(fl[0]), centreCase(fl[1]), 3)
    
    
    # Rafraîchissement de l'affichage
    pygame.display.flip()

    if estPose:
        clock.tick(3)
    else:
        clock.tick(60)



# Fin du programme
