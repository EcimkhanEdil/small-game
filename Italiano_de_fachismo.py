import pygame
from Benito import Settings
import sys
from Pl_1 import Player_1, Player_2, Card
from gvn import Bullet, Bullet_2, Ai_bullet_1, Ai_bullet_2, Ai_bullet_3, Ai_bullet_4
from enemyai import Enemyai
from random import randint
from time import sleep



class Maingame():
    #класс для управления игрой и ресурсами
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        pygame.display.set_caption('7 december 1941 XD')
        self.settings = Settings()# присваиваются настройки класса Settings в переменную 
        self.bullets_1 = pygame.sprite.Group()#создается группа для пуль
        self.bullets_2 = pygame.sprite.Group()
        self.bgg = pygame.transform.scale(pygame.image.load('Images_from_durka//royal_navy.jfif'),(1600,900))
        self.clesh = pygame.transform.scale(pygame.image.load('Images_from_durka//clesh.jfif'),(150,150))

        self.fire_sound = pygame.mixer.Sound('ss.mp3')
        pygame.mixer.music.load("ssd.mp3")  # Фоновая музыка
        pygame.mixer.music.play(-1)

        self.ai_bullets_1 = pygame.sprite.Group()
        self.ai_bullets_2 = pygame.sprite.Group()

        self.last_event_time = pygame.time.get_ticks()  # Время последнего события
        self.event_interval = 2000  # Интервал в миллисекундах (например, 1000 мс = 1 секунда)

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)# создается окно игры
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height

        self.pl_1=Player_1(self) #создается экземпляр класса Player_1
        self.pl_2=Player_2(self)
        self.ai=Enemyai(self)
        self.pl_1_hp_card=Card(self.pl_1.rect.x,700,0,0,self)
        self.pl_1_hp_card.set_text(self.pl_1.hp,27)
        self.pl_2_hp_card=Card(self.pl_2.rect.x,700,0,0,self)
        self.pl_2_hp_card.set_text(self.pl_2.hp,27)
        self.ai_hp_card=Card(self.ai.rect.x,700,0,0,self)
        self.ai_hp_card.set_text(self.ai.hp,27)
        self.gaming = True

    def run_vasya(self):
        while self.gaming:
            self._collide_bullets()
            self._check_1939()
            self._update_events()
            
            self.pl_1.update()
            self.pl_2.update()
            self._update_bullets()
            self.who_win()
            #print(len(self.bullets))
            self._update_screen()
            self.clock.tick(60)
            #print(self.ai.rect.x)
            #print(self.pl_1.prised)
            #print(self.pl_1.hp)

    def _update_screen(self):
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bgg,(0,0))
        self.screen.blit(self.clesh,(0,0))
        for bullet in self.bullets_1.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets_2.sprites():
            bullet.draw_bullet()
        for bullet in self.ai_bullets_1.sprites():
            bullet.draw_bullet()
        for bullet in self.ai_bullets_2.sprites():
            bullet.draw_bullet()
        self.pl_1.blitime()
        self.pl_2.blitime()
        self.ai.blitime()
        self.pl_1_hp_card.rect.y=self.pl_1.rect.y-70
        self.pl_1_hp_card.rect.x=self.pl_1.rect.x
        self.pl_1_hp_card.set_text(f"player 1 HP: {self.pl_1.hp}",27)
        self.pl_1_hp_card.draw_text()
        self.pl_2_hp_card.rect.y=self.pl_2.rect.y-70
        self.pl_2_hp_card.rect.x=self.pl_2.rect.x
        self.pl_2_hp_card.set_text(f"player 2 HP: {self.pl_2.hp}",27)
        self.pl_2_hp_card.draw_text()
        self.ai_hp_card.rect.y=self.ai.rect.y-70
        self.ai_hp_card.rect.x=self.ai.rect.x
        self.ai_hp_card.set_text(f"Final boss ☠️ HP: {self.ai.hp}",27)
        self.ai_hp_card.draw_text()
        self.who_win()
        pygame.display.flip()

    def _check_1939(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                print('secsesfull quit the game!')
            elif event.type == pygame.KEYDOWN:
                self._attack_poland(event)
                self._to_berlin(event)
            elif event.type == pygame.KEYUP:
                self._defend_poland(event)
                self._woflksturm(event)

    def _attack_poland(self,event):
        if event.key == pygame.K_d:
            self.pl_1.moving_right=True
        elif event.key == pygame.K_a:
            self.pl_1.moving_left=True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            self._pl_1_fire_bullets()
        elif event.key == pygame.K_s:
            self.pl_1.prised=True
        elif event.key == pygame.K_w:
            self.pl_1.visenie=True
            #self._prisest_1()
    def _to_berlin(self,event):
        if event.key == pygame.K_l:
            self.pl_2.moving_right=True
        elif event.key == pygame.K_j:
            self.pl_2.moving_left=True
        elif event.key == pygame.K_p:
            sys.exit()
        elif event.key == pygame.K_h:
            self._pl_2_fire_bullets()
        elif event.key == pygame.K_k:
            self.pl_2.prised=True
        elif event.key == pygame.K_i:
            self.pl_2.visenie=True

    def _defend_poland(self,event):
        if event.key == pygame.K_d:
            self.pl_1.moving_right=False
        elif event.key == pygame.K_a:
            self.pl_1.moving_left=False
        elif event.key == pygame.K_s:
            self.pl_1.prised=False
        elif event.key == pygame.K_w:
            self.pl_1.visenie=False
    def _woflksturm(self,event):
        if event.key == pygame.K_l:
            self.pl_2.moving_right=False
        elif event.key == pygame.K_j:
            self.pl_2.moving_left=False
        elif event.key == pygame.K_k:
            self.pl_2.prised=False
        elif event.key == pygame.K_i:
            self.pl_2.visenie=False

    def _pl_1_fire_bullets(self):
        if len(self.bullets_1) < self.settings.bullet_allowed and self.pl_1.prised!=True and self.pl_1.visenie!=True:
            new_bullet = Bullet(self)
            self.bullets_1.add(new_bullet)
            self.fire_sound.play()
    def _pl_2_fire_bullets(self):
        if len(self.bullets_2) < self.settings.bullet_2_allowed and self.pl_2.prised!=True and self.pl_2.visenie!=True:
            new_bullet = Bullet_2(self)
            self.bullets_2.add(new_bullet)
            self.fire_sound.play()

    def _update_bullets(self):
        self.bullets_1.update()
        self.bullets_2.update()
        self.ai_bullets_1.update()
        self.ai_bullets_2.update()
        for bullet in self.bullets_1.copy():
            if bullet.rect.x >= 1600:
                self.bullets_1.remove(bullet)
        for bullet in self.bullets_2.copy():
            if bullet.rect.x <= 0:
                self.bullets_2.remove(bullet)

        for bullet in self.ai_bullets_1.copy():
            if bullet.rect.x >= 1600:
                self.ai_bullets_1.remove(bullet)
        for bullet in self.ai_bullets_2.copy():
            if bullet.rect.x <= 0:
                self.ai_bullets_2.remove(bullet)

    def _update_events(self):
        current_time = pygame.time.get_ticks()  # Получаем текущее время
        if current_time - self.last_event_time > self.event_interval:
            self.last_event_time = current_time  # Обновляем время последнего события
            self._perform_event_1()  # Вызываем событие
            self._perform_event_2()

    def _perform_event_1(self):
        randomik=randint(1,2)
        if randomik==1:
            new_bullet = Ai_bullet_1(self)
            self.ai_bullets_1.add(new_bullet)
            self.fire_sound.play()
        if randomik==2:
            new_bullet = Ai_bullet_3(self)
            self.ai_bullets_1.add(new_bullet)
            self.fire_sound.play()

    def _perform_event_2(self):
        randomik=randint(1,2)
        if randomik==1:
            new_bullet = Ai_bullet_2(self)
            self.ai_bullets_2.add(new_bullet)
            self.fire_sound.play()
        if randomik==2:
            new_bullet = Ai_bullet_4(self)
            self.ai_bullets_2.add(new_bullet)
            self.fire_sound.play()

    def _collide_bullets(self):
        collided_objects_1 = pygame.sprite.spritecollide(self.pl_1, self.ai_bullets_1, True)
        collided_objects_2 = pygame.sprite.spritecollide(self.pl_2, self.ai_bullets_2, True)
        collided_objects_3 = pygame.sprite.spritecollide(self.ai, self.bullets_1, True)
        collided_objects_4 = pygame.sprite.spritecollide(self.ai, self.bullets_2, True)
        for obj in collided_objects_1:
            self.pl_1.hp -= 50  # Наносим урон
        for obj in collided_objects_2:
            self.pl_2.hp -= 50  # Наносим урон

        for obj in collided_objects_3:
            self.ai.hp -= 25  # Наносим урон
        for obj in collided_objects_4:
            self.ai.hp -= 25  # Наносим урон

    def who_win(self):
        if self.ai.hp <= 0:
            b = Card(700,420,0,0,self)
            b.set_text('YOU WIN!',40)
            b.draw_text()
            sleep(1)
            self.gaming = False
        elif self.pl_1.hp <= 0 or self.pl_2.hp <= 0:
            b = Card(700,420,0,0,self)
            b.set_text('YOU LOSE!',40)
            b.draw_text()
            sleep(1)
            self.gaming = False

if __name__ == "__main__":
    ai=Maingame()
    ai.run_vasya()