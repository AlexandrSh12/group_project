import pygame
from pathlib import Path

dir_path = Path.cwd()

pygame.mixer.init()

def load_sound(filename, volume):
    obj = pygame.mixer.Sound(Path(dir_path, "resources", "sound", filename))
    obj.set_volume(volume)
    return obj

click = load_sound("click.wav", 0.09)
shoot_sound = load_sound("shoot.wav", 0.5)
hit_sound = load_sound("enemy_hit.wav", 0.1) 
hit_enemy_sound = load_sound("enemy_dead.wav", 0.1)
victory_sound = load_sound("victory.wav", 0.2)
end_menu_sound = load_sound("dead.wav", 0.2)
main_theme = load_sound("main_theme.wav", 0.2)