import pygame
from pygame.locals import *
import sys, random

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 800
ACC = 0.5
FRIC = -0.2
FPS = 60
FramesPerSecond = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class player(pygame.sprite.Sprite):
  def __init__(self, posx, posy):
    super().__init__()
    self.surf = pygame.Surface((10, 10))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect(center=(posx, posy))
    
    self.pos = vec((posx, posy))
    self.vel = vec((0,0))
    self.acc = vec((0, 0))
    
  def move(self):
    check = random.randint(0, 5)
    if check == 1:
      self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))
      self.acc.x = 0.1
    if check == 0:
      self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))
      self.acc.x = -0.1
    
    self.acc.x += self.vel.x * FRIC
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
    
    if self.pos.x > WIDTH:
            self.pos.x = 0
    if self.pos.x < 0:
            self.pos.x = WIDTH
    if self.pos.y > HEIGHT:
            self.pos.y = 0
    if self.pos.y < 0:
            self.pos.y = HEIGHT
            
all_sprites = pygame.sprite.Group()

for i in range(0, 10):
  cell = player(random.randint(0, WIDTH), random.randint(0, HEIGHT))
  all_sprites.add(cell)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.fill((0,0,0))

    for entity in all_sprites:
      screen.blit(entity.surf, entity.rect)
      entity.move()

    pygame.display.update()
    FramesPerSecond.tick(FPS)
