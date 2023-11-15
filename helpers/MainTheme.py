import pygame
from pathlib import Path
from all_resources import main_theme_path

class MainTheme:
    def __init__(self):
        self.__path = main_theme_path

    def play(self):
        pygame.mixer.music.load(self.__path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
    
    def stop(self):
        pygame.mixer.music.stop()