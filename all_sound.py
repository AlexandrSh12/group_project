import pygame
from pathlib import Path

dir_path = Path.cwd()

pygame.mixer.init()

def load_sound(filename, volume):
    obj = pygame.mixer.Sound(Path(dir_path, "sound", filename))
    obj.set_volume(volume)

click = load_sound("Клик.wav", 0.09)
shoot_sound = load_sound("Выстрел.wav", 0.5)
hit_sound = load_sound("Враг попал.wav", 0.1) 
hit_enemy_sound = load_sound("Враг умер.wav", 0.1)
victory_sound = load_sound("Победа.wav", 0.2)
end_menu_sound = load_sound("Смерть.wav", 0.2)