import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BGSTART


class Menu:
  HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
  HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
  
  def __init__(self, screen):
    image = pygame.transform.scale(BGSTART, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, (0, 0))
    self.font = pygame.font.Font(FONT_STYLE, 30)
    
  def update(self, game):
    pygame.display.update()
    self.handle_events_on_menu(game)
    
  def handle_events_on_menu(self, game):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game.playing = False
        game.running = False
      elif event.type == pygame.KEYDOWN:
        game.run()
        
  def reset_screen_color(self, screen):
    image = pygame.transform.scale(BGSTART, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, (0, 0))
    
  def draw(self, screen, message, x = HALF_SCREEN_WIDTH, y = HALF_SCREEN_HEIGHT, color = (255, 255, 255)):
    text = self.font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)