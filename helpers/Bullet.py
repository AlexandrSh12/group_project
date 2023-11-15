import pygame
import random
from all_resources import attacks
from vars import WIDTH

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(attacks)
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = -20
        self.speedy = -20

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()