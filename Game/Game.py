#Import Modules
import pygame
import sys
import os

#Create world
worldx = 900
worldy = 900
fps = 100
ani = 4

world = pygame.display.set_mode([worldx, worldy])
#Set Color Values
BLACK = (0, 0, 0)

#borders
pygame.draw.rect((900,0,0), (worldx, worldy))

#background
bg_img = pygame.image.load()


#Setup
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

#Main loop
while main:
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


#user
class Player(pygame.sprite.Sprite):
    def _init_(self):
        super(Player,self)._init_()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

#user movement
press_keys = pygame.key.get_pressed()

def update(self, pressed_keys):
    if pressed_key[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_key[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_key[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_key[K_RIGHT]:
        self.rect.move_ip(5,0)



#platforms


#