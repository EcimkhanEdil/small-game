import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.pl_1.rect.midtop

        self.x=float(self.rect.x)
        self.rect.y += 40 

    def update(self):
        self.x+=self.settings.bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet_2(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.pl_2.rect.midtop

        self.x=float(self.rect.x)
        self.rect.y += 40 

    def update(self):
        self.x-=self.settings.bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Ai_bullet_1(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=(255, 0, 0)

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ai.rect.midtop

        self.x=float(self.rect.x)
        self.rect.y += 114 

    def update(self):
        self.x-=self.settings.ai_bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
class Ai_bullet_2(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=(255, 0, 0)

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ai.rect.midtop

        self.x=float(self.rect.x)
        self.rect.y += 114 

    def update(self):
        self.x+=self.settings.ai_bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
class Ai_bullet_3(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=(255, 0, 0)

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ai.rect.midtop

        self.x=float(self.rect.x)
        self.rect.y += 161

    def update(self):
        self.x-=self.settings.ai_bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
class Ai_bullet_4(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=(255, 0, 0)

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ai.rect.midtop

        self.x=float(self.rect.x)
        self.rect.y += 161

    def update(self):
        self.x+=self.settings.ai_bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)