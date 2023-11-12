from pathlib import Path
import pygame

class MainTheme:
    def __init__(self):
        self.__path = Path(Path.cwd(), "resources", "sound", "main_theme.wav")

    def play(self):
        pygame.mixer.music.load(self.__path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
    
    def stop(self):
        pygame.mixer.music.stop()