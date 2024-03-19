import pygame, sys, random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

windowWidth = 640
windowHeight = 480
squareX = 0
squareY = 0
YELLOW = (255, 255, 0)

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Se déplacer et animer les objets !')

while True:

    surface.fill((0, 0, 0))

    # dessiner des rectangles aléatoires
    pygame.draw.rect(surface, YELLOW, (random.randint(0, windowWidth), random.randint(0, windowHeight), 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    pygame.display.update()