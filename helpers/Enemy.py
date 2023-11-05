import pygame
import random

from main import WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, images, speedXRandomScope, speedYRandomScope = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(images)
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(WIDTH)
        self.rect.x = random.randrange(WIDTH, WIDTH + 100)
        self.speedx = random.randrange(speedXRandomScope[0], speedXRandomScope[1])

        if speedYRandomScope != None:
            self.speedy = random.randrange(speedYRandomScope[0], speedYRandomScope[1])
        
        self.__speedXRandomScope = speedXRandomScope
        self.__speedYRandomScope = speedYRandomScope


    def update(self):
        self.rect.x -= self.speedx

        if self.speedy:
            self.rect.y += self.speedy

        if self.rect.right < 0:
            self.rect.y = random.randrange(WIDTH)
            self.rect.x = random.randrange(WIDTH, WIDTH + 100)
            self.speedx = random.randrange(self.__speedXRandomScope[0], self.__speedXRandomScope[1])

            if self.__speedYRandomScope != None:
                self.speedy = random.randrange(self.__speedYRandomScope[0], self.__speedYRandomScope[1])