import pygame
from constante import *
from player import Player
pygame.init()

ecran = pygame.display.set_mode((800,600))
player = Player()
clock = pygame.time.Clock()

running = True
while running:
    tick = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    mouse = pygame.mouse.get_pos()
    player.rotating()


    ecran.blit(fondIMG, (0,0))
    ecran.blit(player.image, (player.rect.x, player.rect.y))
    for i in player.lasers:
        i.move()

        ecran.blit(i.image, i.rect)

    pygame.display.update()


pygame.quit()
