import pygame, sys
from hand import Player1, Player2
from pygame import *


pygame.init()


display_width = 1600
display_height = 1200

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BUTTCON2019")

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
butt = pygame.image.load("butt4.png")


all_sprites_list = pygame.sprite.Group()

player1 = Player1()
player1.rect.x = display_width * 0.10
player1.rect.y = display_height * 0.5
player2 = Player2()
player2.rect.x = display_width * 0.55
player2.rect.y = display_height * 0.5

# Add the car to the list of objects
all_sprites_list.add(player1)
all_sprites_list.add(player2)

p1slaps = 0
p2slaps = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    screen.blit(butt, (0, 0))

    all_sprites_list.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_COMMA:
            p1slaps = 1
        elif event.type == KEYUP and event.key == K_COMMA:
            p1slaps = 0
        elif event.type == KEYDOWN and event.key == K_PERIOD:
            p2slaps = -1
        elif event.type == KEYUP and event.key == K_PERIOD:
            p2slaps = 0

    player1.update(p1slaps)
    player2.update(p2slaps)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
