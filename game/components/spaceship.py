import pygame
from game.components.bullets.bullet import Bullet

from pygame.sprite import Sprite
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import DEFAULT_TYPE, SCREEN_WIDTH,  SCREEN_HEIGHT,SPACESHIP

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
        self.name = self.type
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_u = 0
        
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
            self.shoot(game)

        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

       

    def move_left(self):
        self.rect.x -=  self.SHIP_SPEED 
        

    def move_right(self):
        self.rect.x +=  self.SHIP_SPEED 
       
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT -70: 
            self.rect.y += self.SHIP_SPEED  

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet, game)

    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
