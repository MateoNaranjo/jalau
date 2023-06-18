import pygame

from game.components.bullets.bullet import Bullet


class BulletManager:
    def __init__(self):
        self.bullets =[]
        self.enemy_bullets =[]
        
        
    def update(self,  game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            #if bullet.rect.colliderect(game.player.rect) and bullet.owner=='enemy':
                #self.enemy_bullets.remove(bullet)
             #   game.playing = False
              #  pygame.time.delay(1000)
               # break
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)
            
        

    #def add_bullet(self, bullet):
        #if bullet.owner == 'enemy' and len (self.enemy_bullets) < 1:
         #   self.enemy_bullets.append(bullet)
            

    #def shoot(self, enemy):
        #bullet = Bullet(self, self.type)
        #enemy_bullet = Bullet(self, enemy )
        #self.add_bullet(bullet)
        #self.add_bullet(enemy_bullet)
    
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        
        if bullet.owner == 'player' and len (self.bullets) < 1:
            self.bullets.append(bullet)
                

    
    