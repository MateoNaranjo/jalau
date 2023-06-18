import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT


class Bullet(Sprite):
    BULLET_SIZE =  pygame.transform.scale(BULLET,(10,20))
    BULLET_ENEMY_SIZE =  pygame.transform.scale(BULLET_ENEMY,(10,20))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 20

    def __init__(self, spaceship):
        super().__init__()
        
        self.image = self.BULLETS [spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
        self.ship_owner = spaceship.name
        self.owner = spaceship.type


    def update(self, bullets):
        if self.owner == 'player':
            self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED
        
        if self.rect.y >= SCREEN_HEIGHT or self.rect.y <= 0:
            bullets.remove(self)


    def draw (self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
