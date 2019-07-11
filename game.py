import pygame as pg
import sys
import math
from hand import Player1, Player2, Bruise


pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 255, 0)
GREEN = (0, 255, 0)

display_width = 1600
display_height = 1200

screen = pg.display.set_mode((display_width, display_height))
pg.display.set_caption("BUTTCON2019")


clock = pg.time.Clock()
crashed = False
butt = pg.image.load("butt4.png")
background = pg.image.load("background.png")


all_sprites_list = pg.sprite.Group()
bruise_sprites = pg.sprite.Group()

player1 = Player1(display_width * 0.10, display_height * 0.5)
player2 = Player2(display_width * 0.55, display_height * 0.5)

# Add the car to the list of objects
all_sprites_list.add(player1)
all_sprites_list.add(player2)

slap1 = 0
slap2 = 0
score1 = 0
score2 = 0
start_time1 = 0
start_time2 = 0
player1_charging = 0
player2_charging = 0
font = pg.font.Font(None, 120)
font2 = pg.font.Font(None, 30)
poslog1 = {}
poslog2 = {}


MAX_HEALTH = 500


def draw_health(health, x, y):
    if health > MAX_HEALTH * 2 / 3:
        color = GREEN
    elif health > MAX_HEALTH * 2 / 3:
        color = ORANGE
    else:
        color = RED
    width = min(400 * health / MAX_HEALTH, MAX_HEALTH)
    pg.draw.rect(screen, BLACK, pg.Rect(x - 1, y - 1, 402, 52))
    pg.draw.rect(screen, color, pg.Rect(x, y, width, 50))


while not crashed:

    deltaX1 = 0
    deltaY1 = 0
    deltaX2 = 0
    deltaY2 = 0

    if score1 > MAX_HEALTH:
        fps = font.render("PLAYER1 WINS", True, WHITE)
        screen.blit(fps, (50, display_height - 30))
    elif score2 > MAX_HEALTH:
        fps = font.render("PLAYER2 WINS", True, WHITE)
        screen.blit(fps, (50, display_height - 30))
    else:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True
            # handle p1
            if event.type == pg.KEYDOWN and event.key == pg.K_COMMA:
                start_time1 = pg.time.get_ticks()
            if event.type == pg.KEYUP and event.key == pg.K_COMMA:
                slap1 = 1
                if player1.rect.y < 250:
                    print("wtf")
                else:
                    key = "{}_{}".format(player1.rect.x, player1.rect.y)
                    poslog1[key] = poslog1.get(key, 0) + 5
                    score1 += (pg.time.get_ticks() - start_time1) / poslog1[key]
                    if player1_charging:
                        bruise_sprites.add(Bruise(player1.rect.x, player1.rect.y))
                        player1_charging = 0

            # handle p2 in same way
            if event.type == pg.KEYDOWN and event.key == pg.K_PERIOD:
                start_time2 = pg.time.get_ticks()
            if event.type == pg.KEYUP and event.key == pg.K_PERIOD:
                slap2 = 1
                if player2.rect.y < 250:
                    print("wtf")
                else:
                    key = "{}_{}".format(player2.rect.x, player2.rect.y)
                    poslog2[key] = poslog2.get(key, 0) + 5
                    score2 += (pg.time.get_ticks() - start_time2) / poslog2[key]
                    start_time2 = 0
                    if player2_charging:
                        bruise_sprites.add(Bruise(player2.rect.x, player2.rect.y))
                        player2_charging = 0

            pressed = pg.key.get_pressed()

            if pressed[pg.K_COMMA]:
                if pg.time.get_ticks() - start_time1 > 300:
                    player1_charging = 1

            if pressed[pg.K_PERIOD]:
                if pg.time.get_ticks() - start_time2 > 300:
                    player2_charging = 1

            if pressed[pg.K_LEFT]:
                deltaX1 = -50
            if pressed[pg.K_RIGHT]:
                deltaX1 = 50
            if pressed[pg.K_UP]:
                deltaY1 = -50
            if pressed[pg.K_DOWN]:
                deltaY1 = 50
            if pressed[pg.K_a]:
                deltaX2 = -50
            if pressed[pg.K_d]:
                deltaX2 = 50
            if pressed[pg.K_w]:
                deltaY2 = -50
            if pressed[pg.K_s]:
                deltaY2 = 50

    player1.update(slap1, deltaX1, deltaY1)
    player2.update(slap2, deltaX2, deltaY2)

    screen.blit(butt, (0, 0))
    bruise_sprites.draw(screen)
    screen.blit(background, (0, 0))
    all_sprites_list.draw(screen)
    fps = font2.render(str(int(clock.get_fps())), True, WHITE)
    screen.blit(fps, (50, display_height - 30))
    draw_health(score1, 50, 50)
    draw_health(score2, display_width - 500, 50)
    pg.display.update()
    clock.tick(30)
    slap1 = 0
    slap2 = 0

pg.quit()
quit()
