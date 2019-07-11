import pygame


class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load("slap4.png").convert_alpha(),
            pygame.image.load("unslap4.png").convert_alpha(),
            pygame.image.load("chargeup.png").convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, slaps, deltaX, deltaY):
        self.image = self.images[slaps]
        self.rect.x += deltaX
        self.rect.y += deltaY


class Player2(Player1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.images = list(
            map(lambda x: pygame.transform.flip(x, True, False), self.images)
        )
        self.image = self.images[0]


class Bruise1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bruise2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Bruise2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bruise2.png").convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
