import os
import sys
import pygame
from pathlib import Path

def resource_path(relative):    
    if hasattr(sys, "_MEIPASS"):
        print(sys._MEIPASS)
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def load_image(path, scale = None):
    obj = pygame.image.load(resource_path(Path("resources", "graphics", path)))
    if scale != None:
        obj = pygame.transform.scale(obj, scale)

    return obj

def load_sound(filename, volume):
    obj = pygame.mixer.Sound(resource_path(Path("resources", "sound", filename)))
    obj.set_volume(volume)
    return obj

def load_font(size):
    return pygame.font.Font(resource_path(Path("resources", "fonts", "font.ttf")), size)

# заугрзка музыки
pygame.mixer.init()
click = load_sound("click.wav", 0.09)
shoot_sound = load_sound("shoot.wav", 0.5)
hit_sound = load_sound("enemy_hit.wav", 0.1) 
hit_enemy_sound = load_sound("enemy_dead.wav", 0.1)
victory_sound = load_sound("victory.wav", 0.2)
end_menu_sound = load_sound("dead.wav", 0.2)
main_theme_path = resource_path(Path("resources", "sound", "main_theme.wav"))


# загрузка графики
harry = load_image("harry.png")
background = load_image("backgrounds/level.jpg")
start_menu =load_image("backgrounds/start.png")
end_menu = load_image("backgrounds/end.png", (1200, 600))
victory = load_image("backgrounds/victory.png", (1200, 600))
score_text = load_image("misc/score.png", (130, 50))
hog_logo = load_image("misc/hogwarts_logo.png", (80, 80))
hp = load_image("misc/hp.png", (100, 80))
again_btn = load_image("buttons/again.png", (270, 90))
quit_btn = load_image("buttons/quit.png", (270, 90))
game_icon = load_image("misc/game_icon.png")

# загрузка анимации взрыва противника
explosion_anim = []
for i in range(12):
    img = load_image("explosion/explosion{}.png".format(i), (156, 156))
    img.set_colorkey("black")
    explosion_anim.append(img)

# загрузка всех видов врагов
dementor = load_image("enemys/dementor.png")
death_eater = load_image("enemys/death_eaters.png")
owls = []
clans = []
attacks = []

for filename in ["enemys/owl0.png", "enemys/owl1.png", "enemys/owl2.png"]:
    owls.append(load_image(filename))

for filename in ["enemys/ravenclaw.png", "enemys/hufflepuff.png", "enemys/slytherin.png"]:
    clans.append(load_image(filename))

# загрузка анимации попадания
for filename in ["attack/attack0.png", "attack/attack1.png", "attack/attack2.png", "attack/attack3.png", "attack/attack4.png"]:
    attacks.append(load_image(filename))