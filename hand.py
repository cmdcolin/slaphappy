import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 2
        super().__init__()
        self.images = [
            pygame.image.load("slap4.png").convert_alpha(),
            pygame.image.load("unslap4.png").convert_alpha(),
            pygame.image.load("slap5.png").convert_alpha(),
            pygame.image.load("slap6.png").convert_alpha(),
            pygame.image.load("slap7.png").convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, slaps, deltaX, deltaY):
        self.image = self.images[slaps]
        self.rect.x += deltaX
        self.rect.y += deltaY


class Bruise(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = 1
        super().__init__()
        self.image = pygame.image.load("bruise2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
