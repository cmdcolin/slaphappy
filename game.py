import pygame as pg
import sys
import math
from hand import Player, Bruise


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

# sprites = pg.sprite.Group()
sprites = pg.sprite.LayeredUpdates()


player = Player(display_width * 0.10, display_height * 0.5)

# Add the car to the list of objects
sprites.add(player)

slap = 0
score = 0
start_time = 0
player_charging = 0
font = pg.font.Font(None, 150)
font2 = pg.font.Font(None, 30)
poslog = {}


MAX_SCORE = 500

pg.joystick.init()
joystick = pg.joystick.Joystick(0)
joystick.init()


def draw_health(health, x, y):
    if health > MAX_SCORE * 2 / 3:
        color = GREEN
    elif health > MAX_SCORE * 2 / 3:
        color = ORANGE
    else:
        color = RED
    width = min(400 * health / MAX_SCORE, MAX_SCORE)
    pg.draw.rect(screen, BLACK, pg.Rect(x - 1, y - 1, 402, 52))
    pg.draw.rect(screen, color, pg.Rect(x, y, width, 50))


running = True
win = None
screen.blit(background, (0, 0))

while running:

    deltaX = 0
    deltaY = 0

    if score > MAX_SCORE:
        win = "YOU WIN"
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #     if win is None:
    #         # handle p1
    #         if event.type == pg.KEYDOWN and event.key == pg.K_COMMA:
    #             start_time1 = pg.time.get_ticks()
    #         if event.type == pg.KEYUP and event.key == pg.K_COMMA:
    #             slap1 = 1
    #             if player1.rect.y > 250:
    #                 key = "{}_{}".format(player1.rect.x, player1.rect.y)
    #                 poslog1[key] = poslog1.get(key, 0) + 5
    #                 score1 += (pg.time.get_ticks() - start_time1) / poslog1[key]
    #                 if player1_charging:
    #                     bruise_sprites.add(Bruise1(player1.rect.x, player1.rect.y))
    #                     player1_charging = 0

    #         # handle p2 in same way
    #         if event.type == pg.KEYDOWN and event.key == pg.K_PERIOD:
    #             start_time2 = pg.time.get_ticks()
    #         if event.type == pg.KEYUP and event.key == pg.K_PERIOD:
    #             slap2 = 1
    #             if player2.rect.y > 250:
    #                 key = "{}_{}".format(player2.rect.x, player2.rect.y)
    #                 poslog2[key] = poslog2.get(key, 0) + 5
    #                 score2 += (pg.time.get_ticks() - start_time2) / poslog2[key]
    #                 start_time2 = 0
    #                 if player2_charging:
    #                     player2_charging = 0

    pressed = pg.key.get_pressed()

    if pressed[pg.K_COMMA]:
        print("down")
        slap = 1
        player_charging = 1
    if slap == 1 and not pressed[K_COMMA]:
        print("up")
        slap = 0

    # if pressed[pg.K_PERIOD]:
    #     if pg.time.get_ticks() - start_time2 > 300:
    #         player2_charging = 1

    if pressed[pg.K_LEFT]:
        deltaX = -50
    if pressed[pg.K_RIGHT]:
        deltaX = 50
    if pressed[pg.K_UP]:
        deltaY = -50
    if pressed[pg.K_DOWN]:
        deltaY = 50
    # if pressed[pg.K_a]:
    #     deltaX2 = -50
    # if pressed[pg.K_d]:
    #     deltaX2 = 50
    # if pressed[pg.K_w]:
    #     deltaY2 = -50
    # if pressed[pg.K_s]:
    #     deltaY2 = 50

    joystick = pg.joystick.Joystick(0)
    deltaX += joystick.get_axis(0) * 50
    deltaY += joystick.get_axis(1) * 50
    player_charging = joystick.get_button(14)
    player.update(slap, deltaX, deltaY)

    # for s in bruise_sprites:
    #     screen.blit(background, s.rect, s.rect)
    # for s in sprites:
    #     screen.blit(background, s.rect, s.rect)
    # bruise_sprites.draw(screen)
    ret = sprites.clear(screen, background)
    ret = sprites.draw(screen)

    fps = font2.render(str(int(clock.get_fps())), True, WHITE)
    screen.blit(
        background, (50, display_height - 30), (50, display_height - 30, 100, 20)
    )
    screen.blit(fps, (50, display_height - 30))
    # draw_health(score, 50, 50)
    if win:
        pg.draw.rect(
            screen, BLACK, pg.Rect(0, display_height / 2 - 50, display_width, 100)
        )
        screen.blit(font2.render(win, True, WHITE), (400, display_height / 2))

    pg.display.update()
    # pg.display.flip()

    clock.tick(30)
    slap = 0

pg.quit()
quit()
