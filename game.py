import pygame as pg
import sys
import math
from hand import Player, Bruise, Ouchie, Ooh, Win, Win2


pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE= (255, 165, 0)
YELLOW = (255, 255, 0)

GREEN = (0, 255, 0)

display_width = 400
display_height = 300

flags = pg.DOUBLEBUF|pg.FULLSCREEN
screen = pg.Surface((display_width, display_height), flags)
surface = pg.display.set_mode((800,600),flags)
pg.display.set_caption("BUTTCON2019")


clock = pg.time.Clock()
background = pg.image.load("butt5.small.png")
main_screen = pg.image.load("main-screen.small.png")
instructions = pg.image.load("instructions.small.png")

# sprites = pg.sprite.Group()
sprites = pg.sprite.LayeredUpdates()


player = Player(display_width * 0.10, display_height * 0.5)

# add the car to the list of objects
sprites.add(player)

slap = 0
score = 0
start_time = 0
initial_win = 0
hold_down_time = 0
player_charging = 0
font = pg.font.Font(None, 150)
font2 = pg.font.Font(None, 30)
poslog = {}
super_smack = False


MAX_SCORE = 5000

pg.joystick.init()
joystick = pg.joystick.Joystick(0)
joystick.init()

effect = pg.mixer.Sound("claps.wav")
effect2 = pg.mixer.Sound("clap1.wav")


def draw_health(health, x, y):
    if health > MAX_SCORE * 3/4:
        color = GREEN
    elif health > MAX_SCORE * 1 / 2:
        color = YELLOW
    elif health > MAX_SCORE * 1/4:
        color = ORANGE
    else:
        color = RED
    width = min(display_width/4 * health / MAX_SCORE, MAX_SCORE)
    pg.draw.rect(screen, BLACK, pg.Rect(x - 1, y - 1, display_width/4+2, display_height/16+2))
    pg.draw.rect(screen, color, pg.Rect(x, y, width, display_height/16))


running = True
win = False

intro = True
instruction_screen = False
getting_started = False


def reset():
    global slap, win, super_smack, score, start_time, hold_down_time, player_charging, poslog, getting_started, initial_win, sprites, player,screen
    slap = False
    getting_started = False
    win = None
    super_smack = False
    score = 0
    start_time = 0
    hold_down_time = 0
    initial_win=0
    player_charging = 0
    poslog = {}
    screen.blit(background, (0, 0))
    sprites = pg.sprite.LayeredUpdates()
    player = Player(display_width * 0.10, display_height * 0.5)
    sprites.add(player)




while running:
    deltaX = 0
    deltaY = 0
    pressed = pg.key.get_pressed()
    delta = display_width/30

    if pressed[pg.K_ESCAPE]:
        running = False
    if pressed[pg.K_LEFT]:
        deltaX = -delta
    if pressed[pg.K_RIGHT]:
        deltaX = delta
    if pressed[pg.K_UP]:
        deltaY = -delta
    if pressed[pg.K_DOWN]:
        deltaY = delta

    deltaX += joystick.get_axis(0) * delta
    deltaY += joystick.get_axis(1) * delta
    button_pressed = joystick.get_button(14)
    mp = pressed[pg.K_COMMA] or button_pressed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if intro:
        screen.blit(main_screen, (0, 0))
        if mp:
            getting_started = True
        if getting_started and not mp:
            intro = False
            instruction_screen = True
            getting_started = False

    elif instruction_screen:
        screen.blit(instructions, (50, 50))
        if mp:
            getting_started = True
        if getting_started and not mp:
            instruction_screen = False
            reset()

    else:

        if score > MAX_SCORE:
            if not win:
                win = True
                initial_win = pg.time.get_ticks()
            if pg.time.get_ticks()-initial_win>3000:
                reset()
                intro = True

            for e in sprites:
                if e.text:
                    sprites.remove(e)

            sprites.add(Win(display_width/10, display_height/16))
            sprites.add(Win2(display_width/2, display_height/2))
        elif not win:
            if slap == 0 and mp:
                slap = 2
                hold_down_time = pg.time.get_ticks()
            if slap >= 2 and not mp:
                slap = 1
                start_time = pg.time.get_ticks()
            if slap == 2 and mp and pg.time.get_ticks() - hold_down_time > 500:
                slap = 3
                start_time = pg.time.get_ticks()
                super_smack = True
            if slap == 3 and mp and pg.time.get_ticks() - hold_down_time > 1000:
                slap = 4
                start_time = pg.time.get_ticks()
            if slap == 1 and pg.time.get_ticks() - start_time > 10:
                if super_smack:
                    sprites.add(Bruise(player.rect.x, player.rect.y))
                    super_smack = False
                slap = 0
                if pg.time.get_ticks() - hold_down_time > 1000:
                    sprites.add(Ouchie(display_width/2, display_height/16))
                    score = 0
                    effect2.play()
                else:
                    score += pg.time.get_ticks() - hold_down_time
                    sprites.add(Ooh(display_width/4, display_height/16))
                    effect.play()
                hold_down_time = 0

            for e in sprites:
                if e.text:
                    if pg.time.get_ticks() - e.start > 500:
                        sprites.remove(e)

            player.update(slap, deltaX, deltaY)

        ret = sprites.clear(screen, background)
        ret = sprites.draw(screen)

        draw_health(score, 50, 50)

    pg.transform.scale(screen, (800,600), surface)
    pg.display.update()
    # pg.display.flip()

    clock.tick(30)
    # slap = 0

pg.quit()
quit()
