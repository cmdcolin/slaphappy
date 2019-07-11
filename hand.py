import pygame


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("slap4.png").convert_alpha()
        self.rect = self.image.get_rect()


class Player2(Player1):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.flip(self.image, True, False)
