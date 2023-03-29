import pygame
import sys
import os

worldx = 900
worldy = 900
fps = 100
ani = 4

BLACK = (0, 0, 0)
world = pygame.display.set_mode([worldx, worldy])

clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

while main:
    world.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
    pygame.display.flip()
    clock.tick(fps)