import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import SHIELD_TYPE


class BulletManager:
    def __init__(self):
        self.bullets =[]
        self.enemy_bullets =[]
        # self.ship_bullets = []
        
        
    def update(self,  game):

        # Revisando balas jugador
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.score += 100
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
        
        #revisando balas enemigas
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:    
                    game.death_count += 1
                    game.playing = False
                    pygame.time.delay(1000)
                    break
                self.enemy_bullets.remove(bullet)
                
        '''for bullet in self.bullets:
            bullet.update(self.bullets)
            #for enemy in game.enemy_manager.enemies:
            if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                if game.player.power_up_type != SHIELD_TYPE:    
                    game.death_count += 1
                self.enemy_bullets.remove(bullet)
                

                game.playing = False
                pygame.time.delay(1000)
                break'''
                
                    

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
    
    def add_bullet(self, bullet, game):

        
        if bullet.owner == 'enemy' :
        #if bullet.owner == 'enemy' and len(self.enemy_bullets) < 4:
            bullet_in_list = False
            for enemy_bullet in self.enemy_bullets:
                if enemy_bullet.ship_owner == bullet.ship_owner:
                    bullet_in_list = True
                    break
            
            if not bullet_in_list:

                self.enemy_bullets.append(bullet)
                #self.ship_bullets.append(bullet.ship_owner)
        
        if bullet.owner == 'player' and len (self.bullets) < game.bullets_per_player:
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
                

    
    