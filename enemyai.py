import pygame

class Enemyai:
    def __init__(self, game):
        self.screen=game.screen
        self.settings=game.settings
        self.screen_rect= game.screen.get_rect()

        self.image=pygame.transform.scale(pygame.image.load('Images_from_durka\pixil-frame-0.png'),(240,200))
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom

        self.x=float(self.rect.x)
        self.hp=game.settings.ai_hp

        self.moving_right=False
        self.moving_left=False

    def blitime(self):
        self.screen.blit(self.image, self.rect)