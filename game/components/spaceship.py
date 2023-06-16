import pygame
from game.components.bullets.bullet import Bullet

from pygame.sprite import Sprite
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import SCREEN_WIDTH,  SCREEN_HEIGHT,SPACESHIP
class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        super().__init__()
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        
      
        #self.bullet_manager.add_bullet(self)
        
    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()   
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

        if self.rect.top < 0:
            self.rect.top=0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def move_left(self):
        self.rect.x -=  self.SHIP_SPEED 
        if self.rect.left < 0:
            self.rect.x >=SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x +=  self.SHIP_SPEED 
        if self.rect.right >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT -70: 
            self.rect.y += self.SHIP_SPEED  

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
