import pygame
from pygame.sprite import Sprite
from random import randint
from time import sleep

# Настройки игры
class GameSettings:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        
        # Параметры врага
        self.enemy_hp = 2000
        
        # Параметры пуль
        self.bullet_speed = 10
        self.bullet_size = (15, 3)
        self.bullet_color = (60, 60, 60)
        self.max_bullets = 5
        
        # Скорость пуль врага
        self.enemy_bullet_speed = 5
        
        # Параметры игроков
        self.player_speed = 2.5
        self.player_hp = 100

# Класс игрока
class Player(Sprite):
    def __init__(self, game, image_path, start_pos):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.transform.scale(pygame.image.load(image_path), (60, 120))
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        
        self.x = float(self.rect.x)
        self.hp = self.settings.player_hp
        
        self.moving_right = False
        self.moving_left = False
        self.crouching = False
        self.jumping = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        
        if self.crouching:
            self.rect.y = 840
            self.rect.height = 60
        else:
            self.rect.y = 780
            self.rect.height = 120
        
        if self.jumping:
            self.rect.y = 720
        elif not self.crouching:
            self.rect.y = 780
        
        self.rect.x = self.x
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

# Класс врага
class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.transform.scale(pygame.image.load('Images_from_durka/pixil-frame-0.png'), (240, 200))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom
        
        self.hp = self.settings.enemy_hp
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

# Класс пули
class Bullet(Sprite):
    def __init__(self, game, shooter, direction):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0, 0, *self.settings.bullet_size)
        self.rect.midtop = shooter.rect.midtop
        self.x = float(self.rect.x)
        
        self.direction = direction
    
    def update(self):
        self.x += self.settings.bullet_speed * self.direction
        self.rect.x = self.x
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

# Основной игровой процесс
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('7 December 1941 XD')
        
        self.settings = GameSettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        
        self.player1 = Player(self, 'Images_from_durka/wermacht_s.png', (100, 780))
        self.player2 = Player(self, 'Images_from_durka/wermacht_ss.png', (1000, 780))
        self.enemy = Enemy(self)
        
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        
        self.running = True
    
    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)
    
    def _handle_keydown(self, event):
        if event.key == pygame.K_d:
            self.player1.moving_right = True
        elif event.key == pygame.K_a:
            self.player1.moving_left = True
        elif event.key == pygame.K_f:
            self._fire_bullet(self.player1, 1)
        elif event.key == pygame.K_l:
            self.player2.moving_right = True
        elif event.key == pygame.K_j:
            self.player2.moving_left = True
        elif event.key == pygame.K_h:
            self._fire_bullet(self.player2, -1)
    
    def _handle_keyup(self, event):
        if event.key == pygame.K_d:
            self.player1.moving_right = False
        elif event.key == pygame.K_a:
            self.player1.moving_left = False
        elif event.key == pygame.K_l:
            self.player2.moving_right = False
        elif event.key == pygame.K_j:
            self.player2.moving_left = False
    
    def _fire_bullet(self, shooter, direction):
        if len(self.player_bullets) < self.settings.max_bullets:
            self.player_bullets.add(Bullet(self, shooter, direction))
    
    def _update(self):
        self.player1.update()
        self.player2.update()
        self.player_bullets.update()
        
    def _draw(self):
        self.screen.fill(self.settings.bg_color)
        self.player1.draw()
        self.player2.draw()
        self.enemy.draw()
        
        for bullet in self.player_bullets:
            bullet.draw()
        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()