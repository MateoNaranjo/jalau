import random
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.components.enemies.enemies import Enemy
from game.utils.constants import SCREEN_HEIGHT

class EnemyManager:
    def __init__(self):
        self.bullet_manager = BulletManager()
        self.enemies = []
        self.max_enemies = 5

    def update(self, game,):
        self.add_enemy()
        enemies_to_remove = []
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            if enemy.rect.y >= SCREEN_HEIGHT:
                enemies_to_remove.append(enemy)
            
        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)


    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.max_enemies:
            num_new_enemies = self.max_enemies - len(self.enemies)
            for _ in range(num_new_enemies):
                enemy_type = random.randint(1, 2)
                if enemy_type == 1:
                    enemy = Enemy(enemy_type, bullet_manager=self.bullet_manager)
                else:
                    x_speed = 5
                    y_speed = 2
                    move_x_for = [50, 120]
                    enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for, bullet_manager=self.bullet_manager)
                self.enemies.append(enemy)
                enemy = Enemy(enemy_type, bullet_manager=self.bullet_manager)
                self.enemies.append(enemy)

    
        