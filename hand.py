import pygame


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load("slap4.png").convert_alpha(),
            pygame.image.load("unslap4.png").convert_alpha(),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def update(self, slaps):
        if slaps:
            self.image = self.images[1]
        else:
            self.image = self.images[0]


class Player2(Player1):
    def __init__(self):
        super().__init__()
        self.images = [
            pygame.transform.flip(self.images[0], True, False),
            pygame.transform.flip(self.images[1], True, False),
        ]
        self.image = self.images[0]
