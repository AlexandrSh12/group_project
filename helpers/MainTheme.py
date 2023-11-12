import pygame
from pathlib import Path
from helpers.LoadResources import resource_path

class MainTheme:
    def __init__(self):
        self.__path = resource_path(Path("resources", "sound", "main_theme.wav"))

    def play(self):
        pygame.mixer.music.load(self.__path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
    
    def stop(self):
        pygame.mixer.music.stop()