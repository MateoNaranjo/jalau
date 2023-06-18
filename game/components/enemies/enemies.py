import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import BULLETS_PER_ENEMY, ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS_LIST = [0, 50, 100, 150, 200, 250, 300, 350, 450, 500, 550]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 3
    MOV_X = {0: 'left', 1: 'right'}
    MOVE_X_FOR_RANGE = (95, 200)
    SHOOTING_RANGE = 50
    ENEMIES_TYPE = { 1: ENEMY_1, 2: ENEMY_2 }

    def __init__(self, enemy_type = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30, 100], bullet_manager = None):
        super().__init__()
        self.bullet_manager = bullet_manager
        self.name = 'enemy_' + str(random.randint(1, 19841009))
        #print("nave: ", self.name)
        
        self.image = self.ENEMIES_TYPE[enemy_type]
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)
        self.bullets_per_enemy = BULLETS_PER_ENEMY
        


    def update(self, ships, game):
        self.rect.y += self.speed_y
        #print("Dispara: ", self.name)
        self.shoot(game)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0

    def shoot(self, game):
        current_time = pygame.time.get_ticks()

        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet, game)
            self.shooting_time = random.randint(30, 50)

        












