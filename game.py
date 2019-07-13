import pygame as pg
import sys
import math
from hand import Player1, Player2, Bruise1, Bruise2


pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 255, 0)
GREEN = (0, 255, 0)

display_width = 1600
display_height = 1200

flags = pg.DOUBLEBUF
screen = pg.display.set_mode((display_width, display_height), flags)
pg.display.set_caption("BUTTCON2019")


clock = pg.time.Clock()
background = pg.image.load("butt4.jpg")


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
font = pg.font.Font(None, 150)
font2 = pg.font.Font(None, 30)
poslog1 = {}
poslog2 = {}


MAX_HEALTH = 500

pg.joystick.init()
joystick = pg.joystick.Joystick(0)


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


running = True
win = None

screen.blit(background, (0, 0))
while running:

    deltaX1 = 0
    deltaY1 = 0
    deltaX2 = 0
    deltaY2 = 0

    if score1 > MAX_HEALTH:
        win = "PLAYER1 WINS"
    elif score2 > MAX_HEALTH:
        win = "PLAYER2 WINS"
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if win is None:
            # handle p1
            if event.type == pg.KEYDOWN and event.key == pg.K_COMMA:
                start_time1 = pg.time.get_ticks()
            if event.type == pg.KEYUP and event.key == pg.K_COMMA:
                slap1 = 1
                if player1.rect.y > 250:
                    key = "{}_{}".format(player1.rect.x, player1.rect.y)
                    poslog1[key] = poslog1.get(key, 0) + 5
                    score1 += (pg.time.get_ticks() - start_time1) / poslog1[key]
                    if player1_charging:
                        bruise_sprites.add(Bruise1(player1.rect.x, player1.rect.y))
                        player1_charging = 0

            # handle p2 in same way
            if event.type == pg.KEYDOWN and event.key == pg.K_PERIOD:
                start_time2 = pg.time.get_ticks()
            if event.type == pg.KEYUP and event.key == pg.K_PERIOD:
                slap2 = 1
                if player2.rect.y > 250:
                    key = "{}_{}".format(player2.rect.x, player2.rect.y)
                    poslog2[key] = poslog2.get(key, 0) + 5
                    score2 += (pg.time.get_ticks() - start_time2) / poslog2[key]
                    start_time2 = 0
                    if player2_charging:
                        bruise_sprites.add(Bruise2(player2.rect.x, player2.rect.y))
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

    joystick = pg.joystick.Joystick(0)
    joystick.init()
    deltaX1 = joystick.get_axis(0) * 50
    deltaY1 = joystick.get_axis(1) * 50
    player1_charging = joystick.get_button(14)

    for s in bruise_sprites:
        screen.blit(background, s.rect, s.rect)
    for s in all_sprites_list:
        screen.blit(background, s.rect, s.rect)
    bruise_sprites.draw(screen)
    all_sprites_list.draw(screen)

    fps = font2.render(str(int(clock.get_fps())), True, WHITE)
    screen.blit(fps, (50, display_height - 30))
    draw_health(score1, 50, 50)
    draw_health(score2, display_width - 500, 50)
    if win:
        pg.draw.rect(
            screen, BLACK, pg.Rect(0, display_height / 2 - 50, display_width, 100)
        )
        screen.blit(font2.render(win, True, WHITE), (400, display_height / 2))

    pg.display.update()

    player1.update(slap1, deltaX1, deltaY1)
    player2.update(slap2, deltaX2, deltaY2)
    clock.tick(30)
    slap1 = 0
    slap2 = 0

pg.quit()
quit()
