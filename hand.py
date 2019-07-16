import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 2
        self.start = pg.time.get_ticks()
        super().__init__()
        self.images = [
            pg.image.load("img/slap4.small.png").convert_alpha(),
            pg.image.load("img/unslap4.small.png").convert_alpha(),
            pg.image.load("img/slap5.small.png").convert_alpha(),
            pg.image.load("img/slap6.small.png").convert_alpha(),
            pg.image.load("img/slap7.small.png").convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, slaps, deltaX, deltaY):
        self.image = self.images[slaps]
        self.rect.x += deltaX
        self.rect.y += deltaY


class Bruise(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 1
        self.bruise = 1
        self.start = pg.time.get_ticks()
        super().__init__()
        self.image = pg.image.load("img/bruise3.small.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ouchie(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 1
        self.text = 1
        self.start = pg.time.get_ticks()
        super().__init__()
        self.image = pg.image.load("img/ouchie.small.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ooh(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 1
        self.text = 1
        self.start = pg.time.get_ticks()
        super().__init__()
        self.image = pg.image.load("img/ooh.small.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Win(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 3
        self.text = 1
        self.start = pg.time.get_ticks()
        super().__init__()
        self.image = pg.image.load("img/winner.small.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Win2(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 3
        self.text = 1
        self.start = pg.time.get_ticks()
        super().__init__()
        self.image = pg.image.load("img/winner2.small.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Wtf(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 3
        self.text = 1
        self.start = pg.time.get_ticks()
        super().__init__()
        self.image = pg.image.load("img/wtf.small.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
