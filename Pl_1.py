import pygame


class Card():
    def __init__(self,x,y,width,heigth,game):
        self.screen=game.screen
        self.rect=pygame.Rect(x, y, width, heigth)
    def set_text(self,text,size):
        self.image=pygame.font.Font(None,size).render(str(text),True,(255,0,0))
    def draw_text(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))


class Player_1:
    def __init__(self, game):
        self.screen=game.screen
        self.settings=game.settings
        self.screen_rect= game.screen.get_rect()

        self.image=pygame.transform.scale(pygame.image.load('Images_from_durka\wermacht_s.png'),(60,120))
        self.rect=self.image.get_rect()

        #self.rect.midbottom=self.screen_rect.midbottom

        self.rect.x = 100
        self.rect.y = 780
        self.x=float(self.rect.x)
        self.hp=game.settings.pl_1_hp
        # Устанавливаем начальные координаты
        #print(self.rect.y)
        #print(self.rect.x)
        

        self.moving_right=False
        self.moving_left=False
        self.prised=False
        self.visenie=False

    def update(self):
        if self.moving_right and self.rect.right<620:
            self.x += self.settings.pl_1_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.pl_1_speed

        if self.prised==True:
            self.rect.y=840
            self.rect.height=60
            #print('sdafwfwfwef')
        if self.prised!=True:
            self.rect.y=780
            self.rect.height=120

        if self.visenie==True:
            self.rect.y=720
        if self.visenie!=True and self.prised!=True:
            self.rect.y=780

        self.rect.x=self.x

    def blitime(self):
        self.image=pygame.transform.scale(pygame.image.load('Images_from_durka\wermacht_s.png'),(self.rect.width,self.rect.height))
        self.screen.blit(self.image, self.rect)

class Player_2:
    def __init__(self, game):
        self.screen=game.screen
        self.settings=game.settings
        self.screen_rect= game.screen.get_rect()

        self.image=pygame.transform.scale(pygame.image.load('Images_from_durka\wermacht_ss.png'),(60,120))
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom

        self.rect.x = 1000
        self.rect.y = 780
        self.x=float(self.rect.x)
        self.hp=game.settings.pl_2_hp
        #print(self.rect.y)
        #print(self.rect.x)

        self.moving_right=False
        self.moving_left=False
        self.prised=False
        self.visenie=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.pl_2_speed
        if self.moving_left and self.rect.left>920:
            self.x -= self.settings.pl_2_speed #post 12825184 on a rule 34, i joked you XD

        if self.prised==True:
            self.rect.y=840
            self.rect.height=60
            #print('sdafwfwfwef')
        if self.prised!=True:
            self.rect.y=780
            self.rect.height=120

        if self.visenie==True:
            self.rect.y=720
        if self.visenie!=True and self.prised!=True:
            self.rect.y=780
        self.rect.x=self.x

    def blitime(self):
        self.image=pygame.transform.scale(pygame.image.load('Images_from_durka\wermacht_ss.png'),(self.rect.width,self.rect.height))
        self.screen.blit(self.image, self.rect)