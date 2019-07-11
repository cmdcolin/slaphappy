import pygame as pg, sys, math
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


start_time1 = 0
start_time2 = 0

MAX_HEALTH = 5000


def draw_health(health):
    if health > 66:
        color = GREEN
    elif health > 33:
        color = ORANGE
    else:
        color = RED
    width = int(400 * health / MAX_HEALTH)
    health_bar = pg.Rect(0, 0, width, 7)
    if health < MAX_HEALTH:
        pg.draw.rect(screen, color, health_bar)


while not crashed:

    screen.blit(butt, (0, 0))
    bruise_sprites.draw(screen)
    screen.blit(background, (0, 0))
    all_sprites_list.draw(screen)

    deltaX1 = 0
    deltaY1 = 0
    deltaX2 = 0
    deltaY2 = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
        # handle p1
        if event.type == pg.KEYDOWN and event.key == pg.K_COMMA:
            start_time1 = pg.time.get_ticks()
        if event.type == pg.KEYUP and event.key == pg.K_COMMA:
            slap1 = 1
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
    fps = font2.render(str(int(clock.get_fps())), True, WHITE)
    screen.blit(fps, (50, display_height - 30))
    font.render(str(int(clock.get_fps())), True, WHITE)
    screen.blit(font.render(str(math.floor(score1)), True, WHITE, BLACK), (50, 50))
    font.render(str(score2), True, WHITE)
    screen.blit(
        font.render(str(math.floor(score2)), True, WHITE, BLACK),
        (display_width - font.size(str(math.floor(score2)))[0] - 50, 50),
    )

    pg.display.update()
    clock.tick(30)
    slap1 = 0
    slap2 = 0

pg.quit()
quit()
