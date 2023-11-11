import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, rect, callback):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = rect
        self.__callback = callback


    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.__callback()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                pass